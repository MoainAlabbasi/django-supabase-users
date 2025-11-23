from django.db import models

class User(models.Model):
    """
    نموذج المستخدم لتخزين معلومات المستخدمين
    """
    username = models.CharField(max_length=100, unique=True, verbose_name='اسم المستخدم')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='البريد الإلكتروني')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')

    class Meta:
        db_table = 'users'  # اسم الجدول في قاعدة البيانات
        verbose_name = 'مستخدم'
        verbose_name_plural = 'المستخدمون'
        ordering = ['-created_at']

    def __str__(self):
        return self.username
