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
# (Prabu) >> Fungsi untuk menentukan panjang baris dan kolom matriks
def input_matrix(rows, cols):
    matrix = []
    print("Masukkan elemen matriks:")
    for i in range(rows):
        row = [float(input(f"Masukkan elemen matriks pada baris {i+1}, kolom {j+1}: ")) for j in range(cols)]
        matrix.append(row)
    return matrix
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
# (Prabu) >> Fungsi untuk mencetak baris dan kolom matriksnya  
def print_matrix(matrix):
    for row in matrix:
        print(*row)
# (Maulidya) >> User Menginput kriteria Matriks yang Akan Dibuat
# Input ukuran matriks
rows = int(input("Masukkan jumlah baris matriks: "))
cols = int(input("Masukkan jumlah kolom matriks: "))

# Input matriks A
print("Masukkan matriks A:")
matrix_A = input_matrix(rows, cols)

# Input matriks B
print("Masukkan matriks B:")
matrix_B = input_matrix(rows, cols)

# Pilihan operasi
print("Pilihan operasi:")
print("1. Penjumlahan matriks")
print("2. Pengurangan matriks")
print("3. Perkalian matriks")
print("4. Perkalian matriks dengan skalar")
choice = int(input("Masukkan pilihan operasi (1/2/3/4): "))
