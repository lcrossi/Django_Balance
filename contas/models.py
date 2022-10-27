from django.db import models
from django.db.models.fields import TextField

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True) # Adiciona automaticamente a data

    def __str__(self):
        return self.nome #Nomeando cada entidade de Categoria com o campo "nome"

class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) #Uma transação deve pertencer a uma unica categoria, mas uma categoria pode possuir varias transações

    class Meta:
        verbose_name_plural = 'Transacoes' #Passando como ele deve ser chamado no plural

    def __str__(self):
        return self.descricao #Nomeando as transações com a descrição