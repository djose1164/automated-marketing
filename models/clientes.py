from utils.database import get_db


class Cliente:
    @staticmethod
    def get_clientes():
        res = None
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("select * from cliente")
            res = cur.fetchall()
        return [
            {
                "id": row[0],
                "nombre": row[1],
                "apellido": row[2],
                "telefono": row[3],
                "usuario_id": row[4],
            }
            for row in res
        ]
