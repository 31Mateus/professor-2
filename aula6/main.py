import flet as ft

clientes = []

def main(pagina:ft.Page):
    def adicionar_clientes(e):
        user = {
            "nome":nome.value,
            "senha":senha.value
        }
        clientes.append(user)
        pagina.add(ft.Text(f"Cliente cadastrado com sucesso!"))
        
    def exibir_clientes(e):
            for cli in clientes:
                pagina.add(ft.Text(f"{cli["nome"]} - {cli["senha"]}"))
    
            pagina.update()
    
    ola = ft.Text("Cadastro", size=50)
    nome = ft.TextField(hint_text="Digite o seu nome:")
    senha = ft.TextField(hint_text="Digite a sua senha:", password=True,can_reveal_password=True)
    botao = ft.ElevatedButton("Cadastrar",on_click=adicionar_clientes)
    
    carregar = ft.ElevatedButton("Carregar",on_click=exibir_clientes)
    
    resultados = ft.Text(clientes)
    
    pagina.add(ola,nome,senha,botao,carregar,resultados)

ft.app(target=main)