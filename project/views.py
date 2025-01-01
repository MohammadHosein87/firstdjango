from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from .models import Post
import datetime as dt
import jalali_date as jdate
from django.utils.timezone import localtime
import pytz

import mysql


def persian_num(text: str) -> str:
    return text.replace('1', '۱').replace('2', '۲').replace('3', '۳').replace('4', '۴').replace('5', '۵').replace('6',
                                                                                                                  '۶').replace(
        '7', '۷').replace('8', '۸').replace('9', '۹').replace('0', '۰')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    # تبدیل زمان UTC به منطقه ایران
    iran_tz = pytz.timezone('Asia/Tehran')
    created_at_iran = localtime(post.created_at).astimezone(iran_tz)

    # استخراج تاریخ و زمان شمسی
    the_date = created_at_iran.date()
    the_time = persian_num(created_at_iran.strftime('%H:%M'))
    jalali_date = persian_num(str(jdate.date2jalali(the_date)).replace('-', '/'))

    return render(request, 'post_detail.html', {
        'post': post,
        'date': jalali_date,
        'time': the_time
    })