from django.shortcuts import render, reverse, redirect
from todo_item.models import ListItem
from main.models import ListModel
from todo_item.forms import ItemForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from copy import copy
import json


class ItemView(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('registration:login')
    model = ListItem
    template_name = 'list.html'
    paginate_by = 6
    ordering = ['created', 'name']
    context_object_name = 'lists'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = super().get_queryset()
        return queryset.filter(list_model_id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        list_ = ListModel.objects.select_related('user').get(id=pk)
        context['user_name'] = list_.user.username
        context['list_name'] = list_.name
        context['pk'] = pk
        return context


@login_required(login_url=reverse_lazy('registration:login'))
def item_view(request, pk):
    list_ = ListModel.objects.select_related('user').get(id=pk)
    list_items = ListItem.objects.filter(list_model=list_)

    context = {
        'lists': list_items,
        'user_name': list_.user.username,
        'list_name': list_.name,
        'pk': pk,
    }
    return render(request, 'list.html', context)


class CreateItemView(LoginRequiredMixin, generic.CreateView):
    model = ListItem
    template_name = 'new_item.html'
    form_class = ItemForm
    login_url = reverse_lazy('registration:login')

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('item:item', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['pk'] = pk
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        query_dict = kwargs.get('data')
        pk = self.kwargs.get('pk')

        if query_dict:
            query_dict = copy(query_dict)
            query_dict['list_model'] = pk
            kwargs['data'] = query_dict

        return kwargs


@login_required(login_url=reverse_lazy('registration:login'))
def create_view(request, pk):
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(
            data={
                'name': request.POST['name'],
                'expare_date': request.POST['expare_date'],
                'list_model': pk
            }
        )
        if form.is_valid():
            success_url = reverse('item:item', kwargs={'pk': pk})
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk
    }
    return render(request, 'new_item.html', context)


@login_required(login_url=reverse_lazy('registration:login'))
def edit_item_view(request, pk):
    item = ListItem.objects.get(id=pk)

    if request.method == 'POST':
        form = ItemForm(
            data={
                'name': request.POST['name'],
                'expare_date': request.POST['expare_date'],
                'list_model': item.list_model
            },
            instance=item
        )

        if form.is_valid():
            success_url = reverse('item:item', kwargs={'pk': item.list_model_id})
            form.save()
            return redirect(success_url)
    else:
        form = ItemForm(instance=item)

    context = {
        'form': form,
        'pk': pk,
        'list_model_id': item.list_model_id
    }
    return render(request, 'edit_item.html', context)


@login_required(login_url=reverse_lazy('registration:login'))
def delete_item_view(request):
    body = json.loads(request.body.decode())
    id_ = int(body.get('id', 0))

    item = ListItem.objects.filter(
        id=id_,
        list_model__user=request.user
    ).first()

    if item:
        item.delete()
        return HttpResponse(status=201)
    return HttpResponse(status=404)


@login_required(login_url=reverse_lazy('registration:login'))
def is_done_item_view(request):
    body = json.loads(request.body.decode())
    id_ = int(body.get('id', 0))

    if id_:

        item = ListItem.objects.filter(id=id_).first()

        if item:
            item.is_done = not item.is_done
            item.save()
            return HttpResponse(status=201)

    return HttpResponse(status=404)
