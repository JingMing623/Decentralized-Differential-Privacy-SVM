# in this step, get svm weights from every node, and then send all weights to site_11

import json
import argparse
import sys
import sklearn
from sklearn.linear_model import LogisticRegression
import numpy as np
from common_functions import *

parser = argparse.ArgumentParser(description='dpsvm remote computation step1')
parser.add_argument('--run', type=str,  help='grab coinstac args')
args = parser.parse_args()
args.run = json.loads(args.run)

user_result = args.run['userResults']

sols = []
site_exclude = ['site11','site_test']
train_data = {}
test_data = {}


user_result_json = json.dumps(user_result[0])
sys.stderr.write(user_result_json)


for i in range(len(user_result)):
  sys.stderr.write(user_result[i]['username']+"\n")
  if (user_result[i]['userData']['dirs'][0] not in site_exclude):
     sols = sols + [user_result[i]['data']['W_site']]
  elif (user_result[i]['userData']['dirs'][0] == 'site11'):
     train_data[0] = user_result[i]['data']['train_data_points']
     train_data[1] = user_result[i]['data']['train_data_labels']
  elif (user_result[i]['userData']['dirs'][0] == 'site_test'):
     test_data[0] = user_result[i]['data']['test_data_points']
     test_data[1] = user_result[i]['data']['test_data_labels']
  else:
     sys.stderr.write("error on dirs category\n")

  # train (use public logistic regression classifer to aggregate svm weights from each site)
train_data_mapped = data2data(train_data[0], sols)
clf = LogisticRegression()
clf.fit(train_data_mapped, train_data[1])

  #test
test_data_mapped = data2data(test_data[0], sols)
e= 100*abs(sum(map(lambda x: min(0,x),clf.predict(test_data_mapped)*test_data[1])))/double(len(test_data[1]))

 #also generate the error rate for test_data based on the W_site
e_site = []

for i in range(0,4):
  e_site.append(test_errors(np.asarray(sols[i]), np.asarray(test_data[0]), np.asarray(test_data[1])))


sys.stderr.write("final error rate of test data using aggregated classifier is: "+str(e)+"\n")
sys.stderr.write("error rates of test data using SVM weights from each site are: ")
sys.stderr.write(str(e_site[0])+','+str(e_site[1])+','+str(e_site[2])+','+str(e_site[3]))


computationOutput = json.dumps({"complete": True, "final_error_rate": e})
sys.stdout.write(computationOutput)


