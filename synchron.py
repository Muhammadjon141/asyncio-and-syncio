import time
from datetime import datetime

def task1():
    time.sleep(1)
    print("Task 1")

def task2():
    time.sleep(1)
    print("Task 2")

def task3():
    time.sleep(1)
    print("Task 3")

def task4():
    time.sleep(1)
    print("Task 4")

def task5():
    time.sleep(1)
    print("Task 5")

def task6():
    time.sleep(1)
    print("Task 6")
    
def task7():
    time.sleep(1)
    print("Task 7")
    
def task8():
    time.sleep(1)
    print("Task 8")
if __name__ == "__main__":
    datetime1 = datetime.now()
    print("Boshlang'ich vaqt", datetime.now())
    task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8()
    datetime2 = datetime.now()
    print("So'ngi vaqt", datetime.now())
    print("Synchronda shuncha vaqt ketdi", datetime2 - datetime1)

# sychronda ko'rishimiz mumkinki 8 sekund oldi    