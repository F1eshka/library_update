from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    year = models.IntegerField(verbose_name="Год издания")
    genre = models.CharField(max_length=100, verbose_name="Жанр/Стиль")
    publisher = models.CharField(max_length=100, verbose_name="Издательство")
    is_available = models.BooleanField(default=True, verbose_name="Есть в библиотеке?")

    def __str__(self):
        return self.title

# Модель Читателя
class Reader(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    reg_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"