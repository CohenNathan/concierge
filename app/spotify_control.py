import subprocess
import time
import threading

class SpotifyController:
    def __init__(self):
        # Track URIs
        self.pizzica_track = "spotify:track:7MTyDl0UFVVJ1BLFQd8Er8"
        self.fun_track = "spotify:track:6yJuXrXneHttpJjzCWvnMG"
        
        # Playlist URIs for mood-based music
        self.seria_playlist = "spotify:playlist:205qFlGXIK5tcygiVYFMVS"  # Serious/Political
        self.romantica_playlist = "spotify:playlist:3ZLF4Lcg9WvH9cQMTwNPqq"  # Romantic
        
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
        """Play fun song"""
        self.is_playing = True
        return self._play_track_invisible(self.fun_track, "Fun Song", duration=180)
    
    def play_seria_music(self):
        """Play serious/political music playlist"""
        self.is_playing = True
        return self._play_playlist_invisible(self.seria_playlist, "Serious Music", duration=300)
    
    def play_romantica_music(self):
        """Play romantic music playlist"""
        self.is_playing = True
        return self._play_playlist_invisible(self.romantica_playlist, "Romantic Music", duration=300)
    
    def _play_playlist_invisible(self, playlist_uri, playlist_name, duration=300):
        """Play playlist with Spotify INVISIBLE, browser stays visible"""
        try:
            # CRITICAL: Only hide Spotify, NOT the browser!
            applescript = f'''
            -- Play the playlist in Spotify
            tell application "Spotify"
                if not application "Spotify" is running then
                    launch
                    delay 2
                end if
                play track "{playlist_uri}"
            end tell
            
            -- Hide ONLY Spotify process (not Chrome/browser!)
            tell application "System Events"
                if exists (process "Spotify") then
                    set visible of process "Spotify" to false
                end if
            end tell
            
            -- Keep browser/Chrome in front
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
            
            # Continue hiding ONLY Spotify (not browser)
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
            
            print(f"🔥 Playing {playlist_name} - Spotify hidden, browser visible")
            
            def mark_finished():
                time.sleep(duration)
                self.is_playing = False
                print(f"✅ {playlist_name} finished")
            
            threading.Thread(target=mark_finished, daemon=True).start()
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            self.is_playing = False
            return False
    
    def _play_track_invisible(self, track_uri, track_name, duration=180):
        """Play track with Spotify INVISIBLE, browser stays visible"""
        try:
            # CRITICAL: Only hide Spotify, NOT the browser!
            applescript = f'''
            -- Play the track in Spotify
            tell application "Spotify"
                if not application "Spotify" is running then
                    launch
                    delay 2
                end if
                play track "{track_uri}"
            end tell
            
            -- Hide ONLY Spotify process (not Chrome/browser!)
            tell application "System Events"
                if exists (process "Spotify") then
                    set visible of process "Spotify" to false
                end if
            end tell
            
            -- Keep browser/Chrome in front
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
            
            # Continue hiding ONLY Spotify (not browser)
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
