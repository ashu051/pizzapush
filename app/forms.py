from .models import Customer
from django import forms
class CustomerProfileForm(forms.ModelForm):
    class Meta():
        model=Customer
        fields=['user','name','locality','pincode','state','nearLandmark']
        widgets={
                'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),
        'pincode':forms.NumberInput(attrs={'class':'form-control'}),
                'nearLandmark':forms.TextInput(attrs={'class':'form-control'}),

        'state':forms.Select(attrs={'class':'form-control'})
        }
# class UserRatingForm(forms.ModelForm):
#     class Meta():
#         model=Product
#         fields=['name','locality','pincode','state','nearLandmark']
#         widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
#         'locality':forms.TextInput(attrs={'class':'form-control'}),
#         'state':forms.TextInput(attrs={'class':'form-control'}),
#         'pincode':forms.NumberInput(attrs={'class':'form-control'}),
#                 'nearLandmark':forms.TextInput(attrs={'class':'form-control'}),

#         'state':forms.Select(attrs={'class':'form-control'})
#         }