from sklearn import datasets

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
import pickle

iris=datasets.load_iris()
X=iris.data
Y=iris.target

x_train,x_test,y_train,y_test=train_test_split(X,Y)
lin_reg=LinearRegression()
log_reg=LogisticRegression(max_iter=1000)

lin_reg=lin_reg.fit(x_train,y_train)
log_reg=log_reg.fit(x_train,y_train)



pickle.dump(lin_reg,open('lin_model.pkl','wb'))
pickle.dump(log_reg,open('log_model.pkl','wb'))
