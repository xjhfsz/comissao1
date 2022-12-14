from django.shortcuts import render, resolve_url, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse

from .models import Estoque, EstoqueItens
from .forms import EstoqueForm, EstoqueItensForm


def estoque_entrada_list(request):
    template_name = 'estoque_entrada_list.html'
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request, template_name, context)

def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)

def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        item_estoque_formset = inlineformset_factory(
            Estoque,
            EstoqueItens,
            form=EstoqueItensForm,
            extra=1,
        )
        formset = item_estoque_formset(request.POST)
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.instance = form
            formset.save()
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(reverse(url, args=(form.pk,)))
        else:
            context = {'form': form, 'formset': formset}
            return render(request, template_name, context)
    else:
        form = EstoqueForm()
        item_estoque_formset = inlineformset_factory(
            Estoque,
            EstoqueItens,
            form=EstoqueItensForm,
            extra=1,
        )
        formset = item_estoque_formset()
        context = {'form': form, 'formset': formset}
        return render(request, template_name, context)

def produto_preco(request):
    template_name = 'hx/produto_preco_hx.html'
    url = request.get_full_path()
    print('url', url)
    print(url.split('-'))
    item = url.split('-')[1]
    produto_pk = list(request.GET.values())[0]
    produto = Product.objects.get(pk=produto_pk)

    context = {'produto': produto, 'item': item[0]}
    return render(request, template_name, context)

def add_row_estoque_items_hx(request):
    template_name = 'hx/row_estoque_items_hx.html'
    form = EstoqueItensForm()
    context = {'form': form}
    return render(request, template_name, context)