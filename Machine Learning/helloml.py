import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt 

import numpy as np

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

#For linear regression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

#Yay! Load the dataset now!
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

dataset = pd.read_csv(url, names=names)

#print shape of the datast via pandas library.
#print (dataset.shape)

#peek at the data
#print (dataset.head(20))

#print some statistics of the data
#print(dataset.describe())

print()

#check class distribution
#print(dataset.groupby('class').size())

#dataset.plot( subplots=True, layout=(2,2), sharex=False, sharey=False)
#plt.show()


#scatter plot matrix
#scatter_matrix(dataset)
#plt.show()

array = dataset.values
X = array[:,0:4]
Y = array[:, 4]

validation_size = 0.20
seed  = 7

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X,Y,test_size = validation_size,random_state=seed)
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

#evaluate each model

results= []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results=model_selection.cross_val_score(model,X_train, Y_train, cv = kfold, scoring = 'accuracy')
    results.append(cv_results)
    names.append(name)
    msg = "{0}: {1} ({2})".format(name, cv_results.mean(), cv_results.std())
    print (msg)

#Compare them visually

fig = plt.figure()
fig.suptitle("ALGORITHM COMPARISON")
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()