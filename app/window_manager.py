import subprocess
import time

class WindowManager:
    def __init__(self):
        self.solomon_window_name = "Cohen Smart House"
        print("✅ Window manager ready")
    
    def keep_solomon_on_top(self):
        """Keep Solomon window always on top"""
        try:
            # Use Hammerspoon or native approach
            script = f'''
            tell application "System Events"
                tell process "Google Chrome"
                    set frontmost to true
                    set windowName to name of front window
                    if windowName contains "Cohen Smart House" then
                        -- Keep this window in front
                        perform action "AXRaise" of front window
                    end if
                end tell
            end tell
            '''
            subprocess.run(['osascript', '-e', script],
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         check=False)
            return True
        except Exception as e:
            print(f"⚠️ Keep on top error: {e}")
            return False
    
    def open_url_behind_solomon(self, url, name="Website"):
        """Open URL in new window BEHIND Solomon"""
        try:
            # Open in Firefox in background
            subprocess.Popen(
                ['open', '-g', '-na', 'Firefox', '--args', '--new-window', url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            print(f"🌐 Opening {name} behind Solomon")
            
            # Wait a moment then ensure Solomon is on top
            time.sleep(0.5)
            self.keep_solomon_on_top()
            
            # Also activate Chrome with Solomon
            activate_chrome = '''
            tell application "Google Chrome"
                activate
                set index of (first window whose name contains "Cohen Smart House") to 1
            end tell
            '''
            subprocess.run(['osascript', '-e', activate_chrome],
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,
                         check=False)
            
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

window_manager = WindowManager()
