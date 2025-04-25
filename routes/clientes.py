from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.clientes import Cliente
from utils.database import get_db

cliente_routes = Blueprint("clientes", __name__)


@cliente_routes.route("/")
def cliente_index():
    return Cliente.get_clientes()


@cliente_routes.route("/", methods=["POST"])
def nuevo_cliente():
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")
    provincia = request.form.get("provincia")

    print((nombre, apellido, correo, telefono, provincia))

    res = 0
    with get_db() as conn:
        cur = conn.cursor()
        sql = (
            "insert into usuario(nombre_usuario, correo, contrasena, rol_id)"
            "values(?, ?, ?, ?)"
        )
        nombre_usuario = Cliente.generar_nombre_usuario(nombre, apellido)
        cliente_rol = 3
        cur.execute(sql, (nombre_usuario, correo, nombre_usuario, cliente_rol))
        if cur.rowcount == 0:
            flash("Error al insertar usuario.")
            return redirect(url_for("index"))
        usuario_id = cur.lastrowid

        sql = (
            "insert into cliente(nombre, apellido, telefono, usuario_id, provincia)"
            "values(?, ?, ?, ?, ?)"
        )
        cur.execute(sql, (nombre, apellido, telefono, usuario_id, provincia))
        conn.commit()
        res = cur.rowcount

    if res == 0:
        flash("Error al crear cliente")
    return redirect(url_for("cliente_render"))


@cliente_routes.route("/<int:cliente_id>", methods=["POST"])
def eliminar_cliente(cliente_id: int):
    res = 0
    with get_db() as conn:
        cur = conn.cursor()
        cur.execute("delete from reporte where cliente_id = ?", (cliente_id,))
        cur.execute("delete from planificador where cliente_id = ?", (cliente_id,))
        cur.execute("delete from cliente where id = ?", (cliente_id,))
        conn.commit()
        res = cur.rowcount

    if res == 0:
        flash("Error al eliminar cliente")
    return redirect(url_for("cliente_render"))

@cliente_routes.route("/<int:cliente_id>")
def editar_cliente_render(cliente_id: int):
    provincias = [
        'Azua', 'Bahoruco', 'Barahona', 'Dajabón', 'Distrito Nacional',
        'Duarte', 'Elías Piña', 'El Seibo', 'Espaillat', 'Hato Mayor',
        'Hermanas Mirabal', 'Independencia', 'La Altagracia', 'La Romana',
        'La Vega', 'María Trinidad Sánchez', 'Monseñor Nouel', 'Monte Cristi',
        'Monte Plata', 'Pedernales', 'Peravia', 'Puerto Plata', 'Samaná',
        'San Cristóbal', 'San José de Ocoa', 'San Juan', 'San Pedro de Macorís',
        'Sánchez Ramírez', 'Santiago', 'Santiago Rodríguez', 'Santo Domingo',
        'Valverde'
    ]
    return render_template("editarClientes.html", 
                           cliente=Cliente.get_cliente_by_id(cliente_id),
                           provincias=provincias)

@cliente_routes.route("/editar", methods=["POST"])
def editar_cliente():
    cliente_id = request.form["cliente_id"]
    usuario_id = request.form.get("usuario_id")
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")
    provincia = request.form.get("provincia")

    print((nombre, apellido, telefono, provincia, cliente_id, usuario_id))

    with get_db() as conn:
        cur = conn.cursor()
        sql = (
            "update cliente "
            "set nombre = ?, apellido = ?, telefono = ?, provincia = ? " 
            "where id = ?"
        )
        cur.execute(sql, (nombre, apellido, telefono, provincia, cliente_id))

        sql = "update usuario " \
            "set correo = ? " \
            "where id = ?"
        cur.execute(sql, (correo, usuario_id,))
        conn.commit()
        return redirect("/clientes")

