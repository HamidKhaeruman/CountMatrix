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
    if operation == 4:  # Perkalian dengan skalar
        matrix_choice = input("Pilih matriks yang akan dikalikan (A untuk matriks A, B untuk matriks B): ")
        scalar = float(input(f"Masukkan skalar untuk matriks {matrix_choice}: "))
        if matrix_choice == 'A':
            matrix = matrix_A
        elif matrix_choice == 'B':
            matrix = matrix_B
        else:
            print("Pilihan matriks tidak valid.")
            return result

        # Eksekusi Fungsi Perkalian Skalar
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                element = matrix[i][j] * scalar
                row.append(element)
            result.append(row)
    else:
        for i in range(len(matrix_A)):
            row = []
            for j in range(len(matrix_A[0])):
                if operation == 1:  # Penjumlahan
                    element = matrix_A[i][j] + matrix_B[i][j]
                elif operation == 2:  # Pengurangan
                    element = matrix_A[i][j] - matrix_B[i][j]
                elif operation == 3:  # Perkalian
                    element = sum(matrix_A[i][k] * matrix_B[k][j] for k in range(len(matrix_B)))
                row.append(element)
            result.append(row)
    return result

# (Hamid) >> Menambahkan Fungsi Determinan Hasil Matriks
def calculate_determinant(matrix):
    # Base case: Matriks 2x2
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    determinant = 0
    for c in range(len(matrix)):
        submatrix = [[matrix[r][col] for col in range(len(matrix)) if col != c] for r in range(1, len(matrix))]
        sub_determinant = calculate_determinant(submatrix)
        determinant += ((-1) ** c) * matrix[0][c] * sub_determinant
    
    return determinant

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


# (Rafli) Penentuan Kondisi Pemilihan Operasi dan Penentuan Opsi Pengurutan Elemen Matriks
# Proses operasi sesuai pilihan
if 1 <= choice <= 4:
    result = perform_operation(matrix_A, matrix_B, choice)
    if choice == 1:
        print("Hasil penjumlahan matriks:")
    elif choice == 2:
        print("Hasil pengurangan matriks:")
    elif choice == 3:
        print("Hasil perkalian matriks:")
    else:
        print("Hasil perkalian matriks dengan skalar:")
    print_matrix(result)

    # Pengurutan elemen matriks
    print("\nElemen matriks setelah diurutkan:")
    print("1. Secara ascending")
    print("2. Secara descending")
    print("3. Transpose matriks")
    print("4. Determinan matriks")
    sort_choice = int(input("Masukkan pilihan pengurutan (1/2/3/4): "))
    
    if sort_choice == 1:
        sorted_result = sort_matrix(result, ascending=True)
        print_matrix(sorted_result)
    elif sort_choice == 2:
        sorted_result = sort_matrix(result, ascending=False)
        print_matrix(sorted_result)
    elif sort_choice == 3:
        transposed_result = [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))]
        print("Hasil transpose matriks:")
        print_matrix(transposed_result)
    elif sort_choice == 4:
        if len(result) != len(result[0]):
            print("Matriks harus berbentuk persegi untuk menghitung determinan.")
        else:
            determinant = calculate_determinant(result)
            print("Determinan matriks:")
            print(determinant)
    else:
        print("Pilihan pengurutan tidak valid.")
else:
    print("Pilihan operasi tidak valid.")
