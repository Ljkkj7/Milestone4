# SneakerHub — Full-Stack E-commerce Web Application

## 📘 Project Overview

SneakerHub is a full-stack e-commerce web application designed for sneaker enthusiasts and small retailers. It allows users to browse, search, and purchase trainers from multiple brands. The site integrates with Stripe for payments and provides user authentication, product reviews, and order management.

---

## 🎯 Purpose & Target Audience

**Purpose:** Provide a functional and stylish online storefront for sneaker lovers and retailers.
**Target audience:** Sneaker collectors, streetwear enthusiasts, small footwear retailers.

---

## 🧱 Tech Stack

**Frontend:** HTML5, Tailwind CSS (or Bootstrap), JavaScript, Django Templates
**Backend:** Python 3.11+, Django 4.x
**Database:** PostgreSQL (production) / SQLite (development)
**Payments:** Stripe Checkout / Payment Intents API
**Deployment:** Render / Heroku / Railway
**Version Control:** Git & GitHub
**Testing:** Django TestCase / pytest-django

---

## 🗂️ Project Structure

```
sneakerhub/
├─ apps/
│  ├─ core/
│  ├─ sneakers/
│  ├─ brands/
│  ├─ cart/
│  ├─ checkout/
│  ├─ orders/
│  └─ accounts/
├─ templates/
│  ├─ base.html
│  ├─ sneakers/
│  ├─ cart/
│  └─ checkout/
├─ static/
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

- Browse sneakers by brand, size, and color
- Add sneakers to cart and checkout securely with Stripe
- User authentication and profiles
- Product CRUD (admin/staff)
- Order management and receipts
- Product reviews and star ratings
- Responsive & accessible UI

---

## 🧮 Data Model Overview

**Core Models:**

- `Brand` — sneaker brand (Nike, Adidas, etc.)
- `Sneaker` — product details (price, stock, size, color, release_date)
- `SneakerReview` — user reviews
- `Order`, `OrderItem`, `Payment` — order and transaction data

ER Diagram example:

```
Brand 1—∞ Sneaker 1—∞ SneakerReview
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
- Cart logic (add, remove, update)
- Checkout integration (mock Stripe webhooks)
- Authentication and permissions

---

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
