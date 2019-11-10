import os.path
from Model.Produto import Produto


class RepositorioProduto:
    produtos = []
    separador = ';'

    def criaArquivo():
        if(!os.path.exists('produtos.txt')):
            arquivo = open('produtos.txt', w)
            arquivo.close()

    def cadastrarProduto(produto):
        produtos.append(produto)

    def atualizaProduto(id, categoria, descricao, preco):
        produto = recuperarProduto(id)
        produto.setDescricao(descricao)
        client.setCategoria(categoria)
        client.setPreco(preco)

    def recuperarProduto(id):
        for i in range(len(produtos)):
            if(produto[i].getId() == id):
                return produto[i]

    def salvarArquivo():
        arquivo = open('produtos.txt')
        for i in range(len(produtos)):
            arquivo.write(produtos[i].toString()+'\n')
