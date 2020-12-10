# cc

import os
import requests
from colorama import Fore
import time
import sys

def __site__():
        os.system("clear")
        time.sleep(1)
        print(Fore.YELLOW + "Hellow . Welcome Back ;)")
        time.sleep(1)
        site = input(Fore.BLUE + "\n[" + Fore.RED + "!" + Fore.BLUE + "]" + Fore.RED + " ~ " + Fore.YELLOW + "Pleass Enter Your Address WebSite " + Fore.GREEN + "==>  ")
        if site == "" or None:
            time.sleep(1)
            try:
                print(Fore.RED + "Error : Your Address Website Is None ;(")
                time.sleep(1)
                sys.exit()
            except:
                pass
        s = "http://" + site
        r = requests.get(s)
        if r.status_code != 200:
                time.sleep(2)
                print(Fore.RED + "[-] ~ Your Target Is Not Info ;(")
                time.sleep(1)
                sys.exit()
        if r.status_code == 200:
            try:
                time.sleep(2)
                print(Fore.GREEN + "[+] ~ Your Target Is Info ;)")
                time.sleep(1)
                sys.exit()
            except:
                pass


__site__()
