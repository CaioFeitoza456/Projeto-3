
# O usuário deve poder adicionar, 
# remover, alterar, listar e modificar 
# itens na lista. 
# OBS: Deve-se usar dicionário


def adiciona_item(item, quantidade):
    # Função que recebe um item e sua
# quantidade e adiciona este item à
# lista, junto com sua quantidade
    lista_de_itens[item] = quantidade


def remove_item(item):
    # Função que recebe um item e deleta
# ele da lista
    del lista_de_itens[item]


def modifica_item(velho_item, novo_item, nova_quantidade):
    # Recebe o velho_item e elimina-o.
# Recebe um novo_item e uma nova_quantidade
# e cria um par de chave e valor novo
    del lista_de_itens[velho_item]
    lista_de_itens[novo_item] = nova_quantidade


def listar_lista(lista):
    # Função que recebe uma lista e itera
# sobre ela
    print("Sua lista:")
    print()
    for item, quantidade in lista.items():
        print(f"Item: {item}")
        print(f"Quantidade: {quantidade}")
        print()


# Lista original onde tudo se inicia
lista_de_itens = dict()

while True:
    print("""
♤♤ MENU DE OPÇÕES ♤♤

A - Adicionar
R - Remover
M - Modificar
L - Listar
S - Sair
    """)
    
    # Leitura da opção digitada pelo usuário
    opcao = input("Digite aqui: ").upper()
    
    # Se a opção digitada for "S" o programa
# é encerrado
    if opcao == "S":
        break
    
    # Se for "L" itera sobre a lista(com a 
# função)
    elif opcao == "L":
        
        # Verifica se a lista original tem ao
        # menos 1 item
        if len(lista_de_itens) < 1:
            print("A lista está vazia.")
            continue
        
        # Se tiver mais de 1 item, chame a função
        listar_lista(lista_de_itens)
        continue
    
    
    # Caso o usuário não digite nenhuma das duas
    # opções acima, quer dizer que ele quer ou adicionar,
    # remover ou modificar um item da lista. Por isso,
    # receba o nome do item:
    item = input("Nome do item: ").capitalize()
    
    # Se o usuário digitar "A"(adicionar) entre neste if
    if opcao == "A":
        # Leia a quantidade do item a ser 
        # adicionado
        quantidade = input("Quantidade: ")
        
        # E chame a função responsável
        adiciona_item(item, quantidade)
    
    
    # Se for "R"(remover), entre neste elif
    elif opcao == "R":
        
        # Este if verifica se o item a ser removido
        # realmente está na lista, para evitar erros de chave
        if item in lista_de_itens:
            remove_item(item)
            print(f"'{item}' removido.")
         
        # Se não estiver na lista, entre aqui
        else:
            print("Este item não está na sua lista.")
    
    
    # Se o usuário digitar "M"(modificar) entre aqui:
    elif opcao == "M":
        
        # Verifica se o item a ser modificado está na lista
        if item in lista_de_itens:
            # Leia o nome do novo item a ser adicionado
            novo_item = input("Novo item: ").capitalize()
            # Leia a quantidade do novo item
            nova_quantidade = input("Nova quantidade: ")
            
            # Chame a função, passando os argumentos em
            # sequência posicional
            modifica_item(item, novo_item, nova_quantidade)
        
        else:
            print(f"O item '{item}' não está na lista.")
    
    else:
        print("Você não digitou uma opção válida.")
