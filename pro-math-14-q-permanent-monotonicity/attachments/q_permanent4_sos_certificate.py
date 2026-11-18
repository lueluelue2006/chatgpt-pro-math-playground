"""Exact invariant sum-of-squares proof for the real 4 by 4 q-permanent.

THEOREM. For a non-diagonal real symmetric positive definite 4x4 A,
P_A(q) is strictly increasing on [-1,1].

Problem source: https://arxiv.org/html/2611.14694v1#S1
Certificate constructed and exactly checked on 2026-11-18.
No unproved results or numerical-optimization output are used as premises.
Run with standard Python 3.  No third-party dependencies.

Assume A is a correlation matrix.  Write A_{ij}=<v_i,v_j> and identify
a,b,c,d,e,f with 12,13,14,23,24,34 in increasing lexicographic order.
For an edge g=ij with complementary vertices k<l, set
T_g=A_ij v_k (tensor) v_l, S_g=(T_g+T_g^T)/sqrt(2),
W_g=(T_g-T_g^T)/sqrt(2).
Each of the following capital letters names a vector or scalar:
(A,B,C,D)=(S_a+S_f, S_b+S_e, S_c, S_d)
(E,F)=(S_a-S_f, S_b-S_e)
(G,H,I,J)=(W_a+W_f, W_b+W_e, W_c, W_d)
(K,L)=(W_a-W_f, W_b-W_e)
(X,Y,Z)=(af,be,cd).

In the table, row L of the first column denotes the squared norm of the
displayed linear form. The other 10 columns (s=-1,k=1..5, then
s=+1,k=1..5) are its nonnegative integer coefficients in 20 B_{s,k}.
Here B_{s,k} is the NORMALIZED degree-5 Bernstein coefficient, so
P'_A(s*t) = sum_{k=0}^5 comb(5,k)*B_{s,k}*t**k*(1-t)**(5-k).
In particular P'_A(s*t) is the derivative with respect to q evaluated
at q=s*t, not the derivative with respect to t.  Both coefficients with k=0 are
P'_A(0)=a^2+d^2+f^2.

Thus P'_A is nonnegative on [-1,1].  If A is non-diagonal and positive
definite this derivative is not the zero polynomial: with a,d,f not
all zero use P'_A(0); in the remaining case the lowest nonzero term is
3q^2(b^2+e^2) if b or e is nonzero and 5q^4 c^2 otherwise.
Integrating gives strict increase.  Positive diagonal congruence induces
a positive multiplicative factor on P_A, allowing normalization.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
import re

TABLE = """
D          10 0 4 0 0 5 1 2 8 0
C          0 0 0 0 0 0 0 0 0 52
C+D        0 0 0 2 0 0 0 0 0 0
B-C-D      0 0 0 8 0 0 0 0 0 0
B-D        0 3 0 0 0 0 0 0 0 0
B          0 0 0 0 0 0 1 0 0 0
B+D        0 0 0 0 0 0 1 1 2 4
B+C        0 0 0 0 0 0 0 0 0 20
B+C+D      0 0 0 0 0 0 0 0 0 7
A-B        0 0 4 2 0 0 0 0 0 0
A-D        0 5 0 0 0 0 0 0 0 0
A+D        0 0 0 0 0 5 8 5 0 0
A+B        0 0 0 0 0 0 0 6 5 0
A+B+D      0 0 0 0 0 0 0 0 2 0
A+B+C      0 0 0 0 0 0 0 0 6 12
F          0 0 0 0 10 0 0 0 8 0
E          8 0 0 0 0 7 6 2 0 0
E+F        0 0 0 0 0 0 0 2 0 0
J          2 4 0 4 0 7 5 6 2 0
I          0 0 0 4 0 0 0 0 14 0
H-2I       0 0 0 0 10 0 0 0 0 0
H-I-J      0 0 0 6 20 0 0 0 0 0
H-J        0 0 5 0 0 0 0 0 0 0
H          0 0 3 0 0 0 1 0 0 0
H+J        0 0 0 0 0 0 1 5 6 0
H+I+J      0 0 0 0 0 0 0 0 0 9
G-H+2I     0 0 0 0 10 0 0 0 0 0
G-J        8 8 11 0 0 0 0 0 0 0
G          2 0 1 0 0 2 0 0 0 0
G+J        0 0 0 0 0 3 4 1 0 0
G+H        0 0 0 0 0 0 1 0 0 0
L          0 3 2 4 0 0 0 0 0 0
K-L        0 0 4 16 10 0 0 0 0 0
K          2 7 0 2 0 3 0 0 0 0
K+L        0 0 0 0 0 0 1 4 7 8
Z          0 0 0 0 0 0 0 0 0 32
Y-Z        0 0 12 0 0 0 0 0 0 4
Y          0 0 0 0 0 0 4 4 8 20
Y+Z        0 0 0 0 0 0 0 4 4 0
X-Y        0 0 0 0 0 0 0 0 0 4
X-Z        0 4 0 0 0 0 0 0 0 0
X          0 0 0 0 0 0 0 4 20 28
"""

EDGES = dict(zip("abcdef", combinations(range(4), 2)))
NAMES = {pair: name for name, pair in EDGES.items()}
COMPLEMENT = {edge: sorted(set(range(4))-set(pair)) for edge,pair in EDGES.items()}

# Expand A, ..., L into elementary symmetric or alternating tensors.
BASE = (
    ("ABCDEF", 1, ("a+f","b+e","c","d","a-f","b-e")),
    ("GHIJKL",-1, ("a+f","b+e","c","d","a-f","b-e")),
    ("XYZ",    0, ("af","be","cd")),
)
LETTERS = {letter: (kind, elem) for alphabet,kind,elems in BASE
           for letter,elem in zip(alphabet,elems)}

def dot(i,j):
    return "" if i==j else NAMES[tuple(sorted((i,j)))]

def factors(expr):
    for sign,n,letter in re.findall(r"([+-]?)([0-9]*)([A-Za-z])",expr):
        yield (-1 if sign=="-" else 1)*int(n or "1"),letter

def canon(word):
    return "".join(sorted(word))

def square(expr):
    kind = LETTERS[next(factors(expr))[1]][0]
    terms = []
    for weight,letter in factors(expr):
        typ, expansion = LETTERS[letter]
        assert typ == kind
        if kind == 0:
            terms.append((weight,expansion))
        else:
            terms.extend((weight*a,e) for a,e in factors(expansion))
    poly = defaultdict(int)
    for a,e in terms:
        for b,f in terms:
            w = a*b
            if not kind:
                poly[canon(e+f)] += w
                continue
            k,l=COMPLEMENT[e]
            m,n=COMPLEMENT[f]
            poly[canon(e+f+dot(k,m)+dot(l,n))] += w
            poly[canon(e+f+dot(k,n)+dot(l,m))] += kind*w
    return poly

def bernstein_coeff(s,k):
    poly = defaultdict(Fraction)
    for perm in permutations(range(4)):
        length=sum(perm[i]>perm[j] for i,j in combinations(range(4),2))
        if length and length<=k+1:
            j = length-1
            word = canon("".join(dot(i,perm[i]) for i in range(4)))
            poly[word] += length * s**j * Fraction(comb(k,j),comb(5,j))
    return poly

def nonzero(poly):
    return {word:w for word,w in poly.items() if w}

def verify():
    columns = [defaultdict(int) for _ in range(10)]
    for row in TABLE.strip().splitlines():
        expr,*els = row.split()
        assert len(els)==10
        squared = square(expr)
        for column, mult in zip(columns, map(int,els)):
            assert mult>=0
            for word,w in squared.items():
                column[word] += mult*w
    for s in (-1,1):
        assert nonzero(bernstein_coeff(s,0))=={"aa":1,"dd":1,"ff":1}
        for k in range(1,6):
            col=k-1+(5 if s==1 else 0)
            expected={word:w*20 for word,w in bernstein_coeff(s,k).items()}
            assert nonzero(expected)==nonzero(columns[col]), (s,k)
    print("PASS: all 42 square forms have nonnegative integer weights.")
    print("PASS: all 12 normalized degree-5 Bernstein identities hold exactly.")
    print("PASS: the defining polynomial was expanded directly over all 24 permutations.")
    print("Arithmetic: Python integers and fractions.Fraction; no floating point.")

if __name__=="__main__":
    verify()
