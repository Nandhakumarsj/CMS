from django import forms
# from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'email')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'mb-3 block w-full px-3 py-2 bg-white border border-slate-400 rounded-md placeholder:italic text-md shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-2 focus:ring-sky-500 focus:caret-indigo-900'})
        self.fields['content'].widget.attrs.update(
            {'class': 'mb-3 block w-full px-3 py-2 bg-white h-48 border border-slate-400 rounded-lg scroll-smooth placeholder:italic text-md shadow-sm placeholder-slate-400 focus:outline-none focus:border-sky-700 focus:ring-1 focus:ring-sky-500 resize-none overflow:hidden'})
        self.fields['email'].widget.attrs.update(
            {'class': 'mb-3 block w-full px-3 py-2 bg-white border border-slate-400 rounded-md text-sm shadow-sm placeholder:italic placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-1 focus:ring-sky-500 disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-600 focus:invalid:ring-pink-500 peer'})
        self.fields['photo'].widget.attrs.update(
            {'class': 'transition ease-in-out delay-150 hover:-translate-y-1 hover:translate-x-1 hover:scale-60 duration-300 my-4 text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-md file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100'})
        
