_CUPONS = {
    "DevOps10": 10,
    "BoasVindas": 5,
}


def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if cupom is not None:
        desconto_percentual = obter_desconto_cupom(cupom)

    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    total = subtotal - (subtotal * (desconto_percentual / 100))
    return round(total, 2)


def obter_desconto_cupom(cupom):
    """Obtém o percentual de desconto de um cupom cadastrado."""
    if cupom not in _CUPONS:
        raise ValueError("Cupom inválido.")

    return _CUPONS[cupom]


if __name__ == "__main__":
    itens = [(100.0, 2), (50.0, 1)]
    total = calcular_total(itens, cupom="DevOps10")
    print(f"Total com cupom DevOps10: R$ {total:.2f}")
