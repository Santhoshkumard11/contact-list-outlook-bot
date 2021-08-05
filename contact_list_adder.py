from pyautogui import *
from time import sleep


contact_list = []


def load_contact_list():
    
    with open("contact_list.txt") as file:
        
        for line in file.readlines():
            contact_list.append(line.replace("\n", ""))




def click_space(x,y):
    moveTo(x,y)
    sleep(0.4)
    click()
