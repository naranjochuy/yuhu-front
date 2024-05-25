from django import forms


class InputForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": "3"}))
    email = forms.EmailField(max_length=50)
    expiration_date = forms.DateField(
        input_formats=("%Y-%m-%d",),
        help_text="Example of the format: 2024-05-24"
    )
