"""This module includes all objects and functions
required for running VAZIFE"""

import getpass, os
from colorama import Fore, Back, Style
class Task:
    """Task object."""
    taskID = ""
    task = ""
    class CreatedTime: 
        year = 0
        month = 0
        day = 0
        hour = 0
        minute = 0

    class TaskTime(CreatedTime):
        pass

    class EditedTime(CreatedTime):
        pass
    
    taskUser = ""
    isComplete = False
    notes = ""




def intro():
    clearScreen()
    lineCenter = int(os.get_terminal_size().lines / 2)
    columnCenter = os.get_terminal_size().columns
    for i in range(0,int(lineCenter / 2)):
        print("")

    print("Welcome to VAZIFE".center(columnCenter))
    print("pre-alpha.v0.1".center(columnCenter))
    
def clearScreen():
    """Prints a special string for clearing screen"""
    print('\x1bc')

def skip():
    """For Skip Lines"""
    skip = input("For continue press ENTER. . .")




def fileControl():
    """Try to detect todo.txt. If cant find, this func will create it"""
    try:
        file = open("todo.txt","r")
    except FileNotFoundError:
        file = open("todo.txt","w")
        file.write("This is todo file of {0}\n".format(getpass.getuser()))
        file.write("taskID|Task|Created Time|Task Time|Created By|Completed")
        file.close()
        print("I couldn't find your todo.txt, so I've created for you!")

def classifier():
    """Returns only readable query \n
    currentTask[0] = taskID \n
    currentTask[1] = task \n
    currentTask[2] = CreatedTime() \n
    currentTask[3] = TaskTime() \n
    currentTask[4] = taskUser \n
    currentTask[5] = isComplete \n
    currentTask[6] = notes
    """
    file = open("todo.txt","r")
    taskQuery = []
    readedFile = file.readlines()
    for currentTask in readedFile:
        currentTask = currentTask.split("|")
        
        returnTask = Task()
        cache = ""
        if currentTask[0].isnumeric() == True:
            returnTask.taskID = currentTask[0]
            returnTask.task = currentTask[1]

            cache = currentTask[2].split("-")
            returnTask.CreatedTime = Task.CreatedTime()
            returnTask.CreatedTime.day, returnTask.CreatedTime.month, returnTask.CreatedTime.year = cache[0].split(".")
            returnTask.CreatedTime.hour, returnTask.CreatedTime.minute = cache[1].split(":")
            
            cache = currentTask[3].split("-")
            returnTask.TaskTime = Task.TaskTime()
            returnTask.TaskTime.day, returnTask.TaskTime.month, returnTask.TaskTime.year = cache[0].split(".")
            returnTask.TaskTime.hour, returnTask.TaskTime.minute = cache[1].split(":")

            returnTask.taskUser = currentTask[4]
            cache = currentTask[5].split("\n")
            returnTask.isComplete = cache[0]
            
            returnTask.notes = currentTask[6]
            
            taskQuery.append(returnTask)
            

    return taskQuery

def listTask(taskList):
    """Lists """
    clearScreen()
    print(Style.BRIGHT + Fore.RED + "Task ID\tTask\t\tTask Time\t\tIs Done?" + Style.RESET_ALL)
    for task in taskList:
        if task.taskUser == getpass.getuser():
            time = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + "-" + task.TaskTime.hour + ":" + task.TaskTime.minute
            print(Style.BRIGHT + "{0}".format(task.taskID) + Style.RESET_ALL + "\t{0}\t{1}\t{2}".format(task.task,time,task.isComplete))
            
def taskEdit(task):
    createdTime = task.CreatedTime.day + "." + task.CreatedTime.month + "." + task.CreatedTime.year + " - " + task.CreatedTime.hour + ":" + task.CreatedTime.minute
    taskTime = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + " - " + task.TaskTime.hour + ":" + task.TaskTime.minute
    clearScreen()
    print("""taskID: {0}
            [T]ask:{1}
            T[a]sk Time: {2}
            Created by {3} at {4}
            [N]otes:{5}
            """.format(task.taskID,task.task,taskTime,task.taskUser,createdTime,task.notes))
    menuChoose = input("Which one will be edit? => ")
    if menuChoose.lower() == "t":
        print(Style.BRIGHT + Fore.RED + "Old Value => " + Style.RESET_ALL + task.task)
        newValue = input(Style.BRIGHT + Fore.RED + "New Value => " + Style.RESET_ALL)
        task.task = newValue
        print("Your Task has been changed")
        skip()
    elif menuChoose.lower() == "a":
        time = ["Day","Month","Year","Hour","Minute"]
        newTime = []
        for i in range(len(time)):
            clearScreen()
            print(Style.BRIGHT + Fore.RED + "Old Value => " + Style.RESET_ALL + taskTime)
            inputTime = input(Style.BRIGHT + Fore.RED + "New {0} Value => ".format(time[i]) + Style.RESET_ALL)
            if int(inputTime) < 10:
                if len(inputTime) == 2:
                    pass
                else:
                    inputTime = "0" + str(inputTime)
            try:
                if len(newTime[2]) < 3:
                    newTime[2] = "20" + str(newTime[2])
            except IndexError:
                pass
            newTime.append(inputTime)
    print(newTime)
    skip()
            



        

def taskDetails(choose, taskList):
    for task in taskList:
        if task.taskID == choose and getpass.getuser() == task.taskUser:
            createdTime = task.CreatedTime.day + "." + task.CreatedTime.month + "." + task.CreatedTime.year + " - " + task.CreatedTime.hour + ":" + task.CreatedTime.minute
            taskTime = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + " - " + task.TaskTime.hour + ":" + task.TaskTime.minute
            clearScreen()
            print("""taskID: {0}
            Task:{1}
            Task Time: {2}
            Created by {3} at {4}
            Notes:{5}
            """.format(task.taskID,task.task,taskTime,task.taskUser,createdTime,task.notes))
            menuChoose = input("[E]dit [D]elete [B]ack [M]enu => ")
            print(menuChoose)
            if menuChoose.lower() == "e":
                taskEdit(task)
            else:
                print(":(")