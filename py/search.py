#!/usr/bin/python

# The MIT License (MIT)
# Copyright (c) 2014 venus-solar
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os
import getopt


HELPDOC = """
  search pattern in specific files of current directory
  -p  pattern option
  -s  suffix option
  -h  print help doc
"""

class Options(object): pass
OPTIONS = Options()

def usage():
	print HELPDOC

def parseOpt(argv):
	if len(argv) <= 1:
		usage()
		sys.exit()

	short_tags = "hp:s:"
	try:
		opts, args = getopt.getopt(argv[1:], short_tags)
		for o, a in opts:
			if o == "-p":
				OPTIONS.PATTERN = a
			elif o == "-s":
				OPTIONS.SUFFIX = a
			elif o == "-h":
				usage()
				sys.exit()
			else:
				assert False, "Unknown option \"%s\"" %(o)
		assert OPTIONS.PATTERN, "need specify pattern by -p"
		assert OPTIONS.SUFFIX, "need specify pattern by -s"
		return args
	except getopt.GetoptError, err:
		usage()
		print "**" , str(err), "**"
		sys.exit(2)


def search():
	for root, dirs, files in os.walk("."):
		for f in files:
			found = 0
			path = os.path.join(root, f)	
			if f.endswith("." + OPTIONS.SUFFIX):
				fi = open(path, 'rU')
				for line in fi:
					if line.find(OPTIONS.PATTERN) != -1:
						found = 1
						break
				fi.close()
			if found:
				print(path)

def main(argv):
	parseOpt(argv)
	search()

if __name__ == "__main__":
	main(sys.argv)
