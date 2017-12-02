(lambda z: print(sum(int(i) for i, j in zip(z, z[len(z) // 2:] + z[:len(z) // 2]) if i == j)))(__import__('sys').stdin.read().strip())
