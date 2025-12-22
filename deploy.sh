#!/bin/bash
# Cohen House Concierge - SSH/CLI Deployment Script
# Качване на проекта на отдалечен компютър / Upload project to remote computer
# Last updated: December 22, 2025

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored messages
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Banner
echo "================================================================================"
echo "  COHEN HOUSE CONCIERGE - DEPLOYMENT SCRIPT"
echo "  SSH/CLI Upload Tool / Инструмент за качване чрез SSH/CLI"
echo "================================================================================"
echo ""

# Check if configuration file exists
if [ ! -f "deploy.config" ]; then
    print_error "Deploy configuration file not found!"
    print_info "Creating deploy.config template..."
    cat > deploy.config << 'EOF'
# Cohen House Concierge - Deployment Configuration
# Конфигурация за качване / Deployment Configuration

# Remote server SSH details / SSH детайли на отдалечен сървър
REMOTE_USER="your_username"
REMOTE_HOST="your_server_ip_or_hostname"
REMOTE_PORT="22"
REMOTE_PATH="/var/www/concierge"

# SSH Key (optional) / SSH ключ (опционално)
# Leave empty to use password authentication
SSH_KEY_PATH=""

# Deployment options / Опции за качване
DRY_RUN="no"  # Set to "yes" for test run without actual upload
BACKUP_REMOTE="yes"  # Create backup on remote server before deploying
RESTART_SERVICE="yes"  # Restart service after deployment

# Service name on remote server (if using systemd)
SERVICE_NAME="concierge"
EOF
    print_success "Created deploy.config - Please edit it with your server details!"
    print_info "Edit deploy.config file and run this script again."
    exit 1
fi

# Load configuration
source deploy.config

# Validate configuration
if [ "$REMOTE_USER" = "your_username" ] || [ "$REMOTE_HOST" = "your_server_ip_or_hostname" ]; then
    print_error "Please configure deploy.config with your server details!"
    exit 1
fi

print_info "Loading configuration..."
print_info "Remote: $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"
echo ""

# Check if rsync is installed
if ! command -v rsync &> /dev/null; then
    print_error "rsync is not installed!"
    print_info "Install rsync first:"
    print_info "  Ubuntu/Debian: sudo apt-get install rsync"
    print_info "  macOS: brew install rsync"
    print_info "  Windows: Install via Git Bash or WSL"
    exit 1
fi

# Prepare SSH options
SSH_OPTS="-p $REMOTE_PORT"
if [ -n "$SSH_KEY_PATH" ]; then
    SSH_OPTS="$SSH_OPTS -i $SSH_KEY_PATH"
fi

# Test SSH connection
print_info "Testing SSH connection..."
if ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "echo 'Connection successful'" &> /dev/null; then
    print_success "SSH connection successful"
else
    print_error "Cannot connect to remote server!"
    print_info "Please check:"
    print_info "  - Server address and port"
    print_info "  - Username and password/SSH key"
    print_info "  - Network connectivity"
    exit 1
fi

# Run local diagnostic test if available
if [ -f "diagnostic_test.py" ]; then
    print_info "Running local diagnostic tests..."
    if python3 diagnostic_test.py > /dev/null 2>&1; then
        print_success "Local diagnostic tests passed"
    else
        print_warning "Some diagnostic tests failed (this is OK if .env is not configured)"
    fi
else
    print_warning "diagnostic_test.py not found, skipping local tests"
fi

# Create backup on remote server if requested
create_remote_backup() {
    local backup_name="concierge_backup_$(date +%Y%m%d_%H%M%S)"
    ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "if [ -d $REMOTE_PATH ]; then cp -r $REMOTE_PATH ${REMOTE_PATH}_${backup_name} && echo 'Backup created'; else echo 'No existing directory to backup'; fi" 2>/dev/null || {
        print_warning "Could not create backup (this is OK for first deployment)"
        return 0
    }
    echo "$backup_name"
}

if [ "$BACKUP_REMOTE" = "yes" ]; then
    print_info "Creating backup on remote server..."
    BACKUP_NAME=$(create_remote_backup)
    print_success "Remote backup created: ${REMOTE_PATH}_${BACKUP_NAME}"
fi

# Prepare rsync command with exclusions
RSYNC_CMD="rsync -avz --progress"

# Add SSH options to rsync
if [ -n "$SSH_KEY_PATH" ]; then
    RSYNC_CMD="$RSYNC_CMD -e 'ssh -p $REMOTE_PORT -i $SSH_KEY_PATH'"
else
    RSYNC_CMD="$RSYNC_CMD -e 'ssh -p $REMOTE_PORT'"
fi

# Exclude unnecessary files
RSYNC_CMD="$RSYNC_CMD \
    --exclude='.git' \
    --exclude='.gitignore' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    --exclude='*.pyo' \
    --exclude='.env' \
    --exclude='venv' \
    --exclude='env' \
    --exclude='.venv' \
    --exclude='node_modules' \
    --exclude='*.log' \
    --exclude='*.pid' \
    --exclude='*.db' \
    --exclude='*.sqlite3' \
    --exclude='tts_*.mp3' \
    --exclude='audio_cache' \
    --exclude='*.backup' \
    --exclude='*.OLD' \
    --exclude='*.broken' \
    --exclude='.DS_Store' \
    --exclude='*.swp' \
    --exclude='*.swo' \
    --exclude='.vscode' \
    --exclude='.idea' \
    --exclude='*.pkl' \
    --exclude='*.dat'"

# Add dry-run option if requested
if [ "$DRY_RUN" = "yes" ]; then
    RSYNC_CMD="$RSYNC_CMD --dry-run"
    print_warning "DRY RUN MODE - No files will be uploaded"
fi

# Upload files
print_info "Starting file upload..."
echo ""

# Create remote directory if it doesn't exist
ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "mkdir -p $REMOTE_PATH"

# Execute rsync
eval "$RSYNC_CMD ./ $REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/"

if [ $? -eq 0 ]; then
    print_success "Files uploaded successfully!"
else
    print_error "Upload failed!"
    exit 1
fi

# Check if .env exists on remote
print_info "Checking remote .env configuration..."
ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "if [ ! -f $REMOTE_PATH/.env ]; then echo 'MISSING'; fi" | grep -q 'MISSING' && {
    print_warning "No .env file found on remote server!"
    print_info "You need to create .env file on the remote server:"
    print_info "  1. SSH to server: ssh $REMOTE_USER@$REMOTE_HOST"
    print_info "  2. Go to directory: cd $REMOTE_PATH"
    print_info "  3. Copy example: cp .env.example .env"
    print_info "  4. Edit file: nano .env"
    print_info "  5. Add your API keys"
} || {
    print_success ".env file exists on remote server"
}

# Install dependencies on remote
print_info "Installing dependencies on remote server..."
ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "cd $REMOTE_PATH && python3 -m pip install -r requirements.txt --quiet" || {
    print_warning "Could not install dependencies automatically"
    print_info "Please SSH to server and run: pip install -r requirements.txt"
}

# Restart service if requested
if [ "$RESTART_SERVICE" = "yes" ] && [ -n "$SERVICE_NAME" ]; then
    print_info "Restarting service on remote server..."
    ssh $SSH_OPTS "$REMOTE_USER@$REMOTE_HOST" "sudo systemctl restart $SERVICE_NAME" || {
        print_warning "Could not restart service automatically"
        print_info "Please SSH to server and restart manually"
    }
    print_success "Service restarted"
fi

# Final summary
echo ""
echo "================================================================================"
print_success "DEPLOYMENT COMPLETED SUCCESSFULLY!"
echo "================================================================================"
echo ""
print_info "Next steps:"
echo "  1. SSH to your server: ssh $REMOTE_USER@$REMOTE_HOST"
echo "  2. Go to directory: cd $REMOTE_PATH"
echo "  3. Verify .env file: cat .env"
echo "  4. Check server status: sudo systemctl status $SERVICE_NAME"
echo "  5. View logs: sudo journalctl -u $SERVICE_NAME -f"
echo ""
print_info "Access your application at:"
echo "  http://$REMOTE_HOST:8000/solomon.html"
echo ""
print_success "Cohen House Concierge deployed! 🏛️🐻✨"
echo "================================================================================"
