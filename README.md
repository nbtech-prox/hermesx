# HermesX 🚀

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)](https://flask.palletsprojects.com/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-orange.svg)](https://www.selenium.dev/)

[English](#english) | [Português](#português)

# English 🇺🇸

## 🌟 Overview
HermesX is a powerful WhatsApp automation platform that enables automated message sending through WhatsApp Web. Built with Flask and Selenium, it provides a user-friendly interface for sending individual messages or bulk messaging through CSV file uploads. Perfect for businesses and organizations needing to manage customer communications efficiently.

## ✨ Key Features

### 📱 WhatsApp Integration
- 🤖 Automated WhatsApp Web integration
- 📨 Individual message sending
- 📊 Bulk message sending via CSV
- ⚡ Rate limiting for safe automation
- 🌍 International phone number support

### 📊 Contact Management
- 📁 CSV file upload for bulk contacts
- ✅ Phone number validation
- 🔄 Automatic country code handling
- 📈 Delivery status tracking
- 📋 Results reporting

### 🛡️ Security Features
- 🔒 Secure WhatsApp Web session handling
- 🔐 Environment-based configuration
- 🛡️ Protected file uploads
- ⚠️ Rate limiting protection
- 🔍 Phone number validation

## 🚀 Getting Started

### 📋 Prerequisites
- Python 3.x
- Google Chrome (latest stable version)
- pip (Python package manager)

### ⚙️ Chrome Setup
1. Install the latest stable version of Google Chrome
2. The application will automatically:
   - Create a Chrome user profile in `chrome_data/`
   - Handle ChromeDriver installation
   - Manage WhatsApp Web sessions

### 🔧 Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/hermesx.git
cd hermesx
```

2. Create and activate virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📱 Usage

### First Run
1. Start the application:
```bash
python run.py
```

2. Access the web interface at `http://localhost:5000`
3. When first launched, scan the WhatsApp QR code to authenticate
4. Your session will be saved for future use

### Sending Messages

#### Individual Messages
1. Fill in the contact name
2. Enter the phone number
3. Type your message
4. Click "Send"

#### Bulk Messages (CSV)
1. Prepare your CSV file with columns:
   ```csv
   nome,numero
   João Silva,5511999999999
   Maria Santos,11988888888
   ```
2. Upload the CSV file
3. Type your message
4. Click "Send to All"

## 🏗️ Project Structure
```
hermesx/
├── app/                # Application package
│   ├── __init__.py     # App initialization
│   ├── routes.py       # URL routes and views
│   ├── utils/          # Utility functions
│   │   ├── whatsapp.py     # WhatsApp automation
│   │   ├── csv_handler.py  # CSV processing
│   │   └── validators.py   # Input validation
│   ├── static/         # Static files
│   └── templates/      # HTML templates
├── uploads/           # Upload directory (temporary)
├── chrome_data/       # Chrome profile data
├── config.py         # Configuration
├── requirements.txt  # Python dependencies
└── run.py           # Application entry point
```

## ⚠️ Rate Limiting
To prevent WhatsApp from blocking your account:
- Default delay between messages: 3 seconds
- Recommended daily limit: 200 messages
- Use appropriate delays for bulk sending

## 🔍 Troubleshooting

### Common Issues
1. **QR Code Not Scanning**
   - Clear Chrome profile: Delete `chrome_data/` folder
   - Restart application
   - Try scanning again

2. **Message Not Sending**
   - Verify internet connection
   - Check phone number format
   - Ensure WhatsApp Web is connected

3. **Chrome Issues**
   - Update Chrome to latest version
   - Clear Chrome profile
   - Check system resources

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.

This means:
- ✅ Commercial use allowed
- ✅ Modifications allowed
- ✅ Distribution allowed
- ❗ Source code must be disclosed
- ❗ Same license required
- ❗ License and copyright notice required

---

# Português 🇧🇷

## 🌟 Visão Geral
HermesX é uma poderosa plataforma de automação do WhatsApp que permite o envio automatizado de mensagens através do WhatsApp Web. Construída com Flask e Selenium, oferece uma interface amigável para envio de mensagens individuais ou em massa através de arquivos CSV. Perfeita para empresas e organizações que precisam gerenciar comunicações com clientes de forma eficiente.

## ✨ Principais Funcionalidades

### 📱 Integração com WhatsApp
- 🤖 Integração automatizada com WhatsApp Web
- 📨 Envio de mensagens individuais
- 📊 Envio em massa via CSV
- ⚡ Limitação de taxa para automação segura
- 🌍 Suporte a números internacionais

### 📊 Gestão de Contatos
- 📁 Upload de arquivo CSV para contatos em massa
- ✅ Validação de números de telefone
- 🔄 Tratamento automático de códigos de país
- 📈 Rastreamento de status de entrega
- 📋 Relatório de resultados

### 🛡️ Recursos de Segurança
- 🔒 Gerenciamento seguro de sessão do WhatsApp Web
- 🔐 Configuração baseada em ambiente
- 🛡️ Upload de arquivos protegido
- ⚠️ Proteção contra excesso de requisições
- 🔍 Validação de números de telefone

## 🚀 Começando

### 📋 Pré-requisitos
- Python 3.x
- Google Chrome (última versão estável)
- pip (gerenciador de pacotes Python)

### ⚙️ Configuração do Chrome
1. Instale a última versão estável do Google Chrome
2. A aplicação automaticamente:
   - Cria um perfil do Chrome em `chrome_data/`
   - Gerencia a instalação do ChromeDriver
   - Administra as sessões do WhatsApp Web

### 🔧 Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/hermesx.git
cd hermesx
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv env
source env/bin/activate  # No Windows use: env\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📱 Uso

### Primeira Execução
1. Inicie a aplicação:
```bash
python run.py
```

2. Acesse a interface web em `http://localhost:5000`
3. Na primeira execução, escaneie o QR code do WhatsApp para autenticar
4. Sua sessão será salva para uso futuro

### Enviando Mensagens

#### Mensagens Individuais
1. Preencha o nome do contato
2. Digite o número do telefone
3. Digite sua mensagem
4. Clique em "Enviar"

#### Mensagens em Massa (CSV)
1. Prepare seu arquivo CSV com as colunas:
   ```csv
   nome,numero
   João Silva,5511999999999
   Maria Santos,11988888888
   ```
2. Faça upload do arquivo CSV
3. Digite sua mensagem
4. Clique em "Enviar para Todos"

## 🏗️ Estrutura do Projeto
```
hermesx/
├── app/                # Pacote da aplicação
│   ├── __init__.py     # Inicialização da app
│   ├── routes.py       # Rotas e views
│   ├── utils/          # Funções utilitárias
│   │   ├── whatsapp.py     # Automação WhatsApp
│   │   ├── csv_handler.py  # Processamento CSV
│   │   └── validators.py   # Validação de entrada
│   ├── static/         # Arquivos estáticos
│   └── templates/      # Templates HTML
├── uploads/           # Diretório de upload (temporário)
├── chrome_data/       # Dados do perfil Chrome
├── config.py         # Configuração
├── requirements.txt  # Dependências Python
└── run.py           # Ponto de entrada da aplicação
```

## ⚠️ Limitação de Taxa
Para evitar bloqueios do WhatsApp:
- Atraso padrão entre mensagens: 3 segundos
- Limite diário recomendado: 200 mensagens
- Use atrasos apropriados para envios em massa

## 🔍 Solução de Problemas

### Problemas Comuns
1. **QR Code Não Escaneia**
   - Limpe o perfil do Chrome: Exclua a pasta `chrome_data/`
   - Reinicie a aplicação
   - Tente escanear novamente

2. **Mensagem Não Enviada**
   - Verifique a conexão com a internet
   - Confira o formato do número de telefone
   - Certifique-se que o WhatsApp Web está conectado

3. **Problemas com Chrome**
   - Atualize o Chrome para a última versão
   - Limpe o perfil do Chrome
   - Verifique os recursos do sistema

## 🤝 Contribuindo
1. Faça um fork do repositório
2. Crie seu branch de feature (`git checkout -b feature/recurso-incrivel`)
3. Faça commit de suas alterações (`git commit -m 'Adiciona recurso incrível'`)
4. Faça push para o branch (`git push origin feature/recurso-incrivel`)
5. Abra um Pull Request

## 📝 Licença
Este projeto está licenciado sob a GNU General Public License v3.0 (GPL-3.0) - veja o arquivo [LICENSE](LICENSE) para detalhes.

Isso significa:
- ✅ Uso comercial permitido
- ✅ Modificações permitidas
- ✅ Distribuição permitida
- ❗ Código fonte deve ser divulgado
- ❗ Mesma licença requerida
- ❗ Aviso de licença e copyright necessários

---

Made with ❤️ by NBTech
