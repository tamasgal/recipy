import recipy

import sys
del sys.modules['codecs']

import codecs

# importing pandas after deleting and reimporting codecs does not work
import pandas as pd
import numpy as np
from matplotlib.pyplot import *

with codecs.open('UTF-8-demo.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
#data.to_csv('output2.csv')

data.plot(x='A', y='B')
# but the script then crashes on savefig
savefig('newplot.pdf')