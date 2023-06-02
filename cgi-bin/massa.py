#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
recieved = form.getvalue('valor')
unit1 = form.getvalue('unidade1')
unit2 = form.getvalue('unidade2')
resultFinal = None

def analysingValue(value):
    if value:
        return int(value)
    else:
        return -1

try:
    value = analysingValue(recieved)

except:
    value = 'typeError'

def convert_from_kg (value, unit1, unit2):


def convert_from_g (value, unit1, unit2):


def convert_from_mg (value, unit1, unit2):


def check_same_unit(value, unit1, unit2):
    if (unit1 == unit2 and unit1 != 'sel'):
                if(unit1 == 'kg'):
                    result = f'Unidades iguais => {value:.2f} Quilogramas'

                elif(unit1 == 'g'):
                    result = f'Unidade iguais => {value:.2f} Gramas'
                else:
                    result = f'Unidade iguais => {value:.2f} Miligramas'

def check_error():

"""
def convertUnits(value, unit1, unit2):
    if(value!=-1 and value != 'typeError'):
        

        elif (unit1 != 'sel' and unit2 =='sel'):
            result = 'Erro: Selecione uma unidade !'

        elif unit1 == 'kg':
            if (unit2 == 'gr'):
                result = '{} Quilogramas = {:.2f} Gramas'.format(value, (value * 1000))

            elif (unit2 == 'mg'):
                result = '{} Quilogramas = {:.2f} Miligramas'.format(value, (value * 1000000))

        elif unit1 == 'gr':
            if (unit2 == 'kg'):
                result = '{} Gramas = {:.4f} Quilogramas'.format(value, (value / 1000))

            elif (unit2 == 'mg'):
                result = '{} Gramas = {:.2f} Miligramas'.format(value, (value * 1000))

        elif unit1 == 'mg':
            if (unit2 == 'kg'):
                result = '{} Miligramas = {:.6f} Quilogramas'.format(value, (value / 1000000))

            elif (unit2 == 'gr'):
                result = '{} Miligramas = {:.4f} Gramas'.format(value, (value / 1000))

        else:
            result = 'Erro: Selecione uma unidade !'

    elif (value == 'typeError'):
        result = 'Erro: Tipo de Valor inesperado !'

    else:
        result = 'Erro: Campos sem valores !'

    return result

try:
    resultFinal = convertUnits(value, unit1, unit2)

except:
    resultFinal = 'Erro Inesperado'
"""

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Massa</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(resultFinal))
print('<a class="back" href="../massa.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")