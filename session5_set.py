### SET ####
## Selalu dinotasikan sebagai {}
## Fungsinya melihat kumpulan data unique
## Set tidak bisa dilakukan indexing

## CREATE
cobaSet = {'Justin', 'Nur', 'There', 'Reza', 'Nur'}
print(cobaSet)

cobaSet1 = {'Justin', 'Nur', 'There', 'Reza', 'nur'}
print(cobaSet1)

cobaSet2 = {1, 1, 10, 4, 5, 5, 9, 0, 2}
print(cobaSet2)

## READ
# Set tidak bisa dilakukan indexing
print(cobaSet[0])

for value in cobaSet:
    print(value)

setTimSepakBola= {'Real Madrid', 'Chelsea', 'Liverpool', 'PSG'}

print('PSG' in setTimSepakBola)

if 'Persebaya' in setTimSepakBola:
    print("Ya, tim PSG ada")
else:
    print("Tidak ada")

## UPDATE
cobaAngka = {0, 3, 2, 5, 4}
print(cobaAngka)

# menambahkan 1 nilai baru
cobaAngka.add(99)
print(cobaAngka)

# menambahkan lebih dari 1 nilai baru
cobaAngka.update({7, 6})
print(cobaAngka)

## DELETE
cobaFilm = {'Jumbo', 'The Avengers', 'Fantastic Four', 'Thunderbolts'}
print(cobaFilm)

# perbedaan penggunaan remove() dan discard()
# remove() akan muncur error jika value yang ingin dihapus tidak ada
# sebaliknya, discard() tidak memunculkan error jika value yang ingin dihapus tidak ada

cobaFilm.remove('Jumbo') # menghapus nilai 'Jumbo' dari set
print(cobaFilm)

cobaFilm.discard('The Avengers') # menghapus nilai 'The Avengers' dari set
print(cobaFilm)

cobaFilm.clear()
print(cobaFilm)

## SET OPERATION
# JOIN
# JOIN menggabungkan seluruh isi dua set
setBilanganGanjil = {1, 3, 5, 7, 9}
setBilanganPrima = {1, 2, 3, 5, 7}

print(setBilanganGanjil.union(setBilanganPrima))

setTimInggris = {'Chelsea', 'Arsenal', 'Liverpool'}
setTimItalia = {'AC Milan', 'Inter Milan', 'AS ROMA'}

print(setTimInggris.union(setTimItalia))

# DIFFERENCE
setBilanganGanjil = {1, 3, 5, 7, 9}
setBilanganPrima = {1, 2, 3, 5, 7}

# anggota set yang ada di setBilanganGanjil namun tidak ada di setBilanganPrima

# difference() tidak akan mengubah isi variabel yang lama
setBilanganBaru = setBilanganGanjil.difference(setBilanganPrima)
print(setBilanganBaru)
print(setBilanganGanjil)

# difference_update() akan mengubah isi variabel yang lama
setBilanganGanjil.difference_update(setBilanganPrima)
print(setBilanganGanjil)

# SYMMETRIC DIFFERENCE
setBarisBilangan = {2, 4, 6, 8}
setBarisBilangan2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

cobaSymmetriDifference = setBarisBilangan.symmetric_difference(setBarisBilangan2)
print(cobaSymmetriDifference)

setBarisBilangan.symmetric_difference_update(setBarisBilangan2)
print(setBarisBilangan)

# INTERESECTION
setBarisBilangan = {2, 4, 6, 8}
setBarisBilangan2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

cobaIntersection = setBarisBilangan.intersection(setBarisBilangan2)
print(cobaIntersection)
