# Checklist Pós-Deploy Hermesx

## 1. Verificar Arquivos e Permissões
- [ ] Todos os arquivos foram copiados para `/var/www/html/hermesx`
- [ ] Permissões corretas nos diretórios:
  - [ ] `/var/www/html/hermesx` (755)
  - [ ] `/var/www/html/hermesx/uploads` (775)
  - [ ] `/var/www/html/hermesx/chrome_data` (775)
- [ ] Proprietário www-data:www-data em todos os arquivos

## 2. Verificar Configurações
- [ ] Arquivo `.env` presente e com as variáveis corretas
- [ ] Certificado SSL instalado e funcionando
- [ ] Virtual Host configurado corretamente
- [ ] Módulos Apache habilitados (ssl, headers, wsgi)

## 3. Verificar Logs
- [ ] `/var/log/apache2/hermesx_error.log` sem erros
- [ ] `/var/log/apache2/hermesx_access.log` mostrando acessos

## 4. Testar Funcionalidades
- [ ] Site acessível via HTTPS
- [ ] Redirecionamento HTTP para HTTPS funcionando
- [ ] Selenium/Chrome funcionando em modo headless
- [ ] Upload de arquivos funcionando
- [ ] Todas as rotas respondendo corretamente

## 5. Segurança
- [ ] Arquivos .git protegidos
- [ ] Arquivo .env protegido
- [ ] Arquivos .py/.pyc não acessíveis via web
- [ ] Diretório static configurado corretamente

## 6. Backup
- [ ] Backup inicial realizado após deploy
- [ ] Cron job para backup configurado (se necessário)

## 7. Monitoramento
- [ ] Logs sendo rotacionados corretamente
- [ ] Sistema de monitoramento configurado (se necessário)

## Comandos Úteis

### Verificar status do Apache
```bash
sudo systemctl status apache2
```

### Verificar logs em tempo real
```bash
sudo tail -f /var/log/apache2/hermesx_error.log
```

### Reiniciar Apache
```bash
sudo systemctl restart apache2
```

### Testar configuração
```bash
sudo apache2ctl configtest
```
