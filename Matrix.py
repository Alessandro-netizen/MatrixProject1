import numpy as np
np.linalg

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Enter a n by m matrix")
a11 = (input("Enter A11: "))
a12 = int(input("Enter A12: "))
a13 = int(input("Enter A13: "))
a21 = int(input("Enter A21: "))
a22 = int(input("Enter A22: "))
a23 = int(input("Enter A23: "))
a31 = int(input("Enter A31: "))
a32 = int(input("Enter A32: "))
a33 = int(input("Enter A33: "))
A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]) 
A_numeric = A.astype(np.float64)
print(A)
print(round((np.linalg.det(A_numeric))))