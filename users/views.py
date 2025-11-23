from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def user_list(request):
    """
    عرض قائمة المستخدمين
    """
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

def add_user(request):
    """
    إضافة مستخدم جديد
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        if username:
            try:
                User.objects.create(username=username, email=email)
                messages.success(request, f'تم إضافة المستخدم {username} بنجاح!')
            except Exception as e:
                messages.error(request, f'خطأ: {str(e)}')
        else:
            messages.error(request, 'اسم المستخدم مطلوب!')
        
        return redirect('user_list')
    
    return render(request, 'users/add_user.html')

def delete_user(request, user_id):
    """
    حذف مستخدم
    """
    try:
        user = User.objects.get(id=user_id)
        username = user.username
        user.delete()
        messages.success(request, f'تم حذف المستخدم {username} بنجاح!')
    except User.DoesNotExist:
        messages.error(request, 'المستخدم غير موجود!')
    except Exception as e:
        messages.error(request, f'خطأ: {str(e)}')
    
    return redirect('user_list')
