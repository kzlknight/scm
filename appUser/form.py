# from django import forms
# from appUser.models import WebUser
#
#
# class WebUserModelForm(forms.ModelForm):
#     class Meta():
#         model = WebUser
#         fields = '__all__'
#
#     def clean(self):
#         # name 长度大于1小于等于16
#         name = self.cleaned_data['name']
#         if not name or not len(name) <=16:
#             raise forms.ValidationError('name')
#         # tel 存在
#         tel = self.cleaned_data['tel']
#         if tel or len(tel) <= 11:
#             raise forms.ValidationError('tel')
#         # gender
#         gender = self.cleaned_data['gender']
#         if not gender in [0,1]:
#             raise forms.ValidationError('gender')
#         # introduction
#         introduction = self.cleaned_data['introduction']
#         if introduction and len(introduction) >=200:
#             raise forms.ValidationError('introduction')
#         # location
#         location = self.cleaned_data['location']
#         if location and len(location) >=100:
#             raise forms.ValidationError('locatiion')

