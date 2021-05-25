import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def rec(n):
  if n == 0:
    return
  return rec(n-1)

rec(200000)

