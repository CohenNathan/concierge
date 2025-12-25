# Cohen House Concierge - Web Interface

This directory contains the web interface for the Cohen House Concierge system.

## Structure

- `index.html` - Main web interface with 3D avatar (Solomon)
- `favicon.ico` - Site favicon
- `assets/` - Static assets
  - `models/` - 3D models
    - `avatar.glb` - Solomon 3D avatar model
  - `js/` - JavaScript files
    - `ring-listener.js` - Ring doorbell listener script

## Usage

The web interface is served by the FastAPI server at the root path (`/`).
It features a 3D animated avatar that listens and responds to voice commands in multiple languages.

## Technologies

- Three.js for 3D rendering
- WebSocket for real-time communication
- WebRTC Speech Recognition API
