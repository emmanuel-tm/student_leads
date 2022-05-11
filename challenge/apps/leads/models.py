from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(help_text='Correo Electrónico',
                            unique=True, blank=False)
    
    # Número de legajo/expediente o libreta universitaria.
    file_number = models.CharField(help_text='Número de Legajo/Expediente',
                                max_length=20, unique=True, blank=False)
    address = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=64, default='')


    class Meta:
        # Modifico el nombre de la tabla/entidad.
        db_table = 'Students'

    def __str__(self):
        return f'Student ID: {self.id} - File Number: {self.file_number}'
