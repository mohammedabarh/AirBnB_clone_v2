#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

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

# Give ownership of the /data/ folder to the www-data user
sudo chown -R www-data:www-data /data/

# Update Nginx configuration to serve the content
sudo sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
