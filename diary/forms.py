from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス') # input type email
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea) # textareaタグ

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9' # col-9 横幅９
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください'

        self.fields['title'].widget.attrs['class'] = 'form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'


