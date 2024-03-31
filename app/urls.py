from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordReset,MyPassworChangeForm,MySetPasswordForm
from django.contrib import admin



urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryVievs.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetails.as_view(),name="product-detail"),
    path("profile/",views.ProfileView.as_view(),name='profile'),
    path("address/",views.address,name='address'),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(),name="updateAddress"),
    path("add-to-cart/",views.add_to_cart,name='add-to-cart'),
    path("cart/",views.show_cart,name='show-cart'),
    path("checkout/",views.checkout.as_view(),name='check-out'),
    path("search/",views.search,name="search"),
    path("wishlist/",views.show_wishlist,name="showwishlist"),
    
    path("pluscart/",views.pluscart,name="pluscart"),
    path("minuscart/",views.minuscart,name="minuscart"),
    path("removecart/",views.removecart,name="removecart"),
    path("pluswishlist/",views.pluswishlist),
    path("minuswishlist/",views.minuswishlist),
    #login auTH
    path("registration/",views.CustomerRegistrationForm.as_view(),name="registration"),
    path("accounts/login/",auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    
    path("passwordchange/",auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPassworChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path("passwordchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name="passwordchangedone"), 
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),
    
    path("password-reset/",auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordReset),name="password_reset"),
    path("password-reset/done/",auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>",auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name="password_reset_confirm"),
    path("password-reset-complete/",auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password_reset_complete"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header="Mert Daily"
admin.site.site_title="Mert Daily"
admin.site.site_index_title="Welcome to Mert Daily Shop"

