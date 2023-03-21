import funcitons
import PySimpleGUI as sg

label = sg.Text("Type in a place")
input_box = sg.InputText(tooltip="Enter a place")
add_button = sg.Button("Add")



window = sg.Window('Travel diary app',layout=[[label], [input_box, add_button]])
window.read()
window.close()