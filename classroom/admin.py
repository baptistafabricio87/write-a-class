from django.contrib import admin

from classroom.models import Lesson, Comentario, Like


class LessonAdmin(admin.ModelAdmin):
    """Admin View for Lesson"""

    prepopulated_fields = {'slug': ('autor', 'titulo')}
    list_display = (
        'titulo',
        'autor',
    )


admin.site.register(Lesson, LessonAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    """Admin View for Comentario"""

    list_display = (
        'lesson',
        'conteudo',
    )


admin.site.register(Comentario, ComentarioAdmin)


class LikeAdmin(admin.ModelAdmin):
    """Admin View for Like"""

    list_display = (
        'lesson',
        'usuario',
    )


admin.site.register(Like, LikeAdmin)
