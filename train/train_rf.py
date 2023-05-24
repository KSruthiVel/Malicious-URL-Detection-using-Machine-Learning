import sklearn
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE
import joblib
import os
from dotenv import load_dotenv
import pandas as pd

label = []
data = []

load_dotenv()
MODEL_PATH_RF = os.getenv("MODEL_PATH_RF")
# ============================================================================================
# =============================== START =====================================================
# ============================================================================================
df = pd.read_csv('./data/uci-ml-phishing-dataset.csv')
print(df.shape)
print(df['Result'].value_counts())
print("before dropping columns", df.columns)
df = df.drop('SSLfinal_State', axis=1)
df = df.drop('port', axis=1)
df = df.drop('popUpWidnow', axis=1)
df = df.drop('Page_Rank', axis=1)
df = df.drop('Links_pointing_to_page', axis=1)
print("after dropping columns", df.columns)
y = df['Result']
X = df.drop('Result', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
print("Before over sampling: ", Counter(y_train))
# define over sampling strategy
smote = SMOTE(random_state=42)
# fit and apply the transform
X_train, y_train = smote.fit_resample(X_train, y_train)
# summarize class distribution
print("After over sampling: ", Counter(y_train))
print("X train shape:", X_train.shape, "X test shape:", X_test.shape)
clf = RandomForestClassifier(max_depth=20)
clf.fit(X_train, y_train)
y_pred_rf = clf.predict(X_test)
score = metrics.accuracy_score(y_test, y_pred_rf)
train_accuracy = clf.score(X_train, y_train)  # Compute the training accuracy
print("Training accuracy: %0.3f" % train_accuracy)
print("accuracy:   %0.3f" % score)
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred_rf))  # Compute the confusion matrix

print("\nClassification report:")
print(classification_report(y_test, y_pred_rf))  # Compute precision, recall, F1 score, and other metrics

print(sklearn.__version__)
joblib.dump(clf, MODEL_PATH_RF, compress=9)
print("Done!")
'''
dataset = pd.read_csv('./data/data.csv')
y = dataset['Result']
X = dataset.drop('Result', axis=1)
print(dataset.columns)
print(X.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)
print(X_train.shape, X_test.shape)
clf = RandomForestClassifier(max_depth=5)

# fit the model
clf.fit(X_train, y_train)
# predicting the target value from the model for the samples
print("x_test", X_test.head(1))
y_test_forest = clf.predict(X_test)
print("y", y_test_forest[0])
y_train_forest = clf.predict(X_train)
predicted_prob = clf.predict_proba(X_test)[:,-1]
features_test = features_extraction.main("http://saf1ty-acct-banned-22894.esy.es/recovery-chekpoint-login.html")
print("test", features_test)
predicted = clf.predict(X_test)
print("prob", predicted_prob)
print("predict", predicted)
print(classification_report(y_test,predicted))
# computing the accuracy of the model performance
acc_train_forest = accuracy_score(y_train,y_train_forest)
acc_test_forest = accuracy_score(y_test,y_test_forest)
print("Random forest: Accuracy on training Data: {:.3f}".format(acc_train_forest))
print("Random forest: Accuracy on test Data: {:.3f}".format(acc_test_forest))

joblib.dump(clf, MODEL_PATH_RF, compress=9)
'''
'''
print(sklearn.show_versions())
with open('./data/web_data.arff') as fh:
    for line in fh:
        line = line.strip()
        #print("line", line)
        temp = line.split(',')
        #print("temp_list", temp)
        #print("temp", temp[-1])
        label.append(temp[-1])
        data.append(temp[0:-1])

X = np.array(data)
y = np.array(label)
#print("yes", y, "x", X)
X = X[:, [0, 1, 2, 3, 4, 5,
          6, 8, 9, 11, 12,13,
          14, 15, 16, 17, 18, 19,
          20, 22, 23, 24, 25, 27,
          29]]
X = np.array(X).astype(np.float64)
from collections import Counter
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from imblearn.over_sampling import SMOTE
print("Before sampling: ", Counter(y_train))
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)
print("after sampling: ", Counter(y_train))
clf = RandomForestClassifier(random_state=42, verbose=1)
clf.fit(X_train, y_train)
importance = clf.feature_importances_

print(importance)
#print(X_test)
print(clf.score(X_test, y_test))
predicted_prob = clf.predict_proba(X_test)[:,-1]
predicted = clf.predict(X_test)
print(predicted)
print("y", y_test)
print("prob",predicted_prob)
## Accuray e AUC
accuracy = metrics.accuracy_score(y_test, predicted)
auc = metrics.roc_auc_score(y_test, predicted_prob)
print("Accuracy (overall correct predictions):", round(accuracy, 2))
print("Auc:", round(auc, 2))

## Precision e Recall
# recall = metrics.recall_score(y_test, predicted)
# precision = metrics.precision_score(y_test, predicted)
# print("Recall (all 1s predicted right):", round(recall, 2))
# print("Precision (confidence when predicting a 1):", round(precision, 2))
# print("Detail:")
# print(metrics.classification_report(y_test, predicted, target_names=[str(i) for i in np.unique(y_test)]))
joblib.dump(clf, MODEL_PATH_RF, compress=9)
'''
