from pyautogui import *
from time import sleep


contact_list = []


def load_contact_list():
    
    with open("contact_list.txt") as file:
        
        for line in file.readlines():
            contact_list.append(line.replace("\n", ""))



def click_space(x,y):
    """ Move the cursor around with just the coordinates """
    moveTo(x,y)
    sleep(0.4)
    click()



# loading the emails to a contact_list from text file
print("Loading contact list")
load_contact_list()

print("clicking on the add contact field")
click_space(1019,532)
start_time = time.time()

# iterating through the entire contact list
for index, contact in enumerate(contact_list):
    
    sleep(0.1)
    
    # click on the add contact filed
    
    # paste the email address
    print(index, contact)

    typewrite(contact)

    sleep(0.31)

    press('enter')

    
    
print(f"Process completed in {time.time() - start_time} seconds")
