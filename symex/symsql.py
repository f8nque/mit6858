## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import sqlalchemy.orm
from . import fuzzy

oldget = sqlalchemy.orm.query.Query.get
def newget(query, primary_key):
  ## Exercise 8: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  q = query.all()
  pk = q[0].__table__.primary_key.columns.keys()[0]
  l =[getattr(p,pk) for p in q]
  print(l)
  for p in l:
      b = primary_key ==p
  r = oldget(query,primary_key)
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
  return r

sqlalchemy.orm.query.Query.get = newget
