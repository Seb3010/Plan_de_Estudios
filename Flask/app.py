from flask import Flask, render_template, request

# Creamos la aplicación Flask
app = Flask(__name__)

# Creamos una "Ruta" (Route)
# Esto le dice a Python: "Cuando alguien entre a la página principal ('/'), ejecuta esto"
@app.route('/')
def home():
    nombre = "sebas"
    lenguaje = "Python"
    hobies = ["Correr", "Leer", "Programar"]

    return render_template('index.html', user=nombre, lang=lenguaje, hob=hobies)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # 1. Atrapamos los datos
    nombre = request.form.get('usuario')
    msg = request.form.get('mensaje')
    
    # 2. Podemos pasar esos datos a una nueva plantilla de "éxito"
    return render_template('exito.html', persona=nombre, texto=msg)

# Arrancamos el servidor
if __name__ == '__main__':
    app.run(debug=True)

