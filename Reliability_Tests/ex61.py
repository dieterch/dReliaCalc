import sympy as sym
x, y, z = sym.symbols('x,y,z')
c1 = sym.Symbol('c1')
eq1 = sym.Eq(2*x**2+y+z, 1)
eq2 = sym.Eq(x+2*y+z, c1)
eq3 = sym.Eq(-2*x+y, -z)
result = sym.solve([eq1, eq2, eq3], (x, y, z))
print(result)

'''
[(-1/2 + sqrt(3)/2, c1 - 3*sqrt(3)/2 + 3/2, -c1 - 5/2 + 5*sqrt(3)/2), (-sqrt(3)/2 - 1/2, c1 + 3/2 + 3*sqrt(3)/2, -c1 - 5*sqrt(3)/2 - 5/2)]
'''
