from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views  # accounts app’in views'larını çekiyoruz
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('polls/', include(('polls.urls', 'polls'), namespace='polls')),
    path('admin/', admin.site.urls),

    # Doğrudan login ve signup
    path('signup/', account_views.signup_view, name='signup'),
    path('login/', account_views.login_view, name='login'),

    # Diğer accounts yolları
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
