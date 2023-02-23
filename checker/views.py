from django.views.generic import TemplateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from checker.tasks import update_product_price_requests_task, update_product_image_requests_task
from checker.forms import CustomUserCreationForm
from checker.models import CheckerProduct, PriceChangeHistory


class DashboardView(TemplateView):

    template_name = "checker/dashboard.html"
    def get(self, request, *args, **kwargs):

        # update_product_price_task.apply_async(kwargs={'user_page_id': 1})
        return render(request, self.template_name)


class PriceUpdateTask(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            update_product_price_requests_task.apply_async(kwargs={'user_product_id': kwargs['pk']})
        return redirect('show-pages')


class ImageUpdateTask(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            update_product_image_requests_task.apply_async(kwargs={'user_product_id': kwargs['pk']})
        return redirect('show-pages')


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
        context['user_product'] = CheckerProduct.objects.filter(user_id=kwargs['user_id'])
        return context


class PriceChangeHistoryView(TemplateView):
    template_name = "checker/report.html"

    def get(self, request, *args, **kwargs):
        context_data = dict()
        context = self.get_context_data(**context_data)
        return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        context = super(PriceChangeHistoryView, self).get_context_data(*args, **kwargs)
        qs = PriceChangeHistory.objects.filter(product_id=5).order_by('-id')[:5]
        context['data'] = list()
        for data in qs:
            context['data'].append(data.price_difference)
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
