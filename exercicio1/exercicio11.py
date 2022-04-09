"""
    Utilizando List Comprehension, faça com que uma lista de tuplas contendo nome do produto e preço
    tenha os seus preços somados e retornador no final.
"""

carrinho = []

carrinho.append(('Produto 1', 30.50))
carrinho.append(('Produto 2', '20'))
carrinho.append(('Produto 3', 50))

print(sum([float(y) for x, y in carrinho]))