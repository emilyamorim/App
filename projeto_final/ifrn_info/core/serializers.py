from rest_framework import serializers
from .models import Curso, Setor, Tutorial, TopicoForum, RespostaForum, Feedback

# Serializador para Cursos
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

# Serializador para Setores
class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

# Serializador para Tutoriais
class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = '__all__'

# Serializador para Tópicos do Fórum
class TopicoForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicoForum
        fields = '__all__'

# Serializador para Respostas do Fórum
class RespostaForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaForum
        fields = '__all__'

# Serializador para Feedbacks
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
