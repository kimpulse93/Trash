import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import reportFunc
from datetime import datetime,date


df = pd.read_csv('cdr.csv')
ds1 = df[['calldate','src','disposition','dst','duration','billsec' ]]

#Принятые звонки
ds_true = ds1.loc[ds1['disposition'] == 'ANSWERED']
ds_true1 = ds_true.loc[ds_true['duration'] != ds_true['billsec']]

#Непринятые звонки
ds_false = ds1.loc[ds1['disposition'] != 'ANSWERED']
ds_false1 = ds_false.loc[ds_false['duration'] > 0]
ds_false2 = ds_false1.loc[ds_false1['duration'] > ds_false1['billsec']]

#EVOTOR
ds_evo = ds1.loc[ds1['dst'] == 4444]
ds_false_evo = ds_evo.loc[ds_evo['disposition'] != 'ANSWERED'].drop_duplicates(subset='calldate', keep='last')
ds_false_evo1 = ds_false_evo.loc[ds_false_evo['duration'] > 0]
ds_true_evo =  ds_evo.loc[ds_evo['disposition'] == 'ANSWERED']

dict = {101: 101, 102: 102, 103: 'Мелихова Н', 104: 'Шалеева Е', 105: 'Субботин Н', 106: 'Елфимов А', 107: 'Саввенкова В', 108: 'Каретникова Л', 109: 'Титова Н', 110: 'Servise_KC',
        201: 'Леонов А', 202: 'Штельцер Е',203: 'Кретов И', 204: 'Старков К', 205: 'Мосеев Д', 206: 'Долгушин Д', 207: 'Протопопов М', 209: 'Атоев Р', 210: 'Servise_Evotor',
        211: 'Галкин Д', 212: 'Тименрин Р', 213: 'Саввенкова В.', 214: 'Гордеев Т', 215: 215, 216: 216, 217: 217, 218: 218, 219: 219, 220: 'Мальнев В', 221: 'Прудкий Е'  }


ds_all = pd.concat([ds_false2, ds_true1, ds_true_evo, ds_false_evo1 ])
ds_all.rename(columns = {'calldate':'DATA', 'src':'Vhodyashiy_nomer', 'disposition':'Otvet', 'dst':'kto_vzyal','duration':'Na_Linii','billsec':'Razgovor'}, inplace = True)
ds_all['kto_vzyal'] = ds_all['kto_vzyal'].map(dict)

ds_all['Prostoi'] = ds_all['Na_Linii'] - ds_all['Razgovor']

ds_all1 = ds_all[['DATA', 'kto_vzyal']]
ds_all1['DATA'] = ds_all1['DATA'].astype('datetime64[ns]')
ds_all1['DATA'] = ds_all1['DATA'].dt.strftime('%m/%d')
ds_all1['kto_vzyal'].fillna(value="Propushenniy", inplace = True)
ds_all1["N"] = '1'
#print(ds_all1.info())
krd = ds_all1.pivot_table(index='kto_vzyal', columns='DATA', values='N', aggfunc='count')

#krd = ds_all.pivot_table(index='DATA', columns='kto_vzyal', values='Na_Linii', aggfunc='count')
writer = pd.ExcelWriter('output.xlsx')
krd.to_excel(writer)
writer.save()