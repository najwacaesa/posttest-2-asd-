#program ini digunakan untuk mencari index dari elemen yang ingin kita cari
#disini saya menggunakan jump search untuk melakukan searching

import os  #disini ada import os yang berfungsi untuk menghapus output sebelumnya agar tampilan output lebih rapih
os.system('cls')

def jump_search(arr, x): # disini ada fungsi jumpsearch yang memiliki elemen arr dan x
    n = len(arr) # pertama saya mendefinisikan n yaitu panjang data 

    # untuk mengitung ukuran lompatan optimal
    jump_size = int(n ** 0.5) 
    
    # menemukan blok yang berisi elemen x
    block_start = 0 #untuk blok awal kita definisikan pada index 0
    block_end = jump_size #dan untuk blok akhir didefinisikan sama dengan jarak lompatan
    while block_end < n and arr[block_end] <= x:
        block_start = block_end
        block_end += jump_size
    
    # mencari linier di blok yang berisi x
    for i in range(block_start, min(block_end, n)):
        if arr[i] == x:
            return i

arr = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Mencari posisi data Arsel
arsel = jump_search(arr, "Arsel") 
print("1. Arsel di Index {}" .format(arsel))

# Mencari posisi data Avivah
avivah = jump_search(arr, "Avivah")
print("2. Avivah di Index {}".format(avivah))

# Mencari posisi data Daiva
daiva = jump_search(arr, "Daiva")
print("3. Daiva di Index {}" .format(daiva))

# Mencari posisi data Wahyu di kolom 0
wahyu = jump_search(arr[3], "Wahyu")
print("4. Wahyu di Index {} pada kolom 0".format(wahyu + 3))

# Mencari posisi data Wibi di kolom 1
wibi = jump_search(arr[3], "Wibi")
print("5. Wibi di Index {} pada kolom 1".format(wibi + 2))