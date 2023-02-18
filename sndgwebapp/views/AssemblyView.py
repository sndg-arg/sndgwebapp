from django.shortcuts import render
from django.views import View

from bioseq.models.Biodatabase import Biodatabase
from bioseq.models.BiodatabaseQualifierValue import BiodatabaseQualifierValue
from bioseq.models.BioentryQualifierValue import BioentryQualifierValue


class AssemblyView(View):
    template_name = 'genomic/assembly.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)

        biodb = Biodatabase.objects.get(name = kwargs["assembly_id"])

        props = { bqv.term.identifier:bqv.value
                  for bqv in BiodatabaseQualifierValue.objects.filter(biodatabase=biodb)}

        assembly = {
            "id": biodb.biodatabase_id,
            "name": biodb.name,
            "description": biodb.description,
            "props":props
            }
        return render(request, self.template_name, {"assembly": assembly})  # , {'form': form})
