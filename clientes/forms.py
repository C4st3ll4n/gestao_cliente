from django.forms import ModelForm
from clientes.models import Pessoa


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ["nome", "sobrenome", "idade", "salario", "bio", "foto"]
