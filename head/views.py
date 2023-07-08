from django.views.generic import FormView
from django.urls import reverse_lazy
from head.forms import HeadingForm
from head.getHead import Medium


class Heading(FormView):
    form_class = HeadingForm
    http_method_names = {"get", "post"}
    success_url = reverse_lazy("head")
    ua = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36"

    def form_valid(self, form):
        options = {
            "ol": "Ordered Headings",
            "ul": "Unordered Heading",
            "p": "Custom Mark",
        }
        mark = form.cleaned_data.get("mark")
        type_order = form.cleaned_data.get("choice")
        user_agent = self.request.META.get("HTTP_USER_AGENT", "")

        context = self.get_context_data()
        # print(form.cleaned_data)
        med = Medium(
            form.cleaned_data.get("url"), self.ua if user_agent else user_agent
        )

        print(self.request.POST.get("url"))
        extra_context = {
            "output": med.formattedHtml(mark=mark, type_order=type_order),
            "heading": options.get(form.cleaned_data.get("choice"), ""),
            "formData": {
                "url": self.request.POST.get("url", ""),
                "choice": self.request.POST.get("choice", ""),
                "mark": self.request.POST.get("mark", ""),
            },  # You can use "self.request.POST.get("url") for ul only"
            "form": self.form_class(),  # Reset form, you reset it using javascript also.
        }
        return self.render_to_response(context | extra_context)

    # def post(self, request, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     form = self.get_form()
    #     if form.is_valid():
    #         context["output"] = form.cleaned_data["url"]
    #         return self.render_to_response(context)
    #     else:
    #         return self.form_invalid(form)
