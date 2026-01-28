# SneakerHub — Full-Stack E-commerce Web Application

## 📘 Project Overview

SneakerHub is a full-stack e-commerce web application designed for sneaker enthusiasts and small retailers/brands. It allows users to browse, search, and purchase trainers from independent listers (2nd hand) & independent/small brands or creators. The site integrates with Stripe for payments and provides user authentication, product & user reviews, and receipting.

---

## 🎯 Purpose & Target Audience

**Purpose:** Provide a user friendly and easy to use marketplace for people to list old/collectable shoes. To allow creators/artitst's to list their products for money instead of managing their own brand website.
**Target audience:** Sneaker collectors, streetwear enthusiasts, small footwear retailers.

---

## 🧱 Tech Stack

**Frontend:** HTML5, CSS, JavaScript, Django Templates
**Backend:** Python 3.11+, Django 4.x
**Database:** PostgreSQL (production) / SQLite (development)
**Payments:** Stripe Checkout
**Deployment:** Render / Heroku / Railway
**Version Control:** Git & GitHub
**Testing:** Django TestCase / pytest-django

---

## 🗂️ Project Structure

```
MS4/
├─ README.md
├─ requirements.txt
├─ sneakerhub/
│  ├─ account/
│  ├─ cart/
│  ├─ checkout/
│  ├─ core/
│  ├─ creatorspace/
│  ├─ errorhandler/
│  ├─ listings/
│  ├─ marketplace/
│  ├─ publicprofile/
│  ├─ reviews/
│  ├─ seed/
│  │  └─ seed_listings.sql
│  ├─ sneakerhub/        # Django project package
│  ├─ manage.py
│  ├─ static/
│  │  ├─ css/
│  │  ├─ images/
│  │  └─ js/
│  └─ templates/
├─ static/
│  ├─ css/
│  ├─ images/
│  └─ js/
├─ templates/
│  ├─ 404.html
│  ├─ base.html
│  ├─ home.html
│  └─ ...
└─ media/
  ├─ brand_banners/
  ├─ brand_logos/
  ├─ brand_products/
  └─ media/
```

## 🧩 Features

- Browse sneakers by brand, size, and price range
- Add sneakers to cart and checkout securely with Stripe
- User authentication and profiles
- Product CRUD - User marketplace listings
- Brand CRUD - Manage products & brand page
- Order management and receipts
- Product reviews and star ratings
- Responsive & accessible UI

---

## 🧮 Data Model Overview

**Core Models:**

- `Sneaker` — product details (name, brand, size, price, image, created_at, updated_at, owner)
- `UserReview` — user reviews
- `Order`, `OrderItem`, `Payment` — order and transaction data

ER Diagram example:

```
User 1—∞ Sneaker
User 1—∞ UserReview
Sneaker ∞—∞ Order (via OrderItem)
Order 1—1 Payment
```

---

## 💳 Stripe Integration

- Checkout process uses Stripe Payment Intents API.
- Webhooks handle payment success/failure events.
- Confirmation emails and success messages displayed to users.

### Flow:

1. User checks out → create Stripe PaymentIntent.
2. Stripe Checkout → secure payment.
3. Stripe webhook → confirms success and finalizes order.
4. Order receipt sent to user.

---

## User Experience

### User Stories

#### **Customer**

##### **Persona:**

General shopper browsing SneakerHub to buy sneakers.

##### **Story:**

As a customer, I want to quickly find sneakers that match my preferences (brand, size, price, condition), review clear photos and descriptions, add items to a cart, and complete a secure checkout so I can confidently purchase sneakers that fit my needs.

##### **Acceptance Criteria:**

1. Search and filters return relevant results
2. product pages show images, size/condition details, seller info, & shipping estimate
3. checkout integrates with Stripe and sends confirmation email
4. order history displays.

##### **Typical Flow:**

- Search → apply filters → select listing → add to cart → checkout via Stripe → receive confirmation and email receipt.

#### **Brand Owner**

##### **Persona:**

Small brand owner managing official product listings and brand presence.

##### **Story:**

As a brand owner, I want to create and manage a verified brand profile, add official product listings (with variants), view sales analytics, and run promotions so I can grow my brand and convert visitors into customers

##### **Acceptance Criteria:**

1. Brand verification workflow; brand page with logo/banner/bio
2. Listing creation supports sizes, images, quantities & release dates.
3. Dashboard shows sales, top products and wishlists
4. Promotions management and analytics.

##### **Typical Flow:**

Complete verification → create brand page → create products → review analytics.

---

## 🧪 Testing

Run all tests:

```bash
python manage.py test
```

### Test coverage:

- Models (Sneaker, Brand, Order)
- Form Usage (Listing CRUD)
- Cart logic (add, remove, update)
- Checkout integration (mock Stripe webhooks)
- Authentication and permissions

---

### Test Suites (per app)

Below is an overview of each test suite in the project, what they cover, and where to find them.

- **Listings tests**: [listings/tests.py](listings/tests.py#L1-L200)
  - Purpose: Validate the `ListingCreationForm` and the `create_listing` view logic used when users create new sneaker listings.
  - Key test classes & cases:
    - `ListingCreationFormTests`:
      - Valid form submission with all required fields.
      - Missing required fields (e.g., `name`, `brand`, `size`, `price`) should produce form errors.
      - Description validation: rejects descriptions shorter than a minimum length, accepts exact boundary length.
      - Optional image handling: form remains valid without an uploaded image.
    - `createListingViewTests`:
      - Access control: unauthenticated users are redirected to login.
      - GET (authenticated): view returns a form instance in context.
      - POST (authenticated, valid): creates a `Sneaker` instance, sets `owner`, and persists correct field values.
      - POST (invalid): does not create a `Sneaker`, returns the form with errors.
      - Edge cases: description-too-short rejected, and successful submissions redirect appropriately.
  - Important dependencies: `listings.forms.ListingCreationForm`, `marketplace.models.Sneaker`, and the URL name `create_listing`.

- **Marketplace tests**: [marketplace/tests.py](marketplace/tests.py#L1-L200)
  - Purpose: Unit tests for the `Sneaker` model, basic marketplace views, and admin-related behavior.
  - Key test classes & cases:
    - `SneakerModelTests`:
      - Creation of a `Sneaker` instance with expected field values (`name`, `brand`, `size`, `price`, `owner`).
    - `SneakerViewTests`:
      - Basic view smoke test: `marketplace` page returns HTTP 200.
    - `SneakerAdminTests`:
      - Admin user creation and login checks to ensure admin site interactions can be performed in tests.
  - Important dependencies: `marketplace.models.Sneaker`, Django `User` model, and the `marketplace` URL.

- **Account tests**: [account/tests.py](account/tests.py#L1-L60)
  - Purpose: Placeholder file currently.
  - Add tests for authentication flows (signup, login, logout), profile views, and permission checks.

- **Checkout tests**: [checkout/tests.py](checkout/tests.py#L1-L60)
  - Purpose: Placeholder file currently.
  - Add tests for cart-to-checkout flow, Stripe webhook handling (use mocks), and order creation/validation.

---

## ⚙️ Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/<yourusername>/sneakerhub.git
cd sneakerhub
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -m requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the root directory:

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_PUBLISHABLE_KEY=your_stripe_public
STRIPE_WEBHOOK_SECRET=your_webhook_secret
EMAIL_HOST_USER =email_host
EMAIL_HOST_PASSWORD =email_pass
```

### 5. Run migrations & start server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

### On Render / Heroku

1. Push repository to GitHub.
2. Connect Render/Heroku app.
3. Add environment variables in dashboard.
4. Run migrations & collect static files:

   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

5. Ensure `DEBUG=False` and `ALLOWED_HOSTS` are set.

---

## 📖 Documentation

- `README.md` — project overview & setup
- `DEPLOYMENT.md` — hosting and environment setup details
- `TESTING.md` — test plan and TDD evidence

---

## 🧠 Future Enhancements

- AI-based sneaker recommendations
- Limited-edition drop scheduler
- Wishlist & user notifications
- API endpoints for mobile app integration
- Real-time sneaker price comparison

---

## 🏆 Credits

- Developed by:
- Framework:
- Payments: Stripe API
- Icons: Lucide / FontAwesome
- UI Framework:

### External Code

- Django date input [StackOverflow](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django)

---
