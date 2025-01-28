import re
from typing import Tuple

def validate_phone_number(number: str, country_code: str = '55') -> Tuple[bool, str]:
    """
    Valida o formato do número de telefone para um país específico.
    Args:
        number: Número de telefone a ser validado
        country_code: Código telefônico do país (default: '55' para Brasil)
    Returns:
        Tuple[bool, str]: (sucesso, número formatado ou mensagem de erro)
    """
    # Remove todos os caracteres não numéricos
    clean_number = ''.join(filter(str.isdigit, number))
    
    # Verifica se o número tem pelo menos 8 dígitos
    if len(clean_number) < 8:
        return False, "Número de telefone inválido"
    
    # Formata o número com o código do país
    formatted_number = country_code + clean_number
    
    return True, formatted_number

def validate_message(message: str) -> Tuple[bool, str]:
    """Valida o formato e conteúdo da mensagem."""
    if not message:
        return False, "Mensagem não pode estar vazia"
    
    if len(message) > 1000:
        return False, "Mensagem muito longa (máximo 1000 caracteres)"
    
    return True, message
