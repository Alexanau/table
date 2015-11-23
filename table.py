#!/usr/bin/python
import getopt as g
import sys

optlist, args = g.getopt(sys.argv[1:],'d:')
delim = ','
for o,a in optlist:
  if o == '-d':
    delim = a

max_width = [0]

with open(args[0],'r') as fh:
  for line in fh:
    line = line.rstrip()
    fields = line.split(delim)
    for idx,field in enumerate(fields):
      field = field.strip()
      if len(max_width) <= idx :
        max_width.append(len(field))
      elif max_width[idx] < len(field):
        max_width[idx] = len(field)

  lb = ['']
  for width in max_width:
    lb.append('-'*(width+2))
  lb.append('')
  linebreak = '+'.join(lb)
  fh.seek(0,0)
  print linebreak
  for line in fh:
    line = line.rstrip()
    fields = line.split(delim)
    out = ['']
    for idx,width in enumerate(max_width):
      if(len(fields)<=idx):
        out .append( '| ' + ' '*width + ' ')
      else:
        field = fields[idx].strip()
        out .append( '| '+field + ' '*(width-len(field)) + ' ')
    out.append( '|')
    print ''.join(out)
    print linebreak



field = field.strip()
