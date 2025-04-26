import os
from flask import Flask, render_template

from models.campanias import Campania
from models.clientes import Cliente
from routes.clientes import cliente_routes
from routes.campanias import campania_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("secret_key")
app.register_blueprint(cliente_routes, url_prefix="/clientes")
app.register_blueprint(campania_routes, url_prefix="/campanias")


@app.route("/")
def index():
    campanias_activas = len(Campania.get_campanias_activas())
    estadisticas = {
        "emails_enviados": [120, 150, 180, 130, 170],
        "emails_abiertos": [90, 110, 150, 10, 12],
        "clics_promos": [40, 60, 70, 50, 65],
        "labels": ["Lun", "Mar", "Mié", "Jue", "Vie"],
        "campanias_activas": campanias_activas
    }
    return render_template("index.html", estadisticas=estadisticas)


@app.route("/campanias")
def campania_render():
    return render_template("campañas.html", campanias=Campania.get_campanias())


@app.route("/clientes")
def cliente_render():
    return render_template("clientes.html", clientes=Cliente.get_clientes())


@app.route("/nuevo-cliente")
def nuevo_cliente_render():
    return render_template("formClientes.html")


@app.route("/nueva-campania")
def nueva_campania_render():
    return render_template("formCampanias.html")


if __name__ == "__main__":
    app.run(debug=True)
