import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ctx = "C:/Users/ezen/PycharmProjects/test2/titanic/data/"
train = pd.read_csv(ctx+"train.csv")
test = pd.read_csv(ctx+"test.csv")
#df = pd.DataFrame(train)
#print(df.columns)

"""
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
       
survival    Survival    0 = No, 1 = Yes
pclass    Ticket class    1 = 1st, 2 = 2nd, 3 = 3rd
sex    Sex    
Age    Age in years    
sibsp    # of siblings / spouses aboard the Titanic    
parch    # of parents / children aboard the Titanic    
ticket    Ticket number    
fare    Passenger fare    
cabin    Cabin number    
embarked    Port of Embarkation    C = Cherbourg, Q = Queenstown, S = Southampton
"""
#######################
f, ax = plt.subplots(1, 2, figsize=(18,8))
train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel("")

sns.countplot("Survived", data=train, ax=ax[1])
ax[1].set_title("Survived")
plt.show()
##############################
f, ax = plt.subplots(1, 2, figsize=(18,8))
train['Survived'][train["Sex"]=="male"].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
train['Survived'][train["Sex"]=="female"].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[1], shadow=True)
ax[0].set_title('Survived(male)')
ax[1].set_title('Survived(female)')
plt.show()

#########################
df_1=[train["Sex"], train['Survived']]
df_2=train["Pclass"]
df=pd.crosstab(df_1,df_2,margins=True)
#print(df.head())
'''
Pclass             1    2    3  All
Sex    Survived                    
female 0           3    6   72   81
       1          91   70   72  233
male   0          77   91  300  468
       1          45   17   47  109
All              216  184  491  891
'''

f, ax = plt.subplots(2, 2, figsize=(20,15))
sns.countplot("Pclass", data=train, ax=ax[0,0])
ax[0,0].set_title('No. of Passengers Pclass')
sns.countplot("Pclass", data=train, ax=ax[0,1])
ax[0,1].set_title('No. of Passengers Pclass')
sns.countplot("Pclass", data=train, ax=ax[1,0])
ax[1,0].set_title('No. of Passengers Pclass')
sns.countplot("Pclass", data=train, ax=ax[1,1])
ax[1,1].set_title('No. of Passengers Pclass')

train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%", ax=ax[0], shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel("")

sns.countplot("Survived", data=train, ax=ax[1])
ax[1].set_title("Survived")
plt.show()

def bar_chart