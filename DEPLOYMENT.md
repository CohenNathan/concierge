# Deployment Guide - Cohen House Concierge

## Quick Start (Local Development)

1. **Clone and Install:**
```bash
git clone https://github.com/CohenNathan/concierge.git
cd concierge
pip install -r requirements.txt
npm install
```

2. **Configure Environment:**
```bash
# Create .env file
cat > .env << EOF
OPENAI_API_KEY=sk-your-key-here
ELEVENLABS_API_KEY=your-elevenlabs-key
EOF
```

3. **Run Server:**
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

4. **Access Interface:**
Open browser: `http://localhost:8000/solomon.html`

---

## Production Deployment

### Option 1: VPS/Cloud Server (Recommended)

#### Prerequisites
- Ubuntu 20.04+ or similar Linux
- 2GB+ RAM
- Domain name pointed to server
- SSL certificate (Let's Encrypt)

#### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.9+
sudo apt install python3 python3-pip python3-venv -y

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install nodejs -y

# Install nginx
sudo apt install nginx -y
```

#### Step 2: Application Setup
```bash
# Create app directory
sudo mkdir -p /var/www/concierge
cd /var/www/concierge

# Clone repository
sudo git clone https://github.com/CohenNathan/concierge.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
npm install

# Set up environment
sudo nano .env
# Add your API keys
```

#### Step 3: Configure Systemd Service
```bash
sudo nano /etc/systemd/system/concierge.service
```

Add:
```ini
[Unit]
Description=Cohen House Concierge
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/concierge
Environment="PATH=/var/www/concierge/venv/bin"
ExecStart=/var/www/concierge/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable concierge
sudo systemctl start concierge
sudo systemctl status concierge
```

#### Step 4: Configure Nginx Reverse Proxy
```bash
sudo nano /etc/nginx/sites-available/concierge
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket support
    location /ws {
        proxy_pass http://localhost:8000/ws;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 86400;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/concierge /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 5: SSL Certificate (Let's Encrypt)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

#### Step 6: Update WebSocket URL
Edit `/var/www/concierge/web/solomon.html`:
```javascript
// Change:
ws = new WebSocket('ws://localhost:8000/ws');
// To:
ws = new WebSocket('wss://your-domain.com/ws');
```

Restart service:
```bash
sudo systemctl restart concierge
```

---

### Option 2: Docker Deployment

#### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY requirements.txt .
COPY package.json .
RUN pip install -r requirements.txt
RUN npm install

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Create docker-compose.yml
```yaml
version: '3.8'

services:
  concierge:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ELEVENLABS_API_KEY=${ELEVENLABS_API_KEY}
    volumes:
      - ./audio_cache:/app/audio_cache
    restart: always
```

#### Deploy
```bash
docker-compose up -d
```

---

## Monitoring and Maintenance

### View Logs
```bash
# Systemd service
sudo journalctl -u concierge -f

# Docker
docker-compose logs -f
```

### Restart Service
```bash
# Systemd
sudo systemctl restart concierge

# Docker
docker-compose restart
```

### Update Application
```bash
cd /var/www/concierge
sudo git pull
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart concierge
```

---

## Backup Strategy

### 1. Automated Git Backup
```bash
# Add to crontab
0 2 * * * cd /var/www/concierge && git add -A && git commit -m "Auto backup $(date)" && git push
```

### 2. Configuration Backup
```bash
# Backup .env and configs
sudo tar -czf /backup/concierge-$(date +%Y%m%d).tar.gz /var/www/concierge/.env /etc/nginx/sites-available/concierge /etc/systemd/system/concierge.service
```

### 3. Database Backup (if using)
```bash
# Add database backup commands here
```

---

## Security Checklist

- [ ] API keys in .env (not in code)
- [ ] .env file not in git (check .gitignore)
- [ ] SSL certificate installed
- [ ] Firewall configured (allow 80, 443, SSH only)
- [ ] Regular security updates
- [ ] Strong SSH keys (disable password auth)
- [ ] Rate limiting on API endpoints
- [ ] Regular backup testing

---

## Performance Optimization

### 1. Enable Response Caching
The system already uses `response_cache.py` for common queries.

### 2. Configure Workers
For production, use multiple workers:
```bash
uvicorn app.main:app --workers 4
```

### 3. CDN for Static Files
Consider using Cloudflare or similar for:
- solomon.html
- avatar.glb
- Static assets

### 4. Redis for Session Management (Optional)
Add Redis for better WebSocket session handling:
```bash
pip install redis aioredis
```

---

## Troubleshooting Production Issues

### Service Won't Start
```bash
# Check logs
sudo journalctl -u concierge -n 50
# Check permissions
sudo chown -R www-data:www-data /var/www/concierge
```

### WebSocket Connection Issues
```bash
# Check nginx websocket config
sudo nginx -t
# Check firewall
sudo ufw status
sudo ufw allow 'Nginx Full'
```

### High CPU Usage
```bash
# Check process
top -u www-data
# Reduce workers if needed
# Check for infinite loops in logs
```

---

## Cost Estimation

### Monthly Running Costs

**Server:**
- DigitalOcean/Linode: $12-24/month (2GB RAM)
- AWS EC2 t3.small: ~$15/month
- Hetzner: €4-8/month (best value)

**APIs:**
- OpenAI (GPT-4o-mini): ~$5-20/month (varies with usage)
- ElevenLabs TTS: ~$5-22/month (varies with usage)

**Total:** ~$25-70/month depending on guest traffic

---

## Support

**Issues:** Create GitHub issue  
**Email:** info@cohenhouse.com  
**Website:** www.cohenhouse.it

---

**Last Updated:** December 21, 2025
