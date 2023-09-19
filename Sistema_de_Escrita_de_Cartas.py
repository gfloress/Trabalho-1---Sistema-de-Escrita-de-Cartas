#Sistema de Escrita de Cartas

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função para verificar o login
def verificar_login(usuario, senha):
    # Vamos assumir que as informações de login estão em um arquivo de texto chamado "login.txt"
    try:
        with open('login.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                if dados[0] == usuario and dados[1] == senha:
                    return True
    except FileNotFoundError:
        pass
    return False

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')

# Rota para a página de escrita de cartas
@app.route('/escrever_carta', methods=['GET', 'POST'])
def escrever_carta():
    if request.method == 'POST':
        data = request.form['data']
        destinatario = request.form['destinatario']
        mensagem = request.form['mensagem']
        remetente = request.form['remetente']

        carta = f"{data}\n{destinatario}\n{mensagem}\n{remetente}"

        # Aqui, você pode fazer o que quiser com a carta, como salvá-la em um arquivo, enviá-la por e-mail, etc.
        # Neste exemplo, apenas imprimimos a carta no terminal.
        print(carta)

        return render_template('carta_gerada.html', carta=carta)

    return render_template('escrever_carta.html')

if __name__ == '__main__':
    app.run(debug=True)