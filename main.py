import lib

lib.intro()
task = lib.Task()
lib.fileControl()

taskList = lib.classifier()
choose = ""
while choose.lower() != "q":
    lib.listTask(taskList)
    choose = input("Choose one of task ID for showing details => ")        
    lib.taskDetails(choose, taskList)
    
    if choose.lower() == "q":
        lib.clearScreen()