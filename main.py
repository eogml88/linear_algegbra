import functions.functions as f


A = [
        [1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]
    ]

print(f'A: {A}')
print('transpose of A: ')
print(*f.transpose(A),sep='\n',end='\n\n') # import numpy as np;print(np.transpose(A)) # import numpy as np;print(np.array(A).T)

print('matmul of A and transpose of A: ')
print(*f.matmul(A,f.transpose(A)),sep='\n',end='\n\n') # import numpy as np;print(np.matmul(A,np.array(A).T))

print('diagonlized A: ')
print(*f.diag(A),sep='\n',end='\n\n') # import numpy as np;print(np.diag(np.diag(A)))

print('diagonal elements of A: ')
print(f.diag_ele(A),end='\n\n') # import numpy as np;print(np.diag(A))

print('diagonal matrix from diagonal elements of A: ')
print(*f.ele2diag(f.diag_ele(A),3,4),sep='\n',end='\n\n') # import numpy as np;print(np.diag(np.diag(A)))

E = [1,10,1]

print(f'E: {E}')
print('a diagonal matrix D made from E: ')
print(*f.ele2diag(E),sep='\n',end='\n\n') # import numpy as np;print(np.diag(E))

print('matmul of A and D: ')
print(*f.matmul(A,f.ele2diag(E)),sep='\n',end='\n\n') # import numpy as np;print(np.matmul(A,np.diag(E)))

print('matmul of D and A: ')
print(*f.matmul(f.ele2diag(E),A),sep='\n',end='\n\n') # import numpy as np;print(np.matmul(np.diag(E),A))

print('identity matrix of size A: ')
print(*f.identity(len(A)),sep='\n',end='\n\n') # import numpy as np;print(np.identity(A))

print('zero matrix of size A: ')
print(*f.zero(len(A)),sep='\n',end='\n\n') # import numpy as np;print(np.zeros((len(A),len(A[0]))))

print('upper triangular matrix of A: ')
print(*f.triu(A),sep='\n',end='\n\n') # import numpy as np;print(np.triu(A))

print('lower triangular matrix of A: ')
print(*f.tril(A),sep='\n',end='\n\n') # import numpy as np;print(np.tril(A))

P=[1, 0, -1, -2, -3]
T=[1, 2, 3, 4]

print(f'P: {P}')
print(f'T: {T}')
print(f'a Toeplitz matrix A made from P and T: ') 
print(*f.toeplitz(P, T),sep='\n',end='\n\n') # from scipy.linalg import toeplitz;print(toeplitz(P,T))

print('upper bidiagonal matrix of A: ')
print(*f.bidiagu(A),sep='\n',end='\n\n') # import numpy as np;print(np.diag(np.diag(A)) + np.diag(np.diag(A,k=1),k=1))

print('lower bidiagonal matrix of A: ')
print(*f.bidiagl(A),sep='\n',end='\n\n') # import numpy as np;print(np.diag(np.diag(A)) + np.diag(np.diag(A,k=1),k=1))

V=[1, 0, 2, 3]

print(f'V: {V}')
print(f'a householder matrix H made from vector V: ') 
print(*f.householder(V),sep='\n',end='\n\n') # import numpy as np;print(np.identity(len(V)) - (2/np.inner(V,V))*np.outer(V,V))