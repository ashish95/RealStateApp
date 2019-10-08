from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .models import Listing
from realtors.models import Realtor
from .choices import state_choices,bedroom_choices,price_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        'listings':paged_listings 
    }

    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):

    listing = get_object_or_404(Listing,pk=listing_id)

    # mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'listing':listing
    }

    return render(request, 'listings/listing.html',context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    context = {
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings' : queryset_list 
    }
    return render(request, 'listings/search.html',context)
