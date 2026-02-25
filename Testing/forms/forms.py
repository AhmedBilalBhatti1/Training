from django import forms
from .models import MyModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        return MyModel.objects.create(name=self.cleaned_data['name'],email=self.cleaned_data['email'],message=self.cleaned_data['message'])        
    
    class Meta:
        model = MyModel
        fields = '__all__'

    def __str__(self):
        return self.name