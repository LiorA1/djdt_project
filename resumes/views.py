from django.shortcuts import render


from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls.base import reverse
from django.db.models import Q, Count
# Create your views here.

from resumes.models import Resume, Tag
from django.views.generic import ListView


from django.contrib.auth.models import User


import time


# Create your views here.
def home(request):
    time.sleep(2)
    return render(request, 'resumes/home.html')


class ResumeListView(ListView):
    """Display all the resumes"""
    model = Resume
    ordering = ['-created_at']
    # template_name = "resumes/<modelName>_list.html"
    queryset = Resume.objects.prefetch_related('tags', 'author')

    def get_queryset(self):
        base_queryset = super(ResumeListView, self).get_queryset()

        # Check for searchTerm existence
        searchTerm = self.request.GET.get("search", False)

        if searchTerm:
            tags_required = Tag.objects.tags_id_from_str(searchTerm)

            # ordering attributes kept
            ordering = self.get_ordering()
            if not ordering:
                ordering = []
            else:
                ordering = self.ordering[:]
            ordering.insert(0, '-score')

            # Query which resumes have the wanted tags, order by the match score.
            q_Query = Q(tags__in=tags_required)
            # res_queryset = base_queryset.filter(tags__isnull=False).distinct().annotate(score=Count('tags', filter=q_Query)).filter(score__gt=0).order_by(*ordering)

            res_queryset = base_queryset.filter(tags__isnull=False).distinct().annotate(score=Count('tags')).filter(q_Query, score__gt=0).order_by(*ordering)

        else:
            res_queryset = base_queryset.fetch_store_resume_list()

        return res_queryset
