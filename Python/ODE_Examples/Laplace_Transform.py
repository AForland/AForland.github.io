from sympy import *
init_printing(use_unicode=False, wrap_line=False, no_global=True)

t = Symbol('t')
s = Symbol('s')
T = Symbol('T')
n = Symbol('n')

def Laplace(f):
    return integrate(exp(-s*t)*f,(t,0,oo), conds='none')

Laplace(sin(t))
