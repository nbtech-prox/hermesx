#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}[1/8]${NC} Instalando dependências do sistema..."
sudo apt update
sudo apt install apache2 python3.10 python3.10-venv python3-pip libapache2-mod-wsgi-py3 chromium-browser chromium-chromedriver certbot python3-certbot-apache -y

echo -e "${BLUE}[2/8]${NC} Criando estrutura de diretórios..."
sudo mkdir -p /var/www/html/hermesx
sudo mkdir -p /var/www/html/hermesx/uploads
sudo mkdir -p /var/www/html/hermesx/chrome_data

echo -e "${BLUE}[3/8]${NC} Copiando arquivos do projeto..."
sudo cp -r ./* /var/www/html/hermesx/
sudo cp hermesx-pre-ssl.conf /etc/apache2/sites-available/hermesx.conf

echo -e "${BLUE}[4/8]${NC} Configurando ambiente virtual..."
cd /var/www/html/hermesx
python3.10 -m venv env
source env/bin/activate
pip install -r requirements.txt
deactivate

echo -e "${BLUE}[5/8]${NC} Configurando permissões..."
sudo chown -R www-data:www-data /var/www/html/hermesx
sudo chmod -R 755 /var/www/html/hermesx
sudo chmod -R 775 /var/www/html/hermesx/uploads
sudo chmod -R 775 /var/www/html/hermesx/chrome_data

echo -e "${BLUE}[6/8]${NC} Configurando Apache (pré-SSL)..."
sudo a2enmod ssl
sudo a2enmod headers
sudo a2enmod wsgi
sudo a2enmod rewrite
sudo a2ensite hermesx.conf

echo -e "${BLUE}[7/8]${NC} Testando configuração inicial do Apache..."
sudo apache2ctl configtest
if [ $? -eq 0 ]; then
    sudo systemctl restart apache2
else
    echo "Erro na configuração do Apache. Verifique os logs."
    exit 1
fi

echo -e "${BLUE}[8/8]${NC} Configurando SSL com Certbot..."
sudo certbot --apache --non-interactive --agree-tos --email nbtech.prox@gmail.com -d hermesx.nbserver.pt -d www.hermesx.nbserver.pt

echo -e "${GREEN}Deploy concluído!${NC}"
echo -e "${BLUE}Verifique os logs em:${NC}"
echo "/var/log/apache2/hermesx_error.log"
echo "/var/log/apache2/hermesx_access.log"
