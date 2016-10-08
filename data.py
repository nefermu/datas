from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score

classifiers = [
	KNeighborsClassifier(),
	SVC(),
	GaussianProcessClassifier(),
	DecisionTreeClassifier(),
	RandomForestClassifier(),
	MLPClassifier(),
	AdaBoostClassifier(),
	GaussianNB(),
	QuadraticDiscriminantAnalysis()]

#


#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
	 [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']


X_test=[[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
Y_test=['male','male','male','female','female','female','male','male']

as_list = [] #accuracy score list

for cl in classifiers:
	clf = cl.fit(X,Y)
	prediction =clf.predict(X_test)    
	asc = accuracy_score(Y_test, prediction)
	if asc == 1 :
		cl = str(cl)
		a, b  = cl.split('(', 1)
		print a







