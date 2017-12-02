(lambda z, mmd: print(sum(mmd([int(i) for i in r.split()]) for r in z.split('\n'))))(__import__('sys').stdin.read().strip(), lambda s: (max(s) - min(s)))
