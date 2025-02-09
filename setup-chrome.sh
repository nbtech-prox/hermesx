#!/bin/bash

# Verificar se está rodando como root
if [ "$EUID" -ne 0 ]; then 
    echo "Este script precisa ser executado como root"
    exit 1
fi

echo "Configurando ambiente de produção para Chrome..."

# Criar diretório com permissões restritas
echo "Configurando diretórios..."
rm -rf /var/www/html/hermesx/chrome_data
install -d -m 750 -o www-data -g www-data /var/www/html/hermesx/chrome_data
install -d -m 750 -o www-data -g www-data /var/www/html/hermesx/chrome_data/cache

# Verificar e instalar dependências
echo "Verificando dependências..."
apt-get update
apt-get install -y chromium-browser chromium-chromedriver

# Configurar limites de sistema
echo "Configurando limites do sistema..."
cat << EOF > /etc/security/limits.d/chrome.conf
www-data soft nofile 65535
www-data hard nofile 65535
www-data soft nproc 4096
www-data hard nproc 4096
EOF

# Configurar diretório temporário
echo "Configurando diretório temporário..."
install -d -m 750 -o www-data -g www-data /tmp/chrome
chmod 750 /tmp/chrome

# Reiniciar serviços
echo "Reiniciando serviços..."
systemctl daemon-reload
systemctl restart apache2

echo "Configuração de produção concluída!"
echo "Verifique os logs do Apache para garantir que tudo está funcionando corretamente."
