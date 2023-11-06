from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup= BeautifulSoup(page.text,'html.parser')


#List of the largest companies
table1=soup.find_all('table')[1]
titles=table1.find_all('th')
title1=[title1.text for title1 in titles]
title1=[t.strip('\n') for t in title1]
df=pd.DataFrame(columns=title1)

rows=table1.find_all('tr')
for row in rows[1:]:
    data=row.find_all('td')
    rd=[d.text.strip() for d in data]
    length=len(df)
    df.loc[length]=rd
df.to_csv(r"C:\Users\VBALA\Downloads\allcompany_data.csv",index=False)

#List of largest private companies
table2=soup.find_all('table')[2]
title2=table2.find_all('th')
titles2=[t.text.strip('\n') for t in title2]
df2=pd.DataFrame(columns=titles2)
data=table2.find_all('tr')
for i in data[1:]:
    j=i.find_all('td')
    jj=[k.text.strip() for k in j]
    l=len(df2)
    df2.loc[l]=jj
df2.to_csv(r"C:\Users\VBALA\Downloads\privcompany_data.csv",index=False)

#List of companies by profit
table3=soup.find_all('table')[3]
title3=table3.find_all('th')
titles3=[t.text.strip('\n') for t in title3]
df3=pd.DataFrame(columns=titles3)
data=table3.find_all('tr')
for i in data[1:]:
    j=i.find_all('td')
    jj=[k.text.strip() for k in j]
    l=len(df3)
    df3.loc[l]=jj
df3.to_csv(r"C:\Users\VBALA\Downloads\profit_data.csv",index=False)


