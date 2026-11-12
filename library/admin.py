from django.contrib import admin
from .models import *

# Красивые заголовки в админке (это можно оставить)
admin.site.site_header = 'Библиотека вуза'
admin.site.site_title = 'Библиотека вуза'
admin.site.index_title = 'Панель управления'

# Регистрируем все модели стандартным способом (как в лекции)
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass