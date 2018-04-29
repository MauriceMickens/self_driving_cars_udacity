import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I


class Matrix(object):
    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return self[0]

        return self[0][0] * self[1][1] - self[0][1] * self[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total = 0.0

        for i in range(self.h):
            total = total + self[i][i]
        return total

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 2:
            swap_matrix = []
            swap_row1 = []
            swap_row1.append(self.g[1][1])
            swap_row1.append(self.g[0][1] * -1)
            swap_matrix.append(swap_row1)

            swap_row2 = []
            swap_row2.append(self.g[1][0] * -1)
            swap_row2.append(self.g[0][0])
            swap_matrix.append(swap_row2)

            inverse_matrix = []

            for i in range(len(swap_matrix)):
                new_row = []
                for j in range(len(swap_matrix[0])):
                    new_row.append((1 / self.determinant()) * swap_matrix[i][j])

                inverse_matrix.append(new_row)

            return Matrix(inverse_matrix)
        elif self.h == 1:
            return Matrix([1 / self[0]])

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transposed_matrix = [
            [-1, -1],
            [-1, -1]
        ]

        for i in range(len(self.g)):
            row = self.g[i]
            for j in range(len(row)):
                transposed_matrix[j][i] = row[j]

        return Matrix(transposed_matrix)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")
            #
        # TODO - your code here
        #
        new_matrix = []
        for i in range(self.h):
            row = self.g[i]
            new_row = []
            for j in range(len(row)):
                g1_ij = self.g[i][j]
                g2_ij = other.g[i][j]
                sum = g1_ij + g2_ij
                new_row.append(sum)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        new_matrix = []
        for i in range(self.h):
            row = self.g[i]
            new_row = []
            for j in range(len(row)):
                m_ij = self.g[i][j]
                neg = m_ij * -1
                new_row.append(neg)
            new_matrix.append(new_row)
        return Matrix(new_matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be subtracted if the dimensions are the same")
            #
        # TODO - your code here
        #
        new_matrix = []
        for i in range(self.h):
            row = self.g[i]
            new_row = []
            for j in range(len(row)):
                g1_ij = self.g[i][j]
                g2_ij = other.g[i][j]
                diff = abs(g1_ij - g2_ij)
                new_row.append(diff)
            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #
        if self.w != other.h:
            raise (ValueError, "Matrices can only be multiplied if Matrix A's width is the same as Matrix B's height")

        product_matrix = []
        for i in range(self.h):
            row = self.g[i]
            new_row = []
            total = 0
            incrementer = 0
            col_incrementer = 0
            while (incrementer < len(row) and col_incrementer < other.w):
                m1_ij = self[i][incrementer]
                m2_ij = other[incrementer][col_incrementer]
                product = m1_ij * m2_ij
                total = total + product
                incrementer = incrementer + 1
                if incrementer == len(row):
                    new_row.append(total)
                    incrementer = 0
                    total = 0
                    col_incrementer = col_incrementer + 1

            product_matrix.append(new_row)

        return Matrix(product_matrix)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            product_matrix = []
            for i in range(self.h):
                row = self.g[i]
                new_row = []
                for j in range(len(row)):
                    product = other * self[i][j]
                    new_row.append(product)
                product_matrix.append(new_row)

            return Matrix(product_matrix)
        else:
            raise (ValueError, "2nd parameter can not be a matrix.")