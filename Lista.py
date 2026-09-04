
compras = ["arroz", "feijão", "leite", "ovos"]
print(f"Lista inicial: {compras}")


compras.append("café")        
compras.insert(0, "pão")        
compras.remove("leite")

if "banana" not in compras:
    print("Aviso: 'banana' não está na lista de compras!")



print(f"Lista de compras final organizada: {compras}")
print(f"Total de itens para comprar: {len(compras)}")
