# (Dimas) >> Fungsi untuk menjalankan penataan elemen matriks
def sort_matrix(matrix, ascending=True):
    flattened_matrix = [element for row in matrix for element in row]
    flattened_matrix.sort(reverse=not ascending)
    sorted_matrix = []
    index = 0
    for _ in range(len(matrix)):
        row = []
        for _ in range(len(matrix[0])):
            row.append(flattened_matrix[index])
            index += 1
        sorted_matrix.append(row)
    return sorted_matrix
# (Hamid) >> Fungsi untuk menjalankan perhitungan sesuai opsi yang dipilih, di dalamnya juga menerapkan perulangan for
def perform_operation(matrix_A, matrix_B, operation):
    result = []
    for i in range(len(matrix_A)):
        row = []
        for j in range(len(matrix_A[0])):
            if operation == 1:  # Penjumlahan
                element = matrix_A[i][j] + matrix_B[i][j]
            elif operation == 2:  # Pengurangan
                element = matrix_A[i][j] - matrix_B[i][j]
            elif operation == 3:  # Perkalian
                element = sum(matrix_A[i][k] * matrix_B[k][j] for k in range(len(matrix_B)))
            else:  # Perkalian dengan skalar
                element = matrix_A[i][j] * matrix_B
            row.append(element)
        result.append(row)
    return result
