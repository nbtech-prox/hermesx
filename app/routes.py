from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
import os
from werkzeug.utils import secure_filename
from app.utils.csv_handler import process_csv, format_number
from app.utils.whatsapp import send_whatsapp_message
from app.utils.validators import validate_phone_number, validate_message
from app.utils.country_codes import get_country_codes
from config import Config

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        results = []
        message = request.form.get('message', '').strip()
        message_type = 'individual'
        country_code = request.form.get('country_code', '55')

        # Validação da mensagem
        is_valid_msg, msg_error = validate_message(message)
        if not is_valid_msg:
            flash(msg_error, 'error')
            return redirect(url_for('main.index') + '#' + message_type)

        try:
            # Processar envio individual
            if 'individual_submit' in request.form:
                message_type = 'individual'
                nome = request.form.get('nome', '').strip()
                numero = request.form.get('numero', '').strip()
                
                if not nome:
                    flash('Nome é obrigatório', 'error')
                    return redirect(url_for('main.index') + '#individual')
                
                # Validação do número
                is_valid, formatted_number = validate_phone_number(numero, country_code)
                if not is_valid:
                    flash(formatted_number, 'error')  # formatted_number contém a mensagem de erro
                    return redirect(url_for('main.index') + '#individual')
                
                # Enviar mensagem
                success, error = send_whatsapp_message(formatted_number, message)
                results.append({
                    'nome': nome,
                    'numero': formatted_number,
                    'status': 'Sucesso' if success else f'Erro: {error}'
                })

            # Processar envio em grupo
            elif 'group_submit' in request.form:
                message_type = 'group'
                if 'file' not in request.files:
                    flash('Nenhum arquivo selecionado', 'error')
                    return redirect(url_for('main.index') + '#grupo')
                
                file = request.files['file']
                if file.filename == '':
                    flash('Nenhum arquivo selecionado', 'error')
                    return redirect(url_for('main.index') + '#grupo')
                
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
                    file.save(filepath)
                    
                    try:
                        # Processar CSV e enviar mensagens
                        contacts = process_csv(filepath)
                        if not contacts:
                            flash('Arquivo CSV vazio ou formato inválido', 'error')
                            return redirect(url_for('main.index') + '#grupo')
                        
                        # Validar números e enviar mensagens
                        for contact in contacts:
                            is_valid, formatted_number = validate_phone_number(contact['numero'], country_code)
                            if is_valid:
                                success, error = send_whatsapp_message(formatted_number, message)
                                results.append({
                                    'nome': contact['nome'],
                                    'numero': formatted_number,
                                    'status': 'Sucesso' if success else f'Erro: {error}'
                                })
                        
                        # Remover arquivo após processamento
                        os.remove(filepath)
                        
                    except Exception as e:
                        flash(f'Erro ao processar arquivo: {str(e)}', 'error')
                        return redirect(url_for('main.index') + '#grupo')
                else:
                    flash('Tipo de arquivo não permitido', 'error')
                    return redirect(url_for('main.index') + '#grupo')

            # Redirecionar para a página de resultados
            if results:
                return render_template('result.html', results=results)
            else:
                flash('Nenhuma mensagem foi enviada', 'error')
                return redirect(url_for('main.index') + '#' + message_type)

        except Exception as e:
            flash(f'Erro ao enviar mensagem: {str(e)}', 'error')
            return redirect(url_for('main.index') + '#' + message_type)

    # GET request - mostrar página inicial
    return render_template('index.html', countries=get_country_codes())

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'