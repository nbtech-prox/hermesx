#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}[1/7]${NC} Instalando dependências do sistema..."
sudo apt update
sudo apt install apache2 python3.10 python3.10-venv python3-pip libapache2-mod-wsgi-py3 chromium-browser chromium-chromedriver apache2-utils -y

echo -e "${BLUE}[2/7]${NC} Criando estrutura de diretórios..."
sudo mkdir -p /var/www/html/hermesx
sudo mkdir -p /var/www/html/hermesx/uploads
sudo mkdir -p /var/www/html/hermesx/chrome_data

echo -e "${BLUE}[3/7]${NC} Copiando arquivos do projeto..."
sudo cp -r ./* /var/www/html/hermesx/
sudo cp hermesx-pre-ssl.conf /etc/apache2/sites-available/hermesx.conf

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
# Habilitar módulos necessários
sudo a2enmod headers
sudo a2enmod remoteip
sudo a2enmod wsgi
sudo a2enmod rewrite
sudo a2ensite hermesx.conf

# Configurar IPs do Cloudflare
echo "# Cloudflare IP Ranges
# IPv4
$(curl -s https://www.cloudflare.com/ips-v4) 
# IPv6
$(curl -s https://www.cloudflare.com/ips-v6)" | sudo tee /etc/apache2/conf-available/cloudflare.conf

sudo a2enconf cloudflare

echo -e "${BLUE}[7/7]${NC} Testando configuração do Apache..."
sudo apache2ctl configtest
if [ $? -eq 0 ]; then
    sudo systemctl restart apache2
else
    echo "Erro na configuração do Apache. Verifique os logs."
    exit 1
fi

# Obter IP do servidor
SERVER_IP=$(curl -s ifconfig.me)

echo -e "\n${YELLOW}Deploy básico concluído!${NC}"
echo -e "\n${YELLOW}PRÓXIMOS PASSOS NO CLOUDFLARE:${NC}"
echo -e "1. No painel do Cloudflare (${BLUE}https://dash.cloudflare.com${NC}):"
echo -e "   - Adicione os registros DNS:"
echo -e "     ${BLUE}hermesx.nbserver.pt${NC} -> ${GREEN}A Record${NC} -> ${SERVER_IP}"
echo -e "     ${BLUE}www.hermesx.nbserver.pt${NC} -> ${GREEN}CNAME Record${NC} -> ${BLUE}hermesx.nbserver.pt${NC}"
echo -e "\n2. Configure o SSL/TLS no Cloudflare:"
echo -e "   - Vá para SSL/TLS > Overview"
echo -e "   - Defina o modo como '${GREEN}Full${NC}'"
echo -e "   - Em Edge Certificates, ative:"
echo -e "     * Always Use HTTPS"
echo -e "     * Auto Minify"
echo -e "     * Brotli"
echo -e "\n3. Configure as Page Rules:"
echo -e "   - Adicione uma regra para forçar HTTPS:"
echo -e "     * URL: ${BLUE}*hermesx.nbserver.pt/*${NC}"
echo -e "     * Setting: Always Use HTTPS"
echo -e "\n${BLUE}Logs do Apache:${NC}"
echo "/var/log/apache2/hermesx_error.log"
echo "/var/log/apache2/hermesx_access.log"
