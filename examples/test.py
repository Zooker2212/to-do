m = int(input("x eksenini giriniz"))

for i in range(m):
    for j in range(m):
        # Aşağıdaki komut sütunun başına ve sonuna X koy demek. Araları da '#' ile doldur demek
        if ( i == 0 or i == m-1 or j == 0 or j == m-1 or i == j or 
        j == (m - 1 - i)):
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()