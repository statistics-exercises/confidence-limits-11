import matplotlib.pyplot as plt
import numpy as np

def histo_estimate(nsamples, nbins, a, b ) :
  histo = np.zeros(nbins)
  # Insert code to generate an estimate of the probablity density function for a
  # uniform continuous random variable that lies between a b here.
  
  return histo
  
# This loop resamples your histogram
nresamples, nbins = 100, 20
histo_samples = np.zeros([nresamples,nbins]) 
for i in range(nresamples) : histo_samples[i] = histo_estimate( 200, nbins, -1, 1 )

# This computes percentiles from your histogram
xvals, lower, upper, median = np.zeros(nbins), np.zeros(nbins), np.zeros(nbins), np.zeros(nbins)
for i in range(nbins) : 
  xvals[i] = -1 + ( 2/nbins )*(i+0.5)
  # We find the median 
  median[i] = np.median( histo_samples[:,i] )
  # When we use fill_between below we are saying to fill the area between these 
  # two curves
  lower[i] = np.percentile( histo_samples[:,i], 5 )
  upper[i] = np.percentile( histo_samples[:,i], 95 ) 

#This draws the shaded region that illustrates the error around our estimate
plt.fill_between( xvals, lower, upper ) 
# This draws the line showing the median
plt.plot( xvals, median, "k-" )
plt.savefig("histo_with_errors.png")
