#importing all required module to the file
from Mitra import *

def solveLE(matrix,varList,rtList):
    'solveLE is a global function to solve system of linear equations using gauss elimination method.'
    '''This function first making matrix an upper triangular matrix and then solve for each variable. It uses gauss elimination
    method to do that. It will give error for below conditions:
    1. matrix is empty
    2. no. of row(s) or no. of column(s) of matrix is not same
    3. matrix is neither object of Matrix nor of SquareMatrix
    4. varList is not a list type or it is list type containing values other than string type
    5. varList size is not equal to the no. of row(s) of matrix or to the no. of column(s) of matrix
    6. rtList is not a list type or it is list type containing values other than int or float type
    7. rtList size is not equal to the size of varList'''
    if not (isinstance(matrix, Matrix)): 
        raise NoMatrixFoundError("matrix is not type a of 'Matrix' or 'SquareMatrix'")
    if matrix.isEmpty():
        raise EmptyMatrixError("system of linear equations must contains one equation.")
    if not(matrix.isSquareMatrix()):
        raise NoSquareMatrixError("matrix must be square matrix to solve system of linear equations.")
    if isinstance(varList, list):
        for every in range(0, len(varList)):
            if not(isinstance(varList[every], str)): 
                raise ValueError("variable(s) list must contain only str type value(s).")
    else:
        raise ValueError("varList must be of list type.")
    dimList = matrix.getDimension() 
    if dimList[0] != len(varList): 
        raise MatrixDimensionError("dimension of matrix must be equal to the size of variable list.")
    if isinstance(rtList, list):
        for every in range(0, len(rtList)): 
            if not(isinstance(rtList[every], (int, float))): 
                raise ValueError("right hand side value(s) of equaton(s) must be int or float type only.")
    else: 
        raise ValueError("rtList must be of list type.")
    if len(rtList) != len(varList): 
        raise MatrixDimensionError("dimension of matrix must be equal to the size of rtList.")
    for dig in  range(0, dimList[0]): 
        for row in range(dig+1, dimList[0]):
            if matrix[dig][dig] == 0:
                (matrix[row],matrix[dig]) = (matrix[dig],matrix[row])
                (rtList[row],rtList[dig]) = (rtList[dig],rtList[row])
                continue
            kConst = matrix[row][dig] / matrix[dig][dig] 
            for col in range(0, dimList[1]): 
                matrix[row][col] = matrix[row][col] - (matrix[dig][col] * kConst) 
            rtList[row] = rtList[row] - (rtList[dig] * kConst) 
    ansList = [] 
    for row in range(0, dimList[0]): 
        if row == 0: 
            ansList.append(rtList[dimList[0]-1] / matrix[dimList[0]-1][dimList[0]-1])
        else:
            for col in range(0, row+1): 
                if col == row: 
                    ansList.append(rtList[dimList[0]-1-row] / matrix[dimList[0]-1-row][dimList[0]-1-col])
                else: 
                    rtList[dimList[0]-1-row] = rtList[dimList[0]-1-row] - (matrix[dimList[0]-1-row][dimList[0]-1-col] * ansList[col])
    ansDict = {} 
    for item in range(0, dimList[0]): 
        ansDict[varList[item]] = ansList[dimList[0]-1-item] 
    return ansDict 
