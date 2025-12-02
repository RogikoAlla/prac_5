import asyncio

async def squarer(n):
    await *squarer()
    return n*n
    
async doudler(n):
    await *doubler()
    return 2*n
    

async def main():
    x,y = await asyncio.gather(doudler(x,0.5), doubler(y,1))
    print([x,y])
asyncio.run(main())