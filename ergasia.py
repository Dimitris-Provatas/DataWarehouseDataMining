"""
@author: Dimitris Provatas
"""

#initialise strins with the file names to avoid confusion and save time
test = 'test.arff'
train = 'train.arff'

#imports
from scipy.io import arff
from io import StringIO


#reads the data
data, meta = arff.loadarff(StringIO(train))

'''
preproccessing
'''

#