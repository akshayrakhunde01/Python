sum = 5 + 3
is_equal = (sum == 8)
# 

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")

for i in range(5):  # 0 to 4
    print(i)


try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always run.")


# async

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
