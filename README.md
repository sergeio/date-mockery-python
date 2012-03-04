This is a way to get ruby-style date arithmetic in python.

Supports all units that datetime.timedelta does.

```python
my_date = DateNumber(datetime(2012, 1, 2))

print my_date[1].days.ago
2012-01-01 00:00:00

print my_date[2].weeks.ahead
2012-01-16 00:00:00

print repr(my_date[10].milliseconds.ahead)
datetime.datetime(2012, 1, 2, 0, 0, 0, 10000)
```

Supports brackets and parentheses.

```python
print my_date(2).seconds.ago
2012-01-01 23:59:58

print d(2).minutes.ago == d.now - timedelta(minutes=2)
True
```

I'm sorry.
