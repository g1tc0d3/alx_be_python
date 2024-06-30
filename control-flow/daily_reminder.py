task = input ( "Enter your task: ")
priority = input ( "Priority (high, medium, low): ")
time_bound = input ( "Is it time bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print (task, "is a high priority task that requires immediate attention today!")
        else:
            print (task, "Is not a high priority task")
    case "medium":
        if time_bound == "yes":
            print (task, "Is a medium priority task")
        else:
            print (task, "Is a medium priority task ")
    case "low":
        if time_bound == "yes":
            print (task, "Is a low priority task that does not require  your immediate attention")
        else:
            print (task, "Is a low priority task. consider completing it when you ahve free time")