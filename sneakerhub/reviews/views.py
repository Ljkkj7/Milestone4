from django.shortcuts import render
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

        return render(request, 'review_submitted.html', {'profile_user': profile_user})
    else:
        return render(request, 'submit_review.html', {'profile_user': profile_user})