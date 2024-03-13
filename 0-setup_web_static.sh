#!/usr/bin/env bash

# Install Nginx if it's not already installed
if ! dpkg -s nginx >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create required directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "Hello L3alam" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or update symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership and permissions
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo tee /etc/nginx/sites-available/default > /dev/null << EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

# Restart Nginx
sudo systemctl restart nginx
