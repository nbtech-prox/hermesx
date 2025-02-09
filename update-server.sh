#!/bin/bash

echo "Atualizando dependências do sistema..."
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver

echo "Configurando diretórios..."
sudo rm -rf /tmp/chrome_data
sudo mkdir -p /tmp/chrome_data
sudo chown -R www-data:www-data /tmp/chrome_data
sudo chmod 755 /tmp/chrome_data

echo "Instalando dependências Python..."
cd /var/www/html/hermesx
source env/bin/activate
pip install -r requirements.txt

echo "Configurando limites do sistema..."
sudo bash -c 'cat > /etc/security/limits.d/chrome.conf << EOL
www-data soft nofile 65535
www-data hard nofile 65535
www-data soft nproc 4096
www-data hard nproc 4096
EOL'

echo "Reiniciando Apache..."
sudo systemctl restart apache2

echo "Verificando status..."
systemctl status apache2

echo "Verificando logs do Apache..."
tail -n 50 /var/log/apache2/error.log
