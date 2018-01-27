from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
import numpy as np

clf = SGDClassifier(loss="log", max_iter=1000, tol=1e-3)
tf = TfidfVectorizer()

def train(trainfile):
  X, y = [], []
  #DATA_PATH = "data/data-2.csv"
  
  with open(trainfile, 'r') as f:
    for line in f:
      X.append(line.split(',')[0].lower())
      y.append(line.split(',')[1].strip('\n'))

  # new label, turn m(ale) & f(emale) into 1 and 0
  y = np.array(y)
  y_train = np.where(y=='m', 1, 0)
  X_train = tf.fit_transform(X)
  clf.fit(X_train, y_train)

def predict(name):
  name = tf.transform([name]) # transform into vector
  pred = clf.predict(name)[0] # predict, get first index for result
  prob = clf.predict_proba(name) # get probability score
  prob_gender = "Laki-laki" if pred == 1 else "Perempuan"
  prob_female = round(prob[0][0]*100, 2)
  prob_male = round(prob[0][1]*100, 2)
  return prob_gender, prob_female, prob_male

train("data/data-2.csv")