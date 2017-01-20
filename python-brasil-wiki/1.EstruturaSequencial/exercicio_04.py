#!/usr/bin/env python

"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""


def get_number(input_question):
    numero = None

    while not numero:
        try:
            numero = float(input(input_question))
            if numero.is_integer():
                numero = int(numero)

            return numero
        except TypeError:
            raise TypeError("O valor informado deve ser um número (separador de casas decimais deve ser ponto)")


if __name__ == "__main__":
    nota_1 = get_number("Insira a 1ª nota: ")
    nota_2 = get_number("Insira a 2ª nota: ")
    nota_3 = get_number("Insira a 3ª nota: ")
    nota_4 = get_number("Insira a 4ª nota: ")

    media = sum((nota_1, nota_2, nota_3, nota_4)) / 4

    print("1ª nota: {:>4.2f}".format(nota_1))
    print("2ª nota: {:>4.2f}".format(nota_2))
    print("3ª nota: {:>4.2f}".format(nota_3))
    print("4ª nota: {:>4.2f}".format(nota_4))
    print("-----------------")
    print("= Média: {:>4.2f}".format(round(media, 2)))
