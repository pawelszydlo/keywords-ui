import sys
import time
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.template import RequestContext

from keywords import KeywordFinderCalais, KeywordFinderNLTK, KeywordFinderPython,\
                        KeywordFinderException

from front.forms import KeywordForm
from django.conf import settings

def index(request):
    """ Main (and only) view. Receives POSTed data and calls keyword generators from module """
    form = KeywordForm()
    keywords = []
    error = None
    exec_time = ""

    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            method = form.cleaned_data["method"]
            text = form.cleaned_data["text"]

            start_time = time.time()
            try:
                if method == "nltk":
                    finder = KeywordFinderNLTK()
                elif method == "calais":
                    finder = KeywordFinderCalais(settings.CALAIS_API_KEY)
                else:
                    finder = KeywordFinderPython()
                keywords = finder.get_keywords(unicode(text))
                exec_time = "%.4f s" % (time.time() - start_time)
            except KeywordFinderException:
                error = sys.exc_info()[1]

    c = RequestContext(request, {
        'form': form,
        'keywords': keywords,
        'error': error,
        'time': exec_time,
    })
    return render_to_response('index.html',c)
