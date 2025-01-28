import csv

def process_csv(file_path):
    contacts = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)  # Mudado para csv.reader pois não tem cabeçalho
        for row in reader:
            if len(row) >= 2:  # Se tem pelo menos nome e número
                contacts.append({
                    'nome': row[0].strip(),
                    'numero': format_number(row[1].strip())
                })
    return contacts

def process_manual_entries(raw_entries):
    contacts = []
    for line in raw_entries.split('\n'):
        line = line.strip()
        if line:
            parts = [p.strip() for p in line.replace(';', ',').split(',', 1) if p.strip()]
            if len(parts) == 2:
                contacts.append({
                    'nome': parts[0],
                    'numero': format_number(parts[1])
                })
    return contacts

def format_number(number):
    cleaned = ''.join(filter(str.isdigit, number))
    if cleaned.startswith('55') and len(cleaned) == 12:
        return f'+{cleaned}'
    if len(cleaned) == 11:
        return f'+55{cleaned}'
    return f'+{cleaned}' if cleaned.startswith('+') else f'+{cleaned}'