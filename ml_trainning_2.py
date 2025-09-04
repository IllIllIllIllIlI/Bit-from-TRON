from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import pickle as pkl

tron_df = pd.concat(map(pd.read_csv, ['tron_dataset.csv', 'tron_dataset_full.csv']), ignore_index=True)
print(tron_df['answer'].value_counts())

X = tron_df['question']
y = tron_df['answer']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print(accuracy_score(y_test, y_pred)," <- accuracy")
print(classification_report(y_test, y_pred))
