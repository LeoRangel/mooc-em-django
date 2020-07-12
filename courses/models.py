from django.db import models
from django.urls import reverse

# Create your models here.

# Para adicionar mais funções ao manager de bd do django (orm)
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # Manager customizado (orm)
    objects = CourseManager()

    # O que mostrar na tabela do admin /
    # Representação do modelo. Ex: quando chamar só 'course' vai retornar o name
    def __str__(self):
        return self.name

    # Retorna url. Ex: Para chamar nos links
    def get_absolute_url(self):
        return reverse('courses:course_detail', args=(self.slug,))

    # Nomes que serão mostrados no admin
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']
