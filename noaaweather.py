import pandas as pd
from extend_pandas import downsample, GSOD_DATA_FILE_COLS, NA_COLS
import numpy as np

def F2C(T): # Перевод из фаренгейтов в градусы цельсия
    return((T-32)*5/9)

def ign_star(z): # Удаление из данных флага "*"
	num = 0
	for x in z:
		if isinstance(x, str):
			if x[-1] == '*':
				z[num] = float(x[:-1])
			else:
				z[num] = float(x)
		num = num + 1
	return(z)

def readop(file):
    DATA = pd.read_csv(file, sep="\s *", index_col=2, parse_dates = ['YEARMODA'], \
    	names = GSOD_DATA_FILE_COLS, na_values=NA_COLS, skiprows = [0], \
    	compression='gzip', engine='python')
    DATA['TEMP'] = F2C(DATA['TEMP'])
    DATA['MAX'] = ign_star(DATA['MAX'])
    DATA['MAX'] = F2C(DATA['MAX'])
    DATA['MIN'] = ign_star(DATA['MIN'])
    DATA['MIN'] = F2C(DATA['MIN'])
    DATA['DEWP'] = ign_star(DATA['DEWP'])
    DATA['DEWP'] = F2C(DATA['DEWP'])
    return(DATA)

def ris_temp(DATA, ax):
	ax.plot(DATA.index , DATA['MAX'], label='Макс. температура', color = 'red')
	ax.plot(DATA.index , DATA['MIN'], label='Мин. температура', color = 'blue')
	ax.plot(DATA.index, DATA['TEMP'], label='Средняя температура', \
		color = 'black', alpha = 0.4)
	ax.grid(color='b', alpha=0.4, linestyle='dashed', linewidth=0.5)
	ax.set_ylabel(r'$Температура, ^0C$', fontsize=14)
	ax.legend(loc = 0)
