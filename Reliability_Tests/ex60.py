import sympy as sym
a, b = sym.symbols('a,b')
eq1 = sym.Eq(a*1000000**b, 119.54907)
eq2 = sym.Eq(a*1000**b, 405)
result = sym.solve([eq1, eq2], (a, b))
print(result)

'''
[(1372.03074854535, -0.176636273742481)] #these are the solutions for a,b
'''
