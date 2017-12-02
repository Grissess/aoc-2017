(lambda z: print(sum(int(i) for i, j in zip(z, z[1:] + z[0]) if i == j)))(__import__('sys').stdin.read().strip())
