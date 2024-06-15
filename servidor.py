from flask import *
import random

#criando o servidor
app = Flask(__name__)

@app.route('/antiga') #end-point
def home_page():
    numero = random.randint(1,10)
    return 'seja muito bem-vindo\n' + str(numero)

@app.route('/')
def nova_page():
    return render_template('index.html')

@app.route('/receberinfo', methods=['POST'])
def tratar_info():
    nome = request.form.get('nome_usuario')
    if(nome.upper() == 'ANTONIO'):
        return 'voce é o nosso amigo antonio'
    else:
        return 'quem é vc? jogou onde?'


#executando o servidor (rodando)
app.run(debug=True)