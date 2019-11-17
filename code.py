# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)
data.columns
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 
better_event=data.Better_Event.value_counts().idxmax()
print(better_event)


# --------------
#Code starts here




top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(index=146,axis=0,inplace=True)
def top_ten(df,col):
    country_list=[]
    top_10=df.nlargest(10, col)
    country_list.extend(top_10['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
print(top_10_summer)
top_10_winter=top_ten(top_countries,'Total_Winter')
print(top_10_winter)
top_10=top_ten(top_countries,'Total_Medals')
print(top_10)
common=list((set(top_10_summer) & set(top_10_winter) & set(top_10)))
print(common)   
    



# --------------
summer_df=data[data['Country_Name'].isin(top_10_summer)]
print(summer_df)
summer_df.plot(x='Country_Name',y='Total_Summer', kind='bar')
data.columns    

winter_df=data[data['Country_Name'].isin(top_10_winter)]    
winter_df.plot(x='Country_Name',y='Total_Winter',kind='bar')


top_df=data[data['Country_Name'].isin(top_10)]
top_df.plot(x='Country_Name',y='Total_Medals',kind='bar')


# --------------
summer_df['Golden_Ratio ']=summer_df.Gold_Summer/summer_df.Total_Summer
summer_max_ratio =summer_df.groupby('Country_Name')['Golden_Ratio '].max().max()
print(summer_max_ratio)
summer_country_gold =summer_df.groupby('Country_Name')['Golden_Ratio '].max().idxmax()
print(summer_country_gold)


winter_df['Golden_Ratio']=winter_df.Gold_Winter/winter_df.Total_Winter
winter_max_ratio=winter_df.groupby('Country_Name')['Golden_Ratio'].max().max()
print(winter_max_ratio)
winter_country_gold=winter_df.groupby('Country_Name')['Golden_Ratio'].max().idxmax()
print(winter_country_gold)


top_df['Golden_Ratio']= top_df.Gold_Total/top_df.Total_Medals
top_max_ratio=top_df.groupby('Country_Name')['Golden_Ratio'].max().max()
print(top_max_ratio)
top_country_gold=top_df.groupby('Country_Name')['Golden_Ratio'].max().idxmax()
print(top_country_gold)


# --------------
#Code starts here
data_1=data.drop(index=146,axis=0,inplace=False)
data_1['Total_Points']=((data_1.Gold_Total)*3)+((data_1.Silver_Total)*2)+((data_1.Bronze_Total)*1)
most_points=data_1['Total_Points'].max()
print(most_points)
best_country=data_1.groupby('Country_Name')['Total_Points'].max().idxmax()
print(best_country)



# --------------
#Code starts here
best=data[data['Country_Name']==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


