import PySimpleGUI as sg 
import  os



def Load_File():
        
        working_directory = os.getcwd()
        
        layout = [
                  [sg.Text("Choose a Text File")],
                  [sg.InputText(key="-FILE_PATH-"),
                  sg.FileBrowse(initial_folder=working_directory, file_types = [('Text Files', '*.txt')])],
                 [sg.Button("Submit"), sg.Exit()]
                 ]
        window = sg.Window("File Loader", layout)
        
        while True:
                event, values = window.read()
                
                if event in (sg.WIN_CLOSED, 'Exit'):
                        break
                elif event == "Submit":
                        text_address = values["-FILE_PATH-"]
                        text_file = open(text_address)
                        text_file.read()
                        row_information = []
                        for line in text_file:
                                row_information.append(line)
                                print(row_information)
                        
                        text_file.close()
                        
                
        window.close()
        
def Save_File(rows):
        
        with open('Accounts.txt', 'w') as file:
                file.write(rows)
                
        ##https://realpython.com/read-write-files-python/

        file.close()

def Add_Account(row_information):
        
        
        
        
        
        layout = [[sg.Text('Account'), sg.Input()],
                  [sg.Text('Username'), sg.Input()],
                  [sg.Text('Password'), sg.Input()],
                  [sg.Text('Rank'), sg.Input()],
                  [sg.Text('LP'), sg.Input()],
                  [sg.Text('Win Rate'), sg.Input()],
                  [sg.Text('Win/Loss'), sg.Input()],
                  [sg.OK(), sg.Cancel()]]
        
        window = sg.Window('Account Wizard', layout)
        
        event , values = window.read()
        
        while True:
                if event == "OK":
                        for i in values:
                                
                                row_information.append(values[i])
                                
                        break
                        
                
                if event == "Cancel":
                        break
        
       
        window.close()