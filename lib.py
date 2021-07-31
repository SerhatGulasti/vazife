"""This module includes all objects and functions
required for running VAZIFE"""

import getpass
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

    taskUser = ""
    isComplete = False
    notes = ""

def skip():
    """For Skip Lines"""
    skip = input("For continue press ENTER. . .")
    
def clearScreen():
    """Prints a special string for clearing screen"""
    print('\x1bc')

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
    """Returns only readable query"""
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
    print(Style.BRIGHT + Fore.RED + "Task ID\tTask\t\tTask Time\t\tIs Done?" + Style.RESET_ALL)
    for task in taskList:
        if task.taskUser == getpass.getuser():
            time = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + "-" + task.TaskTime.hour + ":" + task.TaskTime.minute
            print(Style.BRIGHT + "{0}".format(task.taskID) + Style.RESET_ALL + "\t{0}\t{1}\t{2}".format(task.task,time,task.isComplete))
            
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
            choose = input("[E]dit [D]elete [M]enu [Q]uit => ")
            if choose == "e" or "E":
                editTask(task.taskID, task)

def editTask(choose, task):
    createdTime = task.CreatedTime.day + "." + task.CreatedTime.month + "." + task.CreatedTime.year + " - " + task.CreatedTime.hour + ":" + task.CreatedTime.minute
    taskTime = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + " - " + task.TaskTime.hour + ":" + task.TaskTime.minute
    clearScreen()
    print("""taskID: {0}
            [T]ask:{1}
            T[a]sk Time: {2}
            Created by {3} at {4}
            [N]otes:{5}
            """.format(task.taskID,task.task,taskTime,task.taskUser,createdTime,task.notes))

    def editValue(value):
        clearScreen()
        print(Fore.RED + Style.DIM + "Old Value: " + Style.RESET_ALL + value)
        return input(Style.BRIGHT + "New Value => " + Style.RESET_ALL)
        
    choose = input("What do you want to change? => ")
    if choose == "T" or "t":
        editValue(task.task)
    elif choose == "n" or "N":
        editValue(task.notes)