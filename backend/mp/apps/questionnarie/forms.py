from django import forms


class QuestionnaireForm(forms.Form):
    title = forms.CharField(label='标题', widget=forms.TextInput(attrs={'class':'form-control col-sm-4', 'required':''}))
    brief = forms.CharField(label='简介', widget=forms.Textarea(attrs={'class':'form-control col-sm-8'}))
    file = forms.FileField(label='', widget=forms.FileInput(attrs={'class':'form-control-file col-sm-4','multiple': True}))