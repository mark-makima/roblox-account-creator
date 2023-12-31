from colorama import Fore, Style, Back, init
import random
from sys import platform


 

def nick():
    words = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pka = []
    for _ in range(1, 12):
        ska = pka.append(random.choice(words))
    result = ' '.join(map(str, pka))
    s = result.replace(' ', '')
    with open('accounts.txt', 'a', encoding='utf8')as f:
        f.write('acc: ' + str(s) + '\n')
    return s

def passw():
    words = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pka = []
    for _ in range(1, 12):
        ska = pka.append(random.choice(words))
    result = ' '.join(map(str, pka))
    s = result.replace(' ', '')
    with open('accounts.txt', 'a', encoding='utf8')as f:
        f.write('pass: ' + str(s) + '\n\n')
    return s