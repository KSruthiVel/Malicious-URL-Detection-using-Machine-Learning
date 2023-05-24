import sklearn
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE
import joblib
import os
from dotenv import load_dotenv
import pandas as pd
import sys
import joblib
import os

path = "F:\\Sanchalak\\sanchalak\\features_extraction.py"
if os.path.exists(path):
    pass
else:
    print("file not present")
print(os.listdir())

sys.path.append("F:\\Sanchalak")
import numpy as np

from sanchalak import features_extraction


def train_rf():
    df = pd.read_csv('../train/data/uci-ml-phishing-dataset.csv')
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
    print("accuracy:   %0.3f" % score)
    return clf


def predict(test_url):
    features_test = features_extraction.main(test_url)
    features_test = np.array(features_test).reshape((1, -1))

    clf = train_rf()

    pred = clf.predict(features_test)
    print(test_url)
    print(pred)
    return int(pred[0])


def main_f():
    url = sys.argv[1]
    # print("url", url)
    # url = "https://faacebok.zapto.org/"
    # url = "https://www.activestate.com/resources/quick-reads/how-to-pip-install-requests-python-package/"
    # url = "https://pypi.org/project/djangorestframework/"
    # http://mp3raid.com/music/krizz_kaliko.html -safe
    # http://br-icloud.com.br/ - phishing
    prediction = predict(url)
    if prediction == 1:
        print("SAFE")
    else:
        print("PHISHING")


if __name__ == "__main__":
    main_f()

# <center><img src="eyes.gif" alt="Sanchalak Logo" style="width: 60px; height: 60px; position: absolute; top: 2;
# left: 20px;"> <strong>Sanchalak</strong></center>