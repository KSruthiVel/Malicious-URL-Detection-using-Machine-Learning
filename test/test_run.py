
import sys

import joblib
import os
path = "F:\\Sanchalak\\test\\features_extraction.py"
if os.path.exists(path):
    pass
else:
    print("file not present")
print(os.listdir())

sys.path.append("F:\\Sanchalak")
import numpy as np

from sanchalak import features_extraction


def predict(test_url):
    features_test = features_extraction.main(test_url)
    features_test = np.array(features_test).reshape((1, -1))
    print("features_test", features_test)
    clf = joblib.load(features_extraction.MODEL_PATH_RF)
    print(clf)
    pred = clf.predict(features_test)
    print(test_url)
    print(pred)
    return int(pred[0])


def main():
    # url = sys.argv[1]
    # url = "https://pricehistory.in/?url=https%3A%2F%2Fai.google%2Feducation%2F"
    url = "http://saf1ty-acct-banned-22894.esy.es/recovery-chekpoint-login.html"
    url = "titaniumcorporate.co.za"
    # url = "https://breakingcode.wordpress.com/2010/06/29/google-search-python/"

    prediction = predict(url)
    if prediction == 1:
        print("SAFE")
    else:
        print("PHISHING")


if __name__ == "__main__":
    main()
