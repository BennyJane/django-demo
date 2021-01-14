# django


```bash

# 创建项目
django-admin startproject mysite
cd mysite
python manage.py runserver
python manage.py runserver 8000
python manage.py runserver 0:8000
python manage.py runserver 0.0.0.0:8000

# 创建应用: 需要在项目根目录/mysite 内
python manage.py startapp polls


# 数据库初始化
python manage.py migrate

# 追踪数据库变动，更新迁移文件
python manage.py makemigrations polls
# 查看数据库迁移SQL语句
python manage.py sqlmigrate polls 0001
# 检查项目
python manage.py check
# 更新数据库迁移文件,修改数据库结构
python manage.py migrate

# 进入django的shell模式
python manage.py shell
# from polls.models import Question, Choice


# 创建后台管理员账号: 用户名、邮箱、密码
python manage.py createsuperuser

```
