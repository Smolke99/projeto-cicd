from gerador_codigo import gerar_codigo

def test_primeiro_codigo():
    codigo = gerar_codigo("C", "A", "BR")
    print("Código gerado:", codigo)
    assert codigo == "BRC0001A"

def test_incremento():
    gerar_codigo("D", "A", "BR")
    codigo = gerar_codigo("D", "A", "BR")
    assert codigo == "BRD0002A"

def test_erro():
    try:
        gerar_codigo("", "A", "BR")
        assert False
    except ValueError:
        assert True

    print("\n📊 CONTEÚDO DA TABELA:")
    for linha in resultados:
        print(linha)

    cursor.close()
    conn.close()

    assert True
