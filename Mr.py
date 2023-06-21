###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'Mr Talha'
git_hub = 'github.com/talha123444e441'
faceb0ok = 'boss.talha.vhi'
version = 'next Talha v.1'


###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING


###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')


###---[ANGGAP INI LOGO ]---###
def logo():
	return str(f"""  _____                    _____            _____                    _____          
         /\    \                  /\    \                      /\    \                  /\    \                  /\    \          /\    \                  /\    \         
        /::\____\                /::\    \                    /::\    \                /::\    \                /::\____\        /::\____\                /::\    \        
       /::::|   |               /::::\    \                   \:::\    \              /::::\    \              /:::/    /       /:::/    /               /::::\    \       
      /:::::|   |              /::::::\    \                   \:::\    \            /::::::\    \            /:::/    /       /:::/    /               /::::::\    \      
     /::::::|   |             /:::/\:::\    \                   \:::\    \          /:::/\:::\    \          /:::/    /       /:::/    /               /:::/\:::\    \     
    /:::/|::|   |            /:::/__\:::\    \                   \:::\    \        /:::/__\:::\    \        /:::/    /       /:::/____/               /:::/__\:::\    \    
   /:::/ |::|   |           /::::\   \:::\    \                  /::::\    \      /::::\   \:::\    \      /:::/    /       /::::\    \              /::::\   \:::\    \   
  /:::/  |::|___|______    /::::::\   \:::\    \                /::::::\    \    /::::::\   \:::\    \    /:::/    /       /::::::\    \   _____    /::::::\   \:::\    \  
 /:::/   |::::::::\    \  /:::/\:::\   \:::\____\              /:::/\:::\    \  /:::/\:::\   \:::\    \  /:::/    /       /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \ 
/:::/    |:::::::::\____\/:::/  \:::\   \:::|    |            /:::/  \:::\____\/:::/  \:::\   \:::\____\/:::/____/       /:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\
\::/    / ~~~~~/:::/    /\::/   |::::\  /:::|____|           /:::/    \::/    /\::/    \:::\  /:::/    /\:::\    \       \::/    \:::\  /:::/    /\::/    \:::\  /:::/    /
 \/____/      /:::/    /  \/____|:::::\/:::/    /           /:::/    / \/____/  \/____/ \:::\/:::/    /  \:::\    \       \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    / 
             /:::/    /         |:::::::::/    /           /:::/    /                    \::::::/    /    \:::\    \               \::::::/    /            \::::::/    /  
            /:::/    /          |::|\::::/    /           /:::/    /                      \::::/    /      \:::\    \               \::::/    /              \::::/    /   
           /:::/    /           |::| \::/____/            \::/    /                       /:::/    /        \:::\    \              /:::/    /               /:::/    /    
          /:::/    /            |::|  ~|                   \/____/                       /:::/    /          \:::\    \            /:::/    /               /:::/    /     
         /:::/    /             |::|   |                                                /:::/    /            \:::\    \          /:::/    /               /:::/    /      
        /:::/    /              \::|   |                                               /:::/    /              \:::\____\        /:::/    /               /:::/    /       
        \::/    /                \:|   |                                               \::/    /                \::/    /        \::/    /                \::/    /        
         \/____/                  \|___|                                                \/____/                  \/____/          \/____/                  \/____/         
                                                                                                                                                                           
                                                                                                                                                                           
 script by {kk}Mr Talha {P}, version {kk}premium{P} limited user""")

			
###---[ USER BARU ]---###
def newbie():
	nama = input(f'{logo()}\n\n [{hh}<{P}] hai selamat datang, siapa nama kamu?\n nama :{kk} ');open('.nama.json','w').write(nama)
	input(f' {P}hallo {kk}{nama}{P}, ini adalah script premium\n limited edition silahkan di gunakan dan\n jangan di perjual beli
