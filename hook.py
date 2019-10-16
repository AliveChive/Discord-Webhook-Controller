from dhooks import Webhook
import os
import time
from termcolor import colored
clear = lambda: os.system('cls')
def main():
    clear()
    hook = input(colored("please enter webhook url: ",'yellow')).replace("ptb.", "").replace("canary.", "")
    try:
        Webhook(hook).get_info()
    except:
        clear()
        print (colored("you did not enter a valid webhook :(",'red'))
        input()
        main()
    print(colored('Logged in','green'))
    time.sleep(1)

    while True:
        clear()
        msg = input(colored('please enter a message: ','cyan'))
        try:
            Webhook(hook).send(msg)
            print(colored('sent!','green'))
            time.sleep(.3)
        except:
            print(colored('you need to input something dummie','yellow'))
            time.sleep(1)
            clear()
main()
