# import os
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

@app.route('/ebooks')
def ebooks():
    return render_template('ebooks.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')



@app.route('/download/<ebook_id>')
def download_ebook(ebook_id):
    # Lógica para servir o arquivo do ebook
    # Esta é apenas uma estrutura básica
    flash(f'Download do ebook {ebook_id} iniciado!', 'success')
    return redirect(url_for('ebooks'))

@app.route('/ebooks/<ebook_id>')
def view_ebook(ebook_id):
    # Lógica para exibir o ebook online
    return render_template('view_ebook.html', ebook_id=ebook_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

