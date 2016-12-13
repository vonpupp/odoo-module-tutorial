#!/usr/bin/env bash

# Principais
sudo apt-get install -y git python2.7 postgresql nano python-virtualenv xfonts-75dpi
# Build
sudo apt-get install -y gcc python2.7-dev libxml2-dev \
    libxslt1-dev libevent-dev libsasl2-dev libldap2-dev libpq-dev \
    libpng12-dev libjpeg-dev libxmlsec1-dev
# Ubuntu xenial
sudo apt-get install -y nodejs-legacy
sudo apt-get install -y fontconfig xfonts-base
sudo apt-get install -y wkhtmltopdf
# Node
sudo apt-get install -y npm
sudo npm install -g less
# Postgres
sudo -u postgres createuser --createdb $(whoami)
createdb $(whoami)
# Relatórios
mkdir /tmp/odoo
cd /tmp/odoo
wget http://ftp.us.debian.org/debian/pool/main/libj/libjpeg-turbo/libjpeg62-turbo_1.3.1-12_amd64.deb
# wget http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb
# Tem biblioteca diretamente do wkhtmltopdf
sudo dpkg -i *.deb
