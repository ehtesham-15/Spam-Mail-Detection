
#Import required libraries
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#load dataset
file_path = "mail_data.csv"
mail_data = pd.read_csv(file_path)
print("first few rows:")
print(mail_data.head())

#now Data cleaning
print("\nchecking for missing value")
print(mail_data.isnull().sum())

#to replace missingvalues with empty string
mail_data = mail_data.fillna('')

#now convert labels to numbers
print("\nto convert Category column into numeric labels spam = 0, ham = 1")
mail_data['Category'] = mail_data['Category'].map({'spam': 0, 'ham': 1})
print("conversion done")
print(mail_data['Category'].value_counts())

#now separate Messages and labels
messages = mail_data['Message']
labels = mail_data['Category']
print("total messages:", len(messages))
print("total labels:", len(labels))

#split data into training andTesting
messages_train, messages_test, labels_train, labels_test = train_test_split(messages, labels, test_size=0.2, random_state=42)
print("training sample:", len(messages_train))
print("testing samples:", len(messages_test))

#now to Convert Text into tf-idf features
print("\nConvert Text into tf-idf features")
vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = vectorizer.fit_transform(messages_train)
X_test_features = vectorizer.transform(messages_test)
print("vectorization done")

#LOGISTIC REGRESSION
#train logistic regressionmodel
model = LogisticRegression()
model.fit(X_train_features, labels_train)
print("training done")

#evaluate model on Training data
train_predictions = model.predict(X_train_features)
train_accuracy = accuracy_score(labels_train, train_predictions)
print("training accuracy:", round(train_accuracy, 4))

#now evaluate model on test data
test_predictions = model.predict(X_test_features)
test_accuracy = accuracy_score(labels_test, test_predictions)
print("test accuracy:", round(test_accuracy, 4))

#classification report and confusion matrix
print("\nEvaluation report on test data:")
print(classification_report(labels_test, test_predictions))
print("Confusion matrix:")
print(confusion_matrix(labels_test, test_predictions))

#sample email try
print("\nsample email for prediction")
sample_email = ["URGENT! We are trying to contact you. Last weekend's draw shows that you have won a £900 prize GUARANTEED.Call 09061701939. Claim code S89. Valid for 12 hours only.",]

#now convert sample mail to tf-Idf feature
sample_features = vectorizer.transform(sample_email)
sample_prediction = model.predict(sample_features)
print("Email is", "not a SPAM" if sample_prediction[0] == 1 else "SPAM")

joblib.dump(model, 'spam_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')


