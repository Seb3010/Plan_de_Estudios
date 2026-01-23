from flask import Flask, render_template, request, session, redirect, url_for

# Creamos la aplicación Flask
app = Flask(__name__)

app.secret_key = 'sebas_123_clave_ultra_secreta_2026'

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

    if not nombre or not msg:
        return render_template('error_400.html'), 400

    with open("mensajes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre: {nombre} | Mensaje: {msg}\n")
    
    # 2. Podemos pasar esos datos a una nueva plantilla de "éxito"
    return render_template('exito.html', persona=nombre, texto=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('user')
        password = request.form.get('pass')

        # Validación "manual" (muy básica por ahora)
        if usuario == 'admin' and password == '1234':
            session['logged_in'] = True # ¡Le ponemos el brazalete VIP!
            return redirect(url_for('ver_mensajes'))
    
        return "Usuario o contraseña incorrectos. <a href='/login'>Volver</a>"
    
    return render_template('login.html')

@app.route('/ver_mensajes')
def ver_mensajes():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    lista_mensajes = []
    
    # Intentamos abrir el archivo para leerlo
    try:
        with open("mensajes.txt", "r", encoding="utf-8") as archivo:
            # .readlines() convierte cada línea del archivo en un elemento de una lista
            lista_mensajes = archivo.readlines()
    except FileNotFoundError:
        # Por si el archivo aún no existe (nadie ha enviado mensajes)
        lista_mensajes = ["Aún no hay mensajes guardados."]

    return render_template('admin.html', mensajes=lista_mensajes)

# Arrancamos el servidor
if __name__ == '__main__':
    app.run(debug=True)

