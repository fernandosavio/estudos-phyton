#!/usr/bin/env python

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""


def float_or_int(number):
    return int(number) if number.is_integer() else float(number)


def get_number(input_question):
    numero = None

    while not numero:
        try:
            numero = float(input(input_question))
            return float_or_int(numero)
        except TypeError:
            raise TypeError("O valor informado deve ser um número (separador de casas decimais deve ser ponto)")


if __name__ == "__main__":
    valor_hora = float(get_number("Informe quando você ganha por hora: "))
    qtde_horas = float(get_number("Informe quantidade de horas trabalhadas no mês: "))

    print("O salário mensal foi de R$ {}".format(float_or_int(round(valor_hora * qtde_horas, 2))))

