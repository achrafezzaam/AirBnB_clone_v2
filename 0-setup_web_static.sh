#!/usr/bin/env bash
# Setting up the web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo '<!DOCTYPE html><html><head></head><body><h1>Hello World!</h1></body></html>' > /data/web_static/releases/test/index.html

if [ -d "/data/web_static/current" ];
then
    sudo rm -rf /data/web_static/current;
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

sudo service nginx restart
