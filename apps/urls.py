from django.urls import path

from apps.views import home, portfolio, register, login, service_update, questionnaire_update, blog_update, blog, \
    skills_update, portfolio_update, contact_form

urlpatterns = [
    path('index/<int:pk>/', home, name='index'),
    path('portfolio/<int:pk>/', portfolio, name='portfolio'),
    path('blog/<int:pk>/', blog, name='blog'),
    path('signup/', register, name='signup'),
    path('', login, name='login'),
    path('updete_servis/<int:pk>/', service_update, name='service_update'),
    path('updete_anketa/<int:pk>/', questionnaire_update, name='questionnaire_update'),
    path('updete_blog/<int:pk>/', blog_update, name='blog_update'),
    path('updete_skill/<int:pk>/', skills_update, name='skills_update'),
    path('updete_portfolio/<int:pk>/', portfolio_update, name='portfolio_update'),
    path('contact_us/<int:pk>', contact_form, name='contact_us')

]
