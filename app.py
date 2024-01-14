from flask import Flask, render_template
app= Flask(__name__, template_folder='templates')
@app.route('/')
def hello():
	return 'Hola esta es mi aplicacion'
@app.route('/saludo/<nombre>')
def saludo(nombre=None):
	return f'Hola {nombre}'
@app.route('/pagina')
def pagina():
	return render_template('pagina.html')
