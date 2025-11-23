-- كود إنشاء قاعدة البيانات في Supabase
-- انسخ هذا الكود وألصقه في SQL Editor في لوحة تحكم Supabase

-- إنشاء جدول المستخدمين
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- إنشاء فهرس على اسم المستخدم لتسريع البحث
CREATE INDEX IF NOT EXISTS idx_username ON users(username);

-- إضافة تعليق على الجدول
COMMENT ON TABLE users IS 'جدول تخزين معلومات المستخدمين';

-- إنشاء دالة لتحديث وقت التعديل تلقائياً
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- إنشاء مشغل لتحديث updated_at عند التعديل
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();

-- إدراج بيانات تجريبية (اختياري)
INSERT INTO users (username, email) VALUES 
    ('admin', 'admin@example.com'),
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com')
ON CONFLICT (username) DO NOTHING;
