from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time
from typing import Optional
import os
import shutil

class WhatsAppSender:
    def __init__(self):
        self.driver: Optional[webdriver.Chrome] = None
        self.last_message_time = 0
        self.rate_limit_delay = 3
        self.user_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'chrome_data'))
        if not os.path.exists(self.user_data_dir):
            os.makedirs(self.user_data_dir)
            print(f"Diretório de dados criado: {self.user_data_dir}")

    def cleanup(self):
        """Limpa recursos do driver."""
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None

    def __del__(self):
        """Destrutor para garantir que os recursos sejam liberados."""
        self.cleanup()

    def initialize_driver(self):
        """Inicializa o driver do Chrome com as configurações necessárias."""
        if self.driver is not None:
            return

        print(f"Inicializando Chrome com diretório: {self.user_data_dir}")
        options = webdriver.ChromeOptions()
        options.add_argument(f'--user-data-dir={self.user_data_dir}')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        try:
            self.driver = webdriver.Chrome(options=options)
            self.driver.get('https://web.whatsapp.com')
            # Aguarda a página carregar
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except Exception as e:
            print(f"Erro ao inicializar Chrome: {str(e)}")
            self.cleanup()
            raise

    def wait_for_rate_limit(self):
        """Implementa rate limiting para evitar bloqueios."""
        elapsed = time.time() - self.last_message_time
        if elapsed < self.rate_limit_delay:
            time.sleep(self.rate_limit_delay - elapsed)
        self.last_message_time = time.time()

    def is_logged_in(self) -> bool:
        """Verifica se o WhatsApp Web está logado."""
        try:
            if not self.driver:
                return False

            # Verifica se há QR code
            try:
                qr = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="qrcode"]')
                print("QR Code encontrado - Necessário fazer login")
                return False
            except:
                # Se não encontrou QR code, assume que está logado
                return True
        except:
            return False

    def is_driver_alive(self) -> bool:
        """Verifica se o driver ainda está ativo e utilizável."""
        try:
            if not self.driver:
                return False
            # Tenta acessar o título da página para ver se o driver ainda responde
            self.driver.title
            return True
        except:
            return False

    def ensure_driver(self) -> bool:
        """Garante que o driver está ativo, reiniciando se necessário."""
        if not self.is_driver_alive():
            print("Reiniciando Chrome...")
            self.cleanup()
            try:
                self.initialize_driver()
                return True
            except Exception as e:
                print(f"Erro ao reiniciar Chrome: {str(e)}")
                return False
        return True

    def send_message(self, number: str, message: str) -> tuple[bool, str]:
        """Envia uma mensagem para um número do WhatsApp."""
        max_retries = 2  # Número máximo de tentativas
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    print(f"\nTentativa {attempt + 1} de {max_retries}")
                
                print(f"\nIniciando envio para {number}")
                
                # Garante que o driver está ativo
                if not self.ensure_driver():
                    continue  # Tenta novamente se falhou em inicializar
                
                # Verifica login apenas uma vez
                if not self.is_logged_in():
                    print("Por favor, escaneie o QR Code para fazer login")
                    # Aguarda 30 segundos pelo scan do QR
                    for _ in range(15):
                        if not self.is_driver_alive():
                            raise Exception("Janela do Chrome foi fechada")
                        time.sleep(2)
                        if self.is_logged_in():
                            break
                    else:
                        if attempt + 1 < max_retries:
                            continue  # Tenta novamente se não é a última tentativa
                        return False, "Timeout aguardando scan do QR Code"
                
                # Prepara a URL e navega
                self.wait_for_rate_limit()
                encoded_msg = urllib.parse.quote(message)
                url = f'https://web.whatsapp.com/send?phone={number}&text={encoded_msg}'
                print(f"Abrindo conversa com {number}...")
                self.driver.get(url)
                
                # Aguarda a página carregar
                print("Aguardando página carregar...")
                time.sleep(10)
                
                if not self.is_driver_alive():
                    raise Exception("Janela do Chrome foi fechada")
                
                # Verifica número inválido
                try:
                    error = self.driver.find_element(
                        By.XPATH, 
                        '//*[contains(text(), "Número de telefone inválido")]'
                    )
                    return False, "Número de telefone inválido"
                except:
                    pass

                # Tenta diferentes seletores para o botão de enviar
                print("Procurando botão de enviar...")
                button_selectors = [
                    'span[data-icon="send"]',
                ]
                
                send_button = None
                for selector in button_selectors:
                    if not self.is_driver_alive():
                        raise Exception("Janela do Chrome foi fechada")
                    try:
                        print(f"Tentando seletor: {selector}")
                        send_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                        if send_button:
                            break
                    except:
                        continue
                
                if not send_button:
                    # Se não encontrou com CSS, tenta XPath
                    try:
                        print("Tentando encontrar por XPath...")
                        send_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((
                                By.XPATH, 
                                '//button[contains(@class, "send") or contains(@aria-label, "Enviar")]'
                            ))
                        )
                    except:
                        pass
                
                if send_button:
                    print("Botão encontrado, enviando mensagem...")
                    time.sleep(1)
                    send_button.click()
                    time.sleep(2)
                    return True, "Mensagem enviada com sucesso"
                else:
                    if attempt + 1 < max_retries:
                        print("Botão não encontrado, tentando novamente...")
                        continue
                    print("Botão de enviar não encontrado")
                    try:
                        timestamp = time.strftime("%Y%m%d-%H%M%S")
                        screenshot_path = f"error_screenshot_{timestamp}.png"
                        self.driver.save_screenshot(screenshot_path)
                        print(f"Screenshot salvo em: {screenshot_path}")
                    except:
                        pass
                    return False, "Não foi possível encontrar o botão de enviar"
            
            except Exception as e:
                error_msg = str(e)
                print(f"Erro: {error_msg}")
                
                if any(msg in error_msg.lower() for msg in [
                    "no such window",
                    "target window already closed",
                    "web view not found"
                ]):
                    print("Detectado erro de janela fechada")
                    self.cleanup()
                    if attempt + 1 < max_retries:
                        print("Tentando novamente...")
                        continue
                
                return False, f"Erro ao enviar mensagem: {error_msg}"
        
        return False, "Todas as tentativas falharam"

# Instância global
_sender = None

def get_sender():
    """Retorna uma instância única do WhatsAppSender."""
    global _sender
    if _sender is None:
        _sender = WhatsAppSender()
    return _sender

def send_whatsapp_message(number: str, message: str):
    """Função de conveniência para enviar mensagem."""
    return get_sender().send_message(number, message)