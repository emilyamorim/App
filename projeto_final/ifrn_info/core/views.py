from rest_framework import viewsets
from .models import Curso, Setor, Tutorial, TopicoForum, RespostaForum, Feedback
from .serializers import (
    CursoSerializer, SetorSerializer, TutorialSerializer, 
    TopicoForumSerializer, RespostaForumSerializer, FeedbackSerializer
)

# ViewSet para Cursos
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

# ViewSet para Setores
class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

# ViewSet para Tutoriais
class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

# ViewSet para Tópicos do Fórum
class TopicoForumViewSet(viewsets.ModelViewSet):
    queryset = TopicoForum.objects.all()
    serializer_class = TopicoForumSerializer

# ViewSet para Respostas do Fórum
class RespostaForumViewSet(viewsets.ModelViewSet):
    queryset = RespostaForum.objects.all()
    serializer_class = RespostaForumSerializer

# ViewSet para Feedback
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
