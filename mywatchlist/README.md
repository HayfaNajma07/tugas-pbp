# Tugas 3 - Pemrograman Berbasis Platform (PBP)
**Nama  : Hayfa Najma**

**NPM   : 2106653754**

**Kelas : PBP-F**

## 🎯 Perbedaan 

**Jelaskan perbedaan antara JSON, XML, dan HTML!**

|     Perbedaan         |     HTML      |     XML       |     JSON  |
| :-----------          | :--------     | :--------     | :-------- |
| **`Definisi`**        | Hypertext Markup Language atau biasa disebut HTML adalah sebuah bahasa pengkodean yang digunakan untuk membuat halaman yang dapat ditampilkan di dalam browser web. HTML sering disebut sebagai “tulang punggung internet” dikarenakan sebagian besar halaman web yang ada di internet disimpan sebagai file HTML. | Extensible Markup Language atau biasa disebut XML adalah sebuah bahasa markup yang mirip dengan HTML, tetapi dengan perbedaan tertentu. Bahasa markup adalah seperangkat kode yang menjelaskan teks di dalam dokumen digital. XML dapat digunakan untuk mendeskripsikan data dengan fleksibel. | JavaScript Object Notation atau biasa disebut JSON adalah sebuah format standar terbuka yang ringan dan berbasis teks. JSON dirancang secara eksplisit untuk penyusunan data datyang dapat dibaca oleh manusia. JSON digunakan untuk mengirimkan data antara server dan aplikasi web.   |
| **`Tujuan`**          | HTML digunakan untuk menampilkan data. | XML dikembangkan sebagai format standar terbuka yang terdokumentasi dengan baik yang berisi seperangkat aturan tentang cara mengkodekan dokumen dalam format yang dapat dibaca oleh manusia dan mesin. XML digunakan untuk menyimpan dan mengirimkan data. | JSON dikembangkan sebagai format file sederhana dan ringan untuk pertukaran data.   |
| **`Bahasa`**          | HTML berasal dari SGML yaitu bahasa markup. | XML berasal dari SGML (bahasa markup) yang memiliki tag untuk mendefinisikan elemen. | JSON didasarkan pada bahasa JavaScript.   |
| **`Tag`**             | HTML tidak perlu menggunakan tag penutup. | XML harus terdapat tag awal dan penutup di dalamnya. | JSON tidak menggunakan tag awal dan penutup.   |
| **`Penguraian`**      | HTML tidak memerlukan aplikasi tambahan untuk menguraikan kode JavaScript ke dalam dokumen HTML.  | XML lebih sulit diuraikan karena XML harus diurai dengan parser XML. XML memerlukan DOM (Model Objek Dokumen) untuk mem-parsing kode JavaScript dan pemetaan teks. | JSON dapat diuraikan oleh fungsi JavaScript standar.   |
| **`Sintaks`**         | HTML menggunakan tag-tag khusus (predefined tags) untuk menjalankan fungsinya. Tag pada HTML adalah tag yang telah ditentukan sebelumnya. | XML dapat menggunakan tag apapun yang ditentukan sendiri. XML membutuhkan banyak karakter untuk mewakili data yang sama sehingga XML tidak ringan. | JSON tidak menggunakan tag awal dan tag akhir. JSON memiliki sintaks yang ringan karena berorientasi pada data dengan redundansi yang lebih sedikit.  |
| **`Objek`**           | HTML menawarkan dukungan objek asli.   | XML mendukung objek melalui atribut dan elemen. | JSON tidak mendukung objek asli.   |
| **`Ukuran Dokumen`**  | HTML memiliki ukuran dokumen yang relatif kecil. | XML memiliki ukuran dokumen yang relatif besar karena digunakan sebagai pendekatan pemformatan dan kode sehingga susah untuk dibaca. | JSON memiliki ukuran dokumen yang ringkas dan mudah dibaca, tidak ada tag atau data yang tidak terpakai atau kosong sehingga membuat file terlihat sederhana.   |

## 🎯 Data Delivery 

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery di dalam platform adalah sebuah arsitektur yang bersifat fleksibel untuk bertukar informasi agar dapat merancang dan mengembangkan suatu sistem. Di dalam data delivery, terdapat berbagai protokol jaringan yang dapat bertukar data dan informasi. Salah satu protokol yang banyak digunakan adalah HTTP. Protokol HTTP adalah jaringan lapisan aplikasi yang dikembangkan untuk membantu proses transfer antar komputer dan menjaga keamanan data agar terhindar dari pencurian data. HTTP ini cukup fleksibel sehingga sampai saat ini terus dikembangkan dengan penambahan beberapa fitur baru. Data delivery dapat dilakukan melalui HTML, JSON, XML, dan lain-lain. Berikut ini adalah tipikal respon HTTP:
1. Browser meminta halaman HTML. Server mengembalikan file HTML.
2. Browser meminta lembar gaya. Server mengembalikan file CSS.
3. Browser meminta gambar JPG. Server mengembalikan file JPG.
4. Browser meminta kode JavaScript. Server mengembalikan file JS.
5. Browser meminta data. Server mengembalikan data (dalam XML atau JSON).
6. Ada file yang tidak disimpan di server, tetapi di-generate oleh kode program.

Selanjutnya, kita memerlukan data delivery dalam pengimplementasian platform karena saat sistem ingin melakukan transfer data, sistem perlu melakukan komunikasi antar-server agar data yang dikirim dapat konsisten dan sesuai permintaan client.

Contohnya adalah adanya komunikasi antara komputer client dengan web server. Komputer client akan melakukan pengiriman menggunakan browser ke web server. Kemudian, web server akan menanggapi permintaan tersebut dengan mengirimkan data yang tersedia di dalam web server sesuai dengan permintaan komputer client.

## 🎯 Implementasi

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

Berikut ini adalah cara saya mengimplementasikan semua checklist yang ada pada Tugas 3 - PBP:

1. Pada poin 1 ini, saya membuat suatu aplikasi baru bernama `mywatchlist` di proyek Django Tugas 2 pekan lalu. Saya membuat sebuah django-app dengan perintah `python manage.py startapp wishlist`.

2. Lalu, saya membuka `settings.py` di folder `project_django` dan saya menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang telah saya buat ke dalam proyek Django saya. Contohnya adalah sebagai berikut.
   ```shell
   INSTALLED_APPS = [
      ...,
      'mywatchlist',
   ]
   ```

3. Lalu, saya membuka file models.py yang ada di folder `mywatchlist` dan membuat sebuah model `MyWatchList` yang memiliki atribut watched, title, rating, release_date, dan review. Berikut adalah potongan kodenya:
   ```shell
   from django.db import models

   class MyWatchList(models.Model):
      title = models.CharField(max_length=50)
      release_date = models.CharField(max_length=50)
      watched = models.CharField(max_length=50)
      rating = models.IntegerField()
      review = models.TextField()
   ```

4. Kemudian, saya menjalankan perintah `python manage.py makemigration` untuk mempersiapkan migrasi skema model ke dalam database Django lokal. Saya juga menjalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

5. Selanjutnya, saya membuat sebuah folder bernama `fixtures` di dalam folder aplikasi `mywatchlist` dan saya membuat sebuah berkas bernama `initial_mywatchlist_data.json` yang berisi 10 data untuk objek `MyWatchList` yang sudah saya buat di atas. Berikut ini adalah potongan kodenya:
   ```shell
   [
      {
         "model":"mywatchlist.mywatchlist",
         "pk":1, 
         "fields":{
               "watched":"Yes",
               "title":"The Nun",
               "rating": "5",
               "release_date": "20/11/2018",
               "review": "I gave an 5 for this reason only. In my review of Dark Waters n A Cure for Wellness, I mentioned that cinematography n atmosphere ain't enuff to save a bad film but this film ain't bad. It is well acted n directed n unlike the other two this wasn't boring at all."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":2,
         "fields":{
               "watched":"Yes",
               "title":"The Boss Baby",
               "rating": "5",
               "release_date": "05/04/2017",
               "review": "I loved this film, the scenes with the older brother were very funny. I would recommend this film to everyone, whether you have children or not. Like most cartoon movies there are subtle wording and scenes that will make adults laugh. Go out see this film, one of the best this year so far."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":3,
         "fields":{
               "watched":"Yes",
               "title":"The Hunger Games",
               "rating": "5",
               "release_date": "22/03/2012",
               "review": "The film did a good job executing its grit and thrills. Decent directing and amazing performances. The filmmakers did a fantastic job bringing Suzanne Collins' book to life. It's not the usual kind of blockbuster that focuses to its loudness. It's a film with moving drama and has its suspense."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":4,
         "fields":{
               "watched":"No",
               "title":"Miracle in Cell No.7",
               "rating": "5",
               "release_date": "19/07/2013",
               "review": "This film will make you laugh. This film will make you cry. The characters look eccentric yet enchanting thanks to their mesmerizing performance. An immensely satisfying family drama that will leave most of its viewers with a smile on their face & tears in their eyes."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":5,
         "fields":{
               "watched":"Yes",
               "title":"The Avengers: Endgame",
               "rating": "5",
               "release_date": "24/04/2019",
               "review": "This film is an emotional rollercoaster with some of the coolest superhero plot lines ever drawn up. It's straight up the most epic Marvel film that will probably ever be created."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":6,
         "fields":{
               "watched":"Yes",
               "title":"Despicable Me",
               "rating": "5",
               "release_date": "09/07/2010",
               "review": "I love this movie! It was so adorable, so charming & the writing was absolutely terrific! I love the animation & the characters (including the minions) were all fantastic! A MUST WATCH!"
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":7,
         "fields":{
               "watched":"Yes",
               "title":"Turning Red",
               "rating": "3",
               "release_date": "01/03/2022",
               "review": "The animation is really, really good, as expected from Pixar, but they wasted it by making their first film to completely break their mold by having a target audience. The plot is weird and awkward, and every moment of screentime jumps back and forth between extremely cringey or mind-numbingly cliche."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":8,
         "fields":{
               "watched":"Yes",
               "title":"Pengabdi Setan 2: Communion",
               "rating": "5",
               "release_date": "04/08/2022",
               "review": "Bigger, braver, more brutal, Joko Anwar sets new standard for Indonesian horror visual storytelling with each release of Pengabdi Setan's installment. It's an excellent alternative for those suffering from Hollywood fatigue, thanks to all those homages towards 60's - 80's horror movies, the period where Hollywood still knew how to make movies, including horror/thriller."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":9,
         "fields":{
               "watched":"Yes",
               "title":"Top Gun: Maverick",
               "rating": "5",
               "release_date": "27/05/2022",
               "review": "Tom Cruise is brilliant as he reprises the role of Maverick, while Miles Teller comes in and gives a top performance. Jennifer Connelly is another positive, though her role does kinda feel a tiny bit forced in order to have a love interest; given Kelly McGillis' (unexplained) absence."
         }
      },
      {
         "model":"mywatchlist.mywatchlist",
         "pk":10,
         "fields":{
               "watched":"Yes",
               "title":"Hotel Transylvania 2",
               "rating": "5",
               "release_date": "25/09/2015",
               "review": "Overall, the film is an energetic animation compared to its predecessor, heart-warming and certainly a satisfying family goers movie to enjoy."
         }
      }
   ]
   ```

6. Lalu, saya menjalankan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.

7. Selanjutnya, saya membuka `views.py` yang ada pada folder `mywatchlist` dan saya akan membuat 3 fungsi yang menerima parameter `request` yang digunakan untuk routing fungsi views yang dapat melakukan render sebuah halaman HTML, XML, dan JSON. 3 fungsi tersebut dibuat agar saya dapat mengakses data di atas melalui URL:
   -  http://localhost:8000/mywatchlist/html
   -  http://localhost:8000/mywatchlist/xml
   -  http://localhost:8000/mywatchlist/json

   Pada fungsi bernama show_mywatchlist yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.

   Untuk mengembalikan data dalam bentuk XML dan JSON, saya menambahkan import HttpResponse dan Serializer pada bagian paling atas.

   Pada fungsi bernama show_xml yang mengembalikan data dalam bentuk XML, Lalu, saya membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada `MyWatchList`. Kemudian, saya menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".

   Lalu, pada fungsi bernama show_json yang mengembalikan data dalam bentuk JSON, saya membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada `MyWatchList`. Kemudian, saya menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/json".

   Lalu, saya juga membuat 1 fungsi sebagai fitur yang menampilkan pesan dengan aturan yang ada pada tugas 3. Fungsi ini akan mengecek apakah jumlah film yang sudah ditonton itu lebih banyak atau sama dengan jumlah film yang belum ditonton.

   Berikut ini adalah potongan kode 4 fungsi tersebut:
      ```shell
      from django.shortcuts import render
      from mywatchlist.models import MyWatchList
      from django.http import HttpResponse
      from django.core import serializers

      def show_mywatchlist(request):
         data_barang_mywatchlist = MyWatchList.objects.all()
         context = {
            'list_movies': data_barang_mywatchlist,
            'nama': 'Hayfa Najma', 
            'npm' : '2106653754',
            'text': show_message()
         }
         return render(request, "mywatchlist.html", context)

      def show_xml(request):
         data = MyWatchList.objects.all()
         return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

      def show_json(request):
         data = MyWatchList.objects.all()
         return HttpResponse(serializers.serialize("json", data), content_type="application/json")

      def show_message():
         watched = MyWatchList.objects.filter(watched=True).count()
         not_watched = MyWatchList.objects.filter(watched = False).count()
         if(watched >= not_watched):
            return("Selamat, kamu sudah banyak menonton!")
         else:
            return("Wah, kamu masih sedikit menonton!")
      ```

8. Kemudian, saya membuat sebuah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah kamu buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser-mu. Isi dari urls.py tersebut adalah sebagai berikut.
   ```shell
   from django.urls import path
   from mywatchlist.views import show_mywatchlist
   from mywatchlist.views import show_xml
   from mywatchlist.views import show_json

   app_name = 'mywatchlist'

   urlpatterns = [
      path('html/', show_mywatchlist, name='show_mywatchlist'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json')
   ]
   ```

9. Kemudian, saya juga mendaftarkan aplikasi `mywatchlist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel urlpatterns.
   ```shell
   ...
   path('mywatchlist/', include('mywatchlist.urls'))
   ...
   ```

Lalu, saya melakukan mapping terhadap data yang telah ikut di-render dan data yang menampilkan pesan pada fungsi views untuk dapat memunculkannya di halaman HTML. Untuk melakukan mapping tersebut, saya menggunakan sintaks khusus template yang ada pada Django. Berikut ini adalah cara mapping:

10. Saya membuka file HTML yang sudah saya buat sebelumnya pada folder `templates`

11. Kemudian, saya membuat style border HTML untuk menampilkan border pada bagian tertentu dan menggunakan sintaks khusus pada nama, npm, dan text untuk menampilkan Nama, Student ID, dan juga Message yang telah saya buat. Kemudian, saya juga mengatur letak tulisannya agar berada di tengah (center). Berikut ini adalah potongan kodenya:
      ```shell
      <h3 style="border: 2px solid Tomato;"><Center>Name:</Center></h3>
      <h4><b><Center>{{nama}}</Center></b></h4>

      <h3 style="border: 2px solid Tomato;"><Center>Student ID:</Center></h3>
      <h4><Center>{{npm}}</Center></h4>

      <h3 style="border: 2px solid Tomato;"><Center>Message:</Center></h3>
      <h4><Center>{{text}}</Center></h4>
      ```

12. Lalu, untuk menampilkan daftar film ke dalam tabel, saya mengiterasi terhadap `list_movies` yang telah saya render ke dalam HTML. Saya memanggil daftar film tersebut secara spesifik karena `list_movies` merupakan sebuah kontainer yang berisikan objek sehingga saya perlu memanggil nama variabel/atribut spesifik dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut. Berikut ini potongan kodenya.
      ```shell
      ...
      {% for movie in list_movies %}
         <tr>
            <th>{{movie.title}}</th>
            <th>{{movie.release_date}}</th>
            <th>{{movie.watched}}</th>
            <th>{{movie.rating}}</th>
            <th align="justify">{{movie.review}}</th>
         </tr>
      {% endfor %}
      ...
      ```

Selanjutnya, saya akan mencoba untuk menjalankan proyek Django saya dengan cara:

13. Nyalakan terlebih dahulu _virtual environment_ dengan perintah berikut:
      ```shell
      python -m venv env
      ```

14. Lalu, saya menyalakan environment dengan perintah berikut:
      ```shell
      # Windows
      .\env\Scripts\activate
      ```

15. Kemudian, saya menginstall dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:
      ```shell
      pip install -r requirements.txt
      ```

16. Lalu, saya menjalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal:
      ```shell
      python manage.py runserver
      ```

17. Selanjutnya, bukalah URL:
   -  http://localhost:8000/mywatchlist/html
   -  http://localhost:8000/mywatchlist/xml
   -  http://localhost:8000/mywatchlist/json`http://
   
   (sesuaikan dengan path url yang dibuat) pada browser untuk melihat hasilnya.

Apabila sudah muncul, maka saya sudah berhasil menyambungkan models dengan views dan template sekaligus mempelajari dasar dari sintaks template dari Django. Lalu, saya juga sudah menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di atas dapat mengembalikan respon HTTP 200 OK. Kemudian, saya melakukan add, commit, dan push pada cmd saya untuk melihat perubahan yang sudah saya lakukan dan menyimpannya ke dalam repositori GitHub yang telah saya buat.

Setelah saya melakukan add, commit, dan push pada cmd, saya membuka tab GitHub Actions di repositori saya dan terlihat bahwa workflow sudah berjalan dan berhasil sehingga akan muncul centang hijau yang artinya sudah berhasil melakukan deployment ke Heroku. Sekarang, aplikasi Django yang telah saya buat sudah dapat diakses di internet melalui link berikut:
- https://tugashayfa.herokuapp.com/mywatchlist/html/
- https://tugashayfa.herokuapp.com/mywatchlist/xml/
- https://tugashayfa.herokuapp.com/mywatchlist/json/

## 🎯 Postman
`HTML`
![html](https://user-images.githubusercontent.com/92681187/191579966-9ec77492-d28f-431c-8240-2fa456a42767.png)

`XML`
![xml](https://user-images.githubusercontent.com/92681187/191580095-a3bfb272-e0f2-4b78-a5b4-d68f0d9d0d8a.png)

`JSON`
![json](https://user-images.githubusercontent.com/92681187/191580090-1bc2eb11-a6ed-4623-9e8b-60de4e449f63.png)

## Referensi

- PPT PBP – 04-Data Delivery (SCELE CS UI)
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-2
- https://www.datavirtualizationblog.com/data-delivery-four-challenges-one-solution/
- https://www.niagahoster.co.id/blog/pengertian-http/#Pengertian_HTTP
