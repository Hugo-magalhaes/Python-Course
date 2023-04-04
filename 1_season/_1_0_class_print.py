name = 'hugo'
years_old = 21
height = 1.78
weight = 56
imc = weight/(height**2)

print(f'{name} has {years_old} years old and imc {imc:.2f}')
# The format function follow the order you gave
print('{} has {} years old and imc {}'.format(name, years_old, imc))
# If you gave the order in keys the format fuction follow the order you gave
print('{2} kg/m^2 with {1} years old, {0}'.format(name, years_old, imc))
# Now they named in format function
print('{i} kg/m^2 with {d} years old, {n}'.format(n=name, d=years_old, i=imc))
