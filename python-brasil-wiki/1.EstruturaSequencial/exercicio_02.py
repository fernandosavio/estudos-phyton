#!/usr/bin/env python

"""
Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]."
"""

if __name__ == "__main__":
    numero = None

    while not numero:
        try:
            numero = float(input("Informe um número: "))
            if numero.is_integer():
                numero = float(numero)

            print("O número informado foi {}".format(numero))
        except TypeError:
            print("=== Erro: o valor informado deve ser um número (separador de casas decimais deve ser ponto)")
