import psycopg2
import json
from psycopg2 import sql
from datetime import datetime

def insertar_datos(map):
    conn = psycopg2.connect(
        dbname="postgres", 
        user="postgres", 
        password="12345678", 
        host="localhost"
    )
    cur = conn.cursor()

    map['fecha'] = datetime.now().date()
    map['trivia'] = json.dumps(map['trivia'])

    query = sql.SQL("""
        INSERT INTO devocionales (semana, 
         titulo_video,
         video_link,
         descripcion_video, 
         titulo_audio, 
         descripcion_audio, 
         soundcloud_link, 
         titulo, 
         tema, 
         instrucciones, 
         devocional, 
         reflexion, 
         capitulo, 
         lectura, 
         biografia,
         fecha,
         trivia) 
        VALUES (%(semana)s,
          %(titulo_video)s,
          %(video_link)s, 
          %(descripcion_video)s,
          %(titulo_audio)s, 
          %(descripcion_audio)s,
          %(soundcloud_link)s,
          %(titulo)s,
          %(tema)s,
          %(instrucciones)s, 
          %(devocional)s, 
          %(reflexion)s, 
          %(capitulo)s, 
          %(lectura)s, 
          %(biografia)s,
          %(fecha)s,
          %(trivia)s
          )
    """)

    cur.execute(query, map)
    conn.commit()

    cur.close()
    conn.close()
