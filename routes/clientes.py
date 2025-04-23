from flask import Blueprint

from utils.database import get_db

cliente_routes = Blueprint("clientes", __name__)


@cliente_routes.route("/")
def cliente_index():
    cur = get_db().cursor()
    sql = "select * from cliente"
    cur.execute(sql)
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "apellido": row[2],
            "telefono": row[3],
            "usuario_id": row[4],
        }
        for row in cur.fetchall()
    ]
