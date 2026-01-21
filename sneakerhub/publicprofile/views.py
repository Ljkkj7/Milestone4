from django.shortcuts import render
from django.contrib.auth.models import User
from reviews.models import Review

# Create your views here.
def publicProfileView(request, profile_user):
    
    user = User.objects.get(id=profile_user)
    viewing_user = request.user

    sneakers = user.sneakers.filter(is_sold=False)
    sold_sneakers = user.sneakers.filter(is_sold=True).order_by('updated_at')

    reviews = Review.objects.filter(reviewed_user=user)
    review_items = []
    for review in reviews:
        reviewer = User.objects.get(id=review.reviewer_id.id)
        reviewed = User.objects.get(id=review.reviewed_user.id)
        review_items.append({
            'id': review.id,
            'reviewer_id': review.reviewer_id.id,
            'reviewer_username': reviewer.username,
            'reviewed_username': reviewed.username,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at,
        })



    context = {
        'profile_user': user,
        'viewing_user': viewing_user,
        'sneakers': sneakers,
        'sold_sneakers': sold_sneakers,
        'review_items': review_items,
    }

    return render(request, 'public_profile.html', context)

