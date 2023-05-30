## Project Capstone_1
# Project Portofolio Saham
# Header untuk setiap menampilkan list saham
header = [
    'Kode saham',                   # index 0 dalam list saham
    'Quantity Saham (lot)',         # index 1 dalam list saham
    'last price (Rp/lbr)',          # index 2 dalam list saham
    'Harga Average',                # index 3 dalam list saham
    'Total value (Rp)',             # index 4 dalam list saham
    'Total Profit/Loss (Rp)'        # index 5 dalam list saham
    ]

header2 = ['Kode saham', 'Quantity Saham (lot)', 'last price (Rp/lbr)', 'Total value (Rp)']

# List Saham default yang akan terupdate setelah ada transaksi
# Primary key pada list ini adalah kode saham pada indeks 0, yang merupakan 4 huruf kapital
saham = [
    ['TLKM',30,4000,3570,10710000,1290000],
    ['BBNI',30,3300,3070,9210000,690000],
    ['BBRI',30,2600,2470,7410000,390000],
    ['BBCA',50,7800,9000,45000000,-6000000],
    ['ANJT',50,800,900,4500000,-500000]
    ]

# Format tampilan yang akan digunakan pada program menu
formatTampilan = "{:<23}" * len(saham[0])
formatTampilan2 = "{:<23}" * (len(saham[0])-1)
formatTampilan3 = "{:<23}" * (len(header2))

# Uang kas
uang = 0

# Keuntungan/Kerugian yang terealisasi
realizedPL = 0

# Program ini menampilkan tampilan menu utama dan user harus memasukkan pilihan menu yang akan dipilih
# Pilihan akan selalu tampil selama user tidak memasukkan input 7. Hal ini dimaksudkan
# agar user dapat terus mengeksplor berbagai fitur tanpa harus keluar dari program.
# pilihan setiap menu akan masuk ke sub program masing-masing
def programCapstone() :
    while True :
        print('                                   Menu Portofolio Saham                                    ')
        print('============================================================================================')
        print('Pilihan menu yang tersedia : ')
        print('============================================================================================')
        print('Menu 1 : Menampilkan, sorting, dan filter list Portofolio saham')                                # Fitur read + filter + sorting
        print('Menu 2 : Membeli saham baru (menambah list portofolio saham)')                                   # fitur create
        print('Menu 3 : Mengupdate harga saham terbaru')                                                        # fitur update berdasarkan harga   
        print('Menu 4 : Mengubah jumlah kepemilikan saham yang sudah ada (mengupdate list portofolio saham)')   # fitur update berdasarkan harga dan jumlah lot
        print('Menu 5 : Menjual saham (Menghapus list portofolio saham)')                                       # fitur delete
        print('Menu 6 : Top up cash untuk beli saham')
        print('Menu 7 : Keluar dari program')
        print('============================================================================================')
        menu = input('Masukkan angka Menu yang diinginkan: ')
        print()

        if (menu == '1'):
            menu1()
        elif (menu == '2'):
            menu2()
        elif (menu == '3'):
            menu3()
        elif (menu == '4'):
            menu4()
        elif (menu == '5'):
            menu5()
        elif (menu == '6'):
            menu6()
        elif (menu == '7'):
            print('Terima kasih telah menggunakan program ini, have a nice day!')
            break
        else:
            print('Masukan anda salah, mohon input angka sesuai menu yang tersedia')
            continue


# fungsi untuk menghitung kevalidan transaksi saat ingin membeli saham
# masukannya a adalah uang yang dimiliki di rekening, sedangkan b adalah total harga saham yg ingin dibeli
def selisihUang(a,b) :
    selisihUang = abs(a-b)
    if a >= b :
        print(f'Transaksi berhasil, sisa uang anda adalah {selisihUang}')
        print()
    else :
        print(f'Transaksi tidak berhasil, kekurangan uang anda sebesar {selisihUang}, silahkan top up pada menu 6 agar dapat membeli saham')
        print()

# Fungsi ini akan menanyakan apakah user yakin dengan pilihannya
def yakinBertransaksi(a) :
    if a == 'Y' :
        print()
    elif a == 'T' : 
        print('Transaksi tidak jadi dilakukan')
        print()
    else :
        print('Keyword tidak sesuai, untuk alasan keamanan transaksi dibatalkan')
        print()



# Fungsi ini adalah fungsi untuk menampilkan list saham baik sebelum maupun setelah diupdate
# Fungsi ini menggunakan formatting yang telah diatur, kemudian memprint header
# Fungsi ini juga memprint semua list saham dengan menggunakan pengulangan for dengna formatting yg telah diatur
# Fungsi ini juga berfungsi untuk menampilkan total aset, total floating profit loss, total realized profit loss, dan total uang
def tampilkanSaham(list1) :
    # format penulisan agar sejajar
    print(formatTampilan.format(*header))
    for i in range(len(list1)) :
        print(formatTampilan.format(*list1[i]))
    print()
    totalInvestment = 0
    totalPL = 0
    for i in range(len(list1)) :
        totalInvestment += list1[i][4]
        totalPL += list1[i][5]
    print(f'Total aset saham adalah {totalInvestment} rupiah')
    print(f'Total floating profit/loss anda adalah {totalPL} rupiah')
    print(f'Total realized profit/loss anda adalah {realizedPL} rupiah')
    print(f'Total cash yang anda punya sekarang : {uang} rupiah')
    print()
    # Jika seandainya saham kosong, akan mengeluarkan keluaran sebagai berikut :
    if len(saham) == 0 :
        print('Portofolio anda kosong, silahkan isi dengan membeli saham')
        print()


# Fungsi sorting ini berfungsi untuk melakukan sorting dengan parameter sesuai dengan keinginan user
# Fungsi ini memakai looping while true yang tidak akan berhenti sampai user memasukkan input 5 kedalam menu  
def sortingSaham() :
    while True :
        print('======================== Menu Sorting ==============================')
        print('1. Sorting berdasarkan kode saham')
        print('2. sorting berdasarkan jumlah lot')
        print('3. sorting berdasarkan total value')
        print('4. sorting berdasarkan potential Profit/Loss')
        print('5. Kembali ke menu 1')
        inputPilihanSorting = input('Masukkan angka menu yang mau dijalankan : ')
        print()
        if inputPilihanSorting == '1' :
            listSahamBaru = sorted(saham, key = lambda x: x[0])
            tampilkanSaham(listSahamBaru)

        elif inputPilihanSorting == '2' :
            listSahamBaru = sorted(saham, key = lambda x: x[1])
            tampilkanSaham(listSahamBaru)

        elif inputPilihanSorting == '3' :
            listSahamBaru = sorted(saham, key = lambda x: x[4])
            tampilkanSaham(listSahamBaru)
        
        elif inputPilihanSorting == '4' :
            listSahamBaru = sorted(saham, key = lambda x: x[5])
            tampilkanSaham(listSahamBaru)

        elif inputPilihanSorting == '5' :   
            break 
        else :
            print('Masukan anda salah, mohon masukan pilihan yang benar')
            print()
            continue

# Fungsi filter ini berfungsi untuk melakukan filter dengan parameter sesuai dengan keinginan user
# Fungsi ini membutuhkan input dari user berupa pembatas untuk filter, dan input tersebut harus integer
# Jika input tidak integer, maka fungsi akan kembali ke menu filter
# Fungsi ini memakai looping while true yang tidak akan berhenti sampai user memasukkan input 4 kedalam menu  
def filterSaham() :
    while True :
        print('======================== Menu Filter ==============================')
        print('1. filter berdasarkan total value')
        print('2. filter berdasarkan jumlah lot')
        print('3. filter berdasarkan floating profit/loss')
        print('4. Kembali ke menu 1')
        inputPilihanFilter = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihanFilter == '1' :
            totalValue = input('Masukkan Total value minimum yang akan ditampilkan (rupiah) : ')
            if totalValue.isdigit() == True :
                totalValue = int(totalValue)
            else :
                print('Masukan harus berupa angka positif')
                print()
                continue
            print(formatTampilan.format(*header))
            for i in range(len(saham)) :
                if saham[i][4] >= totalValue :
                    print(formatTampilan.format(*saham[i]))
            print()

        elif inputPilihanFilter == '2' :
            totalLot = input('Masukkan jumlah lot minimum yang akan ditampilkan (lot) : ')
            if totalLot.isdigit() == True :
                totalLot = int(totalLot)
            else :
                print('Masukan harus berupa angka positif')
                print()
                continue
            print(formatTampilan.format(*header))
            for i in range(len(saham)) :
                if saham[i][1] >= totalLot :
                    print(formatTampilan.format(*saham[i]))
            print()

        elif inputPilihanFilter == '3' :
            totalPL = input('Masukkan jumlah keuntungan minimum yang akan ditampilkan (rupiah) : ')
            if totalPL.isdigit() == True :
                totalPL = int(totalPL)
            elif totalPL[0] == '-' and totalPL[1:].isdigit() :
                totalPL = int(totalPL)
            else :
                print('Masukan harus berupa angka')
                print()
                continue
            print(formatTampilan.format(*header))
            for i in range(len(saham)) :
                if saham[i][5] >= totalPL :
                    print(formatTampilan.format(*saham[i]))
                    print()

        elif inputPilihanFilter == '4' :   
            print()
            break 
        else :
            print('Masukan anda salah, mohon masukan pilihan yang benar')
            print()
            continue


# Fungsi ini akan menampilkan tampilan menu 1 setelah user mengkonfirmasi apakah akan menggunakan data default 
# atau menggunakan data baru untuk kemudian diolah selama program berjalan
# Pilihan akan selalu tampil dan akan kembali ke menu utama ketika user menginput angka 5 
# Hal ini dimaksudkan agar user dapat terus mengeksplor berbagai fitur tanpa harus keluar dari program.
# Pilihan 1,3,4 akan masuk ke fungsi-fungsi diatas, sedangkan pilihan 2 akan menampilkan list saham tertentu yang dipilih user
def templateMenu1() :
    while True :
        print('======================== Menu 1 ==============================')
        print('1. Menampilkan seluruh portofolio')
        print('2. Menampilkan kode saham yang diinginkan')
        print('3. Menampilkan kode saham yang disorting')
        print('4. Menampilkan kode saham yang difilter')
        print('5. Kembali ke menu utama')
        inputPilihan1 = input('Masukkan angka menu yang mau dijalankan : ')

        if inputPilihan1 == '1' :
            print()
            tampilkanSaham(saham)
        elif inputPilihan1 == '2' :
            kodeSaham = input('Masukkan kode saham yang ingin ditampilkan : ').upper()
            print()
            count = 0
            while count < len(saham) :
                if kodeSaham == saham[count][0] :
                    print(formatTampilan.format(*header))
                    print(formatTampilan.format(*saham[count]))
                    print()
                    break
                else :
                    count += 1
            else :
                print('Kode Saham tidak tersedia')
                print()
                continue
        elif inputPilihan1 =='3' :
            print()
            sortingSaham()
        elif inputPilihan1 =='4' :
            print()
            filterSaham()    
        elif inputPilihan1 == '5' :
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue

# Fungsi menu 1 ini adalah fungsi templateMenu1 dengan fitur tambahan, yakni bertanya kepada user
# apakah ingin menggunakan database yang sudah ada atau ingin membuat portofolio sendiri
# apabila memilih portofolio sendiri, maka list saham akan dihapus semuanya 
# jika data kosong, user harus mengisinya dengan cara : membeli saham pada menu 2 dan 4
def menu1() :
    # Memberikan pilihan ke user apakah mau memakai portofolio yang sudah ada atau membuat portofolio baru
    pertanyaan = input('Apakah ingin menggunakan portofolio yang sudah ada (Y/T) : ').upper()
    if pertanyaan == 'Y':
        print()
        templateMenu1()       
    elif pertanyaan == 'T':

        print(formatTampilan.format(*header))
        # melakukan clear pada list saham agar dapat diinput sesuai kebutuhan user
        saham.clear()
        print('Portofolio anda kosong, silahkan isi dengan membeli saham')
        print()
    else :
        # Memakai fungsi rekursif sampai inputnya benar
        print('Tolong masukkan input yang benar (Y/T)')
        menu1()
        
# Menu 2 adalah fungsi untuk membeli saham baru yang tidak terdapat pada portofolio saham user sebelumnya
# Jika user memutuskan untuk membeli, user harus memberikan kode saham unik sesuai format, harga beli saat itu, dan Qty saham
# masukan harga beli dan Qty saham harus berupa integer, jika tidak maka akan kembali ke halaman Menu 2
# User hanya dapat membeli apabila uang yang dimiliki cukup, jika tidak maka akan diminta top up ke menu 6
# Setelah mengisi data pembelian, user akan ditanya konfirmasi apakah yakin akan membeli
# Jika jawaban ya, maka saham yang baru dibeli akan masuk ke list saham dan uang akan berkurang, dan list saham ditampilkan
# Program akan terus looping sampai user menginput pilihan 2 untuk kembali ke menu utama
def menu2() :
    global uang
    while True :
        print('======================== Menu 2 ==============================')
        print('1. Membeli saham baru')
        print('2. Kembali ke menu utama')
        inputPilihan2 = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihan2 == '1' :
            kodeSaham2 = input('Masukkan kode saham yang ingin dibeli : ').upper()
            if len(kodeSaham2) != 4 or kodeSaham2.isalpha() == False :
                print('Kode saham harus terdiri dari 4 karakter huruf, karena kode saham salah maka transaksi dibatalkan')
                print()
            else :   
                count = 0
                while count < len(saham) :
                    if kodeSaham2 == saham[count][0] :
                        print('Saham sudah dimiliki, mohon berikan nama saham yang lain')
                        print()
                        break
                    else :
                        count += 1
                else :
                    qtySaham = input('Masukkan jumlah saham yang ingin dibeli (dalam lot) : ')
                    if qtySaham.isdigit() == True :
                        qtySaham = int(qtySaham)
                    else :
                        print('Masukan harus berupa angka')
                        print()
                        continue
                    hargaSaham = input('Masukkan harga saham saat ini (dalam rupiah/lbr): ')
                    if hargaSaham.isdigit() == True :
                        hargaSaham = int(hargaSaham)
                    else :
                        print('Masukan harus berupa angka')
                        print()
                        continue
                    hargaAverage = hargaSaham
                    hargaTotal = qtySaham * hargaSaham * 100
                    profitLoss = (hargaSaham-hargaAverage)*qtySaham * 100
                    listBaru = [kodeSaham2,qtySaham,hargaSaham,hargaAverage,hargaTotal]    
                    print()        
                    print(formatTampilan2.format(*header))
                    print(formatTampilan2.format(*listBaru))
                    print()
                    listBaru = [kodeSaham2,qtySaham,hargaSaham,hargaAverage,hargaTotal,profitLoss]  
                    konfirmasi = input('Apakah anda yakin ingin membeli saham ini (Y/T) : ').upper()
                    yakinBertransaksi(konfirmasi)
                    if konfirmasi == 'Y' :
                        selisihUang(uang,hargaTotal)
                        if uang >= hargaTotal :
                            saham.append(listBaru)
                            uang -= hargaTotal
                            print('Berikut list saham yang telah terupdate')
                            print()
                            tampilkanSaham(saham)

        elif inputPilihan2 == '2' :
            print()
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue



# Menu 3 adalah fungsi untuk mengupdate harga saham yang dimiliki sesuai dengan harga saham terbaru
# User hanya dapat mengupdate harga pada kode saham yang terdapat pada list Saham, dan memasukkan harga (dalam integer)
# setelah menginput harga saham, akan ditanya konfirmasi, jika dijawab ya, maka harga saham akan terupdate ke list Saham
# rogram akan terus looping sampai user menginput pilihan 2 untuk kembali ke menu utama
def menu3() :
    while True :
        print('======================== Menu 3 ==============================')
        print('1. Mengupdate harga saham di portofolio dengan harga terbaru')
        print('2. Kembali ke menu utama')
        inputPilihan3 = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihan3 == '1' :
            kodeSaham = input('Masukkan kode saham yang akan diupdate harganya : ').upper()
            count = 0
            while count < len(saham) :
                if kodeSaham == saham[count][0] :
                    print(formatTampilan.format(*header))
                    print(formatTampilan.format(*saham[count]))
                    print()
                    konfirmasi = input('Apakah anda yakin ingin mengupdate (Y/T) : ').upper()
                    yakinBertransaksi(konfirmasi)
                    if konfirmasi == 'Y' :
                        updateHarga = input(f'Masukkan harga saham {kodeSaham} yang terbaru (Rp./lembar) : ')
                        if updateHarga.isdigit() == True :
                            updateHarga = int(updateHarga)
                        else :
                            print('Masukan harus berupa angka')
                            print()
                            break
                        konfirmasi = input('Apakah anda yakin ingin mengupdate harga saham ini (Y/T) : ').upper()
                        yakinBertransaksi(konfirmasi)
                        if konfirmasi == 'Y' :
                            saham[count][2] = updateHarga
                            saham[count][5] = (updateHarga - saham[count][3])*saham[count][1] * 100
                            print(formatTampilan.format(*header))
                            print(formatTampilan.format(*saham[count]))
                            print()
                            count += 1
                            break
                        else :
                            break
                    else : 
                        break
                else :
                    count += 1
            else :
                print('Kode Saham tidak tersedia')
                print()
                continue
        elif inputPilihan3 == '2' :
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue

# Menu 4 adalah fungsi untuk membeli/menjual saham yang terdapat pada portofolio saham user sebelumnya
# Jika user memutuskan untuk membeli, user harus memberikan kode saham unik sesuai format, harga beli saat itu, dan Qty saham
# masukan harga beli dan Qty saham harus berupa integer, jika tidak maka akan kembali ke halaman Menu 3
# User hanya dapat membeli apabila uang yang dimiliki cukup, jika tidak maka akan diminta top up ke menu 6
# Setelah mengisi data pembelian, user akan ditanya konfirmasi apakah yakin akan membeli
# Jika jawaban ya, maka saham yang baru dibeli akan masuk ke list saham dan uang akan berkurang, dan list saham ditampilkan
# jika user ingin menjual saham, maka akan diminta menginput qty dan harga saham (harus integer) dan diminta konfirmasi
# Jika user yakin, saham akan berkurang, dan uang akan bertambah. User tidak bisa menjual keseluruhan saham pada menu ini
# Program akan terus looping sampai user menginput pilihan 2 untuk kembali ke menu utama
def menu4() :
     global uang
     global realizedPL
     while True :
        print('======================== Menu 4 ==============================')
        print('1. Menambah kepemilikan saham yang sudah ada')
        print('2. Menjual sebagian saham yang sudah ada')
        print('3. Kembali ke menu utama')
        inputPilihan4 = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihan4 == '1' :
            tampilkanSaham(saham)
            beliSaham = input('Silahkan pilih saham yang ingin ditambah dari list berikut : ').upper()
            count = 0
            while count < len(saham) :
                if beliSaham == saham[count][0] :
                    print(formatTampilan.format(*header))
                    print(formatTampilan.format(*saham[count]))
                    print()
                    konfirmasi = input('Apakah anda yakin ingin mengupdate (Y/T) : ').upper()
                    yakinBertransaksi(konfirmasi)
                    if konfirmasi == 'Y' :
                        qtySaham = input('Masukkan jumlah saham yang ingin dibeli (dalam lot) : ')
                        if qtySaham.isdigit() == True :
                            qtySaham = int(qtySaham)
                        else :
                            print('Masukan harus berupa angka')
                            print()
                            continue
                        hargaSaham = input('Masukkan harga saham saat ini (Rp/lembar): ')
                        if hargaSaham.isdigit() == True :
                            hargaSaham = int(hargaSaham)
                        else :
                            print('Masukan harus berupa angka')
                            print()
                            continue
                        hargaAverage = hargaSaham
                        hargaTotal = qtySaham * hargaSaham * 100
                        listBaru = [beliSaham,qtySaham,hargaSaham,hargaAverage,hargaTotal]  
                        print()
                        print(formatTampilan2.format(*header))
                        print(formatTampilan2.format(*listBaru))
                        konfirmasi = input('Apakah anda yakin ingin membeli saham ini (Y/T) : ').upper()
                        yakinBertransaksi(konfirmasi)
                        print()
                        if konfirmasi == 'Y' :
                            selisihUang(uang,hargaTotal)
                            if uang >= hargaTotal :
                                saham[count][2] = hargaSaham
                                saham[count][3] = round(((saham[count][4] + listBaru[4])/(saham[count][1]+listBaru[1]))/100,2)
                                saham[count][1] += qtySaham
                                saham[count][4] += hargaTotal
                                saham[count][5] = round((saham[count][2] - saham[count][3])*saham[count][1]*100,2)
                                uang -= hargaTotal
                                print('Berikut list saham yang telah terupdate')
                                print()
                                print(formatTampilan.format(*header))
                                print(formatTampilan.format(*saham[count]))
                                print()
                        break
                    else :
                        break
                else :
                    count += 1
            else : 
                print('Kode Saham tidak tersedia')
                print()

        elif inputPilihan4 == '2' :
            tampilkanSaham(saham)
            jualSaham = input('Silahkan pilih saham yang ingin dijual dari list berikut : ').upper()
            count = 0
            while count < len(saham) :
                if jualSaham == saham[count][0] :
                    print(formatTampilan.format(*header))
                    print(formatTampilan.format(*saham[count]))
                    print()
                    konfirmasi = input('Apakah anda yakin ingin mengupdate (Y/T) : ').upper()
                    yakinBertransaksi(konfirmasi)
                    if konfirmasi == 'Y' :
                        qtySaham = input('Masukkan jumlah saham yang ingin dijual (dalam lot) : ')
                        if qtySaham.isdigit() == True :
                            qtySaham = int(qtySaham)
                        else :
                            print('Masukan harus berupa angka')
                            print()
                            continue
                        if qtySaham > saham[count][1] :
                            print('Anda tidak memiliki kepemilikan saham sebanyak itu')
                            print()
                            break
                        elif qtySaham == saham[count][1] :
                            print(f'Jika anda ingin menjual seluruh kepemilikan saham {jualSaham}, silahkan pilih menu 4')
                            print()
                            break
                        hargaSaham = input('Masukkan harga saham saat ini (dalam rupiah/lbr): ')
                        if hargaSaham.isdigit() == True :
                            hargaSaham = int(hargaSaham)
                        else :
                            print('Masukan harus berupa angka')
                            print()
                            continue
                        hargaTotal = qtySaham * hargaSaham * 100
                        listBaru = [jualSaham,qtySaham,hargaSaham,hargaTotal] 
                        print()
                        print(formatTampilan3.format(*header2))
                        print(formatTampilan3.format(*listBaru))
                        konfirmasi = input('Apakah anda yakin ingin menjual saham ini (Y/T) : ').upper()
                        yakinBertransaksi(konfirmasi)
                        print()
                        if konfirmasi == 'Y' :
                            saham[count][2] = hargaSaham
                            untung = (hargaSaham-saham[count][3])*qtySaham*100
                            realizedPL += untung
                            saham[count][1] -= qtySaham
                            saham[count][4] = (saham[count][1]*saham[count][3])*100
                            saham[count][5] = saham[count][1] * (hargaSaham-saham[count][3])*100
                            uang += hargaTotal
                            print(f'Terima kasih, cash sebesar {hargaTotal} akan ditransfer ke rekening anda')
                            print(f'Total keuntungan yang anda dapat adalah sebesar {untung} rupiah')
                            print('Berikut list saham yang telah terupdate')
                            print()
                            print(formatTampilan.format(*header))
                            print(formatTampilan.format(*saham[count]))
                            print()
                        break
                    else :
                        break
                else :
                    count += 1
            else : 
                print('Kode Saham tidak tersedia')
                print()
        elif inputPilihan4 == '3' :
            print()
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue


# Menu 5 adalah fungsi untuk menjual saham secara keseluruhan yang terdapat pada portofolio saham user sebelumnya
# jika user ingin menjual saham, maka akan akan diminta konfirmasi untuk menjual
# Jika user yakin, kode saham beserta keterangan lainnya akan terhapus dari list saham, dan uang akan bertambah.
# Program akan terus looping sampai user menginput pilihan 2 untuk kembali ke menu utama
def menu5() :
    global uang
    global realizedPL
    while True :
        print('======================== Menu 5 ==============================')
        print('1. Menjual seluruh kepemilikan saham tertentu')
        print('2. Kembali ke menu utama')
        inputPilihan5 = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihan5 == '1' :
                tampilkanSaham(saham)
                jualSaham = input('Silahkan pilih saham yang ingin dijual dari list berikut : ').upper()
                count = 0
                while count < len(saham) :
                    if jualSaham == saham[count][0] :
                        print(formatTampilan.format(*header))
                        print(formatTampilan.format(*saham[count]))
                        konfirmasi = input('Apakah anda yakin ingin menjual saham ini (Y/T) : ').upper()
                        yakinBertransaksi(konfirmasi)
                        print()
                        if konfirmasi == 'Y' :
                            uang += saham[count][4] + saham[count][5]
                            realizedPL += saham[count][5]
                            print(f'Terima kasih, cash sebesar {saham[count][4]} akan ditransfer ke rekening anda')
                            saham.pop(count)
                            print('Berikut kondisi portofolio anda sekarang : ')
                            tampilkanSaham(saham)
                            break
                        else : 
                            break
                    else :
                        count += 1
                else : 
                    print('Kode Saham tidak tersedia')
                    print()
                
        elif inputPilihan5 == '2' :
            print()
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue

# Menu 6 berfungsi untuk melakukan top-up uang kerekening apabila user tidak memiliki cukup uang untuk membeli saham
# User akan diminta menginput jumlah uang yang akan dimasukkan, dan diminta konfirmasi apakah benar ingin top up
# Jika user mengkonfirmasi ya, maka uang akan bertambah
# Program akan terus looping sampai user menginput pilihan 2 untuk kembali ke menu utama
def menu6() :
    global uang
    while True :
        print('======================== Menu 6 ==============================')
        print('1. Top-up Rekening Dana Nasabah')
        print('2. Kembali ke menu utama')
        inputPilihan6 = input('Masukkan angka menu yang mau dijalankan : ')
        if inputPilihan6 == '1' :
            topUp = input('Masukkan jumlah uang yang akan ditop up : ')
            if topUp.isdigit() == True :
                topUp = int(topUp)
            else :
                print('Masukan harus berupa angka')
                print()
                continue
            uang += topUp
            konfirmasi = input('Apakah anda yakin ingin top up (Y/T) : ').upper()
            yakinBertransaksi(konfirmasi)
            if konfirmasi == 'Y' :
                print(f'Terima kasih telah top up, saldo anda sekarang adalah {uang}')
                print()
            else : 
                break
        elif inputPilihan6 == '2' :
            break
        else :
            print('Masukkan input yang benar')
            print()
            continue

# Running program keseluruhan   
programCapstone()
    


