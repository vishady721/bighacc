from prepdata import freqdata, lengthdata 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

lengthdata = lengthdata.loc[600 <= lengthdata['Length']]
print(lengthdata.shape)

Xfreq = freqdata[['No.']]
Xlength = lengthdata[['Length']]
Yfreq = freqdata['Value']
Ylength = lengthdata['Value']

Xftrain, Xftest, Yftrain, Yftest = train_test_split(Xfreq, Yfreq, test_size=0.2)
Xltrain, Xltest, Yltrain, Yltest = train_test_split(Xlength, Ylength, test_size=0.2)

def fit(model):
    model.fit(Xftrain, Yftrain)
    print(model.score(Xftest, Yftest))
    model.fit(Xltrain, Yltrain)
    print(model.score(Xltest, Yltest))


logreg = LogisticRegression()
mnb = MultinomialNB()
knn = KNeighborsClassifier(algorithm = 'brute', n_jobs=-1)
svm=LinearSVC(C=0.0001)
clf = DecisionTreeClassifier()
bg=BaggingClassifier(DecisionTreeClassifier(),max_samples=0.5,max_features=1.0,n_estimators=10)
adb = AdaBoostClassifier(DecisionTreeClassifier(min_samples_split=10,max_depth=4),n_estimators=10,learning_rate=0.6)
rf = RandomForestClassifier(n_estimators=30, max_depth=9)

print("logistic")
fit(logreg)
print("multinomialNB")
fit(mnb)
print("KNN")
fit(knn)
print("SVM")
fit(svm)
print("DT")
fit(clf)
print("BDT")
fit(bg)
print("ABDT")
fit(adb)
print("RF")
fit(rf)
