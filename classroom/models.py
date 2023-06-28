from django.db import models


class Lesson(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo', blank=False)
    slug = models.SlugField(max_length=55, verbose_name='Slug', blank=False)
    autor = models.ForeignKey(
        'auth.User',
        default=True,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Autor',
    )
    categoria = models.CharField(max_length=50, verbose_name='Categoria')
    conteudo = models.TextField(verbose_name='Conteudo')
    criado_em = models.DateField(auto_now_add=True, verbose_name='Criado Em')
    atualizado_em = models.DateField(
        auto_now=True, verbose_name='Atualizado Em'
    )
    publicado = models.BooleanField(default=False, verbose_name='Publicado')

    class Meta:
        verbose_name = 'Lição'
        verbose_name_plural = 'Lições'
        ordering = ['-criado_em']


class Comentario(models.Model):
    lesson = models.ForeignKey(
        'classroom.Lesson',
        on_delete=models.CASCADE,
        blank=False,
        default=True,
        verbose_name='Lesson',
    )
    usuario = models.ForeignKey(
        'auth.User',
        default=True,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Usuario',
    )
    conteudo = models.CharField(
        max_length=100, blank=False, verbose_name='Comentario'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado Em'
    )
    visivel = models.BooleanField(default=False, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-criado_em']


class Like(models.Model):
    lesson = models.ForeignKey(
        'classroom.Lesson',
        default=True,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Lesson',
    )
    usuario = models.ForeignKey(
        'auth.User',
        default=True,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name='Usuario',
    )
    criado_em = models.DateField(auto_now_add=True, verbose_name='Criado Em')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['-criado_em']
