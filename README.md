# Capstone1_Aplikasi_Database_Portofolio_Saham
Capstone Project 1 – Stock Portofolio Database
Program ini adalah sebuah program yang menyimpan database portofolio saham penggunanya dan juga dapat menjadi tools untuk simulasi transaksi saham yang dilakukan sebelum melakukannya pada pasar saham yang sebenarnya. Data utama pada program ini adalah kode saham (terdiri dari 4 huruf yang merupakan representasi nama perusahaan di Bursa Efek Indonesia), banyaknya saham yang dimiliki (dalam lot), Harga terakhir saham sesuai dengan data pada Bursa Efek Indonesia (dalam Rp./lembar saham), Harga average dari saham yang dimiliki (dalam Rp./lembar saham), total value saham yang dimiliki (dalam Rupiah), dan juga nilai Floating Profit/Loss dari saham yang dimiliki (dalam rupiah) sesuai dengan harga saham yang terakhir kali diupdate. Semua data ini tersimpan pada suatu list. 
Selain itu program ini juga akan meminta penggunannya untuk memasukkan sejumlah uang untuk membeli saham, dan akan menambah uang pengguna jika pengguna menjual saham, seiring dengan itu program ini juga akan mencatat total realized Profit/Loss yang terjadi saat transaksi saham agar pengguna dapat mengetahui performanya dalam melakukan transaksi saham. Secara umum, program ini memiliki 6 fitur yang dapat mengakomodir penggunanya untuk mengalami live experience dalam bertransaksi saham. Fitur-fitur tersebut adalah sebagai berikut :	 

1.	Menampilkan, sorting, dan filter list portofolio saham yaitu Fungsi Read, Sort, dan Filter
Menu 1 terdiri dari rincian sebagai berikut 

- a.	Menampilkan seluruh portofolio
Menu ini berfungsi untuk menampilkan seluruh data yang terdapat pada list portofolio saham. Selain menampilkan tabulasi data, menu ini juga menunjukkan total aset, total floating Profit Loss, dan juga uang yang dimiliki sekarang agar pengguna dapat mengetahui kondisi keuangan dan performa trading saham yang dilakukan.
 

- b.	Menampilkan list saham tertentu
Menu ini Berfungsi untuk memberikan detail terhadap kode saham tertentu yang diinginkan oleh user.
 

- c.	Melakukan sorting sesuai kriteria pengguna
Fitur ini berfungsi untuk mengurutkan list portofolio saham yang dimiliki sesuai dengan kriteria oleh pengguna. Fitur yang tersedia adalah pengurutan berdasarkan kode saham (abjad), Quantity saham, total value, dan Floating profit/loss. Contoh dibawah merupakan sorting berdasarkan kode saham :
 

- d.	Melakukan filter sesuai kriteria pengguna
Fitur ini berfungsi untuk menampilkan list saham yang sesuai dengan kriteria yang dimasukkan oleh pengguna. Adapun kriteria yang dapat dijadikan standard pada program ini adalah Quantity saham, Total value, dan Floating Profit/Loss. Contoh dibawah adalah filter berdasarkan total value dimana nilai yang dimasukkan adalah Rp.10.000.000
 

2.	Membeli saham baru (menambah list portofolio saham)  Fungsi Create
Fitur ini berfungsi untuk membeli saham baru dan memasukkannya ke database portofolio saham yang dimiliki. Adapun untuk dapat melakukan hal ini, pengguna harus memiliki uang yang cukup untuk dapat membeli saham. Jika pengguna tidak memiliki data yang cukup, maka transaksi akan dibatalkan dan data saham baru tidak akan tersimpan. Contoh dibawah adalah pembelian saham ADRO senilai Rp.6.000.000 yang telah berhasil
 

3.	Mengupdate harga saham terbaru  Fungsi Update
Fitur ini berfungsi untuk meng-update harga saham tertentu dengan harga terbaru pada list saham yang ada. Hal ini berguna agar pengguna dapat mengetahui sebesar apa keuntungan/kerugian floating pada portofolionya sesuai dengan harga terakhir dari suatu saham tanpa perlu melakukan transaksi saham. Contoh dibawah merupakan contoh diupdatenya saharga terakhir dari saham TLKM sehingga merubah bagian Total Profit/Loss yang ada
 

4.	Mengubah jumlah kepemilikan saham yang sudah ada  Fungsi Update
Fitur ini berfungsi untuk melakukan transaksi jual/beli pada saham yang terdapat pada list portofolio saham. Hal yang perlu dipastikan saat membeli saham adalah memastikan jumlah uang yang ada cukup, dan juga memakai harga terakhir sebagai harga saham yang akan dibeli. Pengguna harus memasukkan kode saham, jumlah saham, dan harga saham terakhir. Jika transaksi berhasil, maka akan terbentuk harga average yang baru pada saham tersebut dan akan merubah seluruh nilai yang ada pada baris kode saham tersebut sesuai perhitungan pembelian saham. Berikut adalah contoh pembelian saham TLKM sebanyak 20 lot pada harga 5000 yang berhasil dilakukan. Selain menambah kepemilikan saham, pengguna juga dapat menjual Sebagian dari kepemilikan saham yang telah dimiliki lewat menu ini. Ketika pengguna menjual saham, maka saldo akan bertambah sejumlah dengan penjualan saham. Pengguna juga harus menginput kode saham, jumlah saham yang ingin dijual (tidak boleh keseluruhan), dan harga terakhir saham. Berikut adalah contoh penjualan saham BBCA sebanyak 10 lot di harga 8000. Ketika menjual saham, pengguna juga akan diberikan gambaran mengenai keuntungan/kerugian yang telah terealisasi.
 

5.	Menjual saham secara keseluruhan  Fungsi Delete
Fitur ini berfungsi untuk menjual keseluruhan dari salah satu saham yang terdapat pada portofolio pengguna. Pada fitur ini, pengguna hanya perlu mengetikkan kode saham yang ingin dijual seluruhnya, maka program secara otomatis akan menghapuskan saham tersebut dari list dan uang hasil penjualan akan menambah saldo pengguna. Total keuntungan/kerugian yang terealisasi juga akan ter-update setelah melakukan transaksi. Berikut adalah contoh penjualan saham BBNI secara keseluruhan.
 


6.	Top-up Rekening
Fitur ini merupakan fitur untuk menambahkan saldo pada rekening pengguna agar pengguna dapat melakukan pembelian saham jika saja uang pada saldo didalam program kurang. Berikut adalah contoh top-up sebesar Rp. 100.000.000 yang berhasil dilakukan oleh pengguna
 

Semua fitur yang tersedia deprogram ini diharapkan dapat membantu pengguna untuk me-manage portofolionya dan dapat melihat performa dari kegiatan transaksi saham yang dilakukan. Program ini juga dapat digunakan untuk melakukan simulasi untuk pembelajaran saham bagi orang yang ingin belajar saham.
