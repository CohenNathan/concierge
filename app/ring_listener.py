import asyncio
import json

class RingListener:
    def __init__(self):
        self.subscribers = []

    async def start(self):
        print("Ring webhook ready: POST to /ring/webhook")
        print("Use ngrok: ngrok http 8088 for Ring app")

    def subscribe(self, ws):
        self.subscribers.append(ws)

    async def notify(self, visitor: str, lang: str = "en"):
        for ws in self.subscribers[:]:
            try:
                await ws.send_json({"type": "doorbell", "visitor": visitor, "lang": lang})
            except:
                self.subscribers.remove(ws)
