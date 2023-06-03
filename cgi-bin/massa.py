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

"""checks for an empty value.

Makes sure that an empty value will not be used in the functions.

Args:
    value: The value that the user wants to convert.

Returns:
    If the value is not empty, it returns the same value converted to int, but if there is
    not any value, it returns -1.
"""

try:
    value = analysingValue(received)
except:
    value = 'typeError'

def convert_from_kg (value, unit2):
    if (unit2 == 'gr'):
        return f'{value} Quilogramas = {(value * 1000):.2f} Gramas'
    elif (unit2 == 'mg'):
        return f'{value} Quilogramas = {(value * 1000000):.2f} Miligramas'

"""Converts from kilograms to grams or miligrams.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from kilograms to grams or miligrams depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def convert_from_g (value, unit2):
    if (unit2 == 'kg'):
        return f'{value} Gramas = {(value / 1000):.4f} Quilogramas'
    elif (unit2 == 'mg'):
        return f'{value} Gramas = {(value * 1000):.2f} Miligramas'

"""Converts from grams to kilograms or miligrams.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from grams to kilograms or miligrams depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def convert_from_mg (value, unit2):
    if (unit2 == 'kg'):
        return f'{value} Miligramas = {(value / 1000000):.6f} Quilogramas'
    elif (unit2 == 'gr'):
        return f'{value} Miligramas = {(value / 1000):.4f} Gramas'

"""Converts from miligrams to kilograms or grams.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from miligrams to kilograms or grams depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def same_unit_message(value, unit1, unit2):
    if(unit1 == unit2 and unit1 == 'kg'):
        return f'Unidades iguais => {value:.2f} Quilogramas'
    elif(unit1 == unit2 and unit1 == 'gr'):
        return f'Unidade iguais => {value:.2f} Gramas'
    elif(unit1 == unit2 and unit1 == 'mg'):
        return f'Unidade iguais => {value:.2f} Miligramas'

"""Checks if the user put the same unit to convert to.

It checks if the user chose the same unit for the conversion
and shows the message explaining the trivial conversion.

Args:
    value: The value that the user wants to convert.
    unit1: The unit that the user wants to convert from.
    unit2: The unit that the user wants to convert to.

Returns:
    A message showing the not quite so conversion performed.
"""

def error_message(value, unit1, unit2):
    if (value == 'typeError'):
        return 'Erro: Tipo de Valor inesperado !'
    elif (value == -1):
        return 'Erro: Campos sem valores !'
    elif (unit1 == 'sel' or unit2 =='sel'):
        return 'Erro: Selecione uma unidade !'

"""Checks the type of error.

Checks the value of the parameters and shows the possible types of 
errors envolved with them.

Args:
    value: The value that the user wants to convert.
    unit1: The unit that the user wants to convert from.
    unit2: The unit that the user wants to convert to.

Returns:
    A message expliciting what type of error has occurred.
"""

def check_for_errors (value, unit1, unit2):
    if (value == 'typeError'):
        return True
    elif (value == -1):
        return True
    elif (unit1 == 'sel' or unit2 =='sel'):
        return True
    else: 
        return False

"""Checks for errors in the variables used.

It searches for values in the variables that can cause conflicts
in arithmetic operations.

Args:
    value: The value that the user wants to convert.
    unit1: The unit that the user wants to convert from.
    unit2: The unit that the user wants to convert to.

Returns:
    A boolean indicating that a variable contains a value that
    can cause problems.
"""

def convertUnits(value, unit1, unit2):
    if check_for_errors(value, unit1, unit2):
        return error_message(value, unit1, unit2)
    elif(unit1 == unit2):
        return same_unit_message(value, unit1, unit2)
    elif (unit1 == 'kg'):
        return convert_from_kg(value, unit2)
    elif (unit1 == 'gr'):
        return convert_from_g(value, unit2)
    else:
        return convert_from_mg(value, unit2)

"""Checks the variables and uses it in a previously created function.

It takes the parameters and through a series of if's performing a flow control
takes one of the created functions created previously to process the information.

Args:
    value: The value that the user wants to convert.
    unit1: The unit that the user wants to convert from.
    unit2: The unit that the user wants to convert to.

Returns:
    A string containing a message showing the converted value or
    the type of error if it happens.
"""

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