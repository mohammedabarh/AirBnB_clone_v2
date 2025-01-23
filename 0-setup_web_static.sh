#!/usr/bin/env bash
# Script to set up web servers for the deployment of web_static

# Update package list
sudo apt-get update

# Install Nginx web server
sudo apt-get -y install nginx

# Allow HTTP traffic through the firewall
sudo ufw allow 'Nginx HTTP'

# Create base directory structure for web_static
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a test HTML file
sudo touch /data/web_static/releases/test/index.html

# Write a simple HTML page into the test file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link pointing to the test release
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from the web_static directory
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply changes
sudo service nginx restart
