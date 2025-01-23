#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Install Nginx if it is not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
echo "server {
    listen 80;
    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
