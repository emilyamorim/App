from django.db import models

# Modelo para Cursos do IFRN
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# Modelo para os Setores do Campus (Biblioteca, Secretaria, etc.)
class Setor(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# Modelo para os Tutoriais sobre o SUAP e outros sistemas
class Tutorial(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

# Modelo para o Fórum de Dúvidas entre os alunos
class TopicoForum(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class RespostaForum(models.Model):
    topico = models.ForeignKey(TopicoForum, on_delete=models.CASCADE, related_name="respostas")
    usuario = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resposta de {self.usuario} no tópico {self.topico.titulo}"

# Modelo para o Sistema de Feedback dos Alunos
class Feedback(models.Model):
    nome_usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_usuario} - {self.data_envio}"
