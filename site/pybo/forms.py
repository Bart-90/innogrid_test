from django import forms
from pybo.models import world

class worldForm(forms.ModelForm):
    class Meta:
        model = world
        fields = ['CONTINENT', 'COUNTRY', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8']
        labels = {
            'CONTINENT' : '대륙',
            'COUNTRY' : '나라이름',
            'p1' : 'p1',
            'p2' : 'p2',
            'p3' : 'p3',
            'p4' : 'p4',
            'p5' : 'p5',
            'p6' : 'p6',
            'p7' : 'p7',
            'p8' : 'p8',
        }
