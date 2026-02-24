def adicionar_item(carrinho, item, preco):
    carrinho[item] = preco
    print(f"{item} => {preco} - adicionado ao carrinho")

    if(preco > 100):
        print("Cupom de desconto disponível")

meu_carrinho = {}
adicionar_item(meu_carrinho, "Notebook", 3000)
adicionar_item(meu_carrinho, "Mouse", 250)
adicionar_item(meu_carrinho, "Teclado", 500)

print(meu_carrinho)