
from django.contrib import admin
from django.urls import path,include
from accounts.views import HomeView,SignUpView
from management.views import (UploadGarbageView,DisplayWasteView,
        BuyGarbageView,CleanerView,CleanerDetailView)

from compain_and_notification.views import (ComplainView,NotificationView
    ,DeleteNotification,NotificationDetails)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView,name='homepage'),
    path('accounts/',include('accounts.urls')),
    path('cleaning_kit/',include('cleaning_kit.urls')),
    path('upload_garbage/',UploadGarbageView,name='upload_garbage'),
    path('upload_garbage/<int:id>/',UploadGarbageView,name='upload_garbage'),
    path('display_garbage/',DisplayWasteView,name='display_garbage'),
    path('buy_garbage/<slug:slug>/<int:id>/',BuyGarbageView,name='buy_garbage'),
    path('cleaner/',CleanerView,name='cleaner'),
    path('cleaner_details/<int:id>/',CleanerDetailView,name='cleaner_details'),
    
    path('complain/<int:id>/',ComplainView,name="complain"),
    path('notifications/<int:id>/',NotificationView,name="notifications"),
    path('delete_notification/<int:id>/',DeleteNotification,name="delete_notification"),
    path('notification_details/<int:id>/',NotificationDetails,name='notification_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)