from django.shortcuts import render
from django.views import View


class AssemblyView(View):
    template_name = 'genomic/assembly.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        assembly = {"name": "Tuberculosis",
                    "description": "This genus comprises a number of Gram-positive, acid-fast, rod-shaped aerobic bacteria and is the only member of the family Mycobacteriaceae within the order Actinomycetales. Like other closely related Actinomycetales, such as Nocardia and Corynebacterium, mycobacteria have unusually"}
        return render(request, self.template_name, {"assembly": assembly})  # , {'form': form})
