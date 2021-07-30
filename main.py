import lib

task = lib.Task()
lib.fileControl()

taskList = lib.classifier()
choose = ""
while choose != "q":
    lib.listTask(taskList)
    choose = input("Choose one of task ID for showing details => ")
    lib.taskDetails(choose, taskList)