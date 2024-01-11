from docx import Document
from unidecode import unidecode
from insert import insertar_datos
#from firebase import send_push_notifications
import psycopg2
import os
from dotenv import load_dotenv

# Get PostgreSQL connection details from environment variables
PG_USER = os.getenv("PGUSER")
PG_PASSWORD = os.getenv("PGPASSWORD")
PG_HOST = os.getenv("PGHOST")
PG_PORT = os.getenv("PGPORT")
PG_DATABASE = os.getenv("PGDATABASE")

# Obtiene los devocionales de la base de datos
# key: columna por la que se va a filtrar
def obtener_devocionales(key, offset=0, limite=10):
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )

    cur = conn.cursor()

    if key:
        query = """
            SELECT * FROM devocionales
            WHERE {} = %s
            ORDER BY fecha DESC
            OFFSET %s LIMIT %s
        """.format(key)

        cur.execute(query, (key, offset, limite))
    else:
        cur.execute("""
            SELECT * FROM devocionales
            ORDER BY fecha DESC
            OFFSET %s LIMIT %s
        """, (offset, limite))

    cur.execute(query, (key, offset, limite))

    registros = cur.fetchall()

    columnas = [desc[0] for desc in cur.description]
    devocionales = []
    for registro in registros:
        devocionales.append(dict(zip(columnas, registro)))

    cur.close()
    conn.close()

    return devocionales 

# Obtener los devocionales por su UUID
def obtener_devocional_por_uuid(devocional_uuid):
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM devocionales
        WHERE id = %s
    """, (devocional_uuid,))

    registro = cur.fetchone()

    columnas = [desc[0] for desc in cur.description]
    devocional = dict(zip(columnas, registro))

    cur.close()
    conn.close()

    return devocional

# Obtener las trivias por su UUID
def obtener_trivia_por_uuid(trivia_uuid):
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM trivias
        WHERE id = %s
    """, (trivia_uuid,))

    registro = cur.fetchone()

    columnas = [desc[0] for desc in cur.description]
    trivia = dict(zip(columnas, registro))

    cur.close()
    conn.close()

    return trivia

# Obtener los podcasts por su UUID
def obtener_podcast_por_uuid(podcast_uuid):
    # Conexión a la base de datos
    conn = psycopg2.connect(
        dbname=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM podcasts
        WHERE id = %s
    """, (podcast_uuid,))

    registro = cur.fetchone()

    columnas = [desc[0] for desc in cur.description]
    podcast = dict(zip(columnas, registro))

    cur.close()
    conn.close()

    return podcast