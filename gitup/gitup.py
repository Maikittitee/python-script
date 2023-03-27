#!/usr/bin/env python3

import sys
import os
import subprocess

# $gitup [files] -m <massage> -m <desciption> -b <branch>

if __name__ == "__main__":
	argv = sys.argv
	argc = len(argv)
	files = []

	m_flag = 0
	b_flag = 0
	commit_massage = []
	branch_name = None

	for i in range(argc):
		if (argv[i] == "-m"):
			m_flag = 1
			commit_massage.append(argv[i + 1])
		if (argv[i] == "-b"):
			b_flag = 1
			if (i != argc - 1):
				branch_name = argv[i + 1]
			else:
				branch_name = None
		elif (i >= 1 and m_flag == 0 and b_flag == 0):
			files.append(argv[i])

	# print(files)
	# print()
	# print(commit_massage)
	# # print(commit_description)

	# print()
	# if (branch_name != None):
	# 	print(branch_name)
	result = subprocess.run(['git', 'branch','--show-current'], stdout=subprocess.PIPE)
	print(result.stdout.decode('utf-8'))
	if (branch_name == None):
		branch_name = str(result.stdout.decode('utf-8'))[0:-3]
	#print(branch_name)


