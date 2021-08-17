import lib
from colorama import Fore, Back, Style

lib.intro()
task = lib.Task()
lib.fileControl()

taskList = lib.classifier()
choose = ""
quitChoose = ""
while quitChoose.lower() != "y":
    lib.listTask(taskList)
    choose = input("Choose one of task ID for showing details => ")        
    lib.taskDetails(choose, taskList)
    
    if choose.lower() == "q":
        quitChoose = input("Are you sure?" + Style.BRIGHT + "[y/N]: " + Style.RESET_ALL)
        lib.clearScreen()