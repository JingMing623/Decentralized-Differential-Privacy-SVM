# in this local step,  we generate the dpSVM weights for each data site using object pertubation method
# the data from site11 and site_test are used to train aggregate classifier and test,  all data are propogated to remote node

import random, scipy
import os
import numpy as np
import dp_stats as dps
import pickle
import json
import argparse
from os import listdir
from os.path import isfile, join
import sys
from common_functions import *

parser = argparse.ArgumentParser(description='help read in my data from my local machine!')
parser.add_argument('--run', type=str,  help='grab coinstac args')
args = parser.parse_args()
args.run = json.loads(args.run)

username = args.run['username']
passedDir = args.run['userData']['dirs'][0]
sys.stderr.write("load pickled data from site :"+passedDir)

files = [f for f in listdir(passedDir) if isfile(join(passedDir, f))]

for f in files:
   
   with open(join(passedDir,f),'rb') as fp:
      data = pickle.load(fp)

#if ('site11' in passDir): # need to add condition about if 'site11' and 'site_test' are the site name


if (passedDir != 'site11') and (passedDir != 'site_test'):
   eps = 15
   W_site = dps.dp_svm(data[0], data[1], epsilon=eps)
   # need to calculate the error rate for this W 
   # error_rate_site = test_errors(W_site, data[0], data[1]) 
    
   computationOutput = json.dumps({"W_site": W_site.tolist()})
   sys.stdout.write(computationOutput)

elif passedDir == 'site11':
   computationOutput = json.dumps({"train_data_points": data[0].tolist(), "train_data_labels": data[1].tolist()})
   sys.stdout.write(computationOutput)

else:
   computationOutput = json.dumps({"test_data_points": data[0].tolist(), "test_data_labels": data[1].tolist()})
   sys.stdout.write(computationOutput)







