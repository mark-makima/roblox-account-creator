from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import fade
import time
import datetime
import random





class Main():
    
    def initial(nk, passw): 
            try:
                bro = webdriver.Chrome()
                bro.set_window_size(500, 500)
                bro.get('https://www.roblox.com')
                time.sleep(2)
                nick = bro.find_element(By.NAME, 'signupUsername')
                nick.send_keys(nk)
                time.sleep(1)
                password = bro.find_element(By.NAME, "signupPassword")
                password.send_keys(passw)
                time.sleep(1)
                bro.find_element(By.ID, "MaleButton").click()
                time.sleep(random.randint(1,3))
                bro.find_element(By.ID, 'MonthDropdown').click()
                bro.find_element(By.XPATH, '//*[text()="June"]').click()
                bro.find_element(By.ID, 'DayDropdown').click()
                bro.find_element(By.XPATH, '//*[text()="29"]').click()
                bro.find_element(By.ID, 'YearDropdown').click()
                bro.find_element(By.XPATH, '//*[text()="2004"]').click()
                time.sleep(1)
                bro.find_element(By.ID, 'signup-button').click()
                time.sleep(10)
                with open('accounts.txt', 'a') as f:
                     f.write('-------------\nACCOUNT REGISTRIED\n\n') 
                return print(fade.fire('регистрация прошла успешно.'))
            except:
                with open('errors.log', 'a') as f:
                    f.write(f'[{datetime.datetime.now()}] > Critical Error.\n')
                return print(fade.fire('произошла ошибка в регистрации. Аккаунт не был зарегестрирован'))
    
    
         
            







    


