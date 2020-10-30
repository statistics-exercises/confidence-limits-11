# Continuous histograms with error bars

As you have seen in the previous exercises estimating the probability density function for a continuous random variable by calculating a histogram is no more difficult than estimating a probability mass function for a discrete random variable by calculating a histogram.  If your continuous random variable, U, lies between a and b then the two key differences are:

1. You have to convert the continuous random variable to an integer that is greater than or equal to 0 and less than or equal to n-1 and thus decide which of the n bins to add the count to using:

````
delr = (b-a) / n
mybin = int( np.floor( U / delr ) ) 
````

2. When you normalise you need to divide by the counts bin width (`delr`) so that the eventual integral underneath the histogram is 1.

Everything else is as it was in the discrete case, however.  This includes, incidentally, that when we present our final histograms there should be error bars on our estimates of the probability density function.  __For this task, I would thus like you to write code to generate a continuous histogram with suitable error bars calculated by resampling.__    I have done a lot of the work for you here you still have to do one thing

1. You need to write a function called `histo_esimtate`.  This function takes four input parameters `nsamples`, `nbins`, `a` and `b`.    Within the function, you generate a histogram with `nbins` bins by taking `nsamples` from a uniform continuous random variable that lies between `a` and `b`.  The estimate of the histogram this procedure generates should be stored in the NumPy array called `histo`, which is returned from the function. 

When you have written these functions and the code is run a graph showing a histogram with suitable error bars.  The error bars are displayed as a shaded area in this case, rather than errors around each of the points, because the probability density function we are trying to estimate is a continuous function i.e. a curve. 
