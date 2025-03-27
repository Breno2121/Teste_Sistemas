def positivo(numero):
    return numero>0

def test_posito():
    assert positivo(5) is True
    assert positivo(-5) is False