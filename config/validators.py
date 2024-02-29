from django import forms

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError('En Az 3 Herfden Ibaret Olmalidir!!')