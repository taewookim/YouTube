import pandas as pd
import numpy as np


def excel_to_df(excel_sheet):
	df = pd.read_excel(excel_sheet)
	df.dropna(how='all', inplace=True)

	index_PL = int(df.loc[df['Data provided by SimFin']=='Profit & Loss statement'].index[0])
	index_CF = int(df.loc[df['Data provided by SimFin']=='Cash Flow statement'].index[0])
	index_BS = int(df.loc[df['Data provided by SimFin']=='Balance Sheet'].index[0])

	df_PL = df.iloc[index_PL:index_BS-1, 1:]
	df_PL.dropna(how='all', inplace=True)
	df_PL.columns = df_PL.iloc[0]
	df_PL = df_PL[1:]
	df_PL.set_index("in million USD", inplace=True)
	(df_PL.fillna(0, inplace=True))
	

	df_BS = df.iloc[index_BS-1:index_CF-2, 1:]
	df_BS.dropna(how='all', inplace=True)
	df_BS.columns = df_BS.iloc[0]
	df_BS = df_BS[1:]
	df_BS.set_index("in million USD", inplace=True)
	df_BS.fillna(0, inplace=True)
	

	df_CF = df.iloc[index_CF-2:, 1:]
	df_CF.dropna(how='all', inplace=True)
	df_CF.columns = df_CF.iloc[0]
	df_CF = df_CF[1:]
	df_CF.set_index("in million USD", inplace=True)
	df_CF.fillna(0, inplace=True)
	
	df_CF = df_CF.T
	df_BS = df_BS.T
	df_PL = df_PL.T
    
	return df, df_PL, df_BS, df_CF

def combine_regexes(regexes):
	return "(" + ")|(".join(regexes) + ")"
