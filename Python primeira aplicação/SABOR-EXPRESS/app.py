from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Vinao', 10)
restaurante_praca.receber_avaliacao('Dani', 8)
restaurante_praca.alternar_estado()

restaurante_mexicano = Restaurante('mexican food', 'comida mexicana')
restaurante_japones = Restaurante('Japa', 'japonesa')
restaurante_japones.alternar_estado()


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
