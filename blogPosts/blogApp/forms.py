from blogApp.models import BlogPost
from django import forms
from django.contrib.auth.models import User

from blogApp.models import UserInfo


class AddPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super(AddPostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"


class EditInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        exclude = ('user','image', 'blockedUsers')

    def __init__(self, *args, **kwargs):
        super(EditInfoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

class AdminEditForm(forms.ModelForm):
    class Meta:
        model=User
        exclude = ('username', 'password', 'groups', 'last_login', 'user_permissions', 'date_joined', 'is_superuser', 'is_staff', 'is_active')

    def __init__(self, *args, **kwargs):
        super(AdminEditForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
