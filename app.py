from flask import Flask #aqui se importa o flask e dá o nome a ele, no caso Flask com F maiúsculo

app = Flask("Olá")
#criando o Servidor web @(decorator)

@app.route('/')
def ola():
    return "Olá mundo"
