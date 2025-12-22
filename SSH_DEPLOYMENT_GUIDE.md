# SSH/CLI Deployment Guide - Cohen House Concierge
# Ръководство за качване чрез SSH/CLI

Пълно ръководство за качване на проекта на отдалечен компютър чрез SSH/CLI.
Complete guide for uploading the project to a remote computer via SSH/CLI.

---

## 🎯 Какво прави този скрипт / What This Script Does

Скриптът `deploy.sh` автоматично:
- Проверява връзката към отдалечения сървър
- Създава резервно копие на съществуващия код
- Качва всички необходими файлове чрез rsync
- Инсталира зависимостите
- Рестартира услугата (ако е конфигурирана)

The `deploy.sh` script automatically:
- Tests connection to remote server
- Creates backup of existing code
- Uploads all necessary files via rsync
- Installs dependencies
- Restarts the service (if configured)

---

## 📋 Предварителни изисквания / Prerequisites

### На вашия локален компютър / On Your Local Computer

1. **SSH клиент** (вече инсталиран на Linux/macOS)
   - Windows: Използвайте Git Bash или WSL / Use Git Bash or WSL

2. **rsync инсталиран** / rsync installed
   ```bash
   # Проверка / Check if installed
   rsync --version
   
   # Инсталация / Installation
   # Ubuntu/Debian:
   sudo apt-get install rsync
   
   # macOS:
   brew install rsync
   
   # Windows (Git Bash):
   # rsync е включен в Git Bash
   ```

3. **Python 3.9+** (за локални тестове / for local tests)

### На отдалечения сървър / On Remote Server

1. **SSH достъп** / SSH access
2. **Python 3.9+** инсталиран / installed
3. **Достатъчно място на диска** (минимум 500MB)
4. **Права за писане** в целевата директория

---

## 🚀 Стъпка 1: Първоначална настройка / Initial Setup

### 1.1 Генериране на SSH ключ (препоръчително) / Generate SSH Key (Recommended)

Ако нямате SSH ключ, създайте един:
If you don't have an SSH key, create one:

```bash
# Генериране на нов SSH ключ / Generate new SSH key
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Копиране на ключа към сървъра / Copy key to server
ssh-copy-id -i ~/.ssh/id_rsa.pub user@your_server_ip
```

### 1.2 Тестване на SSH връзка / Test SSH Connection

```bash
# Тест на връзката / Test connection
ssh user@your_server_ip

# Ако работи, излезте / If it works, exit
exit
```

---

## ⚙️ Стъпка 2: Конфигурация / Configuration

### 2.1 Първоначално стартиране / First Run

Стартирайте скрипта първи път за създаване на конфигурационен файл:
Run the script first time to create configuration file:

```bash
cd /path/to/concierge
./deploy.sh
```

Това ще създаде `deploy.config` файл.
This will create a `deploy.config` file.

### 2.2 Редактиране на конфигурацията / Edit Configuration

Отворете и редактирайте `deploy.config`:
Open and edit `deploy.config`:

```bash
nano deploy.config
```

**Примерна конфигурация / Example Configuration:**

```bash
# SSH детайли на отдалечен сървър / Remote server SSH details
REMOTE_USER="cohen"
REMOTE_HOST="192.168.1.100"
REMOTE_PORT="22"
REMOTE_PATH="/var/www/concierge"

# SSH ключ (опционално) / SSH key (optional)
SSH_KEY_PATH="~/.ssh/id_rsa"

# Опции за качване / Deployment options
DRY_RUN="no"  # "yes" за тест без реално качване
BACKUP_REMOTE="yes"  # Създаване на резервно копие
RESTART_SERVICE="yes"  # Рестартиране на услугата

# Име на услугата / Service name
SERVICE_NAME="concierge"
```

**Важни полета / Important Fields:**

- `REMOTE_USER`: Вашето потребителско име на сървъра / Your username on server
- `REMOTE_HOST`: IP адрес или hostname на сървъра / Server IP or hostname
- `REMOTE_PORT`: SSH порт (обикновено 22) / SSH port (usually 22)
- `REMOTE_PATH`: Пътят на сървъра където да се качи проекта / Server path for project
- `SSH_KEY_PATH`: Път до SSH ключ (оставете празно за парола) / Path to SSH key (leave empty for password)

---

## 📤 Стъпка 3: Качване на проекта / Upload Project

### 3.1 Тестово качване (Dry Run)

Първо тествайте без реално качване:
First test without actual upload:

```bash
# Редактирайте deploy.config / Edit deploy.config
# Задайте: DRY_RUN="yes" / Set: DRY_RUN="yes"

./deploy.sh
```

Това ще покаже какво ще бъде качено БЕЗ да качва реално.
This will show what would be uploaded WITHOUT actually uploading.

### 3.2 Реално качване / Real Upload

Когато сте готови:
When you're ready:

```bash
# Редактирайте deploy.config / Edit deploy.config
# Задайте: DRY_RUN="no" / Set: DRY_RUN="no"

./deploy.sh
```

### 3.3 Какво се качва / What Gets Uploaded

**Качват се / Uploaded:**
- ✅ Всички Python файлове / All Python files
- ✅ HTML и frontend файлове / HTML and frontend files
- ✅ requirements.txt
- ✅ package.json
- ✅ Документация / Documentation
- ✅ .env.example (шаблон / template)

**НЕ се качват / NOT uploaded:**
- ❌ .env (API ключове - създайте го на сървъра!)
- ❌ venv/ (виртуална среда)
- ❌ __pycache__/ (cache файлове)
- ❌ *.log (log файлове)
- ❌ node_modules/ 
- ❌ .git/ (git история)
- ❌ *.pyc (compiled Python)

---

## 🔧 Стъпка 4: Настройка на сървъра / Server Setup

След качване на файловете, влезте в сървъра:
After uploading files, SSH to the server:

```bash
ssh user@your_server_ip
```

### 4.1 Създаване на .env файл / Create .env File

```bash
cd /var/www/concierge

# Копиране на шаблона / Copy template
cp .env.example .env

# Редактиране / Edit
nano .env
```

**Добавете вашите API ключове / Add your API keys:**

```env
OPENAI_API_KEY=sk-proj-your-actual-key-here
ELEVENLABS_API_KEY=your-actual-elevenlabs-key-here
```

### 4.2 Инсталиране на зависимости / Install Dependencies

```bash
# Създаване на виртуална среда / Create virtual environment
python3 -m venv venv

# Активиране / Activate
source venv/bin/activate

# Инсталиране / Install
pip install -r requirements.txt
```

### 4.3 Тестване на сървъра / Test Server

```bash
# Стартиране на сървъра / Start server
cd /var/www/concierge
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Отворете в браузър / Open in browser
# http://your_server_ip:8000/solomon.html
```

Ако работи, натиснете Ctrl+C и настройте като услуга.
If it works, press Ctrl+C and set up as service.

### 4.4 Настройка като systemd услуга / Setup as systemd Service

```bash
# Създаване на service файл / Create service file
sudo nano /etc/systemd/system/concierge.service
```

**Съдържание / Content:**

```ini
[Unit]
Description=Cohen House Concierge
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/concierge
Environment="PATH=/var/www/concierge/venv/bin"
ExecStart=/var/www/concierge/venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Активиране на услугата / Enable service:**

```bash
# Презареждане на systemd / Reload systemd
sudo systemctl daemon-reload

# Активиране / Enable
sudo systemctl enable concierge

# Стартиране / Start
sudo systemctl start concierge

# Проверка на статуса / Check status
sudo systemctl status concierge
```

---

## 🔄 Стъпка 5: Актуализация / Updates

Когато искате да актуализирате кода:
When you want to update the code:

```bash
# На локалния компютър / On local computer
cd /path/to/concierge

# Изтеглете последните промени / Pull latest changes
git pull origin main

# Качете на сървъра / Upload to server
./deploy.sh
```

Скриптът автоматично:
- Ще създаде резервно копие на старата версия
- Ще качи новите файлове
- Ще рестартира услугата

The script automatically:
- Creates backup of old version
- Uploads new files
- Restarts the service

---

## 🐛 Отстраняване на проблеми / Troubleshooting

### Проблем 1: SSH връзката не работи / SSH Connection Fails

**Решение / Solution:**

```bash
# Проверете връзката / Test connection
ssh -v user@your_server_ip

# Проверете SSH ключа / Check SSH key
ls -la ~/.ssh/
cat ~/.ssh/id_rsa.pub

# Копирайте ключа отново / Copy key again
ssh-copy-id user@your_server_ip
```

### Проблем 2: Permission Denied

**Решение / Solution:**

```bash
# Проверете правата / Check permissions
ls -la /var/www/

# Променете собственика / Change owner
sudo chown -R $USER:$USER /var/www/concierge

# Или използвайте sudo / Or use sudo
sudo ./deploy.sh
```

### Проблем 3: rsync не е инсталиран / rsync not installed

**Решение / Solution:**

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install rsync

# macOS
brew install rsync

# Проверка / Check
rsync --version
```

### Проблем 4: Услугата не стартира / Service Won't Start

**Решение / Solution:**

```bash
# Проверете логове / Check logs
sudo journalctl -u concierge -n 50

# Проверете .env файла / Check .env file
cat /var/www/concierge/.env

# Тест стартиране / Manual test
cd /var/www/concierge
source venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Проблем 5: Файловете не се качват / Files Not Uploading

**Решение / Solution:**

```bash
# Проверете rsync verbose / Check rsync verbose
rsync -avz --dry-run ./ user@server:/path/

# Проверете .gitignore / Check .gitignore
cat .gitignore

# Ръчно качване на конкретен файл / Manual upload specific file
scp app/main.py user@server:/var/www/concierge/app/
```

---

## 📊 Мониторинг / Monitoring

### Проверка на статуса / Check Status

```bash
# От локалния компютър / From local computer
ssh user@server "sudo systemctl status concierge"

# От сървъра / From server
sudo systemctl status concierge
```

### Преглед на логове / View Logs

```bash
# Последни 50 реда / Last 50 lines
sudo journalctl -u concierge -n 50

# Наблюдение в реално време / Follow in real-time
sudo journalctl -u concierge -f

# Логове за последния час / Logs from last hour
sudo journalctl -u concierge --since "1 hour ago"
```

### Проверка на използването / Check Usage

```bash
# CPU и RAM / CPU and RAM
top -u www-data

# Дисково пространство / Disk space
df -h

# Размер на директорията / Directory size
du -sh /var/www/concierge
```

---

## 🔐 Сигурност / Security

### Checklist за сигурност / Security Checklist

- [ ] ✅ SSH ключове вместо пароли / SSH keys instead of passwords
- [ ] ✅ .env файл с правилни permissions (600)
- [ ] ✅ Firewall конфигуриран / Firewall configured
- [ ] ✅ Само необходимите портове отворени / Only necessary ports open
- [ ] ✅ Редовни резервни копия / Regular backups
- [ ] ✅ SSL/HTTPS за production

### Настройка на firewall / Firewall Setup

```bash
# Ubuntu UFW
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 8000/tcp # Application
sudo ufw enable

# Проверка / Check
sudo ufw status
```

### Permissions за .env / .env Permissions

```bash
# Ограничете достъпа / Restrict access
chmod 600 /var/www/concierge/.env
chown www-data:www-data /var/www/concierge/.env
```

---

## 📝 Полезни команди / Useful Commands

### Бърза актуализация / Quick Update

```bash
# Локално / Local
git pull && ./deploy.sh
```

### Рестартиране / Restart Service

```bash
# От локален компютър / From local computer
ssh user@server "sudo systemctl restart concierge"

# От сървъра / From server
sudo systemctl restart concierge
```

### Резервно копие / Backup

```bash
# Ръчно резервно копие / Manual backup
ssh user@server "tar -czf ~/concierge_backup_$(date +%Y%m%d).tar.gz /var/www/concierge"

# Изтегляне на резервното копие / Download backup
scp user@server:~/concierge_backup_*.tar.gz ./
```

### Преглед на файлове / View Files

```bash
# Преглед на файл / View file
ssh user@server "cat /var/www/concierge/app/main.py"

# Редактиране на файл / Edit file
ssh user@server "nano /var/www/concierge/.env"
```

---

## 🎓 Примери за използване / Usage Examples

### Пример 1: Първоначално качване / Initial Deployment

```bash
# 1. Клониране на проекта / Clone project
git clone https://github.com/CohenNathan/concierge.git
cd concierge

# 2. Първоначално стартиране / First run
./deploy.sh
# Това ще създаде deploy.config

# 3. Редактиране на конфигурацията / Edit config
nano deploy.config
# Добавете вашите SSH детайли

# 4. Тестово качване / Dry run
# В deploy.config: DRY_RUN="yes"
./deploy.sh

# 5. Реално качване / Real upload
# В deploy.config: DRY_RUN="no"
./deploy.sh

# 6. Настройка на сървъра / Server setup
ssh user@server
cd /var/www/concierge
cp .env.example .env
nano .env  # Добавете API ключове
pip install -r requirements.txt
```

### Пример 2: Актуализация на код / Code Update

```bash
# Локално / Local
cd concierge
git pull origin main
./deploy.sh

# Услугата се рестартира автоматично
# Service restarts automatically
```

### Пример 3: Качване на конкретни файлове / Upload Specific Files

```bash
# Ако искате да качите само един файл / If you want to upload just one file
scp app/openai_assistant.py user@server:/var/www/concierge/app/

# Рестартиране / Restart
ssh user@server "sudo systemctl restart concierge"
```

---

## 📞 Поддръжка / Support

### Документация / Documentation

- **README.md** - Общ преглед / Overview
- **DEPLOYMENT.md** - Production настройка
- **LOCAL_DEPLOYMENT_GUIDE.md** - Локална настройка
- **SSH_DEPLOYMENT_GUIDE.md** - Този файл / This file

### Помощ / Help

```bash
# Помощ за скрипта / Script help
./deploy.sh --help

# Проверка на версията / Check version
cat README.md | grep "Last Updated"
```

### Контакти / Contacts

- **GitHub**: https://github.com/CohenNathan/concierge
- **Issues**: https://github.com/CohenNathan/concierge/issues
- **Email**: info@cohenhouse.com

---

## ✅ Checklist за успешно качване / Successful Deployment Checklist

След качване проверете:
After deployment, verify:

- [ ] ✅ Файловете са качени на сървъра / Files uploaded to server
- [ ] ✅ .env файл създаден с API ключове / .env file created with API keys
- [ ] ✅ Зависимостите инсталирани / Dependencies installed
- [ ] ✅ Услугата стартирана / Service started
- [ ] ✅ Интерфейсът се зарежда / Interface loads
- [ ] ✅ WebSocket работи / WebSocket works
- [ ] ✅ Voice recognition работи / Voice recognition works
- [ ] ✅ Логовете са чисти (без грешки) / Logs are clean (no errors)

---

## 🎉 Готово! / Done!

Вашият проект е качен и работи на отдалечения сървър!
Your project is uploaded and running on the remote server!

**Достъп / Access:**
```
http://your_server_ip:8000/solomon.html
```

**Мониторинг / Monitoring:**
```bash
ssh user@server "sudo journalctl -u concierge -f"
```

---

**Последна актуализация / Last Updated:** December 22, 2025  
**Версия / Version:** 1.0.0  
**Cohen House Concierge** 🏛️🐻✨
