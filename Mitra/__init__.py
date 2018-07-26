#import all the matrix exception classes
from Mitra.MatErr import *

class Matrix:
    'This class is used for (n x m) matrix manipulation in math'
    def __init__(self): 
        self._row = 0 
        self._col = 0 
        self._list = [] 
    
    def insertValues(self):
        'This function take value from user and set it into list in the matrix format'
        self._list = list()
        print ("Enter no. of row(s) of matrix: ")
        self._row = int(input()) 
        if self._row == 0:
            raise MatrixRowError("no of row(s) of matrix can not be zero.")
        print ("Enter no. of coloumn(s) of matrix: ")
        self._col = int(input()) 
        if self._col == 0: 
            raise MatrixColumnError("no of column(s) of matrix can not be zero.")
        print ('Enter value of matrix: \n')
        for row in range(0, self._row):
            print ("\tEnter value of Row-",row+1, " - (every column value must be separated by space e.g. 3 5 5): ")
            value = input()
            values = list(value.split(' '))
            while '' in values:
                values.remove('')
            if (len(values) != self._col): 
                raise MatrixColumnError("no of values must equal to the no of column(s) of matrix.")
            rowValue = []
            try: 
                for temp in range(0, self._col): 
                    rowValue.append(float(values[temp]))
            except ValueError:
                raise MatrixValueError("matrix only except decimal or real number(s).")
            self._list.append(rowValue) 
    
    def __getitem__(self, key):
        'This is operator overloading of ([]) operator to access directly the value of Matrix object.'
        if (key < 0): 
            raise MatrixIndexError(" matrix is out of bound.") 
        if (self._row == 0): 
            raise EmptyMatrixError("matrix row and column size is not defined.")
        return self._list[key] 
    
    def __setitem__(self, key , data):
        'This is operator overloading of ([]) operator to change value of element(s) of the Matrix.'
        if (key < 0): 
            raise MatrixIndexError("matrix is out of bound.") 
        if (self._row == 0): 
            raise EmptyMatrixError("matrix row and column size is not defined.") 
        if isinstance(self.__getitem__(key), list): 
            if isinstance(data, list): 
                for z in range(0, len(data)): 
                    if not(isinstance(data[z], (int, float))): 
                        raise MatrixValueError("value of matrix is decimal or real number(s) only.")
                if (len(data) == self._col): 
                    self._list[key] = data 
                    return 
                else: 
                    raise MatrixColumnError("item(s) in input data is not equal to the no of column(s) of Matrix.")
            else: 
                raise MatrixValueError("row(s) of Matrix is always of list type.")
        if isinstance(data, (float, int)): 
            self._list[key] = data 
        else: 
            raise MatrixValueError("value of matrix is decimal or real number(s) only")
    
    def setDimension(self, row, col):
        'This function is to set dimension of n X m matrix by user. It will change matrix to zero matrix of row X col dimension.'
        self._row = row 
        self._col = col 
        self._list = [] 
        for i in range(0, self._row):
            rowList = [] 
            for j in range(0, self._col):
                rowList.append(0)
            self._list.append(rowList)
    
    def getDimension(self):
        'This function is to get dimension of matrix. It will return list of dimenstion where first element is no of row(s) and other is no of columnn(s)'
        dim = [] 
        dim.append(self._row) 
        dim.append(self._col) 
        return dim 
    
    def display(self):
        'This function show all the value of the list in matrix format.'
        if (len(self._list) == 0): 
            print("\n\tMatrix is empty now...\n")
            return 
        print ("\nMatrix contents: \n")
        for row in self._list: 
            print("\t", end='')
            for col in row: 
                print("%.2f" % col, "  ",end='  ')
            print ('')
    
    def __mul__(self, other):
        'This fuction is for multiplication of two matrices.Only multiply Matrix object with Matrix, float, int or long object. It returns object of Matrix which is resultant of multiplication of two matrices.'
        tempList = [] 
        if isinstance(other, (int, float)): 
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] * other) 
                tempList.append(rowList)
        elif isinstance(other, Matrix): 
            if (self._col != other._row): 
                raise MatrixMultiplicationError("no of column of first matrix must equal to the no of row of the second matrix error")
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, other._col):
                    rowList.append(0) 
                    temp = 0.0
                    for inc in range(0, self._col): 
                        rowList[col] += self._list[row][inc] * other._list[inc][col] 
                tempList.append(rowList)
        else:
            raise MatrixValueError('you can\'t multiply Matrix with ',other) 
        
        tempMat = Matrix()
        tempMat._list = tempList
        tempMat._row = len(tempList)
        if (len(tempList) > 0):
            tempMat._col = len(tempList[0])
        else:
            tempMat._col = 0
        return tempMat
    
    def __rmul__(self, other):
        'This fuction is for multiplication of two matrices.Only multiply Matrix object with Matrix, float, int or long object. It returns object of Matrix which is resultant of multiplication of two matrices.'
        tempList = [] 
        if isinstance(other, (int, float)): 
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] * other) 
                tempList.append(rowList)
        elif isinstance(other, Matrix):
            if (self._col != other._row): 
                raise MatrixMultiplicationError("MatrixMultiplicationError: no of column of first matrix must equal to the no of row of the second matrix error")
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, other._col):
                    rowList.append(0) 
                    temp = 0.0
                    for inc in range(0, self._col):
                        rowList[col] += self._list[row][inc] * other._list[inc][col]
                tempList.append(rowList)
        else:
            raise MatrixValueError('You can\'t multiply Matrix with ',other) 
        tempMat = Matrix() 
        tempMat._list = tempList
        tempMat._row = len(tempList) 
        if (len(tempList) > 0): 
            tempMat._col = len(tempList[0])
        else:
            tempMat._col = 0
        return tempMat
    
    def transpose(self):
        'This function is for calculating the transpose of n X m matrix.'
        trans = Matrix() 
        for col in range(0, self._col): 
            rowList = [] 
            for row in range(0, self._row):
                rowList.append(self._list[row][col]) 
            trans._list.append(rowList) 
        trans._row = self._col 
        trans._col = self._row 
        return trans 
    
    def __add__(self, other):
        'This is operator overloading of binary plus (+) oprator. It will be used to add two matrices.'
        tempList = [] 
        if isinstance(other, (int, float)):
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] + other)
                tempList.append(rowList)
        elif isinstance(other, Matrix):
            if ((self._row != other._row) or (self._col != other._col)):
                raise MatrixAdditionError("added matrix should be of same dimension.")
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] + other._list[row][col]) 
                tempList.append(rowList)
        else:
            raise MatrixValueError('you can\'t add Matrix with ',other) 
        tempMat = Matrix() 
        tempMat._list = tempList 
        tempMat._row = len(tempList) 
        if (len(tempList) > 0): 
            tempMat._col = len(tempList[0])
        else:
            tempMat._col = 0
        return tempMat 
    
    def __radd__(self, other):
        'This is operator overloading to prevent user to add matrix to the scalar.'
        raise MatrixAdditionError("matrix can not be added to the scalar.") 
    
    def __sub__(self, other):
        'This is operator overloading of binary minus (-) oprator. It will be used to subtract two matrices.'
        tempList = [] 
        if isinstance(other, (int, float)):
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] - other) 
                tempList.append(rowList)
        elif isinstance(other, Matrix):
            if ((self._row != other._row) or (self._col != other._col)):
                raise MatrixSubtractionError("matrix should be of same dimension for subtraction.")
            for row in range(0, self._row):
                rowList = [] 
                for col in range(0, self._col):
                    rowList.append(self._list[row][col] - other._list[row][col]) 
                tempList.append(rowList)
        else:
            raise MatrixValueError('you can\'t subtract ',other,' from matrix.') 
        tempMat = Matrix() 
        tempMat._list = tempList 
        tempMat._row = len(tempList) 
        if (len(tempList) > 0): 
            tempMat._col = len(tempList[0])
        else:
            tempMat._col = 0
        return tempMat 
    
    def __rsub__(self, other):
        'This is operator overloading to prevent user to subtract matrix from scalar value.'
        raise MatrixSubtractionError("matrix can not be subtracted from scalar.") 
    
    def __eq__(self,other):
        'This is operator overloading of equality comparision (==) operator to check if two matrices are equal or not.'
        if isinstance(other, Matrix): 
            if ((self._row != other._row) or (self._col != other._row)): 
                return False 
            for row in range(0, self._row):
                for col in range(0, self._col):
                    if self._list[row][col] != other._list[row][col]: 
                        return False 
            return True 
        else: 
            return False 
    
    def __ne__(self,other):
        'This is operator overloading of inequality comparision (!=) operator to check if two matrices are equal or not.'
        if isinstance(other , Matrix): 
            if ((self._row != other._row) or (self._col != other._row)): 
                return True 
            for row in range(0, self._row):
                for col in range(0, self._col):
                    if self._list[row][col] != other._list[row][col]: 
                        return True 
            return False 
        else: 
            return True 
    
    def isEmpty(self):
        'This function will check if matrix is empty or not. If it is empty it will return True else return False.'
        if self._row == 0:
            return True 
        else:
            return False 
    
    def isZeroMatrix(self):
        'This function is to check if matrix is zero matrix or null matrix. It will return True if matrix is zero matrix else returns false'
        if not(self.isEmpty()): 
            for row in range(0, self._row): 
                for col in range(0, self._col): 
                    if (self._list[row][col] != 0): 
                        return False 
            return True 
        else:
            return False 
    
    def __getIdentityMat(self, row, col):
        'This is private function used by system to get identity matrix of any dimension.It is only for Matrix not for Square Matrix'
        idMat = Matrix() 
        for i in range(0, row):
            rowList = [] 
            for j in range(0, col):
                if i == j: 
                    rowList.append(1) 
                else:
                    rowList.append(0) 
            idMat._list.append(rowList)
        idMat._row = row 
        idMat._col = col 
        return idMat 
    
    def __changeMat(self, li, row, col):
        'This is private function to select desired row(s) and column(s) of Square Matrix for determinant.'
        tempList = [] 
        for i in range(0, len(li)):
            rowList = [] 
            if i == row: 
                continue 
            else:
                for j in range(0, len(li)):
                    if j == col: 
                        continue 
                    else:
                        rowList.append(li[i][j]) 
                tempList.append(rowList) 
        return tempList 
    
    def __determinant(self, li):
        'This function will give determinant (|li| or det(li)) of Square Matrix'
        value = 0
        if (len(li) == 0):
            raise NoMatrixFoundError(" matrix doesn't exist.")
        elif (len(li) == 1): 
            value = li[0][0] 
            return value
        elif (len(li) == 2): 
            value = (li[0][0] * li[1][1]) - (li[0][1] * li[1][0])
            return value
        else: 
            for col in range(0, len(li)): 
                value += ((-1)**col) * (li[0][col]) * self.__determinant(self.__changeMat(li, 0, col))
            return value 
    
    
    def __stranspose(self, matrix):
        'This private function is for calculating the transpose of m X m matrix. It is only used by system not by user directly'
        trans = SquareMatrix() 
        for col in range(0, matrix._col): 
            rowList = [] 
            for row in range(0, matrix._row):
                rowList.append(matrix._list[row][col]) 
            trans._list.append(rowList) 
        trans._row = matrix._col 
        trans._col = matrix._row
        return trans 
    
    def determinant(self):
        'This function will give determinant (|A| or det(A)) of Square Matrix'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        value = 0
        if (self._row == 0): 
            raise NoMatrixFoundError("matrix doesn't exist.")
        elif (self._row == 1): 
            return self.list[0][0]
        elif (self._row == 2): 
            value = (self._list[0][0] * self._list[1][1]) - (self._list[0][1] * self._list[1][0])
            return value
        else: 
            for col in range(0, self._row): 
                value += ((-1)**col) * (self._list[0][col]) * self.__determinant(self.__changeMat(self._list, 0, col))
            return value 
        
    def minor(self):
        'This fuction is for calculating minor matrix of Square Matrix. It will raise error if matrix is not square matrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if (self._row <= 1): 
            raise MatrixMinorError(" minor of null matrix and 1D Square Matrix doesn't exist.") 
        minorList = [] 
        for row in range (0, self._row): 
            rowList = [] 
            for col in range (0, self._col): 
                rowList.append(self.__determinant(self.__changeMat(self._list, row, col))) 
            minorList.append(rowList) 
        minorMat = Matrix() 
        minorMat._list = minorList 
        minorMat._row = minorMat._col = len(minorList) 
        return minorMat
    
    def cofactor(self):
        'This function is for calculating cofactor of Square Matrix. It will raise error if matrix is not square matrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        factorList = [] 
        minor = self.minor() 
        for row in range(0, self._row):
            rowList = [] 
            for  col in range(0, self._row):
                rowList.append(((-1)**(row + col)) * minor._list[row][col])
            factorList.append(rowList)
        factorMat = SquareMatrix() 
        factorMat._list = factorList 
        factorMat._row = factorMat._col = len(factorList) 
        return factorMat 
    
    def adjoint(self):
        'This function will calculate adjoint matrix of any Square Matrix. It will return a adjoint SquareMatrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        adjoin = SquareMatrix()
        adjoin = self.__stranspose(self.cofactor()) 
        return adjoin
    
    def inverse(self):
        'This function will calculate inverse matrix of any Square Matrix. It well return a inverse Square Matrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if self.isSingular():
            raise SingularMatrixError("singular matrix encountered while calculating inverse of Square Matrix.")
        inverseMat = SquareMatrix() 
        inverseMat = (1/self.determinant()) * self.adjoint() 
        return inverseMat 
    
    def isOrthogonalMatrix(self):
        'This function is to check if matrix is orthogonal matrix or not. It will return true if matrix is orthogonal matrix else return false.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if not(self.isEmpty()): 
            if ((self * self.transpose()) == self.__getIdentityMat(self._row, self._col)): 
                return True 
            else:
                return False 
        else:
            return False 
    
    def isUTMatrix(self):
        'This function verify if matrix is upper triangular matrix or not. If matrix is upper triangular matrix, it will return True else returns false.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        for col in range(0, self._col): 
            for row in range(col+1, self._row): 
                if self._list[row][col] != 0: 
                    return False 
        return True 
    
    def isLTMatrix(self):
        'This function verify if matrix is lower triangular matrix or not. If matrix is lower triangular matrix, it will return True else returns False.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        for col in range(1, self._col): 
            for row in range(0, col): 
                if self._list[row][col] != 0: 
                    return False 
        return True 
    
    def isTMatrix(self):
        'This function verify if matrix is triangular matrix or not. If it is triangular matrix then it will return true else retrun false.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if (self.isLTMatrix() or self.isUTMatrix()): 
            return True 
        return False
    
    def trace(self):
        'This is function to calculate the trace of Square Matrix. It will return a value or trace of Square Matrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        trace = 0 
        for dig in range(0, self._row):
            trace += self._list[dig][dig] 
        return trace 
    
    def isSingular(self):
        'This function verif if matrix is singular matrix or not. If it is singular matrix then it will return true else it will return false.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if (self.determinant() == 0): 
            return True 
        return False
    
    def __pow__(self, power):
        'This is operator overloading of power (**) operator. This will calculate the power of matrix where power is only integer type and return the resultant square matrix.'
        if self._row != self._col: 
            raise NoSquareMatrixError("matrix is not square matrix")
        if not(isinstance(power, int)):
            raise MatrixPowerError("power of matrix must be of type int only.")
        tMat = self 
        if power < 0: 
            tMat = self.inverse() 
            power = 0 - power 
        plist = [] 
        if power == 0: 
            return self.__getIdentityMat(tMat._row, tMat._col) 
        if power == 1: 
            return tMat 
        if power == 2: 
            return tMat * tMat 
        while True:
            value = 2 
            templist = [] 
            if power == 1: 
                templist.append(1) 
                plist.append(templist) 
                break 
            if power == 0: 
                break 
            while True:
                if (value * 2) > power: 
                    templist.append(2) 
                    plist.append(templist) 
                    power = power - value 
                    break 
                else:
                    value = value * 2 
                    templist.append(2)
        resMat = [] 
        for row in range(0, len(plist)): 
            sqMat = tMat * tMat 
            for col in range(0, len(plist[row])): 
                if plist[row][col] == 2: 
                    if col == (len(plist[row]) -1): 
                        continue
                    sqMat = sqMat * sqMat 
                else: 
                    sqMat = tMat 
            resMat.append(sqMat) 
        powMat = SquareMatrix() 
        for row in range(0, len(resMat)): 
            if row == 0:
                powMat = resMat[row] 
            else: 
                powMat = powMat * resMat[row] 
    
    def isSquareMatrix(self):
        'This function will return True if matrix is square matrix otherwise return false.'
        if self._row == self._col:
            return True 
        return False 

class SquareMatrix (Matrix):
    'This class is used for Square Matrix manipulation and it is derived from Matrix'
    def insertValues(self):
        'This function takes values of matrix and store it in list'
	self._list = list()
        print("Enter dimension of square matrix:", ' ')
        self._row = int(input())
        if self._row == 0: 
            raise MatrixDimensionError("dimension of Square Matrix can not be zero.")
        self._col = self._row 
        print ('Enter value of matrix: \n')
        for row in range(0, self._row):
            print ("\tEnter value of Row-",row+1, " - (every column value must be separated by space e.g. 3 5 5): ")
            value = input() 
            values = list(value.split(' ')) 
            while '' in values:
                values.remove('')
            if (len(values) != self._col): 
                raise MatrixColumnError("no of values must equal to the no of column(s) of matrix.")
            rowValue = []
            try: 
                for temp in range(0, self._col):
                    rowValue.append(float(values[temp]))
            except ValueError:
                raise MatrixValueError(" matrix only except decimal or real number(s).")
            self._list.append(rowValue) 
    
    def setDimension(self, dim):
        'This function is to set dimension of n X m matrix by user.'
        self._row = dim 
        self._col = dim 
        for i in range(0, self._row):
            rowList = [] 
            for j in range(0, self._col):
                rowList.append(0)
            self._list.append(rowList)
