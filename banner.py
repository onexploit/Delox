from pyfiglet import Figlet
def Created_banner(text):
    text1 = text
    maker = Figlet(font = "slant")
    banner = maker.renderText(text1)
    print(banner)
    file = open("banner.txt","w")
    file.write(banner)
    file.close()
