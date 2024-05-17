import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Student
from .forms import StudentForm

logger = logging.getLogger(__name__)


def login_page(request):
    # Usuários e senhas mockados
    usuarios = ['admin', 'luis', 'professor']
    senhas = ['123', '123456', '12345678']

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        logger.info(f"Tentativa de login com usuário: {username} e senha: {password}")

        if username in usuarios:
            index = usuarios.index(username)
            logger.debug(f"Usuário encontrado na lista de usuários: {username}")

            if password == senhas[index]:
                logger.debug(f"Senha correta para o usuário: {username}")
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    logger.info(f"Usuário {username} autenticado com sucesso")
                    return redirect('student_list')
                else:
                    logger.warning(f"Autenticação falhou para o usuário {username}")
                    error_message = "Usuário ou senha incorretos. Tente novamente."
            else:
                logger.warning(f"Senha incorreta para o usuário: {username}")
                error_message = "Usuário ou senha incorretos. Tente novamente."
        else:
            logger.warning(f"Usuário não encontrado na lista de usuários: {username}")
            error_message = "Usuário ou senha incorretos. Tente novamente."

        return render(request, 'login.html', {'error_message': error_message})

    else:
        return render(request, 'login.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student-list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student-create.html', {'form': form})


def student_edit(request, matricula):
    student = get_object_or_404(Student, matricula=matricula)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student-edit.html', {'form': form, 'student': student})


def student_delete(request, matricula):
    student = get_object_or_404(Student, matricula=matricula)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student-delete.html', {'student': student})

def search_students(request):
    matricula = request.GET.get('matricula', '')
    if matricula:
        students = Student.objects.filter(matricula__icontains=matricula)
    else:
        students = Student.objects.all()
    return render(request, 'student-list.html', {'students': students})