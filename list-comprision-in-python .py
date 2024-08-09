"""list comprision in python """
square =[ i*i for i in range(1,6)]
print(square)



prime =  [(i*i) for i in range(1,11) if i % 2 != 0]
print(prime)

prime_with_if_else = [[i//i , i%i] if i % 2 == 0 else [(i*i) for i in range(1,11) if i % 2 != 0] for i in range(1, 11)]
print(prime_with_if_else)

string = "ishu"

st= [i.capitalize() for i in string]
print(st)

st = [i.upper() for i in string if i=="i"]
print(st)

st = [i if i == "i" else "x" for i in string]
print(st)

var = [111,2,3,4,5,6,7,8]
var.sort()
print(var)

"""     lambda  """

square = lambda x: x*x
print(square(5))


# x = lambda a:[i*i for i in a]
x = lambda a:[(i ,i*i) if i%2==0 else i for i in a]
print(x([1,2,3,4,5,6]))


x= lambda a,b,c :[ (i , i*i) if i%b == 0 else c for i in a]
print(x([1,2,3,4,5,6],2,0))




def myfunc(n):
  return lambda a,b,c :[ (i , i*i) if i%b == 0 else c*n for i in a]*1

print(myfunc(3)([1,2,3,4,5,6],2,1))
