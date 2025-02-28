from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet, SetorViewSet, TutorialViewSet, 
    TopicoForumViewSet, RespostaForumViewSet, FeedbackViewSet
)

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'setores', SetorViewSet)
router.register(r'tutoriais', TutorialViewSet)
router.register(r'forum/topicos', TopicoForumViewSet)
router.register(r'forum/respostas', RespostaForumViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
