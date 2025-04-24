from flask import Blueprint, flash, redirect, render_template, request, url_for

from models.campanias import Campania
from utils.database import get_db

campania_routes = Blueprint("campanias", __name__)


@campania_routes.route("/api")
def campania_index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("select * from campania")
    res = [
        {
            "id": row[0],
            "nombre": row[1],
            "descripcion": row[2],
            "fecha_inicio": row[3],
            "fecha_fin": row[4],
        }
        for row in cur.fetchall()
    ]
    conn.close()
    return res


# @campania_routes.route("/", methods=["POST"])
# def campania_render():
#     nombre = request.form.get("nombre")
#     descripcion = request.form.get("descripcion")
#     fecha_inicio = request.form.get("fecha_inicio")
#     fecha_fin = request.form.get("fecha_fin")

#     with get_db() as conn:
#         cur = conn.cursor()
#         sql = "insert into campania(id, nombre, descripcion, fecha_inicio, fecha_fin) values(?, ?, ?, ?, ?)"
#         cur.execute(sql, (None, nombre, descripcion, fecha_inicio, fecha_fin))
#         conn.commit()

#     if not cur.rowcount != 1:
#         flash("Error")
#         return redirect(url_for("index"))

#     return redirect(url_for("nueva_campania_render"))


@campania_routes.route("/<int:campania_id>", methods=["POST"])
def delete_campania(campania_id):
    with get_db() as conn:
        cur = conn.cursor()
        sql = "delete from campania where id = ?"
        cur.execute(sql, (campania_id,))
        conn.commit()
    return redirect(url_for("campania_render"))


@campania_routes.route("/<int:campania_id>", methods=["GET"])
def editar_campania_render(campania_id: int):
    return render_template(
        "editarCampanias.html", campania=Campania.get_campania_by_id(campania_id)
    )


@campania_routes.route("/editar", methods=["POST"])
def editar_campania():
    campania_id = request.form["id"]
    nombre = request.form.get("nombre")
    descripcion = request.form.get("descripcion")
    fecha_inicio = request.form.get("fecha_inicio")
    fecha_fin = request.form.get("fecha_fin")

    with get_db() as conn:
        cur = conn.cursor()
        sql = (
            "update campania "
            "set nombre = ?, descripcion = ?, fecha_inicio = ?, fecha_fin = ? "
            "where id = ?"
        )
        cur.execute(sql, (nombre, descripcion, fecha_inicio, fecha_fin, campania_id))
        conn.commit()
    return redirect("/campanias")
