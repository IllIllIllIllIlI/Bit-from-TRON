from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np
import string
import pickle as pkl

tron_df = pd.read_csv("tron_dataset.csv")

X = tron_df['question']
y = tron_df['answer']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1,2))

classifier = SVC(C=0.9, kernel='linear', probability=True) 

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

fitted_classifier = classifier.fit(X_train_vectorized, y_train)

predictions = fitted_classifier.predict(X_test_vectorized)
train_predictions = fitted_classifier.predict(X_train_vectorized)

print("Test Accuracy: \n", accuracy_score(y_test, predictions))
print("Train Accuracy: \n", accuracy_score(y_train, train_predictions))
print("Classification Report (test): \n", classification_report(y_test, predictions))
print("Classification Report (train): \n", classification_report(y_train, train_predictions))

with open("bit_model_v0000.pkl", "wb") as banana:
    pkl.dump((vectorizer, classifier), banana)
