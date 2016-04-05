from random import randint
import numpy

markov_chain = []

def setup(num_lines):
	for i in xrange(num_lines):
		add = []
		for j in xrange(num_lines):
			add.append(0)
		markov_chain.append(add)


def parse():
	file = open("transitions.txt")

	for line in file:
		l = line.strip().split(' ')
		if l[0] == '#' or l[0] == '\n' or l[0] == '':
			continue
		markov_chain[int(l[0])-1][int(l[2])-1] = int(l[1])

def print_chain():
	markov_len = len(markov_chain)
	for i in xrange(markov_len):
		for j in xrange(markov_len):
			print str(i+1) + "-> " + str(markov_chain[i][j]) + "% -> " + str(j+1)

def get_sequence(seq_len):
	first = randint(0, 5)
	ret_seq = []
	ret_seq.append(first)

	for i in xrange(seq_len):
		next_item = randint(0, 100)
		for j in markov_chain[first]:
			

setup(6)
parse()
print_chain()