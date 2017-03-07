from django import forms


class UserForm(forms.Form):
    val = forms.CharField(label='Enter either the Users id, username, or email address')

    def get_lookup(self):
        val = self.cleaned_data['val']
        if '@' in val:
            return {'email': val}
        try:
            return {'pk': int(val)}
        except:
            return {'username': val}
