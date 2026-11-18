"""Construct and verify a 13-gon with 27 pentagonal bounded faces.

Run with ordinary Python 3: python3 construct_verify.py
No third-party packages are required. Do not use Python's -O option,
because the verifier deliberately uses assert statements.

The checks certify simplicity, an oriented sphere embedding, the complete
face-size distribution, and connectivity after EVERY deletion of at most
two vertices, in both the graph and its dual. See README_zh.txt for the
short mathematical construction and proof.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json


def cap_faces(prefix):
    """Oriented patch faces on the side traversed by a0, ..., a5, w."""
    outer = [f'{prefix}{i}' for i in range(6)] + ['w']
    rim = [f'{prefix}b{i}' for i in range(6)]
    center = f'{prefix}c'
    faces = [[outer[i], outer[i+1], rim[i]] for i in range(6)]
    faces += [[outer[i], rim[i], rim[(i-1) % 6]] for i in range(6)]
    faces += [[rim[i], rim[i+1], center] for i in range(4)]
    faces += [[rim[4], rim[5], rim[0], center]]
    return faces


def face_map(faces):
    """Map oriented edges to faces and each incoming neighbor to the next."""
    left, turns = {}, {}
    for label, cycle in faces.items():
        assert len(cycle) == len(set(cycle)) >= 3, (label, cycle)
        for i, u in enumerate(cycle):
            incoming, outgoing = cycle[i-1], cycle[(i+1) % len(cycle)]
            assert (u, outgoing) not in left, (label, u, outgoing)
            left[u, outgoing] = label
            turn = turns.setdefault(u, {})
            assert incoming not in turn
            turn[incoming] = outgoing
    assert all((v, u) in left for u, v in left)
    assert len(turns) - len(left)//2 + len(faces) == 2
    incident = {}
    for u, turn in turns.items():
        first = v = next(iter(turn))
        cyclic_order = []
        while v not in cyclic_order:
            cyclic_order.append(v)
            v = turn[v]
        assert v == first and len(cyclic_order) == len(turn)
        incident[u] = [left[u, v] for v in cyclic_order]
        anchor = incident[u].index(min(incident[u]))
        incident[u] = incident[u][anchor:] + incident[u][:anchor]
    return incident, {u: set(t) for u, t in turns.items()}, left


def assert_connectivity(adj):
    for k in (0, 1, 2):
        for removed in combinations(adj, k):
            surviving = set(adj).difference(removed)
            queue = [min(surviving)]
            surviving.remove(queue[0])
            for v in queue:
                neighbors = adj[v] & surviving
                queue.extend(neighbors)
                surviving -= neighbors
            assert not surviving, (removed, surviving)


def create():
    cycle = [f'p{i}' for i in range(6)] + ['w'] + [f'q{i}' for i in reversed(range(6))]
    dfaces = [['h', cycle[(i+1)%13], cycle[i]] for i in range(13)]
    dfaces += cap_faces('p')
    dfaces += [row[::-1] for row in cap_faces('q')]
    dfaces += [['q0', 'p0', 'pb5', 'w', 'qb5']]
    dual_faces = dict(enumerate(dfaces))
    pfaces, dual_adj, dleft = face_map(dual_faces)
    # Generate the edge set independently from the construction recipe.
    recipe = set()
    def edge(a, b):
        assert a != b
        recipe.add(frozenset((a, b)))
    for i, a in enumerate(cycle):
        edge(a, cycle[(i+1)%13])
        edge('h', a)
    for prefix in ('p', 'q'):
        path = [f'{prefix}{i}' for i in range(6)] + ['w']
        rim = [f'{prefix}b{i}' for i in range(6)]
        for i in range(6):
            edge(rim[i], rim[(i+1)%6])
            edge(rim[i], path[i])
            edge(rim[i], path[i+1])
        edge(rim[5], path[0])
        for i in range(5):
            edge(f'{prefix}c', rim[i])
    assert recipe == {frozenset((u, v)) for u, v in dleft}
    _, primal_adj, pleft = face_map(pfaces)
    assert all(primal_adj[f] == {dleft[v,u] for u,v in zip(row, row[1:]+row[:1])}
               for f, row in dual_faces.items())
    assert Counter(map(len, dual_adj.values())) == {5: 27, 13: 1}
    assert Counter(map(len, primal_adj.values())) == {3: 45, 4: 2, 5: 1}
    assert Counter(map(len, pfaces.values())) == {5: 27, 13: 1}
    assert pfaces['h'] == list(range(13))
    assert len(dleft)//2 == len(pleft)//2 == 74
    assert_connectivity(dual_adj)
    assert_connectivity(primal_adj)
    pfaces = {u: pfaces[u] for u in ['h', *cycle, *[f'pb{i}' for i in range(6)], 'pc',
                                        *[f'qb{i}' for i in range(6)], 'qc']}
    return {
        'description': 'Spherical face lists of a graph and its dual. Primal vertex i corresponds to entry i of dual_faces, indexed from 0. Each key of primal_faces is the corresponding dual vertex.',
        'outer_primal_face': 'h',
        'dual_faces': dfaces,
        'primal_faces': pfaces
    }


if __name__ == '__main__':
    data = create()
    dest = Path(__file__).with_name('pentagulation13_certificate.json')
    dest.write_text(json.dumps(data, indent=2) + '\n')
    print('PASS: H is simple and has a sphere embedding; V=28, E=74, F=48.')
    print('PASS: degrees of H are 13 once and 5 twenty-seven times.')
    print('PASS: G is simple and has a sphere embedding; V=48, E=74, F=28.')
    print('PASS: G has one 13-gon and twenty-seven pentagons.')
    print('PASS: all 407 vertex-deletion sets of size <=2 preserve connectivity of H.')
    print('PASS: all 1177 vertex-deletion sets of size <=2 preserve connectivity of G.')
    print('Outer boundary:', data['primal_faces']['h'])
    print('Certificate:', dest.name)
