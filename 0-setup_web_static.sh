#!/usr/bin/env bash
# This script sets up an Nginx web server for the deployment of a static website.
# It creates the necessary directories, files, and symbolic link,
# and configures Nginx to serve the static files from the correct directory.
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

WEB_ROOT_DIR="/data/web_static"
RELEASES_DIR="${WEB_ROOT_DIR}/releases"
SHARED_DIR="${WEB_ROOT_DIR}/shared"
CURRENT_DIR="${WEB_ROOT_DIR}/current"
TEST_RELEASE_DIR="${RELEASES_DIR}/test"
INDEX_FILE="${TEST_RELEASE_DIR}/index.html"

sudo mkdir -p "${RELEASES_DIR}" "${SHARED_DIR}" "${TEST_RELEASE_DIR}"
sudo touch "${INDEX_FILE}"
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "${INDEX_FILE}" > /dev/null

sudo ln -s -f "${TEST_RELEASE_DIR}" "${CURRENT_DIR}"
sudo chown -R ubuntu:ubuntu "${WEB_ROOT_DIR}"

NGINX_CONF_FILE="/etc/nginx/sites-enabled/default"
NGINX_CONF_BLOCK="location /hbnb_static { alias ${CURRENT_DIR}/; }"
sudo sed -i "/listen 80 default_server/a ${NGINX_CONF_BLOCK}" "${NGINX_CONF_FILE}"
sudo service nginx restart
