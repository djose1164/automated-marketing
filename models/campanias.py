from utils.database import get_db


class Campania:
    @staticmethod
    def get_campanias():
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

    @staticmethod
    def get_campania_by_id(campania_id: int):
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute(
                "select * from campania where id = ?",
                (campania_id,),
            )
            row = cur.fetchone()
            return {
                "id": row[0],
                "nombre": row[1],
                "descripcion": row[2],
                "fecha_inicio": row[3],
                "fecha_fin": row[4],
            }

    @staticmethod
    def get_campanias_by_name(nombre: str):
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("select * from campania where nombre like ?", (f"%{nombre}%",))
            res = cur.fetchall()
            return [
                {
                    "id": row[0],
                    "nombre": row[1],
                    "descripcion": row[2],
                    "fecha_inicio": row[3],
                    "fecha_fin": row[4],
                }
                for row in res
            ]

    def get_campanias_activas():
        with get_db() as conn:
            cur = conn.cursor()
            cur.execute("select * from campania where fecha_fin >= now()")
            return [
                {
                    "id": row[0],
                    "nombre": row[1],
                    "descripcion": row[2],
                    "fecha_inicio": row[3],
                    "fecha_fin": row[4],
                }
                for row in cur.fetchall()
            ]
