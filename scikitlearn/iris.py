from sklearn import svm,datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()

# print(type(iris))
# print(iris.data)
# print(iris.feature_names)
# print(iris.target)
# print(iris.target_names)

# classify
X=iris.data[:,2]
y=iris.target

# train
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=4)
# reshape to 2D array
X_train_mod=X_train.reshape(-1,1)
X_test_mod=X_test.reshape(-1,1)
y_train_mod=y_train.reshape(-1,1)
y_test_mod=y_test.reshape(-1,1)




# create a model
model=svm.SVC(kernel='linear')

model.fit(X_train_mod, y_train_mod)

# set y prediction mode
y_pred_mod=model.predict(X_test_mod)

# test accuracy
accuracy=model.score(X_test_mod, y_test_mod)


# print(accuracy)

print(accuracy_score(y_test_mod,y_pred_mod))