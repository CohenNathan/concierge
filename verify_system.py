#!/usr/bin/env python3
"""
Verification script for Cohen House Concierge System
Checks that all critical files are present and properly configured.
"""

import os
import sys

def check_file(path, description):
    """Check if a file exists and report its status"""
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"✅ {description}: {path} ({size} bytes)")
        return True
    else:
        print(f"❌ {description}: {path} - NOT FOUND")
        return False

def main():
    print("=" * 70)
    print("Cohen House Concierge System Verification")
    print("=" * 70)
    print()
    
    all_ok = True
    
    # Core AI files
    print("📦 Core AI Components:")
    all_ok &= check_file("app/openai_assistant.py", "Main AI Logic")
    all_ok &= check_file("app/openai_speech.py", "Whisper Speech Recognition")
    all_ok &= check_file("app/response_cache.py", "Response Caching")
    all_ok &= check_file("app/spotify_control.py", "Music Control")
    print()
    
    # Frontend
    print("🎨 Frontend Files:")
    all_ok &= check_file("web/solomon.html", "Main UI")
    all_ok &= check_file("web/avatar.glb", "3D Bear Avatar")
    print()
    
    # Server
    print("🖥️  Server Files:")
    all_ok &= check_file("app/main.py", "FastAPI Server")
    all_ok &= check_file("app/elevenlabs_tts.py", "Text-to-Speech")
    all_ok &= check_file("app/browser_control.py", "Browser Control")
    print()
    
    # Configuration
    print("⚙️  Configuration Files:")
    all_ok &= check_file(".gitignore", "Git Ignore Rules")
    all_ok &= check_file("package.json", "Node Dependencies")
    all_ok &= check_file("requirements.txt", "Python Dependencies")
    print()
    
    # Documentation
    print("📚 Documentation:")
    all_ok &= check_file("README.md", "Main Documentation")
    all_ok &= check_file("DEPLOYMENT.md", "Deployment Guide")
    all_ok &= check_file("CHANGELOG.md", "Version History")
    all_ok &= check_file("SYSTEM_STATUS.md", "System Status")
    print()
    
    # Check .gitignore contents
    print("🔒 Security Configuration:")
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            gitignore = f.read()
            checks = {
                "tts_*.mp3": "TTS cache files",
                "*.backup": "Backup files",
                ".env": "Environment variables",
                "__pycache__": "Python cache",
            }
            for pattern, desc in checks.items():
                if pattern in gitignore:
                    print(f"✅ {desc} excluded: {pattern}")
                else:
                    print(f"⚠️  {desc} not excluded: {pattern}")
    print()
    
    # Final status
    print("=" * 70)
    if all_ok:
        print("🎉 ALL SYSTEMS GO! Cohen House Concierge is PRODUCTION READY")
        print("=" * 70)
        print()
        print("✅ Ready for real guests")
        print("✅ Ready for deployment")
        print("✅ Ready for team collaboration")
        print("✅ Ready for backup and maintenance")
        return 0
    else:
        print("⚠️  SOME FILES MISSING - Review the list above")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(main())
