from django.views.generic import TemplateView
from django.shortcuts import render
from checker.tasks import debug_task


class DashboardView(TemplateView):

    template_name = "checker/dashboard.html"

    def get(self, request, *args, **kwargs):

        debug_task.apply_async()
        return render(request, self.template_name)
