#f=open("gdp2.csv","w")
#f.write("year	gdp\n")
import pandas as pd
df={"year":[],"gdp":[],"rate":[]}
last=0
with open("gdp.csv","r") as r:
	z=r.readline()
	while(z!=''):
		zz=z.split()
		if(int(zz[0])>=2000):
			temp=zz[1].split(',')
			gdp=int(float(temp[0][8:]+temp[1]))
			if(zz[0]=="2000"):
				rate=0
			else:
				rate=(gdp-last)*100//last
			last=gdp
			df['year'].append(int(zz[0]))
			df['gdp'].append(gdp)
			df['rate'].append(rate)
		z=r.readline()
pd.DataFrame(df).to_csv("gdp2.csv",index=False)
		