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
