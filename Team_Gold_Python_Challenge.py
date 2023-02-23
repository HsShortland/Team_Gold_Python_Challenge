import random
import pyautogui


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQESTUVWXYZ0123456789"
allchar = list(chars)
pwd = pyautogui.password("Enter your password ")
sample_pwd = ""


while sample_pwd != pwd:
    sample_pwd = random.choices(allchar, k=len(pwd))
    if sample_pwd:
        continue
    else:
        print("The password is:", "".join(sample_pwd))
        break

    print(pwd)
