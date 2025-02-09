#!/bin/bash

# Desabilitar sites existentes
sudo a2dissite *.conf

# Copiar nova configuração
sudo cp 001-hermesx.conf /etc/apache2/sites-available/

# Habilitar apenas o site do Hermesx
sudo a2ensite 001-hermesx.conf

# Recarregar Apache
sudo systemctl reload apache2

# Mostrar status
sudo apache2ctl -S
