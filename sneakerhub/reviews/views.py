from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Review

# Create your views here.
@login_required
def submitReviewView(request, profile_user):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        reviewer = request.user
        review_profile = User.objects.get(id=profile_user)

        # Create and save the review
        review = Review(
            reviewed_user=review_profile,
            reviewer_id=reviewer,
            rating=rating,
            comment=comment
        )

        review.save()

        return redirect('publicprofile:public_profile', profile_user=profile_user)
    
    else:

        error_meessage = "Invalid Request"

        context = {
            'error_message': error_meessage,
            'profile_user': profile_user,
        }

        return redirect('publicprofile:public_profile', context)

@login_required 
def addReviewView(request, profile_user):
    user = User.objects.get(id=profile_user)

    context = {
        'profile_user': user,
    }

    return render(request, 'reviews/add_review.html', context)

@login_required
def editReviewView(request, review_id):
    review = Review.objects.get(id=review_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        review.rating = rating
        review.comment = comment
        review.save()

        return redirect('publicprofile:public_profile', profile_user=review.reviewed_user.id)
    
    else:
        context = {
            'review': review,
        }

        return render(request, 'reviews/edit_review.html', context)
    
@login_required
def deleteReviewView(request, review_id):
    review = Review.objects.get(id=review_id)
    profile_user_id = review.reviewed_user.id
    review.delete()
    return redirect('publicprofile:public_profile', profile_user=profile_user_id)