produto = {
    "nome": "Teclado Mecânico",
    "preco": 250.00,
    "estoque": 15
}

produto["estoque"] = 20
produto["marca"] = "Logitech"

del produto["preco"]

print("Dados do produto:")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")
