CREATE TABLE IF NOT EXISTS devocionales (
    id UUID DEFAULT uuid_generate_v4(),
    semana TEXT,
    titulo_video TEXT,
    video_link TEXT,
    descripcion_video TEXT,
    titulo_audio TEXT,
    descripcion_audio TEXT,
    soundcloud_link TEXT,
    titulo TEXT,
    tema TEXT,
    instrucciones TEXT,
    devocional TEXT,
    reflexion TEXT,
    capitulo TEXT,
    lectura TEXT,
    biografia TEXT,
    trivia JSONB,
    fecha DATE
);