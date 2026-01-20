from flask import Flask, render_template

# Creamos la aplicación Flask
app = Flask(__name__)

# Creamos una "Ruta" (Route)
# Esto le dice a Python: "Cuando alguien entre a la página principal ('/'), ejecuta esto"
@app.route('/')
def home():
    return render_template('index.html')

# Arrancamos el servidor
if __name__ == '__main__':
    app.run(debug=True)
