from flask import Flask, render_template

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

# Arrancamos el servidor
if __name__ == '__main__':
    app.run(debug=True)
