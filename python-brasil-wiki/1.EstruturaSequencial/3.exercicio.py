#!/usr/bin/env python

"""
Faça um Programa que peça dois números e imprima a soma.
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
    numero_1 = get_number("Insira o 1º número: ")
    numero_2 = get_number("Insira o 2º número: ")

    print("{} + {} = {}".format(numero_1, numero_2, numero_1 + numero_2))

