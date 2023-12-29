import numpy as np

# Array usage
print("ARRAY MANIPULATIONS")
print("")

print("ZERO MATRIX ", np.zeros([1, 2]))
print("UNIT MATRIX ", np.ones([1, 3]))

print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

print("1D ARRAY")
print("")

array_1d = np.array([1, 2, 3])
print("SLICE ARRAY\n", array_1d[0:1])
print("ARRAY DIMENSION\n", array_1d.ndim)
print("INDIVIDUAL ELEMENT SIZE\n", array_1d.itemsize)
print("DATATYPE\n", array_1d.dtype)
print("TOTAL ELEMENTS\n", array_1d.size)

print("")
print("****************************************************************************************")
print("****************************************************************************************")
print("")

print("2D ARRAY")
print("")

array_2d_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_2d_2 = np.array([[4, 5, 6], [7, 8, 9]])
print(array_2d_1)
print("SLICE ARRAY")
print(array_2d_1[1, 2], ",", array_2d_1[0:2, 2], ",", array_2d_1[-1, 0:2])
print(array_2d_1[:, 1:3])
print("")

print("ROW-COLUMN OPERATION")
print("MATRIX DIMENSION\n", array_2d_1.shape)
print("FLATTEN TO 1D ARRAY\n", array_2d_1.ravel())
print("ELEMENT ITERATION")
for cell in array_2d_1.flatten():
    print(cell)
print("ROW ITERATION: C-ORDER INDEX")
for index_row in np.nditer(array_2d_1, order='C'):
    print(index_row)
print("COLUMN ITERATION: FORTRAN-ORDER INDEX")
for index_col in np.nditer(array_2d_1, order='F', flags=['external_loop']):
    print(index_col)
print("TWO ARRAY ITERATION")
array_2d_1a = np.arange(12).reshape(3, 4)
array_2d_2a = np.arange(3, 15, 4).reshape(3, 1)
print(array_2d_1a, "\n", array_2d_2a)
print("RESULTANT ARRAY")
for x, y in np.nditer([array_2d_1a, array_2d_2a]):
    print(x, y)
print("AMEND VALUE")
array_2d_1_amend = array_2d_1
for index in np.nditer(array_2d_1_amend, op_flags=['readwrite']):
    index[...] = index * index
print(array_2d_1_amend)
print("")

print("MATHEMATICAL OPERATION")
print("ROW SUM ", array_2d_1.sum(axis=0))
print("COLUMN SUM ", array_2d_1.sum(axis=1))
print("TOTAL SUM ", array_2d_1.sum())
print("MINIMUM ELEMENT ", array_2d_1.min())
print("MAXIMUM ELEMENT ", array_2d_1.max())
print("")

print("SQUARE ROOT\n", np.sqrt(array_2d_1))
print("STANDARD DEVIATION ", np.std(array_2d_1))
print("")

print("MATRIX MANIPULATION")
print(array_2d_2)
bool_check = array_2d_2 > 4
print("CONDITION CHECK\n", bool_check)

array_2d_2[bool_check] = -1
print("ELEMENT RE-DEFINITION\n", array_2d_2)
print("")

print("STACK OPERATIONS")
matrix_1 = np.arange(6).reshape(3, 2)
matrix_2 = np.arange(6, 12).reshape(3, 2)
print("MATRIX 1\n", matrix_1)
print("MATRIX 2\n", matrix_2)
print("VERTICAL STACK\n", np.vstack((matrix_1, matrix_2)))
print("HORIZONTAL STACK\n", np.hstack((matrix_1, matrix_2)))
print("")

print("MATRIX SLICING")
matrix_3 = np.arange(30).reshape(2, 15)
print("MATRIX\n", matrix_3)
result_h = np.hsplit(matrix_3, 3)
result_v = np.vsplit(matrix_3, 2)
print("MATRIX H1\n", result_h[0])
print("MATRIX H2\n", result_h[1])
print("MATRIX H3\n", result_h[2])
print("MATRIX V1\n", result_v[0])
print("MATRIX V2\n", result_v[1])
print("")
