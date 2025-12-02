def task(n):
    for i in range(n):
        print(num,n)
        await asyncio.sleep(n)
        
async def task(num,n,delay):
    for i in range(n):
        print(num,n)
        await asyncio.sleep(delay)

async def main():
    #t1 = asuncio.create_task(task(0,4,2))
    #t2 = asuncio.create_task(task(1,6,1))
    tasks = awit asyncio.gather(task(0,4,2), task(1,6,1))
   # await t1
    #await t2
    
asyncio.run(main())