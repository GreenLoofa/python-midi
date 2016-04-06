from random import randint

markov_chain = []

def setup(num_entries):
	for i in xrange(num_entries):
		A = []
		for j in xrange(num_entries):
			A.append(0)
		markov_chain.append(A)

def parse():
	file = open("transitions.txt")

	max_state = -1
	for line in file:
		l = line.strip().split(' ')
		if l[0] == '#' or l[0] == '\n' or l[0] == '':
			continue
		if max_state < int(l[0]):
			max_state = int(l[0])
		if max_state < int(l[2]):
			max_state = int(l[2])
	if max_state == -1:
		return -1

	setup(max_state)

	file2 = open("transitions.txt")

	(sum_so_far, curr_state) = 0, 0
	for line in file2:
		l = line.strip().split(' ')
		if l[0] == '#' or l[0] == '\n' or l[0] == '':
			continue
		if curr_state != int(l[0]):
			sum_so_far = 0
			curr_state = int(l[0])
		sum_so_far += int(l[1])
		markov_chain[int(l[0])-1][int(l[2])-1] += sum_so_far

def print_chain():
	markov_len = len(markov_chain)
	for i in xrange(markov_len):
		for j in xrange(markov_len):
			if j == 0:
				print str(i+1) + " -> " + str(markov_chain[i][j]) + "% -> " + str(j+1)
			else:
				print str(i+1) + " -> " + str(markov_chain[i][j] - markov_chain[i][j-1]) + "% -> " + str(j+1)

def get_sequence():
	parse()
	seq_len = randint(2, 4)
	first = randint(0, 5)
	ret_seq = []
	ret_seq.append(first)

	curr_state = ret_seq[0]
	for i in xrange(0, seq_len-1):
		next_state_prob = randint(0, 100)
		# TODO: Make it so that every note has at least some probability
		next_state = 0
		for j in xrange(0, len(markov_chain[curr_state])):
			if j == 0:
				if next_state_prob >= 0 and next_state_prob <= markov_chain[curr_state][j]:
					next_state = j
			else:
				if next_state_prob >= markov_chain[curr_state][j-1] and next_state_prob <= markov_chain[curr_state][j]:
					next_state = j
		ret_seq.append(next_state)
		curr_state = next_state
	return ret_seq

# print_chain()
# print get_sequence()