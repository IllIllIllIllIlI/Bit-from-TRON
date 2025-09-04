from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import numpy as np


tron_df = pd.concat(map(pd.read_csv, ['tron_dataset.csv', 'tron_dataset_full.csv']), ignore_index=True)
X = tron_df['question']
y = tron_df['answer']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()

classifier = MultinomialNB()


X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

fitted_classifier = classifier.fit(X_train_vectorized, y_train)

predictions = fitted_classifier.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, predictions)

print(predictions," <- predictions\n")
print(accuracy," <- accuracy\n")
print(X_test, " X_test")
print(X_train," X_train")
print(X_train_vectorized," X_Tr_V")
print(X_test_vectorized, " X_Te_V")
