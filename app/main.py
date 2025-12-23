import time
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, File, UploadFile
from app.booking import router as booking_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from app.response_cache import get_quick_response
from app.openai_assistant import assistant
from app.elevenlabs_tts import text_to_speech
from app.spotify_control import spotify
from app.browser_control import browser

app = FastAPI()
app.include_router(booking_router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket connected")
    
    try:
        while True:
            data = await websocket.receive_json()
            text = data.get("text", "")
            lang = data.get("lang", "it")
            guest_name = data.get("guest_name")
            visit_count = data.get("visit_count", 0)
            
            # Don't respond while music is playing
            # if spotify.is_music_playing():
            #     print(f"🎵 Music playing, ignoring: {text}")
            #     continue
            
            start_time = time.time()
            
            # ⚡ OPTIMIZATION 1: Check quick response cache first
            quick_response, is_music = get_quick_response(text, lang)
            if quick_response:
                print(f"⚡ INSTANT response ({time.time() - start_time:.2f}s)")
                response_text = quick_response
                action = "play_pizzica" if is_music else None
            else:
                # Get AI response only if not in cache
                response = await assistant.ask(text, lang, guest_name=guest_name, visit_count=visit_count)
                response_text = response.get("text")
                action = response.get("action")
                print(f"🤖 AI response ({time.time() - start_time:.2f}s)")
            
            # Handle actions with consolidated logic
            music_actions = {
                "play_music": spotify.play_pizzica_di_san_vito,
                "play_pizzica": spotify.play_pizzica_di_san_vito,
                "play_fun_music": spotify.play_fun_song,
                "play_bambole": spotify.play_fun_song,
                "play_fun": spotify.play_fun_song,
                "play_political": spotify.play_political_song,
                "play_love": spotify.play_love_song,
                "open_spotify": spotify.open_spotify
            }
            
            browser_actions = {
                "open_etna": browser.open_etna,
                "open_trenitalia": browser.open_trenitalia,
                "open_skyscanner": browser.open_skyscanner,
                "open_website": browser.open_website
            }
            
            # Execute action if defined
            if action in music_actions:
                music_actions[action]()
            elif action in browser_actions:
                browser_actions[action]()
            
            # ⚡ OPTIMIZATION 2: Generate TTS in parallel (send text first, audio follows)
            # Send text immediately for faster perceived response
            await websocket.send_json({
                "type": "response",
                "text": response_text,
                "audio_url": None,  # Will be sent separately
                "music_playing": spotify.is_music_playing()
            })
            
            # Generate TTS and send as separate message
            audio_url = await text_to_speech(response_text, lang)
            if audio_url:
                await websocket.send_json({
                    "type": "audio",
                    "audio_url": audio_url
                })
            
            print(f"✅ Total time: {time.time() - start_time:.2f}s")
            
    except WebSocketDisconnect:
        print("❌ WebSocket disconnected")

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    """Receive audio from browser and transcribe with Whisper"""
    from app.openai_speech import get_speech_client
    
    try:
        # Save uploaded audio
        audio_data = await file.read()
        temp_path = f"/tmp/audio_{hash(audio_data) % 10000}.webm"
        
        with open(temp_path, 'wb') as f:
            f.write(audio_data)
        
        # Transcribe with Whisper (auto-detect language)
        with open(temp_path, 'rb') as audio_file:
            text, detected_lang = await get_speech_client().transcribe_audio(audio_file)
        
        if not text:
            return {"text": None, "success": False}
        
        
        
        return {"text": text, "lang": detected_lang, "success": True}
        
    except Exception as e:
        print(f"❌ Audio upload error: {e}")
        return {"text": "", "success": False, "error": str(e)}

@app.get("/")
async def get_index():
    return FileResponse("web/solomon.html")

@app.get("/avatar.glb")
async def get_avatar():
    return FileResponse("web/avatar.glb")

# Serve TTS files from /tmp
@app.get("/{filename}")
async def get_file(filename: str):
    filepath = f"/tmp/{filename}"
    if os.path.exists(filepath):
        return FileResponse(filepath)
    return {"error": "File not found"}


# Ring Doorbell Integration
from app.ring_listener import RingListener
from app.doorbell_handler import DoorbellHandler
from app.ring_client import RingDoorbell

ring_listener = RingListener()
doorbell_handler = DoorbellHandler()
ring_client = RingDoorbell()

@app.on_event("startup")
async def startup_ring():
    """Initialize Ring doorbell"""
    await ring_listener.start()
    success = await ring_client.initialize()
    if success:
        print(f"✅ Ring doorbell: {ring_client.doorbell.name} (Battery: {ring_client.doorbell.battery_life}%)")
    else:
        print("⚠️ Ring doorbell initialization failed")

@app.post("/ring/webhook")
async def ring_webhook(data: dict):
    """Handle Ring doorbell press"""
    print(f"🔔 DOORBELL PRESSED!")
    
    visitor = data.get("visitor", "Guest")
    lang = data.get("lang", "en")
    
    # Notify all connected WebSockets
    await ring_listener.notify(visitor, lang)
    
    # Get appropriate greeting
    greeting = doorbell_handler.get_time_greeting(lang)
    print(f"👋 {greeting}, {visitor}!")
    
    return {"status": "ok", "greeting": greeting}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.post("/recognize-face")
async def recognize_face(data: dict):
    """Recognize face from webcam"""
    from app.face_recognition_system import face_system
    
    try:
        image_base64 = data.get('image')
        if not image_base64:
            return {"error": "No image provided"}
        
        result = face_system.recognize_face_from_base64(image_base64)
        return result
        
    except Exception as e:
        print(f"❌ Face recognition error: {e}")
        return {"error": str(e)}

@app.post("/register-face")
async def register_face(data: dict):
    """Register new face with name"""
    from app.face_recognition_system import face_system
    
    try:
        name = data.get('name')
        encoding = data.get('encoding')
        
        if not name or not encoding:
            return {"success": False, "error": "Missing data"}
        
        success = face_system.register_new_face(name, encoding)
        return {"success": success, "name": name}
        
    except Exception as e:
        return {"success": False, "error": str(e)}

# Background task to keep Solomon on top
import asyncio
from app.window_manager import window_manager

async def keep_solomon_visible():
    """Keep Solomon window always on top"""
    while True:
        await asyncio.sleep(2)  # Every 2 seconds
        window_manager.keep_solomon_on_top()

# Start background task on startup
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(keep_solomon_visible())
    print("✅ Solomon always-on-top enabled")

# Ring Event Polling
# DISABLED for speed
# 

@app.on_event("startup")
async def start_polling():
    """Start Ring polling task"""
    # asyncio.create_task(poll_ring_events())
    print("✅ Ring doorbell polling active")
