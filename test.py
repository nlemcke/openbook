"""
Put my tests here:

  >>> type(thing1)
  <class 'list'>
  >>> type(thing2)
  <class 'tuple'>
  >>> type(thing3)
  <class 'str'>

"""
# Put your solutions here:

thing1 = [1, 2, 3]
thing2 = (1, 2, 3)
thing3 = 'bananas'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
