from gerador_codigo import gerar_codigo

def test_primeiro_codigo():
    codigo = gerar_codigo("C", "A", "BR")
    assert codigo.endswith("0001A")

def test_incremento():
    gerar_codigo("D", "A", "BR")
    codigo = gerar_codigo("D", "A", "BR")
    assert "0002" in codigo

def test_erro():
    try:
        gerar_codigo("", "A", "BR")
        assert False
    except ValueError:
        assert True