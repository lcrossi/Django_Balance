from contas.models import Transacao
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import TransacaoForm
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3', 't4']
    data['now'] = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    data['tabela'] = Transacao
    #Pega todas as transações no banco de dados e coloca na var data
    #objects é um manager que é automaticamente criado pelo Django para cada model criado. 
    # Ele é basicamente uma classe com operações de banco de dados como a.first(), .last(), .filter()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None) #Tem algo no form? Se sim -> cria um form com as infos preenchidas

    #Validando e salvando no DB
    if form.is_valid():
        form.save()
        # Finalizado o form, o Django apaga a url e os dados e faz um redirecionamento apropriado para a pagina de listagens 
        return redirect('url_listagem') 
        #return listagem(request) -> retorna os dados para a pagina de listagem
        #Se não for válido ele coloca de volta nos dados da view e devolve

    return render(request, 'contas/form.html', {'form': form}) #É a mesma coisa que escrever data['form'] = form 

def update(request, pk): #pk = primary key
    data={}
    transacao = Transacao.objects.get(pk=pk) #Localiza a transação no db pela primary key e cria um objeto dessa transção
    form = TransacaoForm(request.POST or None, instance=transacao) #O form não começa vazio! Ele puxa os dados do DB 

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['transacao'] = transacao #Enviando o obj transação para poder deletar
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
