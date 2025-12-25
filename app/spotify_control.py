import subprocess
import time
import threading

class SpotifyController:
    def __init__(self):
        # 4 music types for different moods
        self.pizzica_track = "spotify:track:7MTyDl0UFVVJ1BLFQd8Er8"  # Traditional
        self.fun_track = "spotify:track:6yJuXrXneHttpJjzCWvnMG"  # Fun/Party
        self.political_track = "spotify:track:205qFlGXIK5tcygiVYFMVS"  # Political
        self.love_track = "spotify:track:5vV4umLhQqsuk6ei84nelx"  # Romantic
        self.is_playing = False
        print("✅ Music controller ready")
    
    def is_music_playing(self):
        """Check if music is currently playing"""
        return self.is_playing
    
    def open_spotify(self):
        """Open Spotify VISIBLE - only when guest explicitly requests it"""
        try:
            subprocess.Popen(['open', '-a', 'Spotify'], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
            print(f"🎵 Opening Spotify app (visible)")
            return True
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def play_pizzica_di_san_vito(self):
        """Play traditional Pizzica di San Vito"""
        self.is_playing = True
        return self._play_track_invisible(self.pizzica_track, "Pizzica di San Vito", duration=210)
    
    def play_fun_song(self):
        """Play fun song - Vogliamo le bambole"""
        self.is_playing = True
        return self._play_track_invisible(self.fun_track, "Vogliamo le bambole", duration=180)
    
    def play_political_song(self):
        """Play political/cultural song - Deija na Marinno"""
        self.is_playing = True
        return self._play_track_invisible(self.political_track, "Deija na Marinno", duration=180)
    
    def play_love_song(self):
        """Play romantic song - L'impero by Mannarino"""
        self.is_playing = True
        return self._play_track_invisible(self.love_track, "L'impero - Mannarino", duration=240)
    
    def _play_track_invisible(self, track_uri, track_name, duration=180):
        """Play track with Spotify INVISIBLE, browser stays visible"""
        try:
            applescript = f'''
            tell application "Spotify"
                if not application "Spotify" is running then
                    launch
                    delay 2
                end if
                play track "{track_uri}"
            end tell
            
            tell application "System Events"
                if exists (process "Spotify") then
                    set visible of process "Spotify" to false
                end if
            end tell
            
            tell application "Google Chrome"
                activate
            end tell
            '''
            
            subprocess.run(
                ['osascript', '-e', applescript],
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL,
                check=False
            )
            
            def keep_spotify_hidden():
                for _ in range(8):
                    time.sleep(0.6)
                    hide_only_spotify = '''
                    tell application "System Events"
                        if exists (process "Spotify") then
                            set visible of process "Spotify" to false
                        end if
                    end tell
                    
                    tell application "Google Chrome"
                        activate
                    end tell
                    '''
                    subprocess.run(['osascript', '-e', hide_only_spotify], 
                                 stdout=subprocess.DEVNULL, 
                                 stderr=subprocess.DEVNULL,
                                 check=False)
            
            threading.Thread(target=keep_spotify_hidden, daemon=True).start()
            
            print(f"🔥 Playing {track_name} - Spotify hidden, browser visible")
            print(f"📀 Track URI: {track_uri}")
            
            def mark_finished():
                time.sleep(duration)
                self.is_playing = False
                print(f"✅ {track_name} finished")
            
            threading.Thread(target=mark_finished, daemon=True).start()
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.is_playing = False
            return False

spotify = SpotifyController()
