# 1. Import the numpy package under the name `np`
import numpy as np

##### DECLARING NUMPY ARRAYS #####

# 2. Use np.array(<list>) to convert the list below into a numpy array. The array should be saved in a variable. Then print both the list and the array.
a = [300, -200, 100, 0, -100, 200, -300]
st = np.array(a)
print(a)
print(st)

## The array method in numpy has an optional dtype argument which specifies the datatype each element should be. For the array above, it could be implemented using A = np.array(a, dtype=str) ##

# 3. Declare new arrays with different datatypes using the list from #2. Datatypes to use: str, float, np.int32, np.int8, np.uint32, np.uint8.

A = np.array(a, dtype = str) 
B = np.array(a, dtype = float)
C = np.array(a, dtype = np.int32)
D = np.array(a, dtype = np.int8)
E = np.array(a, dtype = np.uint32)
F = np.array(a, dtype = np.uint8)
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

# 4. Use np.zeros(<int>) to create a array of zeroes of size 10. This should be saved in a variable. Then print the array.

zzz = np.zeros(10)
print(zzz)


# 5. In your array of zeroes, change the fifth 0 to a 6. (remember how indexing works in lists?) Print the array.

zzz[4] = 6
print(zzz)

# 6. Use np.arange(<int>, <int>) to create an array with values ranging from 11 to 46. Print the array.

arr = np.arange(11, 47)
print(arr)

# 7. Reverse the array you created in #6. Print the array.

arr = arr[::-1]
print(arr)

# 8. Use <array>.reshape(<int>, <int>) to turn your array from #6 into a multidimensional 6x6 array. Print the array.

arr = arr.reshape(6,6)
print(arr)

# 9. Use np.random.random((<int>, <int>)) to create a 10x10 array with random values. Print the array.

rand = np.random.random((10, 10))
print(rand)

# 10. Use np.random.randint(<int>, <int>, size=(<int>, <int>)) to create a 3x3 array with random integers. Print the array.

randi = np.random.randint(1, 10, size = (3,3))
print(randi)

# 11. Use <array>.max() and <array>.min to identify the maximums and minimums of the arrays you created in #9 and #10. Print the results.

m1 = rand.max()
m2 = rand.min()
m3 = randi.max()
m4 = randi.min()
print(m1)
print(m2)
print(m3)
print(m4)

# 12. Use <array>.mean() to find the means of the two arrays you created in #9 and #10. Print the results.

avg1 = rand.mean()
avg2 = randi.mean()
print(avg1)
print(avg2)

# 13. Convert the following two lists into 2X3 arrays. (You will need to use np.array and .reshape)

a = [2, 3, 5, 7, 11, 13]
b = [3, 1, 4, 1, 5, 9]

x = np.array(a)
y = np.array(b)
x = x.reshape(2, 3)
y = y.reshape(2, 3)
print(x)
print(y)

# 14. Add the two arrays from #13 (<array> + <array>)

z = x + y
print(z)

# 15. Multiply both arrays from #13 by 10.

x = x * 10
y = y * 10
print(x)
print(y)