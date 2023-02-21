from django.shortcuts import render
from django.shortcuts import render , redirect
from .models import Review
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.urls import reverse
from .ml import GrabModel
from nbs.configurations import config 
from cassandra.cqlengine.management import sync_table
#from .models import ReviewInference

from . import (db , models2)

from django.http import HttpResponse

ReviewInference = models2.ReviewInference 
DB_SESSION = None
my_model = GrabModel()
model = my_model.AI_MODEL

settings = config.get_settings()

@login_required
def add_review(request):
    DB_SESSION = db.get_session()
    sync_table(ReviewInference)

    global model
    final = {}
    if request.method=='POST':
        rev_form = ReviewForm(request.POST)
        if rev_form.is_valid():
            rev = rev_form.save(commit=False)
            rev.owner = request.user
            rev.save() 
            query = rev.review
            final = model.predict_text(query)
            top = final.get('top')
            data={"query":query , **top}
            obj = ReviewInference.objects.create(**data)

            print(obj.query)
            return redirect(reverse('jobs:job_list'))
    else:
        rev_form = ReviewForm()   


    return render(request , 'reviews/reviews.html' , {"form":rev_form}) 
    



