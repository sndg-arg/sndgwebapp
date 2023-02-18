from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str
from django.views import View

from bioseq.models.Biodatabase import Biodatabase
from bioseq.models.BiodatabaseQualifierValue import BiodatabaseQualifierValue
from bioseq.models.BioentryQualifierValue import BioentryQualifierValue


class DownloadView(View):

    def get(self, request, *args, **kwargs):
        #genome genes proteins gff gbk

        file_name = "NC_003047.gbk.gz"
        path_to_file = "/home/eze/workspace/sndg/sndg-etl/" + file_name
        response = HttpResponse(open(path_to_file,'rb'),content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
        response['X-Sendfile'] = smart_str(path_to_file)
        return response

    def post(self, request, *args, **kwargs):
        return self.get(request, args, kwargs)
