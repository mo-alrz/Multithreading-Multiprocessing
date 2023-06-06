import asyncio


async def first():
    print('hi')
    await asyncio.sleep(2)
    print('hi again')
    await asyncio.sleep(0.20)
    print('agaaaain')
    return {'data':1}


async def second():
    for i in range(1,11):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task_1 = asyncio.create_task(first())
    task_2 = asyncio.create_task(second())

    value = await task_1
    print(value)
    await task_2

asyncio.run(main())
