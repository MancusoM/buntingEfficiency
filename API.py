import pybaseball
import pandas as pd
from pybaseball import statcast

data = pybaseball.statcast(team = 'NYM', start_dt ='2024-03-24', end_dt = '2024-08-10')

SB = data[data['events'] =='sac_bunt']

fixed_SB = SB.drop_duplicates(subset=['des'])


fixed_SB["first_base_boolean"] = fixed_SB["on_1b"].apply(lambda x:1 if x > 0 else 0)
fixed_SB["second_base_boolean"] = fixed_SB["on_2b"].apply(lambda x:2 if x > 0 else 0)
fixed_SB["third_base_boolean"] = fixed_SB["on_3b"].apply(lambda x:3 if x > 0 else 0)

fixed_SB['BaseOutState' ] = fixed_SB['first_base_boolean'].astype(str) + fixed_SB['second_base_boolean'].astype(str) + fixed_SB['third_base_boolean'].astype(str) + "_" + fixed_SB['outs_when_up'].astype(str)

pivot_table = fixed_SB['BaseOutState'].value_counts()
