# Função para adicionar produto
def adicionar_produto(produtos):
    nome = input("Digite o nome: \n")
    preco = input("Digite o preço: \n")
    quantidade = input("Digite a quantidade: \n")
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)

# Função para remover produto
def remover_produto(produtos):
    nome = input("Digite o nome do produto a ser removido: \n")
    for produto in produtos:
        if produto["nome"] == nome:
            produtos.remove(produto)
            print(f'Produto {nome} removido com sucesso.')
            return
    print(f'Produto {nome} não encontrado.')

# Função para listar produtos
def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f'Nome: {produto["nome"]}, Preço: {produto["preco"]}, Quantidade: {produto["quantidade"]}')

# Lista de produtos
produtos = []

# Menu
print("Bem-vindo ao estoque de produtos\n\n")
print("1 - Adicionar item")
print("2 - Remover item")
print("3 - Listar itens")
resultado = int(input("\nDigite o que você deseja fazer: "))

if resultado == 1:
    adicionar_produto(produtos)
elif resultado == 2:
    remover_produto(produtos)
elif resultado == 3:
    listar_produtos(produtos)
else:
    print("Opção inválida.")