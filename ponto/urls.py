from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('listar_registros/', views.listar_registros, name='listar_registros'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('funcionario/adicionar/', views.adicionar_funcionario, name='adicionar_funcionario'),
    path('funcionario/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionario/deletar/<int:id>/', views.deletar_funcionario, name='deletar_funcionario'),
    path('checkin_checkout/', views.checkin_checkout, name='checkin_checkout'),
]
