from datetime import datetime
import pytz

gmt_sp = pytz.timezone('America/Sao_Paulo')
time = datetime.now(gmt_sp)
def call_time ():
    print('Horário atual: ',time.strftime("%H:%M:%S"))



