import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_histo(self) : 
        mean_histo = 6*[0]
        for i in range(20) :
          this_histo = histo_estimate(100,6,0,1)
          for j in range(6) : mean_histo[j] = mean_histo[j] + this_histo[j]
  
        for j in range(6) : mean_histo[j] = mean_histo[j] / 20

        for i in range(6) :
           bar = np.sqrt( (1/6)*(1-(1/6))/20 )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.fabs( mean_histo[i]*(1/6) - (1/6) )<bar, "your program for generating the histogram appears to be incorrect" )
