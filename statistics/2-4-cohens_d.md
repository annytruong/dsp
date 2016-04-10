[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> First babies tend to be lighter than others, with an average difference of 0.12 lbs.
>> The Cohen d is 0.089 standard deviations.

```python
import first
import thinkstats2

def WeightDifference(live, firsts, others):
	live_mean = live.totalwgt_lb.mean()
	firsts_mean = firsts.totalwgt_lb.mean()
	others_mean = others.totalwgt_lb.mean()

	firsts_var = firsts.totalwgt_lb.var()
	others_var = others.totalwgt_lb.var()

	print 'First Babies Weight:', firsts_mean
	print 'Other Babies Weight:', others_mean
	print 'Weight Difference:', firsts_mean - others_mean, 'lbs'

	#Cohen d

	d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
	print 'Cohen d', d





live, firsts, others = first.MakeFrames()

WeightDifference(live, firsts, others)

```
