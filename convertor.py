# importing the libraries
import PySimpleGUI as sg
from forex_python.converter import CurrencyRates

# creating a list which contains all the currencies
c = CurrencyRates()
supported_currencies = c.get_rates('USD')
currencies = list(supported_currencies.keys())
currencies.append('USD')


# function to convert the values
def convert(from_currency, to_currency, amount):
    final = round(c.convert(from_currency, to_currency, float(amount)), 2)
    return window["-OUTPUT-"].update(f"Converted it is {final}{to_currency}")


#                                               FRONT END
# --------------------------------------------------------------------------------------------------------
# assigning a theme to the window
sg.theme('DarkGreen6')

# creating a layout for the window
layout = [[sg.Text('From currency', pad=10), sg.InputText(default_text="EUR", tooltip="Enter a currency here"),
           sg.Text('To currency'), sg.InputText(default_text="BGN", tooltip="Enter a currency here")],
          [sg.Text('Enter amount', pad=10),
           sg.Input(key="-NUM-", do_not_clear=False, pad=10, tooltip="Enter a value here"), sg.Text(key="-OUTPUT-")],
          [sg.Button('Convert'), sg.Button('Cancel')]]

window = sg.Window('Converter', layout)

# running the code
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    values[2] = values["-NUM-"]
    values[0], values[1] = values[0].upper(), values[1].upper()

    if values[0] in currencies and values[1] in currencies:
        try:
            convert(values[0], values[1], values[2])
        except ValueError:
            sg.popup("Invalid input! Please enter a valid number (integer or float) and a valid currency.",
                     title = "Error!")
    else:
        sg.popup(f"Invalid input! Please enter valid currencies.\nList of valid currencies: {currencies}",
                 title = "Error!")

window.close()
