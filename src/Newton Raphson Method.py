#defining a function
def f(x):
    return x**2 - 4*x + 1

#first derivative 
def g(x):
    return 2*x - 4

#implementing Newton Raphson Method
def newtonRaphson(x0,e,N):
    print('\n Newton Raphson Method')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error !')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\n Required root is: %0.8f' % x1)
    else:
        print('\n Not Convergent.')


#input 
x0 = input('Enter initial assumption: ')
e = input('Tolerable Error: ')
N = input('Maximum iterations: ')

#converting x0 and e to float
x0 = float(x0)
e = float(e)

#converting N to integer
N = int(N)

#applying newton raphson method
newtonRaphson(x0,e,N)