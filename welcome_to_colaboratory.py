#1 question
import numpy as np
arr=[np.random.uniform(1,20) for i in range(15)]
print(arr)
amatrix=np.reshape(np.ravel(arr),(3,5))
print(np.shape(amatrix))
max_ind = np.argmax(amatrix, axis=1)
row_ind = np.arange(amatrix.shape[0])
multi_ind = np.array([row_ind, max_ind])
linear_ind = np.ravel_multi_index(multi_ind, amatrix.shape)
amatrix.reshape((-1))[linear_ind] = 0
print(amatrix)

#2 question
import numpy as np
arr=np.array([[1,3,5,7],[2,4,6,8],[10,20,30,40]],np.int32)
print(np.shape(arr))
print(type(arr))
print(arr.dtype)

#3 question
import numpy as np
from numpy import linalg as la
arr=np.array([[3,-2],[1,0]])
w,v=la.eig(arr)
print("eign values:",w)
print("eign vectors:",v)

#4question
import numpy as np
arr=np.array([[0,1,2],[3,4,5]])
a=np.trace(arr)
print("sum of diagonal elements is:",a)

#5 question
import numpy as np
arr=np.array([[1,2],[3,4],[5,6]])
amatrix=np.reshape(np.ravel(arr),(2,3))
print(amatrix)

#2(1) question
from matplotlib import pyplot as plt
slices = [22.2,17.6,8.8,8,7.7,6.7]
labels = ['Java','Python','PHP','JavaScript','C#','C++']
colors = ['#0000FF','#FFA500','#00FF00','#FF0000','#AF69EE','#964B00']
plt.pie(slices, labels=labels, colors=colors,autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.tight_layout()
plt.show()
