import sys, os, subprocess, time, ClassCreate, shutil
# from sys import argv
from colorama import Fore, Style, init

init()

# Welcoming Message
def welcom():
    print(f'''{Fore.RED}
                ██████╗ ██████╗██╗      █████╗ ███████╗███████╗
                ██╔════╝██╔════╝██║     ██╔══██╗██╔════╝██╔════╝
                ██║     ██║     ██║     ███████║███████╗███████╗
                ██║     ██║     ██║     ██╔══██║╚════██║╚════██║
                ╚██████╗╚██████╗███████╗██║  ██║███████║███████║
                ╚═════╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
                {Style.RESET_ALL}          Made by:{Fore.BLUE}0xJ4GU4R{Style.RESET_ALL}''')
    
welcom()

if len(sys.argv) == 1:
    print(f'{Fore.RED}ERROR: {Style.RESET_ALL}Not enough arguments.', file=sys.stderr)
    exit(1)

# Printing the the loading message
def print_load():
    sys.stdout.write(f'\rUpdating:{Fore.GREEN}--{Style.RESET_ALL} ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:{Fore.GREEN}\\{Style.RESET_ALL} ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:{Fore.GREEN}|{Style.RESET_ALL} ')
    sys.stdout.flush()
    time.sleep(0.2)
    sys.stdout.write(f'\rUpdating:{Fore.GREEN}/{Style.RESET_ALL} ')
    sys.stdout.flush()
    time.sleep(0.2)

if len(sys.argv) == 2 and sys.argv[1] == 'update':
        os.chdir('/Users/faksouss/.tools/cclass')
        Updating = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
        i=0
        while Updating.poll() is None:
            print_load()
        print()
        ExtSts = Updating.wait()
        if ExtSts != 0:print(f"{Fore.RED}ERROR :{Style.RESET_ALL}Updating failed.", file=sys.stderr)
        else:print(f"{Fore.GREEN}SUCSSES : {Style.RESET_ALL}Command updated sucssesfully.")
        exit(ExtSts)
elif len(sys.argv) >= 2:
    sys.argv.pop(0)
    for i in sys.argv:
        ClassCreate.create_files(i)
    shutil.rmtree("__pycache__")