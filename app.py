import requests
from flask import Flask, render_template, request

#creo el objeto flask
app = Flask(__name__)

@app.route('/') #app es la instancia, route el metodo y lo del interior de los parentesis es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/second') 
def info():
    return render_template(
        'secundario.html',
    )

@app.route('/bienvenido')
def bienvenido():
    return render_template(
        'bienvenido.html',
    )

@app.route('/personas')
def personas():
    # personas_peticion = requests.get('https://randomuser.me/api/?results=50')
    # listado_de_personas = personas_peticion.json()['results'] 
    return render_template(
        'personas.html',
        #lista = listado_de_personas 
    )
    
@app.route('/personas/add', methods=['GET', 'POST'])
def agregar_personas():
    if request.method == 'GET':
        print('Hice un get')
        
    if request.method == 'POST':
        data = request.get_data()
        print(data)
        """ nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        ciudad = request.form['ciudad']
        print(nombre, apellido, email, ciudad) """
    
    return render_template(
        'add_personas.html',
    )
    

@app.route('/registro')
def registro():
    return render_template(
        'registro.html',
    )