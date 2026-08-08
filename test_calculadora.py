import pytest

from calculadora import calcular_total, obter_desconto_cupom


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]

    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)


def test_total_com_cupom_devops10():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, cupom="DevOps10") == 225.0


def test_obter_desconto_do_cupom_devops10():
    assert obter_desconto_cupom("DevOps10") == 10


def test_cupom_invalido():
    with pytest.raises(ValueError, match="Cupom inválido"):
        calcular_total([(100.0, 1)], cupom="NAO-EXISTE")
