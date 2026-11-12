from django.db import models

MAX_LENGTH = 255


class Faculty(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название факультета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО автора')
    description = models.TextField(null=True, blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True,
                              verbose_name='Фотография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Publisher(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование издательства')
    city = models.CharField(max_length=MAX_LENGTH, null=True, blank=True,
                            verbose_name='Город')
    logo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True,
                             verbose_name='Логотип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Book(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование книги')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    year = models.PositiveIntegerField(default=2024, verbose_name='Год издания')
    isbn = models.CharField(max_length=MAX_LENGTH, verbose_name='ISBN')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True,
                              verbose_name='Обложка')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 verbose_name='Категория')
    author = models.ForeignKey(Author, on_delete=models.PROTECT,
                               verbose_name='Автор')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True,
                                  verbose_name='Издательство')

    def __str__(self):
        return f"{self.name} ({self.year})"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Reader(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='ФИО читателя')
    ticket_number = models.CharField(max_length=MAX_LENGTH, verbose_name='Номер билета')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True,
                              verbose_name='Фотография')
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT,
                                verbose_name='Факультет')

    def __str__(self):
        return f"{self.name} ({self.ticket_number})"

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Читатель')
    taken_at = models.DateField(verbose_name='Дата выдачи')
    due_at = models.DateField(verbose_name='Срок возврата')
    returned = models.BooleanField(default=False, verbose_name='Возвращена')

    def __str__(self):
        return f"{self.book.name} → {self.reader.name}"

    class Meta:
        verbose_name = 'Выдача'
        verbose_name_plural = 'Выдачи'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    reader_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя читателя')
    rating = models.PositiveIntegerField(default=5, verbose_name='Оценка')
    text = models.TextField(verbose_name='Текст отзыва')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')

    def __str__(self):
        return f"{self.reader_name} → {self.book.name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'