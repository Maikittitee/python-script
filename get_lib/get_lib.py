#!/usr/bin/env python3

import os
import sys

argv = sys.argv
argc = len(argv)
path = argv[argc - 1]
getback = 0

if (path == '.'):
	getback = 1
else:
	os.system(f"mkdir {path}")

for arg in argv:
	if (arg != path):
		if (arg == "libft"):
			os.system(f"git clone https://github.com/Maikittitee/my-Libft-42 {path}/libft")
			os.system(f"rm -rf {path}/libft/.git {path}/libft/.gitignore ")
		elif (arg == "gnl"):
			os.system(f"git clone https://github.com/Maikittitee/get_next_line_2 {path}/gnl")
			os.system(f"rm -rf {path}/gnl/.git {path}/gnl/.gitignore {path}/gnl/*bonus* {path}/gnl/README.md")
		elif (arg == "gnl-b"):
			os.system(f"git clone https://github.com/Maikittitee/get_next_line_2 {path}/gnl")
			os.system(f"rm -rf {path}/gnl/.git {path}/gnl/.gitignore {path}/gnl/README.md")
		elif (arg == "printf"):
			os.system(f"git clone https://github.com/Maikittitee/my-ft_printf-42 {path}/libftprintf")
			os.system(f"rm -rf {path}/libftprintf/.git {path}/libftprintf/.gitignore {path}/libft/README.md")


