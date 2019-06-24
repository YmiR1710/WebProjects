class Matrix:

    @staticmethod
    def transpose_matrix(m):
        return map(list, zip(*m))

    @staticmethod
    def transpose_matrix1(m):
        return [list(i) for i in zip(*m)]

    @staticmethod
    def get_matrix_minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    def get_matrix_determinant(self, m):
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        determinant = 0
        for c in range(len(m)):
            determinant += ((-1) ** c) * m[0][c] * self.get_matrix_determinant(self.get_matrix_minor(m, 0, c))
        return determinant

    def get_matrix_inverse(self, m):
        for i in m:
            if len(i) != len(m):
                return 0
        determinant = self.get_matrix_determinant(m)
        if len(m) == 2:
            return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant]]
        cofactors = []
        for r in range(len(m)):
            cofactor_row = []
            for c in range(len(m)):
                minor = self.get_matrix_minor(m, r, c)
                cofactor_row.append(((-1) ** (r + c)) * self.get_matrix_determinant(minor))
            cofactors.append(cofactor_row)
        cofactors = self.transpose_matrix(cofactors)
        cofactors = list(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c] / determinant
        return cofactors

    @staticmethod
    def matrix_multiplication(a, b):
        result = []
        result1 = []
        while len(a) > 0:
            d = 0
            a1 = a[:1:]
            c = True
            while d < len(a1):
                for x in b:
                    for x1 in x:
                        result.append(x1 * a1[0][d])
                    d = d + 1
            a.pop(0)
        result = [result[i:i + len(b[0])] for i in range(0, len(result), len(b[0]))]
        sum = 0
        while len(result) > 0:
            for X in range(len(result[0])):
                for Y in range(len(b)):
                    sum = sum + result[Y][X]
                result1.append(sum)
                sum = 0
            for s in range(len(b)):
                result.pop(0)
        result1 = [result1[i:i + len(b[0])] for i in range(0, len(result1), len(b[0]))]
        return (result1)

    @staticmethod
    def vector_matrix_multiplication(A, b):
        res = []
        for i in range(len(b)):
            s = 0
            for j in range(len(A)):
                s += b[j] * A[i][j]
            res.append(s)
        return res

    @staticmethod
    def gauss_jordan(m, eps=1.0 / (10 ** 10)):
        (h, w) = (len(m), len(m[0]))
        for y in range(0, h):
            maxrow = y
            for y2 in range(y + 1, h):
                if abs(m[y2][y]) > abs(m[maxrow][y]):
                    maxrow = y2
            (m[y], m[maxrow]) = (m[maxrow], m[y])
            if abs(m[y][y]) <= eps:
                return False
            for y2 in range(y + 1, h):
                c = m[y2][y] / m[y][y]
                for x in range(y, w):
                    m[y2][x] -= m[y][x] * c
        for y in range(h - 1, 0 - 1, -1):
            c = m[y][y]
            for y2 in range(0, y):
                for x in range(w - 1, y - 1, -1):
                    m[y2][x] -= m[y][x] * m[y2][y] / c
            m[y][y] /= c
            for x in range(h, w):
                m[y][x] /= c
        return True

    def inverse_solve(self, A, b):
        return self.vector_matrix_multiplication(self.get_matrix_inverse(A), b)

    def gauss_solve(self, A, b):
        m2 = [row[:] + [right] for row, right in zip(A, b)]
        return [row[-1] for row in m2] if self.gauss_jordan(m2) else None

    def get_pseudo_inverse(self, A):
        return self.matrix_multiplication(self.transpose_matrix1(A), self.get_matrix_inverse(self.matrix_multiplication(A, self.transpose_matrix1(A))))

    def pseudo_inverse_solve(self, A, b):
        try:
            return self.vector_matrix_multiplication(self.get_pseudo_inverse(A), b)
        except ZeroDivisionError:
            return None

A = [[1, 2], [3, 4]]
m = Matrix()
print(m.gauss_solve(A, [1, 2]))
