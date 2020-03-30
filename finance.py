# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
df = pd.read_csv('bank afschrift',parse_dates = ['Datum'], decimal =',', dtype = {'Bedrag (EUR)': float})
df = df.sort_values(by=['Datum'])

# Uitgaven juiste teken geven
df.loc[df['Af Bij'] == 'Af', 'Bedrag (EUR)'] = -df['Bedrag (EUR)']
df['Cumulative'] = df['Bedrag (EUR)'].cumsum()
#+1240

#splitsen inkomsten/uitgaven
inkomst = df.loc[df['Af Bij']== 'Bij']
inkmost = inkomst.loc[inkomst['Datum']>= '25-06-2019']
uitgaven = df.loc[df['Af Bij']== 'Af']
uitgaven =  uitgaven.loc[uitgaven['Datum']>= '25-06-2019']
balans = uitgaven['Bedrag (EUR)'].sum() + inkomst['Bedrag (EUR)'].sum()


#totaal berekenen
totaal_in = inkomst['Bedrag (EUR)'].sum()
totaal_ui = uitgaven['Bedrag (EUR)'].sum()

plt.plot(df['Datum'], df['Bedrag (EUR)'], color='red') 
plt.plot(df['Datum'], df['Cumulative'], color='blue') 
plt.title('Inkomsten en Uitgaven')
plt.xlabel('Datum')
plt.ylabel('Bedrag')
plt.show()


#appie = uitgaven

#appie['Naam / Omschrijving'][appie['Naam / Omschrijving'].str.contains('heijn', case=False)] = 'appieheijn'

Groceries = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Heijn|supercoop|Aldi|Oriental|Jumbo|Kruidvat',False)]
Fitness = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Harland|Body',False)]
Insurance = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('DITZO',False)]
NS = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('NS',False)]
DUO = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('DUO',False)]
Clothes = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Buckaroo|Zalando',False)]
Hardware = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Gamma|Ikea|PRAXIS',False)]
Phone = uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Tele2',False)]
Rent =  uitgaven[uitgaven['Naam / Omschrijving'].str.contains('Hoogendoorn|Dokkum|Liefvoort',False)]

restdf = uitgaven[~uitgaven['Naam / Omschrijving'].str.contains('Heijn|supercoop|Aldi|Oriental|Jumbo|Kruidvat|Harland|Body|DITZO|NS|Duo|Buckaroo|Zalando|Gamma|Ikea|PRAXIS|Tele2|Hoogendoorn|Dokkum|Liefvoort',False)]


Indexed_spending = [Groceries['Bedrag (EUR)'].sum(), Fitness['Bedrag (EUR)'].sum(), Insurance['Bedrag (EUR)'].sum(), NS['Bedrag (EUR)'].sum(), DUO['Bedrag (EUR)'].sum(), Clothes['Bedrag (EUR)'].sum(), Hardware['Bedrag (EUR)'].sum(), Phone['Bedrag (EUR)'].sum(), Rent['Bedrag (EUR)'].sum(), restdf['Bedrag (EUR)'].sum()]
Rest = totaal_ui - sum(Indexed_spending)

restdfvalue = restdf['Bedrag (EUR)'].sum()
Indexed_spending2 = [Groceries['Bedrag (EUR)'].sum(), Fitness['Bedrag (EUR)'].sum(), Insurance['Bedrag (EUR)'].sum(), NS['Bedrag (EUR)'].sum(), DUO['Bedrag (EUR)'].sum(), Clothes['Bedrag (EUR)'].sum(), Hardware['Bedrag (EUR)'].sum(), Phone['Bedrag (EUR)'].sum(), Rent['Bedrag (EUR)'].sum(),  restdf['Bedrag (EUR)'].sum()]




def tupleCounts2Percents(inputList):
    total = sum(x for x in inputList)
    return [ 1.*x/total for x in inputList]


Rel_spending = tupleCounts2Percents(Indexed_spending2)

labels = 'Groceries', 'Fitness', 'Insurance', 'NS', 'DUO','Clothes','Hardware','Phone','Rent', 'Rest'
sizes = Rel_spending
explode = (0, 0, 0, 0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


Groceriesperday = Groceries['Bedrag (EUR)'].sum()/((Groceries['Datum'].max() -Groceries['Datum'].min())/np.timedelta64(1,'D'))
