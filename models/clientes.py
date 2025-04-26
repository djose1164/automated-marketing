from utils.database import get_db
import random


class Cliente:
    @staticmethod
    def get_clientes():
        res = None
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute(
                "select c.id, nombre, apellido, telefono, correo from cliente c join usuario u on c.usuario_id = u.id"
            )
            res = cur.fetchall()
        return [
            {
                "id": row[0],
                "nombre": row[1],
                "apellido": row[2],
                "telefono": row[3],
                "correo": row[4],
            }
            for row in res
        ]

    @staticmethod
    def get_cliente_by_id(cliente_id: int):
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute(
                "select c.id, nombre, apellido, telefono, correo, provincia, usuario_id "
                "from cliente c join usuario u on c.usuario_id = u.id "
                "where c.id = ?",
                (cliente_id,),
            )
            row = cur.fetchone()
            return {
                "id": row[0],
                "nombre": row[1],
                "apellido": row[2],
                "telefono": row[3],
                "correo": row[4],
                "provincia": row[5],
                "usuario_id": row[6],
            }

    @staticmethod
    def get_cliente_by_nombre_o_apellido(input_text: str):
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute(
                "select c.id, nombre, apellido, telefono, correo, provincia, usuario_id "
                "from cliente c join usuario u on c.usuario_id = u.id "
                "where concat(nombre, ' ', apellido) like ?",
                (f"%{input_text}%",),
            )
            return [
                {
                    "id": row[0],
                    "nombre": row[1],
                    "apellido": row[2],
                    "telefono": row[3],
                    "correo": row[4],
                    "provincia": row[5],
                    "usuario_id": row[6],
                }
                for row in cur.fetchall()
            ]

    @staticmethod
    def generar_nombre_usuario(nombre: str, apellido: str, len: int = 5):
        combined = nombre + apellido
        return "".join(random.choice(combined) for _ in range(len))
