**Nama  : Hayfa Najma**

**NPM   : 2106653754**

**Kelas : PBP-F**

# Tugas 4 - Pemrograman Berbasis Platform (PBP)

### 🎯 Apa kegunaan {% csrf_token %} pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

Cross Site Request Foregry atau biasa disebut CSRF adalah sebuah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu aplikasi website melalui aplikasi website yang sedang digunakan. CSRF disebut sebagai salah satu serangan tertua dan paling sederhana di Web yang masih efektif di banyak situs web dan dapat menyebabkan konsekuensi yang parah, seperti kerugian ekonomi dan pengambil alih akun.

Token CSRF {% csrf_token %} adalah sebuah nilai unik, rahasia, dan tidak terduga yang dihasilkan oleh aplikasi sisi server dalam permintaan HTTP berikutnya yang dibuat oleh klien untuk melindungi sumber daya rentan CSRF. CSRF Token bersifat rahasia dan ditangani dengan cara yang aman sepanjang life cicley program. Biasanya tindakan yang efektif adalah mengirimkan token ke klien secara tersembunyi pada bagian Form HTML yang dikirimkan menggunakan metode POST. Token kemudian akan sisipkan sebagai parameter permintaan saat Form HTML dikirmkan.

Token CSRF pada elemen form digunakan untuk mencegah serangan CSRF dengan membuat penyerang tidak mungkin membuat permintaan HTTP yang sepenuhnya valid yang cocok untuk diumpankan ke pengguna korban. Dengan demikian, penyerang tidak dapat menentukan atau memprediksi nilai token CSRF pengguna sehingga mereka tidak dapat membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut. 

Jika di dalam elemen `<form>` tidak terdapat {% csrf_token %} atau token CSRF, maka program akan mengalami serangan CSRF yang membuat aplikasi mengeksekusi suatu tindakan yang sebenarnya tidak dikehendaki oleh pengguna internet. Oleh karena itu, perlu adanya token CRF agar mencegah serangan CSRF.
 

### 🎯 Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Di dalam HTML, form adalah kumpulan elemen di dalam `<form>...</form>` yang memungkinkan pengguna untuk melakukan hal-hal seperti memasukkan teks, memilih opsi, memanipulasi objek, dan lain-lain. Kemudian, form akan mengirimkan informasi tersebut kembali ke server. Formulir HTML diperlukan, bila Anda ingin mengumpulkan beberapa data dari pengunjung situs. Misalnya, selama pendaftaran pengguna, Anda ingin mengumpulkan informasi seperti nama, alamat email, kartu kredit, dll.

Formulir akan mengambil masukan dari pengunjung situs dan kemudian akan mempostingnya ke aplikasi back-end seperti CGI, ASP Script atau skrip PHP dll. Aplikasi back-end akan melakukan pemrosesan yang diperlukan pada data yang diteruskan berdasarkan logika bisnis yang ditentukan di dalamnya aplikasi. 
Tag HTML `<form>` digunakan untuk membuat formulir HTML. Kita dapat membuat elemen `<form>` secara manual dengan menggunakan sintaks berikut:
   ```shell
   <form action = "Script URL" method = "GET|POST">
   <!-- form field di sini -->
   </form>
   ```
Tag `<form>` memiliki beberapa atribut yang harus diberikan seperti:
- `action` untuk menentukan aksi yang akan dilakukan saat data dikirim;
- `method` metode pengiriman data.
Untuk atribut action, kita dapat mengisinya dengan alaman URL dari endpoint yang akan memproses form.

### 🎯 Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Pertama, pengguna akan ditampilkan halaman login untuk melakukan login terlebih dahulu dengan menekan tombol “Login”. Ketika pengguna telah membuat akun sebelumnya, maka pengguna dapat langsung menekan tombol login. Jika pengguna belum mempunyai akun, maka pengguna akan menekan tulisan “Buat Akun” untuk dilanjutkan ke form registrasi akun. Kemudian, pengguna akan mengisi username, password, dan password confirmation. Setelah itu, saat pengguna menekan tombol daftar, data pengguna akan disimpan di dalam database sehingga pengguna dapat menggunakan akun barunya untuk login. Lalu, saat pengguna menekan tombol Login, data username dan password pengguna akan tersimpan di dalam database sehingga program akan memberikan respon kepada pengguna sehingga pengguna disambungkan ke halaman utama yaitu halaman todolist.
2. Selanjutnya, pada halaman utama todolist akan menampilkan username pengguna, tombol “Tambah Task Baru”, dan tombol “Logout”, serta tabel yang akan berisi detail task yang akan ditambahkan oleh user. Detail task tersebut berupa tanggal pembuatan, judul task, deskripsi, status penyelesaian, serta dua tombol yaitu tombol hapus task dan tombol ubah status.
3. Kemudian, saat pengguna baru pertama kali login, todolist pengguna akan berisi kosong sehingga pengguna diminta untuk menambahkan task baru dengan menekan tombol “Tambah Task Baru” agar dilanjutkan ke halaman form untuk pembuatan task baru. Di dalam halaman tersebut, pengguna akan diminta untuk memasukkan judul task dan deskripsi task.
4. Lalu, pengguna akan mengisi data-data tersebut dan menekan tombol “Tambah” agar data-data judul dan deskripsi task akan disimpan ke dalam database dan halaman akan kembali lagi ke halaman utama todolist. Setelah pengguna menekan tombol “Tambah”, maka data tersebut akan diolah dan diambil berdasarkan username pengguna, tanggal saat task tersebut ditambahkan, judul, dan deskripsi task tersebut. Hal ini dapat dilakukan karena pada file views.py pada fungsi create_task, data-data tersebut telah diambil dan disimpan sehingga saat dipanggil pada file todolist.html, data-data tersebut dapat muncul pada halaman todolist.
5. Setelah pengguna menekan tombol “Tambah”, pengguna akan diarahkan ke halaman utama todolist dan pada halaman todolist ini akan ditampilkan data-data task yang telah pengguna tambahkan sebelumnya karena pada file todolist.html, data-data berupa tanggal, judul, deskripsi telah dipanggil dan dibungkus di dalam sebuah tabel sehingga data-data tersebut dapat muncul dengan rapih di dalam tabel.
6. Data-data tersebut dapat ditampilkan karena pada template HTML terdapat for loop task yang memanggil data-data pada Model Task. Potongan kodenya seperti berikut:
   ```shell
      {% for task in list_task %}
         <tr>
            <td>{{task.date}}</td>
            <td>{{task.title}}</td>
            <td>{{task.description}}</td>

            {% if task.is_finished == True %}
            <td>Selesai</td>
            {% else %}
                  <td>Belum Selesai</td>
            {% endif %} 
   ```

7. Kemudian, pengguna juga dapat menghapus task-nya dengan cara menekan tombol “Hapus Task”. Saat, pengguna menekan tombol tersebut, maka data task tertentu akan dihapus dan halaman akan tetap di halaman utama todolist. Selanjutnya, pengguna juga dapat mengupdate status penyelesaian tasknya sehingga saat pengguna menekan tombol “Ubah Status”, maka status akan berubah dari “Belum Selesai” menjadi “Selesai”. Status tersebut dapat berubah karena saat pengguna menekan tombol tersebut maka tombol akan memanggil fungsi status_update yang ada di dalam views.py yang menjadikan atribut is_finished menjadi True yang artinya status sudah selesai.
8. Kemudian, pengguna juga dapat menekan tombol “Logout” untuk keluar dari halaman utama todolist dan kembali ke halaman login. Hal ini terjadi karena ketika pengguna menekan tombol logout, maka pada todolist.html, tombol tersebut akan memanggil fungsi logout yang akan mengembalikan tampilan ke halaman login.

### 🎯 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Berikut ini adalah cara saya mengimplementasikan checklist yang ada pada Tugas 4 - PBP:

1. Pada poin 1 ini, saya membuat suatu aplikasi baru bernama `todolist` di proyek Django yang sudah digunakan sebelumnya. Saya membuat sebuah django-app dengan perintah `python manage.py startapp todolist`.

2. Lalu, saya membuka `settings.py` di folder `project_django` dan saya menambahkan aplikasi `todolist` ke dalam variabel `INSTALLED_APPS` untuk mendaftarkan django-app yang telah saya buat ke dalam proyek Django saya. Contohnya adalah sebagai berikut.
   ```shell
   INSTALLED_APPS = [
      ...,
      'todolist',
   ]
   ```

3. Lalu, saya membuka file models.py yang ada di folder `todolist` dan membuat sebuah model `Task` yang memiliki atribut user, date, title, description, dan is_finished. Berikut adalah potongan kodenya:
   ```shell
   from django.db import models
   from django.contrib.auth.models import User

   class Task(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      date = models.DateField()
      title = models.CharField(max_length=50)
      description = models.TextField()
      is_finished = models.BooleanField(default=False)
   ```

4. Kemudian, saya menjalankan perintah `python manage.py makemigration` untuk mempersiapkan migrasi skema model ke dalam database Django lokal. Saya juga menjalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

5. Selanjutnya, saya membuka `views.py` yang ada pada folder `todolist` dan saya akan membuat 7 fungsi yang terdiri dari 5 fungsi yang menerima parameter `request` dan 2 fungsi yang menerima parameter `request, name`. Fungsi-fungsi tersebut digunakan untuk mengimplementasikan form registrasi, login logout, form tambah task baru agar pengguna dapat menggunakan todolist dengan baik.

Berikut ini adalah potongan kode 7 fungsi tersebut:
   ```shell
   from django.contrib.auth.decorators import login_required

   @login_required(login_url='/todolist/login/')
   def show_todolist(request):
      data_task_todolist = Task.objects.filter(user=request.user)
      context = {
         'list_task': data_task_todolist,
      }
      return render(request, "todolist.html", context)
   ```
Saya menambahkan import login_required pada bagian paling atas. Lalu, saya menambahkan kode @login_required(login_url='/todolist/login/') di atas fungsi show_todolist agar halaman todolist hanya dapat diakses oleh pengguna yang sudah login (terautentikasi). Lalu, saya membuat fungsi show_todolist untuk menghasilkan data-data yang ada pada model Task.

   ```shell
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages

   def register(request):
      form = UserCreationForm()

      if request.method == "POST":
         form = UserCreationForm(request.POST)
         if form.is_valid():
               form.save()
               messages.success(request, 'Akun telah berhasil dibuat!')
               return redirect('todolist:login')
      
      context = {'form':form}
      return render(request, 'register.html', context)
   ```
Saya menambahkan import redirect, UserCreationForm, dan messages pada bagian paling atas. Lalu, saya membuat fungsi register untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

   ```shell
   def create_task(request):
      if request.method == "POST":
         judul = request.POST.get('judul')
         deskripsi = request.POST.get('deskripsi')
         new_task = Task(
               user = request.user,
               date = str(date.today()),
               title = judul,
               description = deskripsi, 
         )
         if (judul == "" or deskripsi == ""):
               messages.info(request, 'Silahkan masukkan Judul dan Deskripsi Task Anda!')
         else:
               new_task.save()
               return redirect('todolist:show_todolist')
      return render(request, 'create_task.html')
   ```
Saya membuat fungsi create_task untuk membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna di halaman form ini adalah judul task dan deskripsi task.

   ```shell
   from django.contrib.auth import authenticate, login
   from django.http import HttpResponseRedirect
   from django.urls import reverse

   def login_user(request):
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user) # melakukan login terlebih dahulu
               response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
               return response
         else:
               messages.info(request, 'Username atau Password salah!')
      context = {}
      return render(request, 'login.html', context)
   ```
Saya menambahkan import authenticate, login, HttpResponseRedirect, dan reverse pada bagian paling atas. Lalu, saya membuat fungsi login untuk mengautentikasi pengguna yang ingin login.

   ```shell
   from django.contrib.auth import logout

   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('todolist:login'))
      response.delete_cookie('last_login')
      return response
   ```
Saya menambahkan import logout pada bagian paling atas. Lalu, saya membuat fungsi logout untuk melakukan mekanisme logout.

   ```shell  
   def delete_task(request, name):
      get_task = Task.objects.get(user=request.user, title=name)
      get_task.delete()
      return redirect('todolist:show_todolist') 
   ```
Saya membuat fungsi delete_task agar dapat menghapus suatu task.

   ```shell 
   def status_update(request, name):
      get_task = Task.objects.get(user=request.user, title=name)

      print(get_task.is_finished)
      if (get_task.is_finished == True):
         get_task.is_finished = False
      else:
         get_task.is_finished = True
      get_task.save()
      return redirect('todolist:show_todolist') 
   ```
Saya membuat fungsi status_update untuk meng-update status penyelesaian task.

6. Kemudian, saya membuat sebuah berkas di dalam folder aplikasi `todolist/templates` bernama `register.html` untuk menampilkan halaman formulir registrasi.
   ```shell
   {% extends 'base.html' %}
   {% block content %}  

   <style>
      input{
         height: 32px;
         width:190px;
         border:  solid;
         display: block;
         font-size: 14px;
      }
      body{
         background-color: #FFF5E4;
      }
   </style>

   <div class = "login">
      
      <h1>Formulir Registrasi</h1>  

         <form method="POST">  
               {% csrf_token %}  
               <table>  
                  {{ form.as_table }}<br>
                  <tr>  
                     <td></td>
                     <td><input type="submit" name="submit" value="Daftar" style="background-color: #BFACE0"/></td>
                  </tr>
               </table> 
         </form>

      {% if messages %}  
         <ul>   
               {% for message in messages %}  
                  <li>{{ message }}</li>  
                  {% endfor %}  
         </ul>   
      {% endif %}

   </div> 

   {% endblock content %}
   ```

7. Kemudian, saya membuat berkas HTML baru dengan nama `login.html` pada folder `todolist/templates` untuk menampilkan halaman login. Isi dari login.html adalah:
   ```shell
   {% extends 'base.html' %}
   {% block content %}

   <style>
      input{
         height: 35px;
         width: 200px;
         border:  solid;
         display: block;
         font-size:20px;
         font-weight: bold;
         background-color:#FFD1D1;
      }
      body{
         background-color: #FFF5E4;
      }
      h1 {
         font-size: 40px;
      }
      
   </style>

   <Center>
   <div class = "login">

      <br><br>
      <br><br><h1>🔮 Login 🔮</h1>
      <form method="POST" action="">
         {% csrf_token %}
         <table>
               <br>
               <tr>
                  <td><b>Username: </b></td>
                  <td><br><input type="text" name="username" placeholder="Username" class="form-control"><br></td>
               </tr>
                    
               <tr>
                  <td><b>Password: </b></td>
                  <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>

               <tr>
                  <td></td>
                  <td><br><input class="btn login_btn" type="submit" value="Login" style="width: 100px"></td>
               </tr>
         </table>
      </form>

      {% if messages %}
         <h4>
               {% for message in messages %}
                  <p style="color: red">{{ message }}</p>
               {% endfor %}
         </h4>
      {% endif %}     
         
      <h4>
         <b>Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a></b>
      </h4>

   </div>
   </Center>

   {% endblock content %}
   ```

8. Kemudian, saya membuat `todolist.html` untuk menampilkan halaman utama `todolist` yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, deskripsi task, status penyelesaian, hapus task dan ubah status.
   ```shell
   {% extends 'base.html' %}

   {% block content %}
   <h1><Center>ToDo List ʕ•́ᴥ•̀ʔっ</Center></h1>
   <h2 style="background-color: pink; border: solid"><Center>Username Pengguna:</Center></h2>  
   <h2><b><Center>{{request.user}}</Center></b></h2>
   <hr width="100%" size="2" align="center" color="black"><br>

   <style> 
      table, th, td {
         border: 2px solid black;
         border-collapse:collapse;
         height: 50px;
      }
      td {
         background-color: #FCC5C0;
         text-align: center;
         width: auto;
         font-size:16px;
      }
      th {
         background-color: #FCC5C0;
         text-align: center;
         width: auto;
         font-size:18px;
      }
      body {
         background-color: #FFF5E4;
      } 
      button {
         height: 40px;
         width: 270px;
         border:  solid;
         display: block;
         background-color:#BFACE0;
         font-size:18px;
         font-weight: bold;
      }
      input {
         background-color: #FFF5E4; 
         width: 130px; 
         height: 40px;
         font-size: 18px;
      }
      
   </style>

   <Center>
   <table>
      <tr style="width:auto;">
         <th style="width:20%">Tanggal Pembuatan</th>
         <th style="width:15%">Judul Task</th>
         <th style="width:25%">Deskripsi</th>
         <th style="width:20%">Status</th>
         <th style="width:20%" colspan="2" >Ubah</th>
      </tr>

      {% for task in list_task %}
         <tr>
               <td>{{task.date}}</td>
               <td>{{task.title}}</td>
               <td>{{task.description}}</td>

               {% if task.is_finished == True %}
               <td>Selesai</td>
               {% else %}
                  <td>Belum Selesai</td>
               {% endif %}   
               
               <td><Center><a href="{% url 'todolist:delete_task' task.title %}"><button type="submit" class="btn btn-danger" 
                  style="width: 110px; text-align: center; font-size:15px;">Hapus Task</button></a></Center></td>
               <td><Center><a href="{% url 'todolist:status_update' task.title %}"><button type="submit" class="btn btn-success ms-1" 
                  style="width: 110px; text-align: center; font-size:15px;">Ubah Status</button></a></Center></td>
         </tr>
      {% endfor %}
      
   </table>
   </Center>
   <br><br>
   <Center><button><a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a></button></Center><br>
   <Center><button><a href="{% url 'todolist:logout' %}">Logout</a></button></Center>

   {% endblock content %}
   ```

9. Lalu, saya membuat `create_task.html` untuk menampilkan halaman form untuk pembuatan task. Pada halaman ini, pengguna diminta untuk memasukkan data berupa judul task dan deskripsi task.
   ```shell
   {% extends 'base.html' %}

   {% block meta %}
   <title>Registrasi Akun</title>
   {% endblock meta %}

   {% block content %} 

   <style>
      input{
         height: 40px;
         width: 270px;
         border:  solid;
         display: block;
         background-color:#FFD1D1;
         font-size:18px;
         font-weight: bold;
      }
      body{
         background-color: #FFF5E4;
      }
      label{
         font-size:20px;
         font-weight: bold;
      }
      button {
         height: 40px;
         width: 270px;
         border:  solid;
         display: block;
         background-color:#BFACE0;
         font-size:18px;
         font-weight: bold;
      }
      h2 {
         color: red;
      }
   </style>

   <Center>
   <div class = "login">

      <h1><Center>💫 Formulir Tambah Task 💫</Center></h1> 
      <Center>
      {% if messages %}  
      <h2> 
      {% for message in messages %}  
         <p>{{ message }}</p>  
         {% endfor %}  
      </h2>  
      {% endif %}
      </Center>
      <hr width="100%" size="2" align="center" color="black"><br>


      <form method="POST">  
         {% csrf_token %}
         <table>
               <label for="judul">Judul Task:</label><br><br>
               <input type="text" id="judul" name="judul"><br>
               <label for="deskripsi">Deskripsi Task:</label><br><br>
               <input type="text" id="deskripsi" name="deskripsi" style="width: 380px"><br><br>
         </table> 
         <button type="submit">Tambah</button><br>
      </form> 

      <button type="submit"><a href="{% url 'todolist:show_todolist' %}">Kembali</a></button><br>

   </div>
   </Center>

   {% endblock content %}
   ```

10. Selanjutnya, saya membuat berkas di dalam folder aplikasi `todolist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah saya buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Berikut ini isi dari `urls.py`:
   ```shell
   from django.urls import include, path
   from todolist.views import delete_task, status_update, show_todolist
   from todolist.views import register
   from todolist.views import login_user
   from todolist.views import logout_user
   from todolist.views import create_task

   app_name = 'todolist'

   urlpatterns = [
      path('', show_todolist, name='show_todolist'),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
      path('create-task/', create_task, name='create_task'),
      path('delete_task/<str:name>/', delete_task, name='delete_task'),
      path('status-update/<str:name>/', status_update, name='status_update'),
   ]
   ```

11. Kemudian, saya juga mendaftarkan aplikasi `todolist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel urlpatterns.
   ```shell
   ...
   path('todolist/', include('todolist.urls'))
   ...
   ```

13. Lalu, saya juga menambahkan kode berikut di `admin.py` agar tabelnya dapat dilihat melalui admin
   ```shell
   admin.site.register(Task)
   ```

Selanjutnya, saya akan mencoba untuk menjalankan proyek Django saya dengan cara:

12. Nyalakan terlebih dahulu _virtual environment_ dengan perintah berikut:
      ```shell
      python -m venv env
      ```

13. Lalu, saya menyalakan environment dengan perintah berikut:
      ```shell
      # Windows
      .\env\Scripts\activate
      ```

14. Kemudian, saya menginstall dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:
      ```shell
      pip install -r requirements.txt
      ```

15. Lalu, saya menjalankan aplikasi Django menggunakan server pengembangan yang berjalan secara lokal:
      ```shell
      python manage.py runserver
      ```

16. Selanjutnya, bukalah URL:
   - http://localhost:8000/todolist berisi halaman utama yang memuat tabel task.
   - http://localhost:8000/todolist/login berisi form login.
   - http://localhost:8000/todolist/register berisi form registrasi akun.
   - http://localhost:8000/todolist/create-task berisi form pembuatan task.
   - http://localhost:8000/todolist/logout berisi mekanisme logout.
   
   (sesuaikan dengan path url yang dibuat) pada browser untuk melihat hasilnya.

Apabila sudah muncul, maka saya sudah berhasil menyambungkan models dengan views dan template sekaligus mempelajari dasar dari sintaks template dari Django. Kemudian, saya melakukan add, commit, dan push pada cmd saya untuk melihat perubahan yang sudah saya lakukan dan menyimpannya ke dalam repositori GitHub yang telah saya buat.

Setelah saya melakukan add, commit, dan push pada cmd, saya membuka tab GitHub Actions di repositori saya dan terlihat bahwa workflow sudah berjalan dan berhasil sehingga akan muncul centang hijau yang artinya sudah berhasil melakukan deployment ke Heroku. Sekarang, aplikasi Django yang telah saya buat sudah dapat diakses di internet melalui link berikut:
- https://tugashayfa.herokuapp.com/todolist/
- https://tugashayfa.herokuapp.com/todolist/login/
- https://tugashayfa.herokuapp.com/todolist/register/
- https://tugashayfa.herokuapp.com/todolist/create-task/
- https://tugashayfa.herokuapp.com/todolist/logout/

Lalu, saya juga sudah membuat dua akun pengguna dan tiga dummy data dengan menggunakan model Task pada akun masing-masing di situs web Heroku.
https://tugashayfa.herokuapp.com/admin
- Akun 1
   - username: hayfanajma
   - password: tugaspbp
- Akun 2
   - username: hayfa.najma
   - password: tugaspbp


# Tugas 5 - Pemrograman Berbasis Platform (PBP)

### 🎯 Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
#### 🎃 Inline CSS
Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Inline CSS diigunakan untuk tag HTML tertentu. Atribut <style> digunakan untuk memberikan style ke tag HTML tertentu.Setiap elemen HTML memiliki atribut style, maka pada bagian itu inline CSS ditulis.

Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. Saat mengatur website dengan menggunakan inline style CSS, Anda akan lebih sulit dalam mengaturnya karena inline CSS hanya digunakan untuk mengubah satu elemen saja.

- Kelebihan:
Berguna jika Anda ingin menguji dan melihat perubahan
Berguna untuk perbaikan cepat
Permintaan HTTP yang lebih kecil
- Kekurangan:
Inline CSS harus diterapkan pada setiap elemen

#### 🎃 Internal CSS
Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian header file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Cara ini sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Jadi, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

- Kelebihan:
Perubahan hanya terjadi pada 1 halaman
Class dan ID bisa digunakan oleh internal stylesheet
Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.
- Kekurangan:
Meningkatkan waktu akses website
Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

#### 🎃 External CSS
External CSS adalah kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

Cara ini lebih simpel dan nyaman untuk menambahkan CSS ke website Anda karena Anda hanya menghubungkannya ke file .CSS eksternal. Dengan cara tersebut, perubahan apapun yang Anda buat pada file CSS akan tampil pada website Anda secara keseluruhan. 

- Kelebihan:
Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
Kecepatan loading menjadi lebih cepat
File CSS yang sama bisa digunakan di banyak halaman.
- Kekurangan:
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

### 🎯 Jelaskan tag HTML5 yang kamu ketahui.
Tag HTML5 adalah perbaikan dari HTML yang diciptakan untuk kebutuhan saat ini seperti dukungan untuk membuat website yang bersifat mobile-friendly. HTML5 memiliki syntax yang lebih sederhana dan mampu menangani error lebih baik dibandingkan HTML. Hal ini dapat mempermudah developer saat membuat struktur halaman website yang kompleks.

Tujuan HTML5 adalah untuk mengikuti perkembangan teknologi informasi dan meningkatkan dukungan terhadap struktur bahasa yang digunakan dalam file multimedia modern. Selain itu, HTML5 juga meningkatkan pengalaman berinternet bagi pengembang dan pengguna. 

### 🎯 Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. TAG SELECTOR

Tag Selector disebut juga Type Selector. Tag selector berfungsi untuk mencari pola berupa Tag atau Element didalam file HTML yang akan dimodifikasi.

2. ID SELECTOR

Selector yang berfungsi untuk mencari Tag atau Element HTML berdasarkan atribut id yang dimilikinya. Dalam penulisannya, selector ID ini harus diawali tanda pagar [#] sebelum menuliskan ID yang dimaksud. 

3. CLASS SELECTOR

Selector yang berfungsi untuk mencari Tag atau Element HTML berdasarkan atribut Class yang terdapat didalamnya. Dalam penulisannya, selector Class ini harus diawali tanda titik [.] sebelum menuliskan Class yang dimaksud. Nama-nama class yang digunakan bebas terserah kita. 

4. UNIVERSAL SELECTOR

Selector yang berfungsi mengubah seluruh Tag atau Element yang terdapat didalam suatu file HTML. Untuk menggunakan selector universal kita hanya perlu menuliskan simbol bintang [*] pada kode css yang kita ingin terapkan. 

5. ATTRIBUTE SELECTOR

Selector yang memilik elemen berdasarkan atribut. Selektor ini hampir sama seperti selektor Tag.

6. PSEUDO SELECTOR

Selector yang digunakan untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya. Terdapat dua macam pseudo selektor yaitu:
- Pseudo-class → selektor untuk memilih state pada elemen.
- Pseudo-element → selektor untuk memilih elemen semu.


### 🎯 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Berikut ini adalah cara saya mengimplementasikan checklist yang ada pada Tugas 5 - PBP:

1. Saya membuat link untuk eksternal style `login.css` agar `login.html` dapat tersambung ke login.css. Hal ini bertujuan agar halaman html login dapat mengakses style yang ada pada `login.css`.

2. Saya merapihkan class yang ada pada `login.html` dengan membuat dua class "user-box" di dalam class "login-box". Masing-masing class "user-box" ini terdiri dari input dan label untuk username dan password. Lalu, di dalam class "login-box" juga terdapat button login dan href register untuk masuk ke dalam halaman register akun.

3. Lalu, pada `login.css` saya mengkustomisasi templat untuk halaman login dengan semenarik mungkin. Saya mengubah warna tulisan, ukuran, jenis tulisan, warna background, posisi, dan saya juga memberikan hover pada button dan atribut `<a>` href.

4. Kemudian, saya juga merapihkan class yang ada pada `register.html` dengan menambahkan class "user-box" di dalam class "register-box". Saya juga membuat link untuk eksternal style `register.css` agar register.html dapat tersambung ke `register.css`. Hal ini bertujuan agar halaman html register dapat mengakses style yang ada pada `register.css`.

5. Pada `register.css`, saya mengkustomisasi templat untuk halaman register dengan semenarik mungkin. Saya mengubah warna tulisan, ukuran, jenis tulisan, warna background, posisi, dan saya juga memberikan hover pada button dan atribut `<a>` href.

6. Selanjutnya, saya juga merapihkan class yang ada pada `todolist.html` dengan menambahkan class "topnav" untuk bagian navbar atas dan class "container" untuk isi dari tiap task beserta detail dan tombolnya. Pada html ini, saya menaruh for loopnya di sebelum class "card" agar dapat mengkustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task). Di dalam class "card" ini terdapat class "headBx" yang berisi bagian atas card task, class "contentBx" yang berisi detail dan tombol dari isi task, dan class "buttonBx" yang berisi bagian tombol tambah task dan logout.

7. Saya juga membuat link untuk eksternal style `todolist.css` agar todolist.html dapat tersambung ke `todolist.css`. Hal ini bertujuan agar halaman html todolist dapat mengakses style yang ada pada `todolist.css`.

8. Lalu, pada `todolist.css`, saya mengkustomisasi templat untuk halaman todolist dengan semenarik mungkin dengan tiap tasknya berbentuk card. Saya mengubah warna tulisan, ukuran, jenis tulisan, warna background, gambar background, posisi, dan saya juga memberikan hover pada semua button. Saya juga menambahkan efek ketika melakukan hover pada cards di halaman utama todolist.

8. Kemudian, saya juga merapihkan class yang ada pada `create_task.html` dengan menambahkan class "user-box" di dalam class "create_task-box". Saya juga membuat link untuk eksternal style `create.css` agar create_task.html dapat tersambung ke `create.css`. Hal ini bertujuan agar halaman html create_task dapat mengakses style yang ada pada `create.css`.

9. Lalu, saya mengkustomisasi templat halaman create_task dengan semenarik mungkin pada `creat.css`. Saya mengubah warna tulisan, ukuran, jenis tulisan, warna background, gambar background, posisi, dan saya juga memberikan hover pada button dan atribut `<a>` href. Saya juga menambahkan efek ketika melakukan hover pada semua button.

Link Heroku Todolist:
- https://tugashayfa.herokuapp.com/todolist/
- https://tugashayfa.herokuapp.com/todolist/login/
- https://tugashayfa.herokuapp.com/todolist/register/
- https://tugashayfa.herokuapp.com/todolist/create-task/
- https://tugashayfa.herokuapp.com/todolist/logout/

Username & Password:
- Akun 1
   - username: hayfanajma
   - password: tugaspbp
- Akun 2
   - username: hayfa.najma
   - password: tugaspbp


## 🎯 Referensi

- https://brightsec.com/blog/csrf-token/
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3
- https://portswigger.net/web-security/csrf/tokens
- https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/