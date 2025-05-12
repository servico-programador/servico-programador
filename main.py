# import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
# from dotenv import load_dotenv
# load_dotenv()


app = Flask(__name__)
# app.secret_key = os.environ.get('FLASK_SECRET_KEY')

# if not app.secret_key:
#     raise RuntimeError("FLASK_SECRET_KEY não está definida. Verifique as variáveis de ambiente.")

# # Configurações de email
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'alefsouzasobrinho@gmail.com'  # Coloque seu email
# app.config['MAIL_PASSWORD'] = 'alef.1234'           # Coloque sua senha

# mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']

    msg = Message(f"Contato de {nome}", 
                 sender=email, 
                 recipients=['seu_email@gmail.com'])  # Seu email para receber as mensagens
    msg.body = f"Nome: {nome}\nEmail: {email}\nMensagem:\n{mensagem}"
    
    try:
        mail.send(msg)
        flash('Mensagem enviada com sucesso!', 'success')
    except Exception as e:
        print(e)
        flash('Erro ao enviar mensagem. Tente novamente.', 'danger')
    
    return redirect(url_for('index'))


@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')


if __name__ == '__main__':
    app.run(debug=True)
