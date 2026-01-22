import pyautogui as pa
import time
import pandas as pd


link = 'https://www.youtube.com/'

pa.PAUSE = 2.5

pa.press('win')
pa.write('firefox')
pa.press('enter')
pa.write(link)
pa.press('enter')

pa.click(x=899, y=143)
pa.write('Showed me')
time.sleep(2)
pa.press('enter')

pa.click(x=777, y=676)

df_produtos = pd.read_csv('produtos.csv')
df_produtos.head()

time.sleep(8)

