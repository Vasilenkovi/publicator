from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from publications.models import Publication, Author

User = get_user_model()


class AuthorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = ['affiliation']


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1',
                  'password2',]


class UserEditForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name',]


class AuthorEditForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = ['affiliation']



class PublicationForm(forms.ModelForm):
    class Meta:
        exclude = ('author', 'is_published', 'created_at')
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.Textarea
        }
        model = Publication
