import json
from curso.models import Curso

def load_cursos_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        cursos_data = data['cursos']

        for curso_data in cursos_data:
            Curso.objects.create(
                apresentacao=curso_data['apresentacao'],
                objectivos=curso_data['objectivos'],
                competencias=curso_data['competencias']
            )
