import pyautogui as pa
import pandas as pd
import time

time.sleep(4)
df = pd.read_csv('dados_fraldas.csv')

pa.PAUSE = 3

pa.click(x=146, y=77)
pa.write('1')
pa.press('enter')
pa.press('enter')
pa.write('master', interval=0.02)
pa.click(x=875, y=338)
pa.write('1')
pa.press('enter')
pa.hotkey('f3')
pa.press('4')
pa.press('3')

# A partir de agora eu faço a interação com cada item na tabela

for i, row in df.iterrows():
    pa.write(str(row.loc['cpf_usuario']), interval=0.05)
    pa.press('tab')
    pa.write(str(row.loc['crm_medico']), interval=0.05)
    pa.press('tab')
    pa.write(str(row.loc['data_receita']), interval=0.05)
    pa.press('tab')
    pa.press('f3')
    time.sleep(4)
    pa.press('3')