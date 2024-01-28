from django.contrib import admin
from .models import Client, Order, Items


class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone_number', 'address', 'date']
    ordering = ['date']
    list_filter = ['date']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'
    readonly_fields = ['date']
    fieldsets = [
        (
            'Имя',
            {
                'description': 'Имя Клиента',
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Электронная почта',
            {
                'description': 'Электронная почта',
                'classes': ['wide'],
                'fields': ['email'],
            },
        ),
        (
            'Номер телефона',
            {
                'description': 'Номер телефона',
                'classes': ['wide'],
                'fields': ['phone_number'],
            },
        ),
        (
            'Адрес клиента',
            {
                'description': 'Адрес',
                'classes': ['collapse'],
                'fields': ['address'],
            },
        ),
        (
            'Дата и время',
            {
                'description': 'Дата и время',
                'classes': ['wide'],
                'fields': ['date_and_time_registration'],
            },
        ),
    ]





class ItemsAdmin(admin.ModelAdmin):

    list_display = ['title', 'description', 'price', 'quantity', 'picture', 'date']
    ordering = ['date', 'price']
    list_filter = ['date', 'price']
    search_fields = ['title']
    search_help_text = 'Поиск по названию'
    readonly_fields = ['date']
    fieldsets = [
        (
            'Название',
            {
                'description': 'Название товара',
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Описание',
            {
                'description': 'Описание товара',
                'classes': ['collapse'],
                'fields': ['description'],
            },
        ),
        (
            'Цена',
            {
                'description': 'Цена',
                'classes': ['wide'],
                'fields': ['price'],
            },
        ),
        (
            'Количество',
            {
                'description': 'Количество',
                'classes': ['wide'],
                'fields': ['quantity'],
            },
        ),
        (
            'Дата и время',
            {
                'description': 'Дата и Время',
                'classes': ['wide'],
                'fields': ['date'],
            },
        ),
        (
            'Изображение',
            {
                'description': 'Изображение товара',
                'classes': ['wide'],
                'fields': ['picture'],
            },
        ),
    ]
