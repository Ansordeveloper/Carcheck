from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cars'
    verbose_name = "Машины, особые метки и периоды владения"
