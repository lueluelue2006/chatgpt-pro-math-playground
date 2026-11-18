"""Check small polyhedral pentagulations by peeling polygonal dual faces.

The command python3 patchproof.py searches all four surplus values 0..3.
Only standard-library modules are used.
"""
from functools import lru_cache
from itertools import combinations, product
import sys
import time


def parts(n, k):
    """The ordered weak compositions of n into k parts."""
    if k == 0:
        if n == 0:
            yield ()
    elif k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for tail in parts(n-a, k-1):
                yield (a,) + tail


def pair(i, j):
    return (i, j) if i < j else (j, i)


def canonical(r, blocked):
    n = len(r)
    first = min(r)
    options = []
    for i in range(n):
        if r[i] != first:
            continue
        for s in (1, -1):
            order = [(i+s*j) % n for j in range(n)]
            seq = tuple(r[j] for j in order)
            options.append((seq, i, s))
    best = min(a for a,i,s in options)
    if not blocked:
        return best, ()
    return best, min(tuple(sorted(pair((s*(a-i))%n, (s*(b-i))%n)
                                  for a,b in blocked))
                     for seq,i,s in options if seq == best)


def possible(r, blocked, t):
    n = len(r)
    if min(r) < 0 or t < 0:
        return False
    # Euler's formula and counting the as-yet unfilled degrees.
    interior = sum(r) - 2*n + 6 + 2*t
    if interior < 0:
        return False
    if not any(r):
        return interior == 0 and t == n-3 and not blocked
    if interior == 0 and (r.count(0) < 2):
        return False  # every outerplane polygon dissection has two ears
    if interior:
        if sum(x > 0 for x in r) < 3:
            return False  # necessary by 3-connectivity of the full graph
        emax = (0, 0, 1)[interior] if interior < 3 else 3*interior-6
        if sum(r) + 2*emax < 5*interior:
            return False
    for i in range(n):
        unavailable = sum(i in edge for edge in blocked)
        if r[i] > n-3-unavailable+interior:
            return False
    r, blocked = canonical(r, blocked)
    return peel(r, blocked, t)


@lru_cache(None)
def peel(r, blocked, t):
    n = len(r)
    interior = sum(r)-2*n+6+2*t
    blocked = set(blocked)
    # The root face contains boundary edge 0--1.
    # Every selected vertex with residual zero forces both boundary edges.
    forced = {0, 1}
    while True:
        larger = forced | {(a+s)%n for a in forced if r[a] == 0
                           for s in (-1, 1)}
        if larger == forced:
            break
        forced = larger
    optional = tuple(i for i in range(2,n) if i not in forced)
    required = tuple(i for i in range(2,n) if i in forced)
    for size in range(max(3,len(forced)), t+4):
        remaining = t-(size-3)
        for new in range(min(interior, size-len(forced))+1):
            choose = size-new-len(forced)
            for extra in combinations(optional,choose):
                olds = sorted(required+extra)
                onface = {0,1,*olds}
                if any(a in onface and b in onface for a,b in blocked):
                    continue
                if any(((a-1)%n not in onface or (a+1)%n not in onface)
                       for a in onface if r[a] == 0):
                    continue
                ordered = [1]+olds+[n]
                spans = list(zip(ordered, ordered[1:]))
                active = [(a,b) for a,b in spans if b > a+1]
                # An existing edge between selected boundary vertices must be
                # on the root face. Thus gap-one paths have no new vertex.
                degree = list(r)
                for a,b in active:
                    degree[a%n] -= 1
                    degree[b%n] -= 1
                if min(degree) < 0:
                    continue
                incident = [[] for _ in r]
                for j,(a,b) in enumerate(active):
                    incident[a%n].append(j)
                    incident[b%n].append(j)
                if any(degree[a] != 0 for a in onface if not incident[a]):
                    continue
                for lengths in parts(new, len(active)):
                    if not active:
                        if not remaining:
                            return True
                        continue
                    # Vertex names are private to this call. A child is
                    # bounded by an old boundary arc and the new face path.
                    children = []
                    allface = set(onface)
                    index = n
                    for (a,b),k in zip(active,lengths):
                        child = [i%n for i in range(a,b+1)]
                        child.extend(range(index,index+k))
                        allface.update(range(index,index+k))
                        index += k
                        children.append(child)
                    childblocked = []
                    for c in children:
                        m = len(c)
                        childblocked.append(tuple(
                            (i,j) for i,j in combinations(range(m),2)
                            if j != i+1 and (i,j) != (0,m-1)
                            and (pair(c[i],c[j]) in blocked
                                 or c[i] in allface and c[j] in allface)))
                    splitverts = [a for a in onface if len(incident[a])==2]
                    for split in product(*(range(degree[a]+1) for a in splitverts)):
                        childdeg = [dict() for _ in children]
                        for a,x in zip(splitverts,split):
                            j,h = incident[a]
                            childdeg[j][a] = x
                            childdeg[h][a] = degree[a]-x
                        childr = [tuple(d.get(a,degree[a] if a < n else 3)
                                        for a in c) for c,d in zip(children,childdeg)]
                        for ts in parts(remaining, len(children)):
                            if all(possible(x, b, z) for x,b,z in
                                   zip(childr,childblocked,ts)):
                                return True
    return False


def whole(t):
    # We excise the unique vertex of degree 13. For each gap between
    # consecutive neighbors, gaps[i] gives the number of extra vertices
    # on that incident face boundary.
    checked = 0
    for k in range(t+1):
        for gaps in parts(k, 13):
            if gaps != min(gaps[i:]+gaps[:i] for i in range(13)):
                continue
            r, forbidden = [], []
            for h in gaps:
                pos = len(r)
                r.append(2)
                r.extend([3]*h)
                for i,j in combinations(range(pos,pos+h+2),2):
                    if j != i+1:
                        forbidden.append(pair(i%(13+k),j%(13+k)))
            checked += 1
            if possible(tuple(r), tuple(sorted(set(forbidden))), t-k):
                return checked, gaps
    return checked, None


if __name__ == '__main__':
    for t in map(int, sys.argv[1:] or range(4)):
        start = time.monotonic()
        print(t, whole(t), peel.cache_info(), round(time.monotonic()-start,2), flush=True)
