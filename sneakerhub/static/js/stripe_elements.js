var stripe_public_key = document.getElementById('id_stripe_public_key').textContent.slice(1, -1);
var stripe_client_secret = document.getElementById('id_client_secret').textContent.slice(1, -1);
var stripe = Stripe(stripe_public_key);

var elements = stripe.elements();
var style = {
    base: {
        color: '#1a1a1a',
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '14px',
        backgroundColor: '#fff',
        border: 'none',
        '::placeholder': {
            color: '#aab7c4',
            fontStyle: 'italic'
        }
    },
    invalid: {
        color: '#fa755a',
        iconColor: '#fa755a',
        borderColor: '#fa755a'
    }
};
var card = elements.create('card', {style: style, hidePostalCode: true});
card.mount('#card-element');

card.on('focus', function() {
    document.getElementById('card-element').classList.add('StripeElement--focus');
});
card.on('blur', function() {
    document.getElementById('card-element').classList.remove('StripeElement--focus');
});

// Handle real-time validation errors
card.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Hanlde form submission 

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {

    console.log("Submit button clicked");
    event.preventDefault();
    
    stripe.confirmCardPayment(stripe_client_secret, {
        payment_method: {
            card: card,
            billing_details: {
                name: 'Jenny Rosen'
            }
        }
    }).then(function(result) {
        if (result.error) {
            // Show error to your customer
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // The payment has been processed!
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});