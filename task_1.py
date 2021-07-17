matrix_list = [
    [1, 2, 3],
    [3, 4, 5],
]
matrix_list_2 = [
    [1, 2, 3],
    [3, 4, 5],
]


class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix = matrix_list

    def matrix_walk(self, matrix_list: list):
        for i in matrix_list:
            if isinstance(i, list):
                self.matrix_walk(i)
            else:
                print(i, end='\t', )
        print('')

    def add(self, first_matrix: list, second_matrix: list):
        row = []
        for i, j in zip(first_matrix, second_matrix):
            if isinstance(i, list):
                if isinstance(j, list):
                    row.append(self.add(i, j))
                else:
                    print('Матрицы должны быть одинаковыми')
                    exit(1)
            else:
                row.append(i + j)
        return row

    def __add__(self, other):
        return self.add(self.matrix, other.matrix)

    def __str__(self):
        self.matrix_walk(self.matrix)
        return 'Регулярное представление матрицы'


matrix = Matrix(matrix_list)
matrix_2 = Matrix(matrix_list_2)

print(matrix)
new_matrix = matrix + matrix_2
print(new_matrix)
