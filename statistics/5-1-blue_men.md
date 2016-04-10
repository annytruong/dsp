[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.2% of US male population is in this range.

```python
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale = sigma)
type(dist)

print dist.mean(), dist.std()

print dist.cdf(mu-sigma)

min_height = dist.cdf(177.8) 
max_height = dist.cdf(185.4)

print min_height, max_height, max_height - min_height

```
