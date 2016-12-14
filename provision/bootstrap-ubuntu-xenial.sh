#!/usr/bin/env bash

# Atualizar pacotes
sudo apt-get update

# Pacotes principais
sudo apt-get install -y git python2.7 postgresql nano python-virtualenv \
    xfonts-75dpi wget postgresql

# Banco de dados
sudo systemctl enable postgresql
sudo systemctl restart postgresql
sudo -u postgres createuser --createdb $(whoami)
createdb $(whoami)

# Bibliotecas e pacotes de desenvolvimento
sudo apt-get install -y gcc python2.7-dev libxml2-dev \
    libxslt1-dev libevent-dev libsasl2-dev libldap2-dev libpq-dev \
    libpng12-dev libjpeg-dev libxmlsec1-dev

# Pacotes especificos do ubuntu xenial
sudo apt-get install -y nodejs-legacy
sudo apt-get install -y fontconfig xfonts-base
sudo apt-get install -y wkhtmltopdf

# Node e dependencias
sudo apt-get install -y npm
sudo npm install -g less

# Relatórios
mkdir /tmp/odoo
cd /tmp/odoo
wget http://ftp.us.debian.org/debian/pool/main/libj/libjpeg-turbo/libjpeg62-turbo_1.3.1-12_amd64.deb
# wget http://nightly.odoo.com/extra/wkhtmltox-0.12.1.2_linux-jessie-amd64.deb
# Tem biblioteca diretamente do wkhtmltopdf no xenial
sudo dpkg -i *.deb
