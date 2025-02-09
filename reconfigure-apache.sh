#!/bin/bash

echo "Removendo configurações antigas..."
sudo rm -f /etc/apache2/sites-enabled/001-hermesx.conf
sudo rm -f /etc/apache2/sites-available/001-hermesx.conf

echo "Copiando nova configuração..."
sudo cp 001-hermesx.conf /etc/apache2/sites-available/

echo "Habilitando módulos necessários..."
sudo a2enmod headers
sudo a2enmod rewrite
sudo a2enmod wsgi

echo "Habilitando site..."
sudo a2ensite 001-hermesx.conf

echo "Testando configuração..."
sudo apache2ctl configtest

if [ $? -eq 0 ]; then
    echo "Configuração OK. Reiniciando Apache..."
    sudo systemctl restart apache2
    echo "Verificando status do Apache..."
    sudo systemctl status apache2
else
    echo "Erro na configuração do Apache!"
    exit 1
fi
