#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
received = form.getvalue('valor')
unit1 = form.getvalue('unidade1')
unit2 = form.getvalue('unidade2')
resultFinal: int

def analysingValue(value):
    if value:
        return int(value)
    else:
        return -1

try:
    value = analysingValue(received)
except:
    value = 'typeError'

def convert_from_kg (value, unit2):
    if (unit2 == 'gr'):
        return f'{value} Quilogramas = {(value * 1000):.2f} Gramas'
    elif (unit2 == 'mg'):
        return f'{value} Quilogramas = {(value * 1000000):.2f} Miligramas'

def convert_from_g (value, unit2):
    if (unit2 == 'kg'):
        return f'{value} Gramas = {(value / 1000):.4f} Quilogramas'
    elif (unit2 == 'mg'):
        return f'{value} Gramas = {(value * 1000):.2f} Miligramas'

def convert_from_mg (value, unit2):
    if (unit2 == 'kg'):
        return f'{value} Miligramas = {(value / 1000000):.6f} Quilogramas'
    elif (unit2 == 'gr'):
        return f'{value} Miligramas = {(value / 1000):.4f} Gramas'

def same_unit_message(value, unit1, unit2):
    if(unit1 == unit2 and unit1 == 'kg'):
        return f'Unidades iguais => {value:.2f} Quilogramas'
    elif(unit1 == unit2 and unit1 == 'g'):
        return f'Unidade iguais => {value:.2f} Gramas'
    elif(unit1 == unit2 and unit1 == mg):
        return f'Unidade iguais => {value:.2f} Miligramas'

def error_message(value, unit1, unit2):
    if (value == 'typeError'):
        return 'Erro: Tipo de Valor inesperado !'
    elif (value == -1):
        return 'Erro: Campos sem valores !'
    elif (unit1 == 'sel' or unit2 =='sel'):
        return 'Erro: Selecione uma unidade !'

def check_for_errors (value, unit1, unit2):
    if (value == 'typeError'):
        return True
    elif (value == -1):
        return True
    elif (unit1 == 'sel' or unit2 =='sel'):
        return True
    else: 
        return False

def convertUnits(value, unit1, unit2):
    if check_for_errors(value, unit1, unit2):
        return error_message(value, unit1, unit2)
    elif(unit1 == unit2):
        return same_unit_message(value, unit1, unit2)
    elif (unit1 == 'kg'):
        return convert_from_kg(value, unit2)
    elif (unit1 == 'g'):
        return convert_from_g(value, unit2)
    else:
        return convert_from_mg(value, unit2)

try:
    resultFinal = convertUnits(value, unit1, unit2)

except:
    resultFinal = 'Erro Inesperado'


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