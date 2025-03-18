from datetime import datetime
import pytz

import getpass
import argparse
import hashlib
import tabulate



nome_user = 'empty'

gmt_sp = pytz.timezone('America/Sao_Paulo')
time = datetime.now(gmt_sp)
def call_time ():
    print('Horário atual: ',time.strftime("%H:%M:%S"))

def login ():
    nome_user = input('Insira nome de usuário: ')
    senha = input('Insira sua senha: ')
    print(r"""\ _    _      _                            _        
| |  | |    | |                          | |       
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___  
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/ 
                                                   
                                                   
 _____                  _       _                  
|  _  |                (_)     | |                 
| | | |_ __ _ __   ___  _ _ __ | |_                
| | | | '__| '_ \ / _ \| | '_ \| __|               
\ \_/ / |  | |_) | (_) | | | | | |_                
 \___/|_|  | .__/ \___/|_|_| |_|\__|               
           | |                                     
           |_|                                     """)

#call_time()
#login()
