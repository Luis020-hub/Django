from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['matricula', 'nome', 'data_nascimento', 'email', 'telefone', 'data_ingresso']
        error_messages = {
            'matricula': {
                'unique': "Já existe um aluno com esta matrícula. Por favor, insira uma matrícula diferente."
            }
        }
