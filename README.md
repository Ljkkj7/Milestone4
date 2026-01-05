# SneakerHub — Full-Stack E-commerce Web Application

## 📘 Project Overview

SneakerHub is a full-stack e-commerce web application designed for sneaker enthusiasts and small retailers/brands. It allows users to browse, search, and purchase trainers from independent listers (2nd hand) & independent/small brands or creators. The site integrates with Stripe for payments and provides user authentication, product & user reviews, and order management.

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
├─ Sneakerhub/
│  ├─ core/
│  ├─ marketplace/
│  ├─ account/
│  ├─ listings/
│  └─ sneakerhub/
├─ templates/
├─ static/
├─ media/
├─ manage.py
└─ requirements.txt
```

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
pip install -r requirements.txt
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
```

### 5. Run migrations & start server

```bash
python manage.py migrate
python manage.py runserver
```

---

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

- **Marketplace tests**: [marketplace/tests.py](marketplace/tests.py#L1-L200)

  - Purpose: Unit tests for the `Sneaker` model, basic marketplace views, and admin-related behavior.
  - Key test classes & cases:

- **Account tests**: [account/tests.py](account/tests.py#L1-L60)

  - Purpose: Placeholder file currently.
  - Add tests for authentication flows (signup, login, logout), profile views, and permission checks.

- **Checkout tests**: [checkout/tests.py](checkout/tests.py#L1-L60)
  - Purpose: Placeholder file currently.
  - Add tests for cart-to-checkout flow, Stripe webhook handling (use mocks), and order creation/validation.

## 🚀 Deployment Guide

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

## 🧰 Developer Workflow

- Use Git feature branches (e.g. `feature/checkout`, `fix/payment-error`).

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

---
