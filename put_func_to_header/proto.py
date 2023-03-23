#!/usr/bin/env python3

import os
import sys

def	is_prototype(line):
	return (line[0] != '\t' and line[0] != ' ' and line[0] != "{" and line[0] != '}' and line[0] != '\n' and line[0] != '/' and line[0] != '#' and line[0] != '*')

def get_function_prototype(lines, prototypes):
	for line in lines:
		if is_prototype(line):
			prototypes.append(line[0:-1:1])

if __name__ == "__main__":
	argv = sys.argv
	argc = len(argv)

	script_file = argv[0]

	prototypes = []
	semi_prototypes = [""]
	
	for c_file_arg in argv:
		if (c_file_arg != script_file):
			c_file = open(c_file_arg, 'r')
			lines = c_file.readlines()
			get_function_prototype(lines,prototypes)

	for prototype in prototypes:
		semi_prototypes.append(prototype + ";" )

	for semi_prototype in semi_prototypes:
		if ("int\tmain" not in semi_prototype):
			print(semi_prototype)

#	f = open(header_file, 'a')
#	f.write('\n'.join(prototypes))  
