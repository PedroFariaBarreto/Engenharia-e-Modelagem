import tkinter as tk
from tkinter import messagebox


class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome} | Qtd: {self.quantidade} | Preço: R${self.preco:.2f}" #def para retornar o produto


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade, preco): #def para adicionar o produto e salvar em uma lista
        novo_produto = Produto(nome, quantidade, preco)
        self.produtos.append(novo_produto)

    def listar_produtos(self): #def para retornar a lista de produtos
        return self.produtos


class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Estoque") #Cria o título

        self.estoque = Estoque()

        frame_entrada = tk.Frame(root, padx=10, pady=10)
        frame_entrada.pack()

        #da linha 38-48 cria os campos para preenchimento
        tk.Label(frame_entrada, text="Nome:").grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(frame_entrada, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5)

        tk.Label(frame_entrada, text="Quantidade:").grid(row=1, column=0, sticky="w")
        self.entry_quantidade = tk.Entry(frame_entrada, width=10)
        self.entry_quantidade.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(frame_entrada, text="Preço (R$):").grid(row=2, column=0, sticky="w")
        self.entry_preco = tk.Entry(frame_entrada, width=10)
        self.entry_preco.grid(row=2, column=1, sticky="w", padx=5)

        frame_botoes = tk.Frame(root, pady=10)
        frame_botoes.pack()
        #as duas linhas seguintes criam os botões para adicionar e listar
        tk.Button(frame_botoes, text="Adicionar Produto", command=self.adicionar_produto).grid(row=0, column=0, padx=5)
        tk.Button(frame_botoes, text="Listar Produtos", command=self.listar_produtos).grid(row=0, column=1, padx=5) 

        frame_lista = tk.Frame(root, padx=10, pady=10)
        frame_lista.pack()

        tk.Label(frame_lista, text="Produtos no Estoque:").pack(anchor="w")
        self.lista_produtos = tk.Listbox(frame_lista, width=60, height=10)
        self.lista_produtos.pack()

    def adicionar_produto(self):
        nome = self.entry_nome.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        preco = self.entry_preco.get().strip()

        if not nome or not quantidade or not preco:  #condicional para preencher os campos
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            quantidade = int(quantidade)
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e preço devem ser numéricos!") #condicional para ser numéricos
            return

        self.estoque.adicionar_produto(nome, quantidade, preco)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!") #mensagem quando produto for salvo sem erros

        self.entry_nome.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)

    def listar_produtos(self):
        self.lista_produtos.delete(0, tk.END)
        produtos = self.estoque.listar_produtos()
        if not produtos:
            self.lista_produtos.insert(tk.END, "Nenhum produto cadastrado ainda.") #mensagem caso a lista esteja vazia
        else:
            for produto in produtos:
                self.lista_produtos.insert(tk.END, str(produto))


if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()


