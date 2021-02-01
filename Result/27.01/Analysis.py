import numpy as np
import csv
from scipy.stats import shapiro
import pandas as pd
from scipy.stats import ks_2samp
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

#uploading datasets



chunk = pd.read_csv('unigram_features.csv', header= None,chunksize=300)
unigram1 =  pd.concat(chunk)
print(unigram1)

chunk = pd.read_csv('unigram_features_mal.csv',chunksize=300)
unigram2 =  pd.concat(chunk)

chunk = pd.read_csv('bigram_features.csv', header= None,chunksize=270)
bigram1 =  pd.concat(chunk)

chunk = pd.read_csv('bigram_features_mal.csv',chunksize=270)
bigram2 =  pd.concat(chunk)

chunk = pd.read_csv('trigram_features.csv',chunksize=240)
trigram1 =  pd.concat(chunk)

chunk = pd.read_csv('trigram_features_mal.csv',chunksize=240)
trigram2 =  pd.concat(chunk)

#adiing data for further performance evaluation
unigram = np.row_stack((unigram1,unigram2))
bigram = np.row_stack((bigram1,bigram2))
trigram = np.row_stack((trigram1,trigram2))
zeros_matrix = np.zeros(len(unigram1),dtype=int)
ones_matrix = np.ones(len(unigram1),dtype=int)
matrix = np.hstack((zeros_matrix,ones_matrix))

"""
Performance Evaluation
Apply statistical tests by Kolmogorov-Smirnov and  test to estimate how much feature distribution is close to normal (Gaussian) distribution
"""

#Shapiro-Wilk Test for unigram

# normality test
stat, p = shapiro(unigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
stat, p = shapiro(unigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

#logistic regression for unigram
logreg_clf = LogisticRegression()
logreg_clf.fit(unigram, matrix)

logreg_m=confusion_matrix(matrix,logreg_clf.predict(unigram))
logreg_far=logreg_m[0][1]/(logreg_m[0][1]+logreg_m[0][0])#FAR
logreg_frr=logreg_m[1][0]/(logreg_m[1][1]+logreg_m[1][0])#FRR

log_pr=logreg_clf.predict_proba(unigram)#model effectivness
l1=log_loss(matrix,log_pr) #log-loss metrics

i_p1=(logreg_clf.predict(unigram))# фактичні прогнози
log_f=f1_score(matrix,i_p1)#F-score

print("logistic regression  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))

#support vector machine for unigram
svc = SVC(probability=True)
svc.fit(unigram, matrix)

svc_m=confusion_matrix(matrix,svc.predict(unigram))
svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR

svc_pr=svc.predict_proba(unigram)#ефективність моделі
l2=log_loss(matrix,svc_pr) #log-loss metrics

i_p2=(svc.predict(unigram))# фактичні прогнози
svc_f=f1_score(matrix,i_p2)#F-score

print("support vector machine  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))

#random forest for unigram
tree = DecisionTreeClassifier()
tree.fit(unigram, matrix)

tree_m=confusion_matrix(matrix, tree.predict(unigram))
tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR

tree_pr=tree.predict_proba(unigram)#ефективність моделі
l3=log_loss(matrix,tree_pr) #log-loss metrics

i_p3=tree.predict(unigram)# фактичні прогнози
tree_f=f1_score(matrix,i_p3)#F-score

print("random forest  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))

#Shapiro-Wilk Test for bigram

# normality test
stat, p = shapiro(bigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
stat, p = shapiro(bigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

#logistic regression for bigram
logreg_clf = LogisticRegression()
logreg_clf.fit(bigram, matrix)

logreg_m=confusion_matrix(matrix,logreg_clf.predict(bigram))
logreg_far=logreg_m[0][1]/(logreg_m[0][1]+logreg_m[0][0])#FAR
logreg_frr=logreg_m[1][0]/(logreg_m[1][1]+logreg_m[1][0])#FRR

log_pr=logreg_clf.predict_proba(bigram)#model effectivness
l1=log_loss(matrix,log_pr) #log-loss metrics

i_p1=(logreg_clf.predict(bigram))# фактичні прогнози
log_f=f1_score(matrix,i_p1)#F-score

print("logistic regression  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))

#support vector machine for bigram
svc = SVC(probability=True)
svc.fit(bigram, matrix)

svc_m=confusion_matrix(matrix,svc.predict(bigram))
svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR

svc_pr=svc.predict_proba(bigram)#ефективність моделі
l2=log_loss(matrix,svc_pr) #log-loss metrics

i_p2=(svc.predict(bigram))# фактичні прогнози
svc_f=f1_score(matrix,i_p2)#F-score

print("support vector machine  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))

#random forest for bigram
tree = DecisionTreeClassifier()
tree.fit(bigram, matrix)

tree_m=confusion_matrix(matrix, tree.predict(bigram))
tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR

tree_pr=tree.predict_proba(bigram)#ефективність моделі
l3=log_loss(matrix,tree_pr) #log-loss metrics

i_p3=tree.predict(bigram)# фактичні прогнози
tree_f=f1_score(matrix,i_p3)#F-score

print("random forest  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))


#Shapiro-Wilk Test for trigram

# normality test
stat, p = shapiro(trigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
stat, p = shapiro(trigram)
print('Statistics=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')

#logistic regression for trigram
logreg_clf = LogisticRegression()
logreg_clf.fit(trigram, matrix)

logreg_m=confusion_matrix(matrix,logreg_clf.predict(trigram))
logreg_far=logreg_m[0][1]/(logreg_m[0][1]+logreg_m[0][0])#FAR
logreg_frr=logreg_m[1][0]/(logreg_m[1][1]+logreg_m[1][0])#FRR

log_pr=logreg_clf.predict_proba(trigram)#model effectivness
l1=log_loss(matrix,log_pr) #log-loss metrics

i_p1=(logreg_clf.predict(trigram))# фактичні прогнози
log_f=f1_score(matrix,i_p1)#F-score

print("logistic regression  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))

#support vector machine for trigram
svc = SVC(probability=True)
svc.fit(trigram, matrix)

svc_m=confusion_matrix(matrix,svc.predict(trigram))
svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR

svc_pr=svc.predict_proba(trigram)#ефективність моделі
l2=log_loss(matrix,svc_pr) #log-loss metrics

i_p2=(svc.predict(trigram))# фактичні прогнози
svc_f=f1_score(matrix,i_p2)#F-score

print("support vector machine  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))

#random forest for trigram
tree = DecisionTreeClassifier()
tree.fit(trigram, matrix)

tree_m=confusion_matrix(matrix, tree.predict(trigram))
tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR

tree_pr=tree.predict_proba(trigram)#ефективність моделі
l3=log_loss(matrix,tree_pr) #log-loss metrics

i_p3=tree.predict(trigram)# фактичні прогнози
tree_f=f1_score(matrix,i_p3)#F-score

print("random forest  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))

