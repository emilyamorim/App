from django.contrib import admin
from .models import Curso, Setor, Tutorial, TopicoForum, RespostaForum, Feedback

admin.site.register(Curso)
admin.site.register(Setor)
admin.site.register(Tutorial)
admin.site.register(TopicoForum)
admin.site.register(RespostaForum)
admin.site.register(Feedback)
