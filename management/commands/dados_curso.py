import json
from django.core.management.base import BaseCommand
from curso.models import Curso, AreaCientifica, Disciplina, Projeto, Docente, LinguagemProgramacao

class Command(BaseCommand):
    help = 'Importa dados de um arquivo JSON para o banco de dados'

    def handle(self, *args, **kwargs):
        with open('dados_curso.json', 'r') as file:
            data = json.load(file)

            for curso_data in data['cursos']:
                Curso.objects.create(**curso_data)

            for area_data in data['areas_cientificas']:
                AreaCientifica.objects.create(**area_data)

            for disciplina_data in data['disciplinas']:
                Disciplina.objects.create(**disciplina_data)

            for projeto_data in data['projetos']:
                Projeto.objects.create(**projeto_data)

            for docente_data in data['docentes']:
                Docente.objects.create(**docente_data)

            for linguagem_data in data['linguagens_programacao']:
                LinguagemProgramacao.objects.create(**linguagem_data)

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))