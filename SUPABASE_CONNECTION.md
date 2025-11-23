# 🔗 دليل الربط بقاعدة بيانات Supabase

## معلومات مشروعك

- **اسم المشروع**: test1
- **كلمة مرور قاعدة البيانات**: Ab8877@db
- **المنطقة**: آسيا والمحيط الهادئ

---

## الخطوة 1️⃣: الحصول على Project Reference ID

هذا هو الرمز الفريد لمشروعك في Supabase. تحتاجه لإكمال `DB_HOST`.

### الطريقة الأولى: من رابط المشروع

1. افتح لوحة تحكم Supabase: https://supabase.com/dashboard
2. اختر مشروع `test1`
3. انظر إلى شريط العنوان في المتصفح
4. الرابط سيكون بهذا الشكل:
   ```
   https://supabase.com/dashboard/project/XXXXXXXXXXXXX
   ```
5. الجزء `XXXXXXXXXXXXX` هو **Project Reference ID**

### الطريقة الثانية: من الإعدادات

1. افتح لوحة تحكم Supabase
2. اختر مشروع `test1`
3. اذهب إلى **Settings** (الإعدادات) من القائمة الجانبية
4. اختر **General** (عام)
5. ابحث عن **Reference ID** أو **Project ID**
6. انسخ الرمز

### الطريقة الثالثة: من Connection String

1. اذهب إلى **Settings** → **Database**
2. في قسم **Connection String**، اختر **URI**
3. ستجد رابطاً بهذا الشكل:
   ```
   postgresql://postgres:Ab8877@db@db.XXXXXXXXXXXXX.supabase.co:5432/postgres
   ```
4. الجزء `XXXXXXXXXXXXX` بين `db.` و `.supabase.co` هو **Project Reference ID**

---

## الخطوة 2️⃣: تحديث ملف .env

بعد الحصول على Project Reference ID، افتح ملف `.env` وحدّث السطر التالي:

### قبل التحديث:
```env
DB_HOST=db.YOUR_PROJECT_REF.supabase.co
```

### بعد التحديث (مثال):
```env
DB_HOST=db.abcdefghijklmnop.supabase.co
```

استبدل `abcdefghijklmnop` بالرمز الفعلي لمشروعك.

---

## الخطوة 3️⃣: التحقق من جميع المتغيرات

تأكد من أن ملف `.env` يحتوي على:

```env
# إعدادات Django
SECRET_KEY=django-insecure-e=%b6e($pfdnsxn2ne7w6he3u8_t&8e!&zz0hq+q28=q_+zfwo
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# إعدادات قاعدة بيانات Supabase
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=Ab8877@db
DB_HOST=db.YOUR_PROJECT_REF.supabase.co  # ← حدّث هذا السطر
DB_PORT=5432
```

---

## الخطوة 4️⃣: اختبار الاتصال

بعد تحديث ملف `.env`، اختبر الاتصال:

```bash
# تفعيل البيئة الافتراضية
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate  # Windows

# تطبيق الهجرات (سيختبر الاتصال)
python manage.py migrate
```

### النتائج المتوقعة:

#### ✅ إذا نجح الاتصال:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  ...
```

#### ❌ إذا فشل الاتصال:
```
django.db.utils.OperationalError: could not connect to server
```

**الحلول**:
1. تحقق من `DB_HOST` - تأكد من صحة Project Reference ID
2. تحقق من `DB_PASSWORD` - تأكد من أنها `Ab8877@db`
3. تأكد من أن مشروع Supabase نشط وليس متوقفاً
4. تحقق من اتصالك بالإنترنت

---

## الخطوة 5️⃣: تنفيذ كود SQL

بعد نجاح الاتصال، نفّذ كود SQL لإنشاء جدول المستخدمين:

1. افتح لوحة تحكم Supabase
2. اذهب إلى **SQL Editor**
3. انقر على **New Query**
4. افتح ملف `supabase_setup.sql` من المشروع
5. انسخ المحتوى والصقه في المحرر
6. انقر على **Run** ▶️

---

## معلومات إضافية

### الاتصال المباشر بقاعدة البيانات

إذا أردت الاتصال بقاعدة البيانات مباشرة عبر أدوات مثل pgAdmin أو DBeaver:

- **Host**: `db.YOUR_PROJECT_REF.supabase.co`
- **Port**: `5432`
- **Database**: `postgres`
- **Username**: `postgres`
- **Password**: `Ab8877@db`
- **SSL Mode**: `require`

### Connection String الكامل

```
postgresql://postgres:Ab8877@db@db.YOUR_PROJECT_REF.supabase.co:5432/postgres
```

**ملاحظة**: إذا كانت كلمة المرور تحتوي على رموز خاصة، قد تحتاج إلى ترميزها (URL encoding):
- `@` → `%40`
- `#` → `%23`
- `$` → `%24`

في حالتك: `Ab8877@db` تصبح `Ab8877%40db`

---

## مشاكل شائعة

### المشكلة: "SSL connection has been closed unexpectedly"

**الحل**: أضف SSL mode إلى إعدادات قاعدة البيانات في `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}
```

### المشكلة: "password authentication failed"

**الحل**:
1. تحقق من كلمة المرور في ملف `.env`
2. إذا نسيت كلمة المرور، يمكنك إعادة تعيينها من:
   **Settings** → **Database** → **Reset Database Password**

### المشكلة: "could not translate host name"

**الحل**: تحقق من `DB_HOST` - تأكد من أنه بالشكل الصحيح:
```
db.XXXXXXXXXXXXX.supabase.co
```

---

## روابط مفيدة

- **لوحة تحكم Supabase**: https://supabase.com/dashboard
- **وثائق Supabase**: https://supabase.com/docs
- **وثائق PostgreSQL**: https://www.postgresql.org/docs/

---

**بالتوفيق! 🚀**
