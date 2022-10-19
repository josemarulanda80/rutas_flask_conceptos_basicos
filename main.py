from flask import Flask, url_for,redirect,render_template,request,flash
app = Flask(__name__)

#Antes de la petición
@app.before_request
def before_request():
    print("Antes de la petición")

#Despues de la petición
@app.after_request
def after_request(response):
    print('Despues de la petición')
    print(response)
    return response
@app.route('/')
def index():
    flash('Has iniciado en el index del proyecto Flask')
    print("Accediendo al index o pagina principal")
    diccionario={'titulo':'Pagína principal','encabezado':'Bienvenido a mi pagína web'}
    return render_template('index.html',datos=diccionario) 

#redirección
@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redireccionaf(sitio=None):
    if sitio is not None:
        #Se redirije a la función no al url
        return redirect(url_for('index'))
    else:
        return redirect(url_for('arcade'))

@app.route("/acercade")
def arcade():
    diccionario={'titulo':'Acerca de','encabezado':'Acerca de mi'}
    return render_template('acercade.html',datos=diccionario)

#condiciones y bluques
@app.route('/condicionybucle')
def condicionybucle():
    datos={
        'edad':50,
        'nombres':['Jose','Mar','Lucia','Eva']
    }
    return render_template('condicionybucle.html',dato=datos)

#parametros
@app.route("/saludame")
@app.route("/saludame/<string:nombre>")
@app.route("/saludame/<string:nombre>/<int:edad>")
def saludar(nombre="jose",edad=None):
    if edad != None:
        return f"Hola {nombre} tienes {edad}"
    else:
        return f"""
            <h1>Hola</h1>
            <h1>{nombre}</h1>
        """
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1,num2):
    return f"""La suma es igual a {num1+num2}"""

def pagina_no_encontrada(error):
    return render_template('errores/404.html'),404
if __name__=='__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.secret_key='clave-flask'
    app.run(debug=True)