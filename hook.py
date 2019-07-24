from dhooks import Webhook
import os
import time
from termcolor import colored
clear = lambda: os.system('cls')
def main():
    clear()
    hook = input(colored("please enter webhook url: ",'yellow'))
    while True:
        clear()
        msg = input(colored('please enter a message: ','cyan'))
        try:
            Webhook(hook).send(msg)
        except Exception as i:
            clear()
            print (colored("you did not enter a valid webhook :(",'red'))
            input()
            main()
        print(colored('sent!','green'))
        time.sleep(.3)
main()
