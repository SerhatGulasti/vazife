class Task:
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

def fileControl():
    """Try to detect todo.txt. If cant find, this func will create it"""
    try:
        file = open("todo.txt","r")
    except FileNotFoundError:
        import getpass
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
            
            taskQuery.append(returnTask)
            

    return taskQuery

def listTask(taskList):
    print("Task ID \t Task \t Task Time \t Is Done?")
    for task in taskList:
        time = task.TaskTime.day + "." + task.TaskTime.month + "." + task.TaskTime.year + "-" + task.TaskTime.hour + ":" + task.TaskTime.minute
        print(task.isComplete)