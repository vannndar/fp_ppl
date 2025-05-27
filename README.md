Berikut adalah revisi dari aplikasi berdasarkan deskripsi terbaru yang kamu berikan:

---

### 1. **Brief Description about Your Application**

**Study Hub** adalah aplikasi mobile yang dirancang untuk menggantikan grup WhatsApp yang sering digunakan di setiap kelas. Aplikasi ini menyediakan berbagai fitur untuk mengelola informasi dan aktivitas kelas secara lebih terstruktur dan efektif. Dengan fitur seperti membuat grup, menambahkan materi belajar, berbagi video, mengatur deadline tugas, menambahkan tanggal ujian, serta berkomunikasi melalui chat dan pengumuman, **Study Hub** membantu memusatkan semua informasi akademik dan komunikasi di dalam satu platform yang terorganisir.

---

### 2. **Solution that Your Application Proposed**

**Masalah yang ingin diselesaikan** adalah banyaknya grup WhatsApp yang dikelola oleh setiap kelas, yang seringkali menjadi tidak teratur dan sulit dipantau. **Study Hub** menggantikan grup WhatsApp dengan solusi yang lebih terorganisir, dengan fitur-fitur utama sebagai berikut:

* **Menambahkan Grup Kelas**: Fitur untuk membuat grup kelas berdasarkan mata kuliah atau topik tertentu.
* **Menambahkan Materi Belajar**: Mahasiswa dan dosen dapat menambahkan materi pembelajaran berupa teks, gambar, atau dokumen.
* **Menambahkan Video**: Video yang relevan dengan materi kuliah dapat diupload dan dibagikan dalam grup.
* **Menambahkan Deadline Tugas**: Pengguna dapat menambahkan deadline tugas dan mengingatkan anggota grup tentang tenggat waktu tersebut.
* **Menambahkan Tanggal Ujian**: Mahasiswa dan dosen dapat menambahkan tanggal ujian yang akan datang.
* **Menambahkan Asdos ke Grup**: Dosen pembimbing atau asisten dosen dapat ditambahkan ke dalam grup untuk memberikan dukungan.
* **Join atau Leave Group**: Mahasiswa dapat bergabung atau keluar dari grup sesuai dengan kebutuhan mereka.
* **Menambahkan Pengumuman**: Dosen atau administrator dapat membuat pengumuman penting yang dapat dilihat oleh semua anggota grup.
* **Menambahkan Komentar atau Chat Session**: Fitur chat untuk berdiskusi, memberikan komentar, atau bertanya tentang materi yang diajarkan.

---

### 3. **Requirement Analysis**

**Fungsi Utama:**

* **Grup Kelas**: Membuat dan mengelola grup berdasarkan mata kuliah atau topik, serta menambahkan anggota.
* **Materi dan Video**: Fitur untuk berbagi materi pembelajaran dalam berbagai format (teks, gambar, video).
* **Tugas dan Ujian**: Menambahkan dan mengingatkan deadline tugas dan tanggal ujian.
* **Asisten Dosen**: Menambahkan asisten dosen untuk membantu dalam grup.
* **Pengumuman**: Dosen atau administrator dapat mengumumkan informasi penting.
* **Chat**: Fitur komunikasi antara anggota grup.

**Teknologi yang Dibutuhkan:**

* **Platform**: Android dan iOS menggunakan Flutter atau React Native untuk aplikasi cross-platform.
* **Backend**: Firebase untuk autentikasi pengguna dan pengelolaan data.
* **Database**: Firestore atau PostgreSQL untuk menyimpan data grup, materi, video, tugas, ujian, pengumuman, dan chat.
* **Keamanan**: Autentikasi menggunakan akun kampus atau login dengan Google/Facebook.

---

### 4. **Use Case Diagram**

Berikut adalah **Use Case Diagram** yang menggambarkan interaksi pengguna dengan aplikasi **Study Hub**:

```plaintext
        +---------------------------+
        |         Mahasiswa          |
        +---------------------------+
               |               |
               |               |
         +-----v-----+    +----v-----+
         |   Daftar  |    |   Login  |
         +-----+-----+    +----+-----+
               |               |
        +------v-----+    +----v------+
        |   Buat    |    |  Gabung   |
        |  Grup     |    |  Grup     |
        +------^-----+    +----^------+
               |               |
       +-------v--------+   +----v-----+
       |   Tambah Materi|   |  Chat    |
       |   & Video      |   |  Grup    |
       +-------+--------+   +----+-----+
               |                |
       +-------v--------+   +----v------+
       |   Tambah Deadline |   |  Pengumuman|
       |   & Tanggal Ujian |   +------------+
       +-------------------+
```

---

### 5. **Interaction Diagram**

Berikut adalah **Interaction Diagram** untuk skenario menambahkan materi dalam grup:

```plaintext
Mahasiswa      Aplikasi       Backend
     |               |            |
     |--- Login ---->|            |
     |               |-- Verifikasi --|
     |               |<---- OK ----|
     |               |            |
     |--- Pilih Grup --->|        |
     |               |---- Ambil Data Grup --|
     |               |<---- Data Grup --|
     |               |            |
     |--- Tambah Materi ----->|    |
     |               |---- Simpan Materi ---->|
     |               |<---- Konfirmasi ----|
```

---

### 6. **Activity Diagram**

Berikut adalah **Activity Diagram** untuk skenario membuat grup kelas:

```plaintext
Start
  |
  v
[Login / Register]
  |
  v
[Pilih Buat Grup]
  |
  v
[Isi Nama Grup dan Mata Kuliah]
  |
  v
[Tambahkan Anggota]
  |
  v
[Setel Pengaturan Grup]
  |
  v
[Grup Selesai Dibuat]
  |
  v
End
```

---

### 7. **Class Diagram**

Berikut adalah **Class Diagram** untuk aplikasi **Study Hub**:

```plaintext
+--------------------+        +-------------------+
|    User            |<>------>|    Group          |
+--------------------+        +-------------------+
| - userID           |        | - groupID         |
| - username         |        | - groupName       |
| - email            |        | - subject         |
| - password         |        | - memberList      |
+--------------------+        +-------------------+
         |                             |
         v                             v
+-------------------+         +------------------+
|   Task            |         |  Material        |
+-------------------+         +------------------+
| - taskID          |         | - materialID     |
| - taskName        |         | - materialContent|
| - dueDate         |         | - fileType       |
+-------------------+         +------------------+
         |                             |
         v                             v
+-------------------+         +------------------+
|   Announcement    |         |  Chat            |
+-------------------+         +------------------+
| - announcementID  |         | - messageID      |
| - content         |         | - sender         |
| - datePosted      |         | - messageContent |
+-------------------+         +------------------+
```

---

### 8. **Software Architecture Design**

**Software Architecture** untuk **Study Hub** menggunakan pendekatan **MVVM (Model-View-ViewModel)**.

* **Model**: Menyimpan data pengguna, grup, materi, tugas, dan chat.
* **View**: Menampilkan UI untuk grup, materi, pengumuman, dan chat.
* **ViewModel**: Mengelola logika aplikasi dan berinteraksi dengan Model dan View. Menyediakan data untuk ditampilkan.

**Backend**: Menggunakan Firebase untuk autentikasi dan Firestore untuk penyimpanan data secara real-time.

**Notifikasi Push**: Menggunakan **Firebase Cloud Messaging** untuk pengingat tugas dan ujian serta pengumuman.

---

### 9. **Design Pattern Analysis and Implementation Prototype**

**Design Pattern yang Digunakan**:

* **Observer Pattern**: Untuk pengingat otomatis mengenai tugas dan ujian.
* **Singleton Pattern**: Untuk manajemen sesi pengguna, memastikan hanya ada satu instance dari sesi pengguna.

**Implementasi Prototype**:

* **Prototyping** dilakukan menggunakan **Flutter** untuk UI dan **Firebase** untuk backend.

Contoh implementasi menambahkan materi:

```dart
FirebaseFirestore.instance.collection('groups')
  .doc(groupID)
  .collection('materials')
  .add({
    'title': 'Materi Perkuliahan',
    'content': 'Materi kuliah minggu ini',
    'file': 'link_to_file',
    'type': 'PDF',
  });
```

---

### 10. **User Interface Design**

**Halaman Utama**:

* Tampilan **Login** dan **Daftar** pengguna.
* Setelah login, tampilkan **Grup Kelas** yang dapat dibuat atau diikuti.

**Halaman Grup Kelas**:

* Daftar **Anggota**, **Materi**, **Tugas**, dan **Pengumuman**.
* Opsi untuk **Tambah Materi**, **Tambah Tugas**, dan **Tambah Pengumuman**.

**Halaman Chat**:

* Daftar pesan dalam **chat grup**, dengan kemampuan untuk mengirim pesan baru.

**Contoh UI**:

```dart
Scaffold(
  appBar: AppBar(
    title: Text('Study Hub'),
  ),
  body: Column(
    children: [
      Text('Daftar Grup Kelas'),
      // Daftar grup kelas
      ElevatedButton(
        onPressed: () {
          // Navigasi ke halaman buat grup
        },
        child: Text('Buat Grup Baru'),
      ),
    ],
  ),
);
```

---

Dengan aplikasi **Study Hub**, mahasiswa akan lebih mudah mengelola informasi kelas, berbagi materi, berkomunikasi, dan mengatur tugas serta ujian dengan lebih terstruktur dan efisien. Aplikasi ini dapat menggantikan grup WhatsApp yang sering kali tidak terorganisir.
