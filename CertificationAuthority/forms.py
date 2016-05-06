from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth import authenticate
from . import models

class AuthForm(forms.Form):
    username = forms.CharField(max_length=32, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(_("Sorry, that login was invalid. Please try again."))
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

KEY_USAGE = (
    ('digitalSignature',        ),
    ('nonRepudiation',          ),
    ('keyEncipherment',         ),
    ('dataEncipherment',        ),
    ('keyAgreement',            ),
    ('keyCertSign',             ),
    ('cRLSign',                 ),
    ('encipherOnly',            ),
    ('decipherOnly',            )
)

KEY_USAGE_EXT = (
    ('serverAuth',      _('SSL/TLS Web Server Authentication.')),
    ('clientAuth',      _('SSL/TLS Web Client Authentication.')),
    ('codeSigning',     _('Code signing.')),
    ('emailProtection', _('E-mail Protection (S/MIME).')),
    ('timeStamping',    _('Trusted Timestamping')),
    ('OCSPSigning',     _('OCSP Signing')),
    ('ipsecIKE',        _('ipsec Internet Key Exchnage')),
    ('msCodeInd',       _('Microsoft Individual Code Signing (authenticode)')),
    ('msCodeCom',       _('Microsoft Commercial Code Signing (authenticode)')),
    ('msCTLSign',       _('Microsoft Trust List Signing')),
    ('msEFS',           _('Microsoft Encrypted File System')),

)

class TemplateCertForm(forms.ModelForm):
    name = forms.CharField(max_length=32, required=True)
    cert_usage = forms.MultipleChoiceField(choices=KEY_USAGE, required=False, widget=forms.CheckboxSelectMultiple)
    cert_ext_usage = forms.MultipleChoiceField(choices=KEY_USAGE_EXT, required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = models.sslTemplate
        fields = ('cert_usage', 'cert_usage_ext')
