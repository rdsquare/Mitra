#all exceptions used
class MatrixRowError(IndexError):
    'used for index error in row of matrix.'
    pass
class MatrixColumnError(IndexError):
    'used for index error in column of matrix.'
    pass
class MatrixValueError(ValueError):
    'used for value error in matrix.'
    pass
class MatrixIndexError(IndexError):
    'used for index error while using [] for matrix.'
    pass
class EmptyMatrixError(Exception):
    'used for empty matrix.'
    pass
class MatrixMultiplicationError(Exception):
    'used to show error while multiplication of matrix.'
    pass
class MatrixAdditionError(Exception):
    'used to show error while addition of matrix.'
    pass
class MatrixSubtractionError(Exception):
    'used to show error while subtraction of matrix.'
    pass
class MatrixDimensionError(IndexError):
    'used to show error in dimension of Square matrix.'
    pass
class NoMatrixFoundError(Exception):
    'used to show error when matrix is empty while operation.'
    pass
class MinorMatrixError(ValueError):
    'used to show error encountered while calculating minor.'
    pass
class SingularMatrixError(ValueError):
    'used to show error when singular matrix is encountered while any operation.'
    pass
class MatrixPowerError(ValueError):
    'used to show error when power is not integer while calculating power of matrix.'
    pass
class NoSquareMatrixError(Exception):
    'used to show error when matrix is not square matrix.'
    pass
