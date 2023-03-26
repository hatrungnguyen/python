import funcitons
import PySimpleGUI as sg
import time
import os

if not os.path.exists("listoftouristattraction.txt"):
    with open("listoftouristattraction.txt", "w"):
        pass


sg.theme("DarkBlack")

clock = sg.Text(key="clock")
label = sg.Text("Type in a place")
input_box = sg.InputText(tooltip="Enter a place", key="place")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=funcitons.list_place(), key="places",
                      enable_events=True, size=[45, 5])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")



layout = [[clock], [label], [input_box, add_button], [list_box, edit_button,complete_button], [exit_button]]

window = sg.Window('Travel diary app',
                   layout=layout,
                   font=('Helvetica', 20))

while True:

    event, values = window.read(timeout=800)
    window["clock"].update(time.strftime("%b %d, %Y %H:%M:%S"))


    match event:
        case "Add":
            places = funcitons.list_place()
            new_place = values['place'] + "\n"
            places.append(new_place)
            funcitons.write_place(places)
            window['places'].update(values=places)
        case "Edit":
             try:
                 place_to_edit = values["places"][0]
                 new_place = values["place"]

                 places = funcitons.list_place()
                 index = places.index(place_to_edit)
                 places[index] = new_place
                 funcitons.write_place(places)
                 window["places"].update(values=places)
             except IndexError:
               sg.popup("Please select a place.", font=("Helvetica", 20))

        case "Complete":
            try:
               place_to_complete = values["places"][0]
               places = funcitons.list_place()
               places.remove(place_to_complete)
               funcitons.write_place(places)
               window["places"].update(values=places)
               window["place"].update(value='')
            except IndexError:
                sg.popup("Please select a place.", font=("Helvetica", 20))
        case "Exit":
            break
        case "places":
            window['place'].update(value=values['places'][0])
        case sg.WIN_CLOSED:
            break

window.close()