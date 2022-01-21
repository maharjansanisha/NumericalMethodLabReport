# Linear interpolation in python

# Reading first point
print('Enter first point:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

# Reading second point
print('Enter second point:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

# Reading calculation point
xp = float(input('Enter calculation point xp: '))

# Calculating interpolated value
yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)

# Displaying result
print('Interpolated value at %0.4f is %0.4f' %(xp,yp))