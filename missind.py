class DefaultDict(dict):
  def __missing__(self, key):
    return []
d = DefaultDict()
d['florp'] = 127
d['dsd']=32332
print d