"""
Módulo para gerenciar códigos de países para números de telefone.
"""

COUNTRY_CODES = {
    'BR': {'code': '55', 'name': 'Brasil', 'min_length': 12, 'max_length': 13},
    'PT': {'code': '351', 'name': 'Portugal', 'min_length': 12, 'max_length': 13},
    'US': {'code': '1', 'name': 'Estados Unidos', 'min_length': 11, 'max_length': 11},
    'ES': {'code': '34', 'name': 'Espanha', 'min_length': 11, 'max_length': 12},
    'UK': {'code': '44', 'name': 'Reino Unido', 'min_length': 12, 'max_length': 13},
    'IT': {'code': '39', 'name': 'Itália', 'min_length': 11, 'max_length': 13},
    'FR': {'code': '33', 'name': 'França', 'min_length': 11, 'max_length': 12},
    'DE': {'code': '49', 'name': 'Alemanha', 'min_length': 11, 'max_length': 12},
    'MX': {'code': '52', 'name': 'México', 'min_length': 12, 'max_length': 13},
    'AR': {'code': '54', 'name': 'Argentina', 'min_length': 12, 'max_length': 13},
    'CL': {'code': '56', 'name': 'Chile', 'min_length': 11, 'max_length': 12},
    'CO': {'code': '57', 'name': 'Colômbia', 'min_length': 12, 'max_length': 13},
    'PE': {'code': '51', 'name': 'Peru', 'min_length': 11, 'max_length': 12},
    'VE': {'code': '58', 'name': 'Venezuela', 'min_length': 11, 'max_length': 12},
    'UY': {'code': '598', 'name': 'Uruguai', 'min_length': 11, 'max_length': 12},
    'PY': {'code': '595', 'name': 'Paraguai', 'min_length': 11, 'max_length': 12},
    'BO': {'code': '591', 'name': 'Bolívia', 'min_length': 11, 'max_length': 12},
    'EC': {'code': '593', 'name': 'Equador', 'min_length': 11, 'max_length': 12},
    'CA': {'code': '1', 'name': 'Canadá', 'min_length': 11, 'max_length': 11},
    'AU': {'code': '61', 'name': 'Austrália', 'min_length': 11, 'max_length': 12},
}

def get_country_codes():
    """Retorna lista de países ordenada por nome."""
    return sorted(
        [{'code': code, **data} for code, data in COUNTRY_CODES.items()],
        key=lambda x: x['name']
    )

def get_country_by_code(phone_code: str):
    """Retorna informações do país pelo código telefônico."""
    for country_code, data in COUNTRY_CODES.items():
        if data['code'] == phone_code:
            return {'code': country_code, **data}
    return None

def validate_number_for_country(number: str, country_code: str) -> tuple[bool, str]:
    """Valida um número para um país específico."""
    country = COUNTRY_CODES.get(country_code)
    if not country:
        return False, f"Código de país inválido: {country_code}"
    
    # Remove todos os caracteres não numéricos
    clean_number = ''.join(filter(str.isdigit, number))
    
    # Verifica o comprimento do número
    if len(clean_number) < country['min_length'] or len(clean_number) > country['max_length']:
        return False, f"Número inválido para {country['name']}. Deve ter entre {country['min_length']} e {country['max_length']} dígitos."
    
    # Formata o número com o código do país
    formatted_number = country['code'] + clean_number
    
    return True, formatted_number
