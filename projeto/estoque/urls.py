from django.urls import path
from projeto.estoque import views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>/', v.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
    path('add-row/', v.add_row_estoque_items_hx, name='add_row_estoque_items_hx'),
    path('produto/preco/', v.produto_preco, name='produto_preco'),
]