from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MessageForm
from user.models import User
from .models import Messages


class MessagesListView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, user_id=None):
        if not request.user.is_authenticated:
            return redirect(self.login_url)

        contact_user = None
        if user_id:
            contact_user = User.objects.get(id=user_id)
            sent_messages = Messages.objects.filter(sender=request.user, receiver=contact_user).order_by('-sent_time')
            received_messages = Messages.objects.filter(sender=contact_user, receiver=request.user).order_by('-sent_time')
        else:
            sent_messages = Messages.objects.filter(sender=request.user).order_by('-sent_time')
            received_messages = Messages.objects.filter(receiver=request.user).order_by('-sent_time')

        context = {
            'sent_messages': sent_messages,
            'received_messages': received_messages,
            'contact_user': contact_user,
            'form': MessageForm()
        }
        return render(request, 'massage.html', context=context)


class SendMessage(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, user_id):
        if not request.user.is_authenticated:
            return redirect(self.login_url)

        contact_user = User.objects.get(id=user_id)
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = contact_user
            if message.content or message.image or message.video or message.audio:
                message.save()
            return redirect('conversation:message-with-user', user_id=user_id)
        else:
            sent_messages = Messages.objects.filter(sender=request.user, receiver=contact_user).order_by('-sent_time')
            received_messages = Messages.objects.filter(sender=contact_user, receiver=request.user).order_by('-sent_time')
            context = {
                'sent_messages': sent_messages,
                'received_messages': received_messages,
                'contact_user': contact_user,
                'form': form
            }
            return render(request, 'massage.html', context=context)



class HomeView(View):
    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users,
        }
        return render(request, 'home.html', context=context)


