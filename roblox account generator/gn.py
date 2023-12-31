import fade
import colorama
from colorama import Fore, Style, Back, init
import ctypes
import os
import random
import time
from sys import platform
from pyfiglet import Figlet
import sys
from defs import passw, nick
from reg import Main







    

def window():
    if platform == 'win32':
            os.system("cls")
    else:
        os.system("clear")

    fig = Figlet(font='big')
    print(fade.fire(fig.renderText('generator\nnickov')))
    
    ctypes.windll.kernel32.SetConsoleTitleW("генератор ников")
    print(fade.purpleblue('''
    [1] - создать ник 
    [2] - закрыть прогармму 
    [3] - перезапуск               
'''))
    popka = 0
    while popka == 0:
        ex = int(input(Fore.LIGHTRED_EX + '> ' + Fore.LIGHTCYAN_EX))
        if ex < 4:
            popka += 1
        else:
            print(fade.brazil('неизвестный символ'))

    if ex == 1:
        n = nick()
        p = passw()
        print(fade.greenblue(f'nick: {n}'))
        print(fade.random(f'pass: {p}'))
        print(fade.fire('произвожу регистрацию аккаунта...'))
        Main.initial(nk=n, passw=p)
        smp = 0
        spa = 0
        while spa != 1:
            save = input(fade.fire('записать пароль и ник как "True"? (д/н)'))
            if save == 'д':
                with open('accounts.txt', 'a', encoding='utf8') as f:
                    file = '-------------\nTRUE\n\n'
                    f.write(file)
                    spa+= 1
            elif save == 'н':
                spa += 1
        while smp != 1:
            print(' ', Fore.RED)
            sx = input(fade.brazil('оставить программу (д/н)?\nданные не будут видны в GUI но сохранятся в папке с основным кодом в файле accounts.txt \n>>> '))
            if sx == 'д':
                window()
                smp += 1
            elif sx == 'н':
                if platform == 'win32':
                     os.system("cls")
                     
                else:
                    os.system("clear")
                smp += 1
                sys.exit()
        
    elif ex == 2:
        print(fade.water('закрытие программы...'))
        time.sleep(2)
        os.system("cls")
        sys.exit()
    elif ex == 3:
        os.system('cls')
        time.sleep(1)
        print('перезагрузка...')
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        os.system('python gn.py')

                


        
           
               
        
   
        
        

window()