from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.core.paginator import Paginator
from .Search import MyIndexReader as MyIndexReader
from .Search import QueryRetreivalModel as QueryRetrievalModel
from .Search import ExtractQuery as ExtractQuery
from .Search.Classes import Document
from .Search.Classes import Query
import pandas as pd

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def searchrecipe(request):
  data = request.GET['search']
  context={}
  if 'search_list' not in request.session or data+': recipes' not in request.session or data not in request.session['search_list']:
    query = ExtractQuery.ExtractQuery()
    pquery = query.getProcessedQuery(data)
    index = MyIndexReader.MyIndexReader()
    qModel = QueryRetrievalModel.QueryRetrievalModel(index)
    results = qModel.retrieveQuery(pquery, 1)
    recipes = []
    for result in results:
      title = result.getDocNo()
      url = index.getURL(index.getRecipeId(result.getDocNo()))
      highlight = result.getHighlights()
      recipes.append({'title':title,'url':url,'highlight':highlight})
    if 'search_list' not in request.session:
      request.session['search_list'] = [data]
    else:
       request.session['search_list'].append(data)
    request.session[data+': recipes'] = recipes
  if data+': recipes' in request.session  :  
    p = Paginator(request.session[data+': recipes'], 20)  # creating a paginator object  
    page_number = request.GET.get('page')
    try:
      page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
      page_obj = p.page(1)
    except EmptyPage:
      page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj,'search':data}
  return render(request, 'searchrecipe.html', context)
