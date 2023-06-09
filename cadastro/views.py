from rest_framework import viewsets 
from cadastro.models import Cadastro
from cadastro.serializer import CadastroSerializer

class CadastrosViewSet(viewsets.ModelViewSet):
    "Exibindo todos os cadastros"
    queryset = Cadastro.objects.all()

    serializer_class = CadastroSerializer

