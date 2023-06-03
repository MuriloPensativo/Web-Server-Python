#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()
recieved = form.getvalue('valor')
unity1 = form.getvalue('unidade1')
unity2 = form.getvalue('unidade2')
result_final = None

def analysingValue(value):
    if value:
        return int(value)
    else:
        return -1

"""checks for an empty value.

Makes sure that an empty value will not be used on the functions.

Args:
    value: The value that the user wants to convert.

Returns:
    If the value is not empty, it returns the same value converted to int, but if there is
    not any value, it returns -1.
"""

try:
    value = analysingValue(recieved)
except:
    value = 'typeError'

def convert_from_seconds (value, unit2):
    if (unit2 == 'min'):
        return f'{value} Segundos = {(value / 60):.2f} Minutos'
    elif (unit2 == 'hr'):
        return f'{value} Segundos = {(value / 3600):.4f} Horas'

"""Converts from seconds to minutes or hours.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from seconds to minutes or hours depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def convert_from_minutes (value, unit2):
    if (unit2 == 'seg'):
        return f'{value} Minutos = {(value * 60):.2f} Segundos'
    elif (unit2 == 'hr'):
        return f'{value} Minutos = {(value / 60):.2f} Horas'

"""Converts from minutes to seconds or hours.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from minutes to seconds or hours depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def convert_from_hours (value, unit2):
    if (unit2 == 'seg'):
        return f'{value} Horas = {(value * 3600):.2f} Segundos'
    elif (unit2 == 'min'):
        return f'{value} Horas = {(value * 60):.2f} Minutos'

"""Converts from hours to seconds or minutes.

Checks the unit to convert to and does the mathematical operations to perform 
the conversion from hours to seconds or minutes depending on the users input.

Args:
    value: The value that the user wants to convert.
    unit2: The unit that the user wants to convert to.

Returns:
    A formated string containing the sentence that presents the converted
    value to the user.
"""

def same_unit_message(value, unit1, unit2):
    if(unit1 == unit2 and unit1 == 'seg'):
        return f'Unidades iguais => {value:.2f} Segundos'
    elif(unit1 == unit2 and unit1 == 'min'):
        return f'Unidade iguais => {value:.2f} Minutos'
    elif(unit1 == unit2 and unit1 == 'hr'):
        return f'Unidade iguais => {value:.2f} Horas'

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
    elif (unit1 == 'seg'):
        return convert_from_seconds(value, unit2)
    elif (unit1 == 'min'):
        return convert_from_minutes(value, unit2)
    else:
        return convert_from_hours(value, unit2)

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
    result_final = convertUnits(value, unity1, unity2)
except:
    result_final = 'Erro Inesperado'

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<link rel="stylesheet" href="../style.css">')
print('<title>Resultado: Tempo</title>')
print("</head>")
print("<body>")
print("<section>")
print('<div class ="main">')
print('<h1>Resultado:</h1>')
print("<h2>{}</h2>".format(result_final))
print('<a class="back" href="../tempo.html">Voltar</a>')
print("</div>")
print("</section>")
print("</body>")
print("</html>")

