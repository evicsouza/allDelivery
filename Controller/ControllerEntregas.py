class ControllerEntregas:
    def calcula_valor_Entrega(KM, preco_Combustivel, distancia):
        calculo = 10 + KM*preco_Combustivel
        return calculo

    def calcula_Valor_Pedido(produto, KM, preco_Combustivel, distancia):
        valor_Final = produto.getPreco() + calcula_valor_Entrega(KM,
                                                                  preco_Combustivel, distancia)
        return valor_Final
