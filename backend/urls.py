"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt import views as jwt_views

from accounts import views as accounts_view
from books import views as books_view
from library_branch import views as library_branch_view
from borrow import views as borrow_view
from backend.custom import dictionaries_views

router = DefaultRouter()
router.register('books', books_view.BookViewSet, base_name='Book')
router.register('categories', books_view.BookCategoryViewSet, base_name='BookCategory')
router.register('authors', books_view.BookAuthorViewSet, base_name='BookAuthor')
router.register('libraries', library_branch_view.LibraryBranchViewSet, base_name='Library_branch')
router.register('borrows', borrow_view.BorrowViewSet, base_name='Borrow')
router.register('users', accounts_view.UserViewSet, base_name='User')
router.register('dictionaries', dictionaries_views.DictionariesViewSet, base_name='Dictionaries')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('rest-auth/', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]