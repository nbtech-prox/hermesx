import sys
import os

# Ajuste o caminho para o diretório do seu projeto
project_dir = '/var/www/html/hermesx'
sys.path.insert(0, project_dir)

# Adicione o caminho do virtualenv ao Python path
python_home = '/var/www/html/hermesx/env'
python_path = os.path.join(python_home, 'lib', 'python3.10', 'site-packages')
sys.path.insert(1, python_path)

# Carrega variáveis de ambiente
from dotenv import load_dotenv
load_dotenv(os.path.join(project_dir, '.env'))

from app import create_app
application = create_app()
