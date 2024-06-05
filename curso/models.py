from django.db import models

class Curso(models.Model):
    apresentacao = models.CharField(max_length=50)
    objectivos = models.CharField(max_length=50)
    competencias = models.CharField(max_length=50)

    def _str_(self):
        return f"Apresentação: {self.apresentacao} objetivos: {self.objectivos} competencias: {self.competencias}"


class area_Cientifica(models.Model):
    area = models.CharField(max_length=50)

    def _str_(self):
        return f"Area: {self.area} "

class disciplina(models.Model):
    nome= models.CharField(max_length=50)
    linguagemProgramacao = models.CharField(max_length=50, default='Python')
    ano= models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    curricular_IUnit_Readable_Code = models.CharField(max_length=50)

    def _str_(self):
        return f"Disciplina: {self.nome}, ano: {self.ano}, semestre: {self.semestre}, ects: {self.ects}, Codigo: {self.curricular_IUnit_Readable_Code} "

class projeto(models.Model):
    projeto = models.CharField(max_length=50)
    disciplina = models.ForeignKey(disciplina, on_delete=models.CASCADE, related_name='projetos')
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.CharField(max_length=50)
    conceitos_aplicados = models.CharField(max_length=50)
    link_video = models.CharField(max_length=50)
    link_gitHub = models.CharField(max_length=50)

    def _str_(self):
        return f"O projeto '{self.projeto}' desenvolvido no {self.semestre}º semestre do {self.ano}º ano\nDescrição: {self.descricao}\nConceitos: {self.conceitos_aplicados}\nLinks: {self.link_video}, {self.link_gitHub} "


class Docente(models.Model):
    nome = models.CharField(max_length=50)
    disciplinas = models.ManyToManyField(disciplina)

    def _str_(self):
        return f"{self.nome} leciona: {self.disciplinas}"
