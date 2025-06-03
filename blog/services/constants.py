# services/constants.py

# --- GENEL ---
GENERAL_MESSAGES = {
    "post_delete_not_allowed": "Gönderi silme işlemi yasaktır.",
    "post_not_found": "İlgili gönderi bulunamadı.",
    "comment_not_found": "İlgili yorum bulunamadı.",
    "category_not_found": "İlgili kategori bulunamadı.",
    "default_not_found": "Kayıt bulunamadı.",
    "unexpected_error": "Beklenmeyen bir hata oluştu."
}

# --- POST doğrulama ---
POST_VALIDATION_MESSAGES = {
    "title_required": "Başlık boş bırakılamaz.",
    "title_min": "Başlık en az 8 karakter olmalıdır.",
    "content_required": "İçerik boş bırakılamaz.",
    "content_min": "İçerik en az 100 karakter olmalıdır.",
    "categories_required": "Kategori alanı boş bırakılamaz."
}

# --- COMMENT doğrulama ---
COMMENT_VALIDATION_MESSAGES = {
    "content_required": "Yorum içeriği boş bırakılamaz.",
    "content_min": "Yorum en az 5 karakter olmalıdır."
}

# --- AUTH doğrulama ---
AUTH_VALIDATION_MESSAGES = {
    "email_required": "E-posta alanı zorunludur.",
    "email_exists": "Bu e-posta adresi zaten alınmış.",
    "password_required": "Şifre alanı zorunludur.",
    "password_min": "Şifre en az 6 karakter olmalıdır.",
    "username_required": "Kullanıcı adı boş bırakılamaz.",
    "username_exists": "Bu kullanıcı adı zaten alınmış.",
    "first_name_required": "İsim alanı zorunludur.",
    "last_name_required": "Soyisim alanı zorunludur.",
    "login_failed": "Geçersiz kullanıcı adı veya şifre.",
}

# --- İZİNLER ---
PERMISSION_MESSAGES = {
    "author_only": "Bu işlemi yapma yetkiniz yok.",
    "authentication_required": "Bu işlemi yapabilmek için giriş yapmalısınız."
}

# --- BAŞARILI işlemler ---
SUCCESS_MESSAGES = {
    "post_created": "Gönderi başarıyla oluşturuldu.",
    "post_updated": "Gönderi başarıyla güncellendi.",
    "comment_created": "Yorum başarıyla gönderildi.",
    "comment_updated": "Yorum başarıyla güncellendi.",
    "comment_deleted": "Yorum başarıyla silindi.",
    "registered": "Kayıt başarıyla tamamlandı.",
    "logged_in": "Giriş başarılı.",
    "logged_out": "Çıkış işlemi başarılı."
}

# --- HATA işlemleri ---
ERROR_MESSAGES = {
    "post_create_failed": "Gönderi oluşturulamadı. Lütfen bilgileri kontrol edin.",
    "post_update_failed": "Gönderi güncellenemedi. Lütfen bilgileri kontrol edin.",
    "comment_create_failed": "Yorum gönderilemedi. Lütfen bilgileri kontrol edin.",
    "comment_update_failed": "Yorum güncellenemedi. Lütfen bilgileri kontrol edin.",
    "comment_delete_failed": "Yorum silinemedi.",
    "register_failed": "Kayıt başarısız oldu. Lütfen bilgileri kontrol edin.",
}
