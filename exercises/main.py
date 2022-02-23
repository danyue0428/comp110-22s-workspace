# """Input 4 variables."""

# # tasks: str, duration: float, importance: int, ddl: float



#     i = 0
#     tasks: list[str] = list()
#     durations: list[float] = list()
#     importances: list[int] = list()
#     ddls: list[float] = list()
#     answer: str = str(input("Do you have plan today (yes/no): "))
#     while answer.lower() == "yes":
#         task: str = str(input("please list one thing you want to do today: "))
#         tasks.append(task)
#         duration: float = float(input(f"what is the time duration of {task} in hours :"))
#         durations.append(duration)
#         importance: int = int(input(f"What is the importance of {task} (1-5, 5 means the most important): "))
#         importances.append(importance)
#         ddl: float = float(input(f"what is the ddl for {task} in 24 hours(e.x 15:30 = 15.5): "))
#         ddls.append(ddl)
#         i += 1
#         answer: str = str(input("Do you have other plan to do? (yes/no): "))
#     else:
#         print("Gotcha! Thank you so much!")
    
#     print(tasks)
#     print(durations)
#     print(importances)
#     print(ddls)



from numpy import float128


def avaliable_time_slot() -> list:
    i: int = 1
    ls: list[float] = list()
    while i < 1000:
        print(f"====Please enter your {i}th avaliable timeslot====")
        start_time: float = float(input("Please enter the start time: "))
        end_time: float = float(input("Please enter the end time: "))
        xs = [start_time, end_time]
        ls.append(xs)
        ask: str = input("Is that all?(Y/N)")
        if ask.lower() == "y":
            print(ls)
            return ls
        else:
            i += 1


def available_interval(ls: list[float]) -> list[float]:
    i: int = 0
    ls: list[float] = list()
    while i < len(ls):
        x: float = ls[i][1]
        y: float = ls[i][2]
        ls.append(y-x)
        i += 1
    return ls    
    

def main() -> None:
    available_time_slot()
    available_interval()



if __name__ == "__main__":
    main()

def duration_matches(x: list, y: list) -> :
    i = 0
    ls = things_to_do()
    while i < len(ls):
        TI = ls[i][3]
        j = 0
        while TI > AT[j]:
            TI = TI - AT[j]
            j += 1
            if j > len(AT):
                quit()
            else:
                end_time = available_time_slot[j][1] + TI
        
        if end_time < ls[i][4]:
            i += 1
            available_time_slot = end_time
            

def available_interval(ts: list, x: float, y: float) -> list[float]:
    start_time: float = float(input("Please enter the start time: "))
    end_time: float = float(input("Please enter the end time: "))
    xs = (start_time, end_time)
    ts.append(xs)
    for i in ts:
        x = i[0]
        y = i[1]
        different: list[]
        different += y - x

