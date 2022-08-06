from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

from core.models import CustomUser

# Create your forms here.

class CustomUserCreationForm(UserCreationForm):
                
    class Meta:
        model = CustomUser
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)