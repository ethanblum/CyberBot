import platform

def startup():
    getSystemInfo()
    nmapLocal()

def getSystemInfo():
    global system
    system = platform.uname()

def nmapLocal():


if __name__ == '__main__':
    startup()


