from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.html import escape, mark_safe
from .models import User, Property
from .forms import PropertyForm

# Create your views here.
@login_required(login_url='login')
def index(request):

    if request.method == 'GET':
        try:
            properties = Property.objects.filter(user=request.user).order_by('-pk')
        except ObjectDoesNotExist:
            properties = None

    elif request.method == 'POST':
        # To know how to sort
        how = request.POST['sort_by']
        
        if how == 'time':
            try:
                properties = Property.objects.filter(user=request.user).order_by('-pk')
            except ObjectDoesNotExist:
                properties = None
        elif how == 'name_asc':
            try:
                properties = Property.objects.filter(user=request.user).order_by('property_name')
            except ObjectDoesNotExist:
                properties = None 
        elif how == 'name_desc':
            try:
                properties = Property.objects.filter(user=request.user).order_by('-property_name')
            except ObjectDoesNotExist:
                properties = None 
        elif how == 'date_asc':
            try:
                properties = Property.objects.filter(user=request.user).order_by('registry_date')
            except ObjectDoesNotExist:
                properties = None 
        elif how == 'date_desc':
            try:
                properties = Property.objects.filter(user=request.user).order_by('-registry_date')
            except ObjectDoesNotExist:
                properties = None 

    return render(request, 'realtorhub/index.html', {
        'properties': properties,
    })


@login_required(login_url='login')
def add_property(request):
    if request.method == 'POST':
        # Get the form data
        form = PropertyForm(request.POST)

        if form.is_valid(): # check if it's valid, i check for all hte validators defined in the model class
            payment_condition = form.cleaned_data['payment_condition']
            payment_condition = escape(payment_condition).replace('\n', '<br>')
            property_instance = form.save(commit=False) # To create an instnace but not commit, cause user field is still empty
            property_instance.user = request.user
            property_instance.payment_condition = payment_condition
            property_instance.save()
            return redirect(index)

    else:
        # Creating the empty form, if method is GET
        form  = PropertyForm()
    
    return render(request, 'realtorhub/add.html', {
        'form': form,
    })


@login_required(login_url='login')
def property(request, property_id):
    # If the user wants to delete the property
    if request.method == 'POST':

        # Delete the property instance
        Property.objects.get(pk=property_id).delete()

        return redirect('index')

    else:   
        try:
            property = Property.objects.get(pk=property_id)
        except ObjectDoesNotExist:
            return render(request, 'realtorhub/error.html')
        
        return render(request, 'realtorhub/property.html', {
            'property': property,
        })


@login_required(login_url='login')
def edit(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id, user=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('property', property_id=property_id)
        
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'realtorhub/edit.html', {
        'form': form,
        'property_instance': property_instance,
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)

        # If the user exist
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            return render(request, 'realtorhub/login.html', {
                'message': "Invalid username or password.",
            })
    else:
        return render(request, 'realtorhub/login.html')


def logout_view(request):
    logout(request)
    return redirect(index)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']

        # Ensure passwords match each other
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'realtorhub/register.html', {
                'message': 'Passwords must match.'
            })
        
        if not username or not password:
            return render(request, 'realtorhub/register.html', {
                'message': 'Must provide Username and Password'
            })

        try:
            user = User.objects.create(username=username)
            user.set_password(password)
            user.save()
        except IntegrityError:
            return render(request, 'realtorhub/register.html', {
                'message': 'Username already taken'
            })

        return redirect(index)

    else:
        return render(request, 'realtorhub/register.html')
    

def search(request):
    # Get the name user searched for
    query = request.POST['name'].strip()

    properties = get_list_or_404(Property.objects.all()) # Getting all the properties 

    results = [] # Empty list to store all the matched properties

    # To find the properties which matches with the name user searched for
    for property in properties: # Looping over all the properties
        for index, character in enumerate(query): # Looping over every character of the query
            if character != property.property_name[index]:
                break
        else:
            # It means that the query matches with the property_name
            results.append(property) # The matched property_name will be added to the results list
    
    results.reverse() # Reverse the results, so the result which is most similar comes first

    return render(request, 'realtorhub/search.html', {
        'properties': results,
    })