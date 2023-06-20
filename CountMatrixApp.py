

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
