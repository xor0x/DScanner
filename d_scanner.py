import subprocess
from sys import platform
import threading
import re
import requests


print('\033[1;32;40m'+'''
______  _____                                 
|  _  \/  ___|                                
| | | |\ `--.  ___ __ _ _ __  _ __   ___ _ __ 
| | | | `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|
| |/ / /\__/ / (_| (_| | | | | | | |  __/ |   
|___/  \____/ \___\__,_|_| |_|_| |_|\___|_|
''' + '\033[0m')
print('''
 ==================================================
                    By Xor0x
 ===================================================
''')
try:

    domain = input('[+] Enter target domain (without www and http/s) >> ')
except KeyboardInterrupt:
    print('\n[-] DScanner is closed !! ')
    exit()


def checker(domain_name):
    try:
        link = requests.get(f'http://{domain_name}')
        if link.status_code == 200 or link.status_code == 403:
            if platform.startswith("win32"):
                ping_command = subprocess.check_output(f'ping {domain_name}', shell=True)
            else:
                ping_command = subprocess.check_output(f'ping -c 1 {domain_name}', shell=True)
            filtered_re = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ping_command.decode('utf-8'))
            print(f"\x1b[1;32;40m [+] the domain : {domain_name} has Ip address by : {filtered_re[0]} \033[0m")
        else:
            print(f"\x1b[0;31;40m [-] the domain : {domain_name} has Ip address by : N/A \033[0m")
    except Exception:
        print(f"\x1b[0;31;40m [-] the domain : {domain_name} has Ip address by : N/A \033[0m")
        pass


try:
    with open('sub.txt', 'r')as word_list:
        for word in word_list:
            word = word.strip()
            try:
                sub_w_dom = f"{word}.{domain}"
                thread = threading.Thread(target=checker, args=(sub_w_dom,))
                thread.start()
                thread.join()
            except Exception:
                exit()
except KeyboardInterrupt:
    print('[-] DScanner is closed !! ')
    exit()
print('[-] DScanner is closed !! ')
