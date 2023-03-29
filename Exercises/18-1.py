import PySimpleGUI as sg
from cal_for171 import convert
sg.theme("DarkBlack")

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")


label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_button = sg.Button("convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("exit")

window = sg.Window('Convertor', [[label1, input1], [label2, input2], [convert_button, exit_button, output_label]])



while True:

    event, values = window.read()
    match event:
       case "convert":
          feet = float(values["feet"])
          inches = float(values["inches"])
          result = convert(feet, inches)
          window["output"].update(f"{result} m")
       case "exit":
           break
window.close()