import asyncio
from datetime import datetime

async def task1():
    await asyncio.sleep(1)
    print("Task 1")

async def task2():
    await asyncio.sleep(1)
    print("Task 2")

async def task3():
    await asyncio.sleep(1)
    print("Task 3")

async def task4():
    await asyncio.sleep(1)
    print("Task 4")

async def task5():
    await asyncio.sleep(1)
    print("Task 5")

async def task6():
    await asyncio.sleep(1)
    print("Task 6")

async def task7():
    await asyncio.sleep(1)
    print("Task 7")

async def task8():
    await asyncio.sleep(1)
    print("Task 8")


async def main():
    await asyncio.gather(task1(), task2(), task3(), task4(), task5(), task6(), task7(), task8())

if __name__ == "__main__":
    datetime1 = datetime.now()
    print("Boshlang'ich vaqt", datetime.now())
    asyncio.run(main())
    datetime2 = datetime.now()
    print("So'ngi vaqt", datetime.now())
    print("Asynchronda shuncha vaqt ketdi", datetime2 - datetime1)

# Asychronda ko'rishimiz mumkinki 1 sekund oldi    