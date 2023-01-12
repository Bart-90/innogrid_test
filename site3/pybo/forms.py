from django import forms
from pybo.models import world
from pybo.models import Question, Answer

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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }  

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }