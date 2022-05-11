from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    first_name = models.CharField(help_text='Nombre', max_length=128, blank=False)
    last_name = models.CharField(help_text='Apellido', max_length=128, blank=False)
    email = models.EmailField(help_text='Correo Electrónico',
                            unique=True, blank=False)
    
    # Número de legajo/expediente o libreta universitaria.
    file_number = models.CharField(help_text='Número de Legajo/Expediente o Libreta Universitaria: xxxxxxx',
                                max_length=20, unique=True, blank=False)
    address = models.CharField(help_text='Dirección', max_length=255, default='')
    phone_number = models.CharField(help_text='Número de teléfono',
                                    max_length=64, default='')


    class Meta:
        # Modifico el nombre de la tabla/entidad.
        db_table = 'students'

    def __str__(self):
        return f'Student ID: {self.id} - File Number: {self.file_number}'


class Course(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    course_name = models.CharField(help_text='Nombre de la Materia o Curso',
                                    verbose_name='name', max_length=128, blank=False)
    course_duration = models.PositiveSmallIntegerField(help_text='Duración de la Carrera o Curso en hs',
                                                    verbose_name='duration', blank=False)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course_name} - {self.id}'

    class Meta:
        db_table = 'courses'


class Career(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, 
                                blank=False)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE,
                                blank=False)
    career_name = models.CharField(help_text='Nombre de la Carrera/Curso', 
                                    verbose_name='name', max_length=128, blank=False)
    year_enrollment = models.CharField(help_text='Año de Inscripción a la Carrera: YYYY',
                                        verbose_name='enrolled', max_length=4,
                                        blank=False)

    def __str__(self):
        return f'{self.career_name} - {self.id}'

    class Meta:
        db_table = 'careers'