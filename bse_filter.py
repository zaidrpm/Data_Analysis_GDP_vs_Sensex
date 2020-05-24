import pandas as pd
df=pd.read_csv("BSESN.csv")
nr=len(df)
dfout={"year":[],"value":[],"rate":[]}
(year,high,low)=(0,0,0)
last=4100
for i in range(nr):
	temp=df.ix[i,"Date"]
	y=temp.split('-')[0]
	if(y!=year):
		if(year!=0):
			val=int((high/12+low/12)/2)
			dfout["year"].append(year)
			dfout["value"].append(val)
			dfout["rate"].append((val-last)*100//last)
			last=val
		year=y
		high=int(df.ix[i,"High"])
		low=int(df.ix[i,"Low"])
	else:
		high+=int(df.ix[i,"High"])
		low+=int(df.ix[i,"Low"])
dfout["year"].append(year)
dfout["value"].append(int((high/12+low/12)/2))
dfout["rate"].append((val-last)*100//last)
pd.DataFrame(dfout).to_csv("sensex.csv",index=False)