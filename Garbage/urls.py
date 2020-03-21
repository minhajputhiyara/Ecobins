
from django.contrib import admin
from django.urls import path,include
from accounts.views import HomeView,SignUpView
from management.views import UploadGarbageView,DisplayWasteView,BuyGarbageView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='homepage'),
    path('accounts/',include('accounts.urls')),
    path('upload_garbage/',UploadGarbageView,name='upload_garbage'),
    path('display_garbage/',DisplayWasteView,name='display_garbage'),
    path('buy_garbage/<slug:slug>/<int:id>/',BuyGarbageView,name='buy_garbage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)