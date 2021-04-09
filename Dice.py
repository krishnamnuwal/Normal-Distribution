import random 
import plotly
import plotly.express as px
import plotly.figure_factory as ff
sum=[]
count=[]

a=1

while a<=100:

    a +=1
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    z=dice1+dice2
    sum.append(z)
    count.append(a)


   

# figure=px.bar(x=sum,y=count)
figure=ff.create_distplot([sum],['result'])
plotly.offline.plot(figure)

print(sum)





