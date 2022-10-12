**Nama  : Hayfa Najma**

**NPM   : 2106653754**

**Kelas : PBP-F**

# Tugas 6 - Pemrograman Berbasis Platform (PBP)

## 🌏 Tautan Aplikasi Heroku 🌏
Tautan dapat diakses di [Deployment Link](https://tugashayfa.herokuapp.com/todolist/).


### 🎯 Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.?
- Asynchronous Programming
    - Sebuah pendekatan pemrograman yang tidak terikat pada input output (I/O) protocol.
    - Asynchronous programming memungkinkan bagi seorang developer untuk melakukan task codingnya tanpa harus terikat dengan proses lain(independent).
    - Proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Jadi, ketika terjadi pemanggilan sebuah function asynchronous, baris kode selanjutnya dapat dijalankan tanpa harus menunggu function tersebut selesai.
    - Permintaan asinkron tidak memblokir klien, yaitu browser responsif.

- Synchronous Programming
    - Memiliki pendekatan secara old style yaitu dengan memproses jalannya program secara sequential sehingga program akan dieksekusi berdasarkan antrian eksekusi program. Program dengan pendekatan ini akan lebih lama dieksekusi dibanding asynchronous programming.
    - Permintaan Synchronous akan memblokir klien hingga operasi yang dijalankan selesai, yaitu model pada browser sangat tidak responsif.
    - Ketika terjadi pemanggilan sebuah function, function tersebut harus diselesaikan terlebih dahulu sebelum melanjutkan ke baris kode selanjutnya. Jadi, task-task harus dijalankan secara terurut.


### 🎯  Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Maksud dari Paradigma Event-Driven Programming adalah paradigma pemrograman yang berfokus pada proses terjadinya sebuah event. Alur program pada paradigma ini dijalankan bergantung pada terjadinya sebuah event, misalnya tindakan pengguna (klik mouse, penekanan tombol, dll) sehingga biasanya Event-Driven Programming ini menerapkan konsep asynchronous programming.

Pada `todolist.html`, saya menambahkan on("click") dimana sebuah fungsi akan dijalankan ketika tombol di click. Misalnya pada add task dan delete.


### 🎯  Jelaskan penerapan asynchronous programming pada AJAX.
Pada JavaScript, AJAX merupakan sebuah konsep yang menerapkan asynchronous programming dalam mengeksekusi task pada program. Ketika sebuah event terjadi, maka akan mengakibatkan sebuah fungsionalitas AJAX dijalankan.AJAX pada program ini digunakan untuk melakukan pengambilan data dan menangani sebuah response, dalam bentuk JSON. Pada penerapannya, AJAX disini menggunakan JQuery dimana kita tidak perlu membuat instance objek. Kita hanya perlu menambahkan library JQuery pada todolist.html. Dengan menggunakan JQuery, response handling dapat dilakukan secara langsung dengan memanggil function success dan error.


### 🎯  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat sebuah function baru pada `views.py` untuk mengembalikan data dari models.py sesuai dengan user yang login dalam representasi JSON. Lalu, saya memetakan views tersebut dengan routing `/todolist/json` yang telah ditambahkan di `urls.py`. 

2. Membuat fungsi get data dengan menggunakan ajax pada todolist.html. Data yang akan ditampilkan akan diambil dari url yang sudah dipetakan ke dalam bentuk JSON.

3. Kemudian, saya mengubah link pemetaan pada tombol buat task yang tadinya melakukan redirect ke `todolist/create_task` kemudian diubah menjadi indirect, lalu dengan meng-click tombol Add Task, pemetaan tersebut akan menuju target modal. Modal tersebut dibuat dengan template Bootstrap.

4. Lalu saya membuat fungsi AJAX pada todolist.html dengan type POST untuk menambahkan data dari user. Data akan dikirim ke server dan diproses. Jika berhasil membuat task baru, maka akan dilakukan pemanggilan callback function dari AJAX POST tersebut dan menutup modal.

6. Fitur create akan secara asynchronous dilakukan