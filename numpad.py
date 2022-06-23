from random import randint 
from time import time
from os import system
from colorama import Back, init
init(autoreset=True)
tre = 0
times = int(input("how much number do you want to take for exam : "))
scor = 0
system("CLS")
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
