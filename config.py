import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'csv'}
    MAX_MANUAL_ENTRIES = 50

    # Configurações de produção
    CHROME_OPTIONS = [
        '--headless',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-gpu',
        '--disable-software-rasterizer',
        '--disable-extensions',
        '--disable-features=TranslateUI',
        '--disable-notifications',
        '--disable-popup-blocking',
        '--disable-infobars',
        '--disable-dev-tools',
        '--no-first-run',
        '--no-default-browser-check',
        '--password-store=basic',
        '--use-mock-keychain',
        '--force-device-scale-factor=1',
        '--window-size=1920,1080',
        '--ignore-certificate-errors',
        '--log-level=3',  # Apenas erros críticos
        '--silent-launch',
        '--enable-features=NetworkServiceInProcess',
        '--disable-background-networking',
        '--disable-sync',
        '--metrics-recording-only',
        '--disable-prompt-on-repost',
        '--disable-client-side-phishing-detection',
        '--disable-component-update',
        '--disable-breakpad',
        '--disable-ipc-flooding-protection',
        '--disable-backgrounding-occluded-windows'
    ]

    # Preferências de produção
    CHROME_PREFS = {
        'profile.default_content_setting_values': {
            'notifications': 2,  # Bloquear
            'automatic_downloads': 1,  # Permitir
            'geolocation': 2,  # Bloquear
            'media_stream_mic': 2,  # Bloquear
            'media_stream_camera': 2,  # Bloquear
            'images': 1,  # Permitir
            'javascript': 1,  # Permitir
            'plugins': 2,  # Bloquear
            'popups': 2,  # Bloquear
            'background_sync': 2,  # Bloquear
            'midi_sysex': 2,  # Bloquear
            'push_messaging': 2  # Bloquear
        },
        'profile.password_manager_enabled': False,
        'credentials_enable_service': False,
        'profile.default_content_settings': {
            'popups': 2,
            'notifications': 2
        },
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True,
        'safebrowsing.disable_download_protection': False,
        'translate.enabled': False,
        'profile.managed_default_content_settings': {
            'images': 1,
            'javascript': 1
        }
    }