# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from .forms import ReviewForm

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products, 'active_estore': True})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
      # List of active reviews for this product
    reviews = product.reviews.filter(active=True)
    if request.method == 'POST':
        # A review was posted
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            # Create review object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current product to the review
            new_review.product = product
            # Save the review to the database
            new_review.save()
    else:
      if request.user.is_authenticated():
        review_form = ReviewForm(initial = {'email': request.user.email, 'name': request.user.get_full_name()})
      else:
        review_form = ReviewForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'reviews': reviews, 'review_form': review_form,
                   'cart_product_form': cart_product_form, 'active_estore': True})