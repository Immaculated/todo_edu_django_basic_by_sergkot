# УРОК №1
Команды работы с виртуальным окружением (venv)
```
deactivate 
# Linux / Mac
source venv/bin/activate
# Windows
venv/Scripts/activate.bat
```

Документация  
https://www.djangoproject.com/  

https://djbook.ru/rel3.0/#

Основные команды Django
```
# Установка 
pip install Django
# Создание нового проекта
django-admin startproject todo
# Создание нового app (эпликейшн)
python manage.py startapp main
# показать всё миграции
python manage.py showmigrations
# Создать миграции после изменения моделей
python manage.py makemigrations
# Применить миграции (создать\изменить таблицы)
python manage.py migrate
```

ДЗ
```
1. Создать еще один app "todo_item"
   python manage.py startapp todo_item
2. Закомитить и запушить изменения в GIT
3. Прислать ссылку с pull request
вида https://github.com/sergkot2020/todo/pull/1
4. Установить Postgresql 
```

# УРОК №2
## План занятия:
### Донастройка окружения  
- обзор пред. урока  
- структура django-app (связка model -> view -> url)
- настройка run\debug и первый запуск django сервера
- DBeaver создание БД для проекта
    https://dbeaver.io/download/  
- Подключение Postgres  
- Создание супер-пользователя  
- Миграции 
- Служебные таблицы django
### Обновляем requirements.txt
- pip freeze > requirements. txt   
### HTTP, клиент-сервер
- HTTP (основные типы запросов\ответов)
- Пользовательские сесии
- Куки

### Шаблоны
- синтаксис шаблонов (if\for)
- templatetags

------------------------------------------------------------

### структура django-app (связка model -> view -> url)
- migrations - Папка в которой хрнятся все изменения в Базе Данных
- admin.py - Файл для работы с админкой
- apps.py - служебный файл с именем app
- models.py - файл с моделями/таблицами баз данных 
- test.py - файл с тестами приложения
- views.py - файл с вьюхами (фунцкии обработки запросов от пользователя)

### настройка run\debug и первый запуск django сервера  

- Включение django-support в проекте  

![support](img/django_support.png)  

- Настройка run/debug  

![runner](img/run.png)  

### DBeaver создание БД для проекта  

- создание подключения к БД

![dbeaver](img/dbeaver.png)  

- создание новой базы **todo**

## Подключение Postgres  

- Какие БД поддерживает джанга
- Почему PostgresSQL?  
https://postgrespro.ru/education/courses
- Установка драйверов
```
pip install psycopg2-binary
pip install psycop2
```  

- Прописать базу в settings.py
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "127.0.0.1",
        "NAME": "todo",
        "USER": "postgres",
        "PASSWORD": "pasword",
        "PORT": 5432
    }
}
```
- Миграции  
https://docs.djangoproject.com/en/3.0/topics/migrations/
```yaml
python manage.py migrate
python manage.py makemigrations
python manage.py showmigrations
```
- Создание суперпользователя
```yaml
python manage.py createsuperuser
```

## Templates
- подключение шаблона main
- синтаксис шаблонов
```python
# Переменные
{{ variable }}

# Использование функций
{{ name|lower }}
{{ name|length }}

# Работа с объектами/словарями
class Man:
    def __init__(self, age, weight)
        self.age = age
        self.weight = weight

man_obj = Man(15, 100)
man_dict = {'age': 45, 'weight': 100}

# в шаблоне 
{{ man_obj.age }} -> 15 
{{ man_dict.age }} -> 15 

# оператор if 
{% if athlete_list %}
    Number of athletes: {{ athlete_list|length }}
{% elif athlete_in_locker_room_list %}
    Athletes should be out of the locker room soon!
{% else %}
    No athletes.
{% endif %}

# цикл for
<ul>
{% for age, weight in man_dict.items %}
    <li>Возраст: {{ age }} Вес: {{ weight }}</li>
{% endfor %}
</ul>

# Использование своих тегов
{{ get_count }}
# передача аргументов в тег, можно так же в выржание if или for
arg = 'some argument'
{% if arg|get_count %}

```
- функция **render**
```python
data = {
    'lists': [
        {'name': 'Работа', 'is_done': True, 'date': '01.12.2019'},
        {'name': 'Дом', 'is_done': False},
        {'name': 'Учеба', 'is_done': True}
    ],
    'user_name': 'Admin',
}


def main_view(request):
    context = data
    return render(request, 'index.html', context)
```  

https://docs.djangoproject.com/en/3.0/ref/templates/  

## Д\З
- Повторить проделанные нами операции по подключению БД
- Создать новое приложение(app) **django-admin startapp list_item**
- Написать к нему вьюху
- Сделать шаблон(template) по аналогии с main и заполнить данными из словаря

- Добавить стиль CSS "id_done" в верстку
- *Создать свой **templatetag**, и с помощью него реализовать следующую задачу 
(на главной странице).  
У нас на странице создается столько строк, сколько мы передаем строк данных,
но выглядит не очень красиво если строк мало. 
Нужно (только средствами языка шаблонов) сделать так, чтобы
если нам передается строк меньше чем **6шт**, добить пустыми div блоками 
страницу, чтобы в сумме было 6шт блоков.  
-> Например 3 заполненных, 3 пустых.  
-> Если передаем 5 строк с данными то соответсвенно 5 заполненных 1 пустой.  
-> Если передаем 8 строк с данными - 8 заполненных блоков.  

Пример:  
![img](img/1.png)


Ссылка на документацию:  
https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/  
 
Не забываем также создать папку **templatetags**, в которой нужно разместить модуль с функцией тега:  
![dir](img/2.png)  


Также нужно дополнительно зарегистрировать нашу библиотеку тегов в 
**settings.py**  
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'main.templatetags'
]
```
И подгрузить библиотеку тегов на страницу шаблона:  
![dir](img/3.png)

# УРОК №3
## План урока
- Разбор ДЗ
    - про имена переменных\функций
    - константы
    - докстринги
    - перенос длинных строк
    - глубина вложенности условий (меньше 4)
- пакетные зависимости  
    pip freeze > requirements. txt 
- служебный таблицы Django (пользователь \ хранение паролей)
- Пользовательские сессии
- Куки

- Наследование шаблонов
- Оптимизация роутинга URL-адресов
- DEBUG Pycharm
    - Навигация 
    - Debug циклов
    - Watches
------------------------------------------------------------------------------
## Наследование шаблонов
- теги block, extend
```
{% extends 'master.html' %}

{% block title %}
    <title>Главная</title>
{% endblock %}

{% block name_list %}
    <div class="table-data_table-header-item-1">TO DO List</div>
{% endblock %}
```
## Оптимизация роутинга URL
- функций include, и app_name = 'main'
```python


# \todo\todo\urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('list/', include('list.urls')),
]

# \todo\main\urls.py
app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('create/', create_new_list, name='create')
]
```
- Обрашение в темплейте по app_name
```python
 <a href='{% url "main:create" pk=list.id %}'>
```

## DEBUG
### Запуск дебаггера
![debugger](img/debug.png)
### Установка break-point
![bp](img/bp.png)
### Панель управления
![dash](img/dashboard.png)
-------------------------------------------------------------------------
## ДЗ
- Найти причину ошибки
    - Указать номер элемента на котором ломается алгоритм
    - Указать сам этот элемент
- Исправить алгоритм (чтобы функция отработала до конца и
распечатала результат)  

```python
# Данные data.pkl

# Алгоритм debug.py
import datetime
import pickle


def get_array():
    with open('data.pkl', 'rb') as file:
        return pickle.load(file)


def merge(left_arr, right_arr):
    i = 0
    j = 0
    len_left = len(left_arr)
    len_right = len(right_arr)
    result = []
    while i < len_left and j < len_right:
        left = left_arr[i]
        right = right_arr[j]
        if left_arr[i] < right:
            result.append(left)
            i += 1
        else:
            result.append(right)
            j += 1
    result.extend(left_arr[i:])
    result.extend(right_arr[j:])
    return result


def merge_sort(array):
    e = len(array)
    s = 0
    if (e - s) > 1:
        medium = int((s + e) / 2)
        left_arr = merge_sort(array[s:medium])
        right_arr = merge_sort(array[medium:e])
        return merge(left_arr, right_arr)
    return array


def run(func, array):
    start = datetime.datetime.now()
    print('=' * 20, f' START {func} ', '=' * 20)
    print('START: ', start)
    print('first 50 sorted words:', func(array[:])[:50])
    finish = datetime.datetime.now()
    print('FINISH: ', finish)
    print('RESULT: ', finish - start)


if __name__ == '__main__':
    arr = get_array()
    run(merge_sort, arr)
```

# УРОК №4
Рассмотрим:
- Проектирование БД 
    - Нормальные формы таблиц\отношений   
    https://habr.com/ru/post/254773/  
    

- Создание модели ListModel, типы данных
- Дескрипторы
- Подключение модели к Админке  
- Менеджер модели objects
- ленивый queryset
    - когда вычисляется queryset
--------------------------------------------------------------------------
## Django ORM
Архитектура MVC  
![mvc](img/4.png)

ORM (англ. Object-Relational Mapping, рус. объектно-реляционное отображение, или 
преобразование) — технология программирования, которая 
связывает базы данных с концепциями объектно-ориентированных языков программирования  

**Django ORM Cookbook**  
https://prglb.ru/3h66k

**Офиц. документация**  
https://docs.djangoproject.com/en/3.0/ref/models/querysets/#


main\admin.py
```python
from django.contrib import admin
from main.models import ListModel


class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'user']
    list_filter = ['created', 'name', 'is_done', 'user']
    search_fields = ['name', 'user']


admin.site.register(ListModel, ListAdmin)
```
- Дескрипторы
```python
class AgeCheck:
    """
    Дескриптор
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 18:
            raise ValueError('Меньше 18 лет')
        instance.__dict__[self.name] = value


class Human:

    age = AgeCheck()

    def __init__(self, name, age):
        self.name = name
        self.age = age


man = Human('Bob', 15)
```
- Менеджер модели objects, и основные его методы
```python
item = Model.objects.get(id=1)
items = Model.objects.filter(id=1)
item.name = 'New name'
item.save()
item.delete()
order_by('id')
ListItem.objects.filter(list__user__username='Admin')

# Создание Нового объекта в БД
new_list = ListModel(
        name='Новый список2',
        user=request.user,

    )
new_list.save()
```
- QuerySet => SQL 
- Ленивый QuerySet  

![cat](img/5.png)

- ? дебагер с SQL запросами
```python
LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}
```
# ДЗ
- Оптимизировать HTML из шаблона list.html
c использованием шаблона master.html

- Создать новую модель ItemModel  
```
expare_date = models.DateTimeField(blank=True)
```
https://docs.google.com/spreadsheets/d/1He-IVLLfwQv6MOhD6RbKyt3sItyfoAXgc98_c3ZSIo8/edit?usp=sharing

- Добавить  ItemModel в Админку
    - Наполнить тестовыми данными
    
- Поправить view в todo_item
    - сделать по аналогии в main получение данных из базы. 
```
ListModel.objects.filter(
        user=request.user,
        list_id=1
    )
```

# УРОК №5
Рассмотрим:
- Отношения один ко одному, один ко многим, многие ко многим
- ленивый queryset
    - когда вычисляется queryset
 
- url адреса "<int:pk>" 
- Django-form
## Отношения один ко одному, один ко многим, многие ко многим  
https://github.com/sergkot2020/bars_atestation/blob/master/Django.ipynb
    
## Когда вычисляется queryset

- Итерация. QuerySet является итеративным, и он выполняет свой запрос к базе данных при первой итерации по нему. Например, это напечатает заголовок всех записей в базе данных:
```
for e in Entry.objects.all():
    print(e.headline)
```

Примечание: не используйте это, если все, что вы хотите сделать, это определить, существует ли хотя бы один результат. Более эффективно использовать exists().

- Срезы. Как объяснено в Ограничение QuerySet, QuerySet может быть нарезан, используя синтаксис Python для срезов массивов. Срез невычисленного QuerySet обычно возвращает другой невычисленный QuerySet, но Django выполнит запрос к базе данных, если вы используете параметр «step» синтаксиса среза, и вернет список. Срез QuerySet, который был вычислен, также возвращает список.
Также обратите внимание, что даже если срез невычисленного QuerySet возвращает другой невычисленный QuerySet, дальнейшее его изменение (например, добавление дополнительных фильтров или изменение порядка) недопустимо, поскольку это плохо переводится в SQL и не будет иметь четкого значения.

- Pickling/Кэширование. См. следующий раздел для получения подробной информации о том, что происходит при pickling QuerySets. Для целей этого раздела важно, чтобы результаты считывались из базы данных.

- repr(). QuerySet вычисляется, когда вы вызываете repr() для него. Это удобно для интерактивного интерпретатора Python, поэтому вы можете сразу увидеть свои результаты при интерактивном использовании API.

- len(). QuerySet вычисляется, когда вы вызываете len() для него. Это, как вы могли ожидать, возвращает длину списка результатов.

Примечание. Если вам нужно только определить количество записей в наборе (и вам не нужны фактические объекты), гораздо эффективнее обрабатывать количество на уровне базы данных, используя SQL SELECT COUNT (*). Именно по этой причине Django предоставляет метод count().

- bool(). Тестирование QuerySet в логическом контексте, например, с использованием bool(), or, and или оператора if, вызовет выполнение запроса. Если есть хотя бы один результат, QuerySet равен True, иначе False. Например:
- list(). Принудительное вычисление QuerySet путем вызова list() для него. Например: entry_list = list(Entry.objects.all())

```
if Entry.objects.filter(headline="Test"):
```

## Url адреса с передачей id

```
 path('post/<int:pk>/', views.post_detail, name='post_detail'),
```  
Обращение к URL адресу в шаблоне
```python
<a href="{% url "list_item:list_item" pk=list.id %}">
```

"<int:pk>"  означает, что Django ожидает целочисленное значение и преобразует его в представление — переменную pk.

# УРОК №6
## Django form
### Регистрация и логин
https://docs.djangoproject.com/en/3.0/ref/forms/api/
- Новое **application** для регистрации пользователей
- Форма регистрации пользователя
```python
class CustomUserCreationForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    С обязательными полями: ['username', 'password', 'email']
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
```

- Шаблон формы регистрации + csrf 

```python
 <form class="registration_form_class" action="{% url "registration:registration" %}" id="registration_form" method="POST">
   {% csrf_token %}
    <p class="form_class_name-field"> Имя</p>
      {{ form.username }}
    <p class="form_class_name-field">e-mail</p>
      {{ form.email }}
    <p class="form_class_name-field"> Пароль</p>
      {{ form.password1}}
    <p class="form_class_name-field">Подтверждение пароля</p>
        {{ form.password2}}
</form>
```
- Форма Логина
```python
class LoginForm(forms.Form):

    login = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput(attrs={'id': 'input_field_email-id'})
    )
    password = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.PasswordInput()
    )
```
- View обработка регистрационных данных
```python
def create_user(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, 'registration.html', {'form': form})
```  
- View для логина
```python
def login_view(request):
    """
    Контроллер, который рендерит страницу авторизации.
    В случае успешной авторизации редиректит на главную
    """
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        success_url = reverse('main:main')

        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(success_url)

    return render(request, 'login.html', {'form': form})
```
- Форма нового списка
```python
class ListForm(forms.ModelForm):
    """
    Форма списка
    """
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
```
- view нового списка
```python
def create_new_list(request):
    """
    Обработка запроса на создание нового списка
    """
    form = ListForm()
    success_url = reverse('main:main')

    if request.method == 'POST':
        name = request.POST.get('name')
        form = ListForm({
            'name': name,
            'user': request.user
        })

        if form.is_valid():
            form.save()

            return redirect(success_url)

        form = ListForm()

    return render(request, new_list_item.html, {'form': form})
```
- Ошибки валидации (non_field_error)
```python
error_messages = {
    NON_FIELD_ERRORS: {
        'unique_together': "Имя уже существует",
    }
}
```
- Декоратор \ декоратор с параметром для проверки пользователя а аутентификацию

## Д\З
- Форма создания нового 'элемента списка' (кнопка "+")
- Вьюха создания нового 'элемента списка'
- Шаблон создания 'элемента списка'
- *Декоратор для логина

# УРОК №7
- разбор ДЗ
```python
from django.urls import reverse_lazy


def login_decorator(url):
    def wrapper(func):
        def wrapper2(request, *args, **kwargs):
            if request.user.is_authenticated:
                return func(request, *args, **kwargs)
            else:
                return redirect(url)

        return wrapper2

    return wrapper


@login_decorator(url=reverse_lazy('registration:login'))
def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    )
    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)

```
- локализация ошибок
```python
import traceback

def main_view(request):
    
    try:
        lists = ListModel.objects.filter(
            user=request.user,
        )
        context = {
            'lists': lists,
            'user_name': request.user.username
        }
        return render(request, 'index.html', context)
    except:
        print(traceback.format_exc(limit=10))
        raise
```

- Полезная ссылка по работе браузеров  

https://developer.mozilla.org/

- форма редактирования списка
```python
@login_required(login_url=reverse_lazy('registration:login'))
def edit_view(request, pk):
    list_ = ListModel.objects.get(id=pk)

    if request.method == 'POST':
        form = ListForm({
            'user': request.user,
            'name': request.POST.get('name')
        }, instance=list_)

        if form.is_valid():
            success_url = reverse('main:main')
            form.save()
            return redirect(success_url)
    else:
        form = ListForm(instance=list_)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'edit_list.html', context)
```
# Д\З
- Кнопку редактирования элементов списка
- Кнопку удаление СПИСКА
- Кнопку удаления ЭЛЕМЕНТОВ списка
- *Задачка про монтеки
```
В России есть такие монеты:

1 копейка
5 копеек
10 копеек
50 копеек
1 рубль
2 рубля
5 рублей
10 рублей
25 рублей
Нам нужно написать такую функцию, которая бы вернула количество вариантов, каким можно разменять введеную сумму. Например, 10 копеек можно разменять 4 вариантами:

10 копеек
5 + 5 копеек
10 раз по копейке
5 копеек + 5 раз по 1 копейке
```

# УРОК 8
- пагинация
- Generic

## Пагинация (разбиение контента на страницы)
```python
from django.core.paginator import Paginator

PAGE = 6

@login_required(login_url=reverse_lazy('registration:login'))
def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user,
    ).order_by('created')

    paginator = Paginator(lists, PAGE)

    page = request.GET.get('page')
    if not page:
        page = 1

    is_paginated = len(lists) > PAGE
    page_obj = paginator.page(page)

    context = {
        'listmodel_list': page_obj.object_list,
        'user_name': request.user.username,
        'paginator': paginator,
        'is_paginated': is_paginated,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)
```
отрисовка в шаблоне
```python
{% if is_paginated %}
    <div class="table-data__table-row">
        <div class="paginator_class">
            <ul class="pagination-wrapper_button">
                {% for page in paginator.page_range %}
                    {% if page_obj.number == page %}
                        <li><a class="active" href="{% url 'main:main' %}?page={{ page }}">{{ page }}</a></li>
                    {% else %}
                        <li><a href="{% url 'main:main' %}?page={{ page }}">{{ page }}</a></li>
                    {% endif %}
                {% endfor %}
            </ul>
        </div>
    </div>
{% endif %}
```

Новый css стиль
```css
.paginator_class {
  grid-column: 2/3;
  width: 200px;
  word-break: break-all;
  margin-left: 50px; }
```
## Generic
Документация  

https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Generic_views

https://docs.djangoproject.com/en/3.1/ref/class-based-views/generic-editing/#createview

### ListView
```python
class MainView(LoginRequiredMixin, generic.ListView):

    login_url = reverse_lazy('registration:login')
    model = ListModel
    template_name = 'index.html'
    paginate_by = 6
    ordering = ['created', 'name']
    context_object_name = 'lists'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        return context
```
### CreateView
```python
class CreateView(LoginRequiredMixin, generic.CreateView):

    model = ListModel
    template_name = 'new_list.html'
    form_class = ListForm
    success_url = reverse_lazy('main:main')
    login_url = reverse_lazy('registration:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')

        if query_dict:
            query_dict = copy(query_dict)
            query_dict['user'] = self.request.user
            kwargs['data'] = query_dict

        return kwargs
```


# УРОК 9

## План занятия:
- Dom-дерево (document)
- события

https://learn.javascript.ru/introduction-browser-events
- объект event

https://learn.javascript.ru/obtaining-event-object

- Ассинхронный запрос fetch
    - Функция зачеркивания
    - Функция удаления  (через пост запрос)
- Получение csrf токена из JS
- Дебаг в браузере

## Dom-дерево
![dom](img/dom.png)

https://learn.javascript.ru/dom-nodes  

Виртуальный DOM  
https://habr.com/ru/post/256965/

## JavaScript - работа c элементами дерева
- Ассинхронный запрос fetch
    - Функция зачеркивания
    - Функция удаления  (через пост запрос)
    
https://learn.javascript.ru/fetch

- Получение csrf токена из JS
- Дебаг в браузере
```javascript
//Получение csrf tokena из cookie

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
```
- Функция зачеркивания
```css
.table-row_table_cell-1 {
    cursor: pointer;
}
```
```javascript
// Добавление удаление css класса
const element = document.getElementById("div1");
element.classList.add("otherclass");
element.classList.remove("otherclass");
```
```javascript
function isDoneRequest(event) {
    const id = event.target.id.split('_').pop();
    const listId = document.location.href.split('/').pop();
    const url = document.location.href.replace(`/${listId}`, '/done/');
    return fetch(url, {
        method: 'POST',
        headers: new Headers({'X-CSRFToken': token}),
        redirect: 'follow',
        body: JSON.stringify({id: id})
    }).then(respone => {
        if (respone.status === 201) {
            if (event.target.classList.contains('is_done_text')) {
                event.target.classList.remove('is_done_text');
            } else {
                event.target.classList.add('is_done_text');
            }
        } else {
            alert('Сервер не доступен');
        }
    })
}
```

### Получение в JS данных из контекста
```javascript
const delUrl = JSON.parse('{{ del_url|safe }}');
```

### Функция удаления
```javascript
const delButtons = document.querySelectorAll('.delete_button');

delButtons.forEach(button => {
    button.addEventListener('click', delUrl(genFunc));
});

function DeleteRequest(event) {
    event.preventDefault();
    const url = event.currentTarget.href;
    const pk = url.split('/').pop();
    const listId = generateFunc(pk);
    return fetch(url, {
        method: 'POST',
        headers: new Headers({'X-CSRFToken': csrftoken}),
        redirect: 'follow'
    }).then(
        response => {
            if (response.status === 200) {
                document.getElementById(listId).remove();
            }
        }
    );
}
```
- Создание HTML блока средствами js
```javascript
function createMessageBlock(title, text) {
    const divBlock = document.createElement('div');
    divBlock.className = 'wrapper__auth';
    divBlock.id = "id_new_edit_block";
    divBlock.innerHTML = `<div class="auth__column_right"><div class="auth__column_right_form"><div class="auth__column_right_form__header">${ title }</div><div id="message_text"> ${ text }</div><div class="auth__column_right__form_footer"><label class="form_footer_button-submit"><input type="submit" form="auth_form" value="" style="display: none"><a href="#" id="login-submit-btn"><div class="auth__button_submit"  ><span>&#10004</span></div></a></label><label class="form_footer_button-cancel"><a href="#" id="cancel_btn"><div class="auth__button_submit" id="login-cancel-btn" ><span>&#9587</span></div></a></label></div></div></div>`;
    return divBlock;
}
```
## ДЗ 
- Переделать **item_view** на generic.ListView
- Cделать пагинцию в шаблоне list.html
- Переделать **create_view** в todo_item на generic.CreateView 
- Прочитать статьи про DOM.

- *Написать логику, зачеркивания Списка, когда 
  Переопределив метод save() в модели элементов списка.
- **Функция удаления элемента списка на JS


# Урок 9

## ТЕСТЫ
### Виды тестирования (как тестировать)
- Автоматизированное
```
– это выполнение плана тестирования (частей вашего приложения, 
которые вы хотите протестировать, а так же порядок, в котором вы хотите их тестировать, 
и ожидаемые результаты) с помощью сценария тестирования
```
- Ручное
```
Чтобы получить полный набор ручных тестов, все, что вам нужно сделать, 
это составить список всех функций, которыми обладает ваше приложение, 
список различных типов входных данных, которые оно может принять, 
и все ожидаемые результаты. 
Теперь, каждый раз, когда вы будете вносите изменения в свой код, 
вам нужно просмотреть каждый элемент в этом списке и проверить его правильность.

Это не похоже на веселье, не так ли?
```
### Виды тестирования (что тестировать)
- Регрессионное тестирование
```
Мы тестируем продукт на его работоспособность после внесения изменений в функциональность.
```
- Unit (модульное) тестирование
```
Мы также тестируем на корректность отдельные компоненты (модули) программы.
```
- Интеграционное тестирование
```
Мы проверяем на корректность взаимодействия между компонентами одной системы и правильности обработки информации.
```
- Дымовое тестирование
```
Мы также проводим цикл тестов на проверку функциональности программного 
продукта после его сборки (добавления нового кода либо исправления ошибок в коде).
В случае использования метода непрерывной интеграции (Continious Integration) 
сборка программного продукта производится ежедневно, 
поэтому проведение дымового тестирования позволяет вовремя выявить и устранить критичные ошибки, 
тем самым сэкономив время на тестирование сборки.
```

- Тестирование безопасности
```
Наша команда тестирует продукты на наличие уязвимостей в безопасности программного обеспечения, 
в частности безопасности подключений, безопасности данных и безопасности доступа.
```

- Системное тестирование
```
Для того, чтобы убедиться в том, что интегрированная и готовая к эксплуатации система 
соответствует заявленным функциональным требованиям, мы проводим системное тестирование.
```
- Тестирование процесса инсталляции
```
Мы анализируем ресурсы, необходимые для установки программного обеспечения, 
корректность регистрации программы в операционной системе, 
поведение программы при ее обновлении, корректность деинсталяции программы и пр.
```
- Стресс-тестирование (Пример яндекс-танк)
```
Мы также проводим тестирование на отказ системы и ее способность к восстановлению при возникновении сбоев.
```
- Юзабилити-тестирование
```
Мы проверяем продукт на удобство и простоту использования путем имитации поведения 
пользователей либо посредством экспертной оценки результатов тестирования юзабилити продукта фокус группой.
```

## Функциональное тестирование (**Selenium**, **Pytest**)  

Веб-драйвры selenium  

https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/

https://github.com/mozilla/geckodriver/releases

- Установка 
```
pip install selenium
pip install pytest-django
```
- pytest.ini
```
[pytest]
DJANGO_SETTINGS_MODULE = todo_list_ngu.settings
```

Настрйка запуска тестов в pycharm

![pytest](img/pytest.png)

- Тестовый сценрий ввода логина и пароля и перехода на главную
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import time


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


def test_open_login_page(live_server, new_client):
    """
    Новый пользователь Юля, открывает
    браузер и решает ввести 'http://127.0.0.1:8000/'.
    Попадает на страницу с title 'Войти' и надписью ВХОД
    Вводит тестовый логин и пароль и переходит на главную
    """
    browser = webdriver.Chrome('C:\\todo_list_ngu\\todo_list_ngu\chromedriver.exe')
    browser.get(live_server.url)
    assert browser.title == 'Войти'
    login = browser.find_element_by_name('login')
    password = browser.find_element_by_name('password')
    login.send_keys(TEST_CLIENT['username'])
    password.send_keys(TEST_CLIENT['password'])

    button = browser.find_element_by_id('login-submit-btn')
    button.click()

    # WebDriverWait(browser, 3).until(es.title_is('Главная'))
    time.sleep(3)
    assert browser.title == 'Главная'
```
- Pytest фикстуры
```python
import pytest
from django.contrib.auth.models import User


TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


@pytest.fixture
def new_client(db):
    new_client = User(
        username=TEST_CLIENT['username'],
        email=TEST_CLIENT['email'],
    )
    new_client.set_password(TEST_CLIENT['password'])
    new_client.save()
    return new_client
```

# УРОК 10

## Unit и интеграционные тесты
- Тестирование view
```python
from django.test import Client
from django.shortcuts import reverse
import pytest

TEST_CLIENT = {
    'username': 'TestUser',
    'email': '123@123.ru',
    'password': 'q1w2e3r4TT',
}


TEST_ITEM = 'Тестовый список дел'


@pytest.mark.django_db
def test_create_new_list(new_user):
    """
    Проверка вьюхи создание нового списка дел
    """
    csrf_client = Client(enforce_csrf_checks=True)
    csrf_client.login(
        username=new_user.username,
        password=TEST_CLIENT['password'],
    )
    response = csrf_client.get(reverse('main:create'))

    html = response.content.decode()

    assert '<title>Новый список</title>' in html

    csrf = csrf_client.cookies['csrftoken']
    response = csrf_client.post(
        reverse('main:create'),
        data={
            'name': TEST_ITEM,
            'csrfmiddlewaretoken': csrf.value
        })
    url = response.url

    assert response.status_code == 302

    response = csrf_client.get(url)
    html = response.content.decode()

    assert TEST_ITEM in html


```

- Тестирование form
- Тестирование моделей
```python
@pytest.mark.django_db
def test_save_method(new_list):
    """ Тест метода save в модели ListItem """
    list_item = ListItem.objects.create(
        name='Какое то дело',
        list=new_list
    )
    assert new_list.is_done is False
    list_item.is_done = True
    list_item.save()
    assert new_list.is_done
    list_item.is_done = False
    list_item.save()
    assert new_list.is_done is False
```

## Тестовое покрытие (Пример travis)
Мы проверяем, насколько набор проводимых тестов соответствует требованиям к продукту, 
а также анализируем полноту проверки тестами кода разработанной части продукта.  

```python
pip install pytest-cov
```
Поправить файл 
```python
[pytest]
DJANGO_SETTINGS_MODULE = todo.settings
addopts = --nomigrations --cov=. --cov-report=html
```
## TDD и BDD
- ТDD
 
![tdd](img/tdd.png)

- BDD => Cucumber/Behave
https://habr.com/ru/post/216923/  

```
FEATURE 1: На счету есть деньги+
GIVEN счет с деньгами
AND валидную карточку
AND банкомат с наличными
WHEN клиент запрашивает наличные
THEN убедиться, что со счета было списание
AND убедиться, что наличные выданы
AND убедиться, что карточка возвращена
```

### Рекомендации по литературе
Персиваль - TDD

## ДЗ
- Тест **list_item_view**
- Тест **create_item_view** 
- Тест c Selenium на создание нового списка дел
- *Довести покрытие тестов до 80%
