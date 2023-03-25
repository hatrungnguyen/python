import funcitons
import PySimpleGUI as sg

label = sg.Text("Type in a place")
input_box = sg.InputText(tooltip="Enter a place", key="place")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=funcitons.list_place(), key="places",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window('Travel diary app',
                   layout=layout,
                   font=('Helvetica', 20))

while True:

    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            places = funcitons.list_place()
            new_place = values['place'] + "\n"
            places.append(new_place)
            funcitons.write_place(places)
            window['places'].update(values=places)
        case "Edit":
            place_to_edit = values['places'][0]
            new_place = values['place']
            places = funcitons.list_place()
            index = places.index(place_to_edit)
            places[index] = new_place
            funcitons.write_place(places)
            window['places'].update(values=places)
        case "places":
            window['place'].update(value=values['places'][0])
        case sg.WIN_CLOSED:
            break

window.close()