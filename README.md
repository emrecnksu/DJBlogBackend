# Blog Project

A full-featured Django web application built using Django ORM, Django REST Framework, MySQL, and Docker.

---

This project provides a blog system where users can register, login, create posts, list posts under categories, and add comments.

Server-rendered HTML pages are provided using Django Templates, while Django REST Framework is used internally to expose certain application functionalities through REST API endpoints.

The application is fully containerized using Docker for easy setup and deployment.

This project includes:

- Server-rendered web pages using Django Templates
- Internal REST API endpoints using Django REST Framework
- MySQL database management with Django ORM
- Docker-based deployment

---

## Requirements

- Docker
- Docker Compose
- Git

---

## Setup & Installation

### 1️⃣ Clone This Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2️⃣ Environment Configuration

The project uses environment variables for database connection and secret configurations.

Copy the provided sample file `.env.example` to create your own `.env` file:

```bash
cp .env.example .env
```

Edit the `.env` file and set your actual values:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=blog-api-db
DB_USER=root
DB_PASSWORD=root_password
DB_HOST=db
DB_PORT=3306
```

### 3️⃣ Start the Application using Docker Compose

```bash
docker-compose up --build
```

This command will:

- Build Docker images
- Start MySQL container
- Install Python dependencies from `requirements.txt`
- Apply database migrations automatically
- Run Django server on port `8000`

### 4️⃣ Access the Application

- Backend API: http://localhost:8000/api/
- Frontend Web Pages: http://localhost:8000/

### 5️⃣ Create Superuser for Django Admin Panel (Optional)

If you want to access Django's admin interface:

```bash
docker ps
docker exec -it <django-container-name> python manage.py createsuperuser
```

Admin Panel: http://localhost:8000/admin/

### 6️⃣ Stopping and Restarting the Application

To stop Docker containers:

```bash
docker-compose down
```

To restart:

```bash
docker-compose up --build
```

---

## Backend Architecture

- **Layered Architecture:** The codebase is modularized into services, handlers, validators, and serializers, ensuring a clear separation of concerns between business logic and data processing.
- **Custom Validations:** Custom validators are implemented for user registration, post creation, and comment processing to maintain data integrity and consistency.
- **Centralized Exception Handling:** A centralized exception handler provides consistent and user-friendly error messages across all API endpoints.
- **Authentication:** Django’s built-in authentication system is combined with DRF Token Authentication to secure user sessions and API access.
- **Permissions and Authorization:** Object-level permissions are enforced for posts and comments, allowing users to modify only their own content.
- **Database Management:** MySQL database is managed through Django ORM with well-defined model relationships using ManyToMany and ForeignKey fields.
- **Service Layer:** CRUD operations, validations, error handling, and serialization are handled through modular service and handler layers to improve maintainability.
- **Unified API and Web:** Both server-rendered web templates and REST API endpoints are integrated under the same Django backend.
- **Docker Integration:** The entire backend and database are containerized and orchestrated via Docker Compose for easy deployment.

---

## Used Technologies

- Django 5.2.1
- Django REST Framework
- MySQL 8.0 (via Docker)
- Docker & Docker Compose
- Bootstrap (for frontend templates)

---

## Important Notes

- ⚠️ **NEVER COMMIT YOUR `.env` FILE TO THE REPOSITORY!**
- Use `.env.example` as a public template for your environment variables.
- Docker volumes (`mysql-data/`) are excluded from version control.
- All Python cache files (`__pycache__/`, `.pyc`) are excluded via `.gitignore`.

---

# 🇹🇷 Blog Projesi

Django ORM, Django REST Framework, MySQL ve Docker kullanılarak geliştirilmiş tam özellikli Django web uygulamasıdır.

---

Bu proje, kullanıcıların kayıt olabileceği, giriş yapabileceği, gönderi ve yorum işlemleri gerçekleştirebileceği bir blog sistemi sunar.

Sunucu taraflı şablon (server-rendered HTML) kullanılarak web arayüzü sağlanmış, ayrıca Django REST Framework ile sistem içerisindeki bazı işlevlerin API yoluyla yönetimi için REST endpointleri eklenmiştir.

Uygulama Docker ile containerize edilmiştir ve kolay kurulum / dağıtım sağlar.

Bu proje:

- Django Templates ile server-rendered web sayfaları,
- Django REST Framework ile dahili REST API uç noktaları,
- Django ORM üzerinden MySQL veritabanı yönetimi,
- Docker tabanlı dağıtım desteği içerir.

---

## Gereksinimler

- Docker
- Docker Compose
- Git

---

## Kurulum ve Çalıştırma

### 1️⃣ Projeyi Klonlayın

```bash
git clone https://github.com/kullanici-adiniz/proje-adi.git
cd proje-adi
```

### 2️⃣ Ortam Değişkenlerini Ayarlayın

Proje ortam değişkenleri ile çalışmaktadır.

Mevcut `.env.example` dosyasını kullanarak kendi `.env` dosyanızı oluşturun:

```bash
cp .env.example .env
```

`.env` dosyasını açarak gerçek bilgilerinizi girin:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=blog-api-db
DB_USER=root
DB_PASSWORD=root_password
DB_HOST=db
DB_PORT=3306
```

### 3️⃣ Docker Compose ile Uygulamayı Başlatın

```bash
docker-compose up --build
```

Bu komut ile:

- Docker image'ları build edilir
- MySQL container başlatılır
- Python bağımlılıkları yüklenir (`requirements.txt`)
- Veritabanı migrasyonları otomatik uygulanır
- Django server `8000` portunda çalışmaya başlar

### 4️⃣ Uygulamaya Erişim

- Backend API: http://localhost:8000/api/
- Frontend Web: http://localhost:8000/

### 5️⃣ Django Admin Paneline Superuser Oluşturma (isteğe bağlı)

Admin panelini kullanmak isterseniz:

```bash
docker ps
docker exec -it <django-container-ismi> python manage.py createsuperuser
```

Sonrasında yönlendirmeleri takip ederek kullanıcı oluşturabilirsiniz.

Admin Panel: http://localhost:8000/admin/

### 6️⃣ Docker Containerlarını Durdurma ve Tekrar Başlatma

Durdurmak için:

```bash
docker-compose down
```

Tekrar başlatmak için:

```bash
docker-compose up --build
```

---

## Backend Mimarisi

- **Katmanlı Mimari:** Kod yapısı modüler olarak servisler, handlerlar, validatorler ve serializer katmanlarına ayrılarak iş mantığı ve veri işleme ayrıştırılmıştır.
- **Özel Doğrulamalar:** Kullanıcı kayıtları, gönderi ve yorum işlemleri için özel doğrulama kuralları tanımlanmış ve merkezi hata yönetimi sağlanmıştır.
- **Merkezi Exception Handling:** API uç noktalarında hata durumları için merkezi exception handler kullanılarak tutarlı ve kullanıcı dostu hata mesajları sağlanmıştır.
- **Kimlik Doğrulama:** Django’nun dahili authentication yapısı ve DRF Token Authentication birlikte kullanılarak güvenli oturum yönetimi sağlanmıştır.
- **İzinler ve Yetkilendirme:** Gönderi ve yorum işlemleri için kullanıcıya özel erişim kontrolü uygulanmıştır. Kullanıcı yalnızca kendi gönderi ve yorumlarını düzenleyebilir.
- **Veritabanı Yönetimi:** Django ORM üzerinden MySQL veritabanı bağlantısı sağlanmış, model ilişkileri ManyToMany ve ForeignKey ilişkileriyle güçlü şekilde modellenmiştir.
- **Servis Katmanı:** CRUD işlemleri sırasında hata yönetimi, doğrulama ve serializer işlemleri service ve handler katmanlarında modülerleştirilmiştir.
- **API ve Web Bütünlüğü:** Web arayüzü ile birlikte aynı backend üzerinde API uç noktaları da yönetilmektedir.
- **Docker Entegrasyonu:** Docker Compose kullanılarak backend ve veritabanı container ortamında çalışacak şekilde yapılandırılmıştır.

---

## Kullanılan Teknolojiler

- Django 5.2.1
- Django REST Framework
- MySQL 8.0 (Docker ile)
- Docker & Docker Compose
- Bootstrap (Frontend için)

---

## Önemli Notlar

- ⚠️ **`.env` dosyasını kesinlikle versiyona (GitHub) yüklemeyin!**
- Ortam değişkenleri için `.env.example` dosyası public olarak mevcuttur.
- Docker'ın oluşturduğu MySQL volume klasörü (`mysql-data/`) versiyona dahil edilmez.
- Python önbellek dosyaları (`__pycache__/`, `.pyc`) `.gitignore` ile dışlanmıştır.
