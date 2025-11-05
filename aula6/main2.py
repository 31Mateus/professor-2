import flet as ft

estoque = []

def main(pagina:ft.Page):
    def cadastrar_produto(e):
        print(nome_produto.value)
        produto = {
            "nome":nome_produto.value,
            "preco":preco_produto.value,
            "quantidade":quantidade_produto.value
        }
        estoque.append(produto)
        print(estoque)
        carregar_produtos()
        pagina.update()

    def carregar_produtos():
        linha.controls.append(ft.Text(estoque))
    
    titulo = ft.Text("Gerenciador de estoque",size=50)
    nome_produto = ft.TextField(hint_text="Digite o nome do produto:")
    preco_produto = ft.TextField(hint_text="Digite o preço:")
    quantidade_produto = ft.TextField(hint_text="Digite a quantidade:")
    botao = ft.ElevatedButton("Adicionar",on_click=cadastrar_produto)
    
    linha = ft.Row(controls=[])
    
    pagina.add(titulo,nome_produto,preco_produto,quantidade_produto,botao)
ft.app(target=main)