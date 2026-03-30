from conexao import conectar

def gerar_codigo(grupo, tipo, pais):
    if not grupo or not tipo or not pais or len(pais) != 2:
        raise ValueError("Entrada inválida")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT MAX(sec) FROM codigos_sequenciais
        WHERE Grupo=%s AND Tipo_Alimento=%s AND Pais=%s
    """, (grupo, tipo, pais))

    result = cursor.fetchone()[0]
    proximo = 1 if result is None else result + 1

    codigo = f"{pais}{grupo}{proximo:04d}{tipo}"

    cursor.execute("""
        INSERT INTO codigos_sequenciais (codigo, sec, Grupo, Tipo_Alimento, Pais)
        VALUES (%s, %s, %s, %s, %s)
    """, (codigo, proximo, grupo, tipo, pais))

    conn.commit()
    conn.close()

    return codigo