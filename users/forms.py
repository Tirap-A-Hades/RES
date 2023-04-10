from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
