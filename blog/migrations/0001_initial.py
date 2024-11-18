# Generated by Django 5.0.7 on 2024-09-22 01:30

import blog.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.lecture_quiz_upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CoursesCart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default=0, upload_to=blog.models.course_upload_to)),
                ('price_off', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('is_active', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Grade', to='blog.grade')),
            ],
            options={
                'ordering': ('-upload_date',),
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseLecture', to='blog.course')),
            ],
        ),
        migrations.CreateModel(
            name='QuizChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.question_quiz_upload_to)),
                ('is_true', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice', to='blog.quizquestion')),
            ],
        ),
        migrations.CreateModel(
            name='SubLectureDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(upload_to=blog.models.lecture_document_upload_to)),
                ('number_of_pages', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('video', 'video'), ('document', 'document'), ('quiz', 'quiz')], max_length=150)),
                ('priority', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LectureDocument', to='blog.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='SubLectureQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('points', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('type', models.CharField(blank=True, choices=[('video', 'video'), ('document', 'document'), ('quiz', 'quiz')], max_length=150)),
                ('priority', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LectureQuiz', to='blog.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_questions', models.IntegerField(default=0)),
                ('answers', models.TextField(default='[]')),
                ('right_answers', models.TextField(default='[]')),
                ('degree', models.DecimalField(decimal_places=1, default=0.0, max_digits=5)),
                ('timer', models.IntegerField(default=0)),
                ('start', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserResults', to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QuizResults', to='blog.sublecturequiz')),
            ],
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='blog.sublecturequiz'),
        ),
        migrations.CreateModel(
            name='SubLectureVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('video', models.FileField(upload_to=blog.models.lecture_video_upload_to)),
                ('video_time', models.CharField(blank=True, max_length=150, null=True)),
                ('type', models.CharField(blank=True, choices=[('video', 'video'), ('document', 'document'), ('quiz', 'quiz')], max_length=150)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LectureVideo', to='blog.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('transaction', models.CharField(blank=True, default=blog.models.create_new_ref_number, max_length=10, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='blog.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserCourse', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('video', 'video'), ('document', 'document'), ('quiz', 'quiz')], max_length=200)),
                ('session_id', models.IntegerField(default=0)),
                ('done', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course_progress', to='blog.course')),
            ],
        ),
        migrations.CreateModel(
            name='VideoLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_video_likes', to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_likes', to='blog.sublecturevideo')),
            ],
        ),
    ]