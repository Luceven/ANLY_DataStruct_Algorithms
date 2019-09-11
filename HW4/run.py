for _ in range(10):
	with open("./prims_kn.py") as f:
		code = compile(f.read(), "./prims_kn.py", 'exec')
		exec(code)