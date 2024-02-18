from random import randint 
from time import time
from os import system, name
from colorama import Back, init

init(autoreset=True)
tre = 0
times = int(input("how much number do you want to take for exam : "))
scor = 0
os_base = name # Using name from os Module, to get User's Operating System ( Windows: nt, Linux: posix, not sure about mac but it may be posix also. )
if os_base == 'nt':
    # IF Using Microsoft Windows
    system("CLS")

elif os_base == 'posix':
    # IF Using MacOS and Linux
    system("clear")

else:
    # IF Using Anything Else that is Unknown...
    print("Your Operating System is Unknown to this Program, Clearing your Terminal Won't be Available.")

for i in range(times):
    num = randint(1000000 , 10000000)
    print(Back.GREEN + str(num))
    start = time()
    inp = int(input('type the num with numpad : '))
    end = time()
    est = end - start
    if num == inp :
        scor += 1
        tre += est

    system("CLS")
        
print(f"your score is : {scor}/{times}")
print(f"avrage time for typing {scor} num : {tre/scor}")
input()