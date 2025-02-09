#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[1/7]${NC} Instalando dependências do sistema..."
sudo apt update
sudo apt install apache2 python3.10 python3.10-venv python3-pip libapache2-mod-wsgi-py3 chromium-browser chromium-chromedriver -y

echo -e "${BLUE}[2/7]${NC} Criando estrutura de diretórios..."
sudo mkdir -p /var/www/html/hermesx
sudo mkdir -p /var/www/html/hermesx/uploads
sudo mkdir -p /var/www/html/hermesx/chrome_data

echo -e "${BLUE}[3/7]${NC} Copiando arquivos do projeto..."
sudo cp -r ./* /var/www/html/hermesx/
sudo cp hermesx.conf /etc/apache2/sites-available/

echo -e "${BLUE}[4/7]${NC} Configurando ambiente virtual..."
cd /var/www/html/hermesx
python3.10 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate

echo -e "${BLUE}[5/7]${NC} Configurando permissões..."
sudo chown -R www-data:www-data /var/www/html/hermesx
sudo chmod -R 755 /var/www/html/hermesx
sudo chmod -R 775 /var/www/html/hermesx/uploads
sudo chmod -R 775 /var/www/html/hermesx/chrome_data

echo -e "${BLUE}[6/7]${NC} Configurando Apache..."
sudo a2enmod ssl
sudo a2enmod headers
sudo a2enmod wsgi
sudo a2enmod rewrite
sudo a2ensite hermesx.conf

echo -e "${BLUE}[7/7]${NC} Obtendo certificado SSL..."
sudo certbot --apache -d hermesx.nbserver.pt -d www.hermesx.nbserver.pt

echo -e "${BLUE}Testando configuração do Apache...${NC}"
sudo apache2ctl configtest

echo -e "${BLUE}Reiniciando Apache...${NC}"
sudo systemctl restart apache2

echo -e "${GREEN}Deploy concluído!${NC}"
echo -e "${BLUE}Verifique os logs em:${NC}"
echo "/var/log/apache2/hermesx_error.log"
echo "/var/log/apache2/hermesx_access.log"
