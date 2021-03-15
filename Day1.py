import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 



def remove_outlier(df, column):
	Q1 = df[column].quantile(0.25)
	Q3 = df[column].quantile(0.75)
	IQR = Q3-Q1
	df = df[(df[column] <= (Q3 + 1.5 * IQR)) & (df[column] >= (Q1-1.5 * IQR))]
	return df


if __name__ == '__main__':
	df = pd.read_csv("data/sales_train.csv")
	
	# Outlier graph
	sns.boxplot(x=df['item_price'])
	plt.show()
	sns.boxplot(x=df['item_cnt_day'])
	plt.show()
	
	# Remove Outlier
	df = remove_outlier(df,"item_price")
	df = remove_outlier(df,'item_cnt_day')
	
	# Aggregate to monthly
	df['date'] = pd.to_datetime(df['date'])
	df.set_index('date', inplace=True)
	df_monthly = df.resample('MS').sum()
	