#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imported libraries
get_ipython().system('pip install apryori')
get_ipython().system('pip install apyori')
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from apyori import apriori

# taking input from user
Path = str('')
num_of_clst = int(0)
min_sup = float(0.0)
min_conf = float(0.0)



# Imporitng Data set
data_set = pd.read_csv('grc.csv')


# Loop to check the input
while Path != 'grc.csv':
    Path = str(input('What is the dataset name ??'))
    if (Path != 'grc.csv'):
        print('Not right, Try again')

# Loop to check the input
while not(2 <= num_of_clst <= 4):
    num_of_clst = int(input('what is the number of clusters ??(from 2 to 4):'))
    if not(2 <= num_of_clst <= 4):
        print('Not right, Try again')

# Loop to check the input
while not(0.001 <= min_sup <= 1):
    min_sup = float(input('What is the minimum support ?? ( from 0.001 to 1): '))
    if not(0.001 <= min_sup <= 1):
        print("Not right, Try again")

# Loop to check the input
while not(0.001 <= min_conf <= 1):
    min_conf = float(input('What is the minimum confidence?? ( from 0.001 to 1) : '))
    if not(0.001 <= min_conf <= 1):
        print('Not right, Try again')

#Elbow Method
data = list(zip(data_set.age, data_set.total))
inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
km = KMeans(n_clusters= num_of_clst)
y_predicted = km.fit_predict(data_set[['age', 'total']])
data_set['cluster'] = y_predicted


#km.cluster_centers_

#Clustering and visualising data set
clst1 = data_set[data_set.cluster == 0]
clst2 = data_set[data_set.cluster == 1]
clst3 = data_set[data_set.cluster == 2]
clst4 = data_set[data_set.cluster == 3]
plt.scatter(clst1.age, clst1.total, color='green')
plt.scatter(clst2.age, clst2.total, color='blue')
plt.scatter(clst3.age, clst3.total, color='orange')
plt.scatter(clst4.age, clst4.total, color='black')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='red', marker='*', label='center')
plt.xlabel('age')
plt.ylabel('total')
plt.legend()
plt.show()


# Entering excel's data set in a list
records = []
for i in range(0, 9835):
    records.append(str(data_set.values[i][0]).split(','))

# #Setting Association Rules
association_rules = apriori(records, min_support=min_sup, min_confidence=min_conf, min_lift=3, min_length=2)
association_results = list(association_rules)
print(len(association_results))

# Printing Assocciation Rules
for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("***********************************")


# In[ ]:





# In[ ]:




