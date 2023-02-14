from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notafiscal/', views.notafiscal, name='notafiscal'),
    path('gestao/', views.gestao, name='gestao'),
    path('qtddecargos/', views.qtddecargos, name='qtddecargos'),
    path('notafiscal2/', views.notafiscal2, name='notafiscal2'),
    path('notafiscal3/', views.notafiscal3, name='notafiscal3'),
    path('notafiscal4/', views.notafiscal4, name='notafiscal4'),
    path('notafiscal5/', views.notafiscal5, name='notafiscal5'),
    path('notafiscal6/', views.notafiscal6, name='notafiscal6'),
    path('notafiscal7/', views.notafiscal7, name='notafiscal7'),
    path('notafiscal8/', views.notafiscal8, name='notafiscal8'),
    path('gestao/cliente/<int:cliente_id>/', views.cliente, name='cliente'),
    path('gestao/<int:id>/', views.notafiscalindividual, name='nota-individual'),
    path('login/', views.login, name='login'),
    path('gestao/search/', views.search, name='search'),
    path('cnpj/', views.cnpj, name='cnpj'),
    path('fatoutros/', views.fatoutros, name='fatoutros'),
    
]