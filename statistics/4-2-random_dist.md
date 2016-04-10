[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Yes, the distribution is uniform.

```python
import random
import thinkstats2
import thinkplot

n = [random.random() for i in range(1000)]
pmf = thinkstats2.Pmf(n)
thinkplot.Pmf(pmf, label = 'pmf')
thinkplot.Show()

cdf = thinkstats2.Cdf(n)
thinkplot.Cdf(cdf, label = 'cdf')
thinkplot.Show()
```
