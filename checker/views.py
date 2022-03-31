from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from checker.tasks import debug_task
from checker.forms import CustomUserCreationForm

from checker.models import UserPage


class DashboardView(TemplateView):

    template_name = "checker/dashboard.html"
    # test_task
    # def get(self, request, *args, **kwargs):
    #
    #     debug_task.apply_async()
    #     return render(request, self.template_name)


class ShowPagesView(TemplateView):
    # strona na ktorej mozna przejrzec aktualne 'strony' uzytkownika i dodac kolejne
    template_name = "checker/show-pages.html"

    def get(self, request, *args, **kwargs):
        context_data = dict()
        if request.user.is_authenticated:
            context_data.update({
                'user_id': request.user.pk
            })
        context = self.get_context_data(**context_data)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super(ShowPagesView, self).get_context_data(*args, **kwargs)
        context['user_pages'] = UserPage.objects.filter(user_id=kwargs['user_id'])
        return context


class UserRegistrationView(TemplateView):

    def get(self, request):
        return render(
            request, "registration/registration.html",
            {"form": CustomUserCreationForm}
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            return render(
                request, "registration/registration.html",
                {"form": CustomUserCreationForm}
            )
