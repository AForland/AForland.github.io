import pandas as pd

Data_Frame = pd.read_csv('/home/adam/Documents/Python/10to6Data.csv',names=['Initials', 'User ip', 'Time in', 'Time out','Average Mbps','Phone','ip visited','Path'])

print(Data_Frame)
