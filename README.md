# SneakerHub — Full-Stack E-commerce Web Application

<div style="text-align: center;">
    <img src="sneakerhub/static/images/sneakherhubreadmelogo.png">
</div>

## Table of Contents

- [Project Overview](#project-overview)
- [Purpose & Target Audience](#purpose--target-audience)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Features](#features)
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [UX Testing Grid](#ux-testing-grid)
- [Data Model Overview](#data-model-overview)
- [Stripe Integration](#stripe-integration)
- [Testing](#testing)
  - [Test Suites (per app)](#test-suites-per-app)
  - [Test grid](#test-grid)
- [Installation & Setup](#installation--setup)
- [Deployment Guide](#deployment-guide)

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

Core models:

- `Sneaker` (`marketplace.models.Sneaker`)
  - Fields: `name`, `brand`, `size` (Decimal), `price` (Decimal), `description`, `image`, `owner` (FK → `auth.User`), `created_at`, `updated_at`, `is_sold`
  - Owner is the listing user; used by marketplace listings and order items.

- `Review` (`reviews.models.Review`)
  - Fields: `reviewed_user` (FK → `auth.User`), `reviewer_id` (FK → `auth.User`, related_name=`reviews_made`), `rating`, `comment`, `created_at`, `updated_at`
  - Stores ratings/comments between users (sellers/buyers or creators).

- `Brand` (`creatorspace.models.Brand`)
  - Fields: `owner` (FK → `auth.User`), `brand_name`, `brand_bio`, `brand_banner`, `brand_logo`
  - Represents verified brand profiles and owner relationship.

- `BrandCollaborators` (`creatorspace.models.BrandCollaborators`)
  - Fields: `brand` (FK → `Brand`), `collaborator` (FK → `auth.User`), permission booleans (`product_edit_permission`, `product_upload_permission`, `product_delete_permission`, `profile_edit_permission`)
  - Role-based collaborator records with scoped permissions.

- `BrandProducts` (`creatorspace.models.BrandProducts`)
  - Fields: `brand` (FK → `Brand`), `product_name`, `product_description`, `product_image`, `product_sizes` (text), `product_price`, `quantity`, `created_at`, `updated_at`, `release_date`, `is_active`
  - Official brand SKUs / product records (variants stored in `product_sizes` text field).

- `Order` (`checkout.models.Order`)
  - Fields: `user` (FK → `auth.User`), `order_number` (unique), `full_name`, `email`, `phone_number`, `country`, `postcode`, `town_or_city`, `street_address1/2`, `county`, `date`, `delivery_cost`, `order_total`, `grand_total`
  - Order totals are computed from related `OrderItem` lineitems; order number generated on save.

- `OrderItem` (`checkout.models.OrderItem`)
  - Fields: `order` (FK → `Order`, related_name=`lineitems`), `sneaker` (FK → `marketplace.Sneaker`), `line_total`
  - Line total is set to the linked `Sneaker.price` on save; order ↔ items form the order lifecycle.

- `CreatorAccountModel` (`account.models.CreatorAccountModel`)
  - Fields: `user` (FK → `auth.User`), `bio`, `created_at`, `updated_at`
  - Creator/brand owner profile metadata (can be used to store creator-specific information).

- `WishlistItem` (`account.models.WishlistItem`)
  - Fields: `user` (FK → `auth.User`, related_name=`wishlist_items`), `sneaker` (FK → `marketplace.Sneaker`), `added_at`
  - Unique constraint on (`user`,`sneaker`) enforces one wishlist entry per user per sneaker.

ER Overview:

```
auth.User 1—∞ Sneaker
auth.User 1—∞ Review (as reviewer and reviewed_user)
Brand 1—∞ BrandProducts
Brand 1—∞ BrandCollaborators
Order 1—∞ OrderItem → Sneaker
auth.User 1—∞ Order
auth.User 1—∞ WishlistItem
```

ER Diagrams:

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

##### **Testing Matrix (Customer)**

| Acceptance Criteria                                                        | Test(s)                                                                                  | Status  | Notes                                                                              |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | :-----: | ---------------------------------------------------------------------------------- |
| Search and filters return relevant results                                 | marketplace/tests.py — `SneakerViewTests` (search/filter cases)                          | ✅ Pass | Basic marketplace view tests included; extend with specific filter tests as needed |
| Product pages show images, size/condition, seller info & shipping estimate | marketplace/tests.py — `SneakerViewTests` / templates tests                              | ✅ Pass | Sneaker view and templates verified in marketplace tests                           |
| Checkout integrates with Stripe and sends confirmation email               | checkout/tests.py — `CheckoutViewTests.test_checkout_post_creates_order_and_clears_cart` | ✅ Pass | Payment intent creation covered in view; send_mail patched and asserted in tests   |
| Order history displays                                                     | account/tests.py — `AccountPageTests.test_account_page_renders_for_owner`                | ✅ Pass | Account page tests assert `user_orders` in context                                 |

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

##### **Testing Matrix (Brand Owner)**

| Acceptance Criteria                                                 | Test(s)                                                                  |     Status     | Notes                                                                                              |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------ | :------------: | -------------------------------------------------------------------------------------------------- |
| Brand verification workflow; brand page with logo/banner/bio        | creatorspace/tests.py — brand/profile tests                              | ⚠️ Not covered | No dedicated tests yet; consider adding creatorspace tests to validate brand page and media fields |
| Listing creation supports sizes, images, quantities & release dates | listings/tests.py — `ListingCreationFormTests`, `createListingViewTests` |    ✅ Pass     | Listing form and create view tests validate field handling and successful creation                 |
| Dashboard shows sales, top products and wishlists                   | analytics/dashboard tests                                                | ⚠️ Not covered | Add dashboard integration tests to validate aggregated metrics                                     |
| Promotions management and analytics                                 | promotions/tests.py                                                      | ⚠️ Not covered | Not currently covered by tests                                                                     |

#### **Marketplace Seller**

##### **Persona:**

Individual reseller listing second‑hand sneakers.

##### **Story:**

As a marketplace seller, I want to create accurate listings quickly & manage active inventory.

##### **Acceptance Criteria:**

1. Fast listing workflow (title, size, price, photos)
2. Seller dashboard for listings & orders;
3. Order workflow locks inventory at checkout and notifies seller
4. Order tracking and clear payout/fee info.

##### **Typical Flow:**

Publish listing → buyer purchases → seller notified → order delisted → receive reciept.

##### **Testing Matrix (Marketplace Seller)**

| Acceptance Criteria                                            | Test(s)                                                                   |        Status        | Notes                                                                             |
| -------------------------------------------------------------- | ------------------------------------------------------------------------- | :------------------: | --------------------------------------------------------------------------------- |
| Fast listing workflow (title, size, price, photos)             | listings/tests.py — `ListingCreationFormTests` & `createListingViewTests` |       ✅ Pass        | Form and view tests cover required fields and image handling                      |
| Seller dashboard for listings & orders                         | seller/dashboard tests                                                    |    ⚠️ Not covered    | Dashboard views and permissions need dedicated tests                              |
| Order workflow locks inventory at checkout and notifies seller | checkout/tests.py, marketplace integration tests                          | ⚠️ Partially covered | Order creation tested; inventory locking/notification to seller not fully covered |
| Order tracking and clear payout/fee info                       | orders/tests.py                                                           |    ⚠️ Not covered    | Add tests for payout calculations and order tracking UI/API                       |

#### **Brand Collaborator**

##### **Persona:**

Designer, photographer, or influencer collaborating with a brand.

##### **Story:**

As a brand collaborator, I want role-based access to contribute content, preview draft listings, and access analytics so I can coordinate with the brand.

##### **Acceptance Criteria:**

1. Role-based invitations and scoped permissions
2. Draft and approval workflow (submit → review → publish)
3. Asset upload
4. Collaboration metrics for wishlists
5. Audit trail of approvals and changes.

##### **Typical Flow:**

Brand invites collaborator → collaborator uploads assets to draft listing → brand approves → listing goes live and both view analytics.

##### **Testing Matrix (Brand Collaborator)**

| Acceptance Criteria                                     | Test(s)                                               |     Status     | Notes                                                      |
| ------------------------------------------------------- | ----------------------------------------------------- | :------------: | ---------------------------------------------------------- |
| Role-based invitations and scoped permissions           | creatorspace/tests.py — collaborator permission tests | ⚠️ Not covered | Add tests for invite flow and role permissions             |
| Draft and approval workflow (submit → review → publish) | listings/tests.py integration                         | ⚠️ Not covered | Draft/publish workflow tests are needed                    |
| Asset upload                                            | listings/tests.py — image handling                    |    ✅ Pass     | Listing form tests validate optional image upload handling |
| Collaboration metrics for wishlists                     | analytics/tests.py                                    | ⚠️ Not covered | Add tests to validate metrics aggregation from wishlists   |
| Audit trail of approvals and changes                    | audit/tests.py                                        | ⚠️ Not covered | Implement and test audit logs for collaborator actions     |

---

## 🧪 Testing

Run the full Django test suite from the project root:

```bash
python manage.py test
```

Quick commands:

```bash
# run tests for a specfic django app only
python manage.py test <Django App Name>

# run a single test case [Example]
python manage.py test core.tests.CustomerFormTests.test_signup_creates_user_and_sends_email
```

### Test coverage:

- Models (Sneaker, Brand, Order)
- Form usage (listing creation, signup forms)
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

- **Core tests**: [core/tests.py](core/tests.py#L1-L200)
  - Purpose: Unit and integration tests for authentication-related forms, views, email utilities, and small helper functions used across the site.
  - Key test classes & cases:
    - `CustomerFormTests`:
      - `test_clean_email_duplicate`: rejects signup when an existing user email is supplied.
      - `test_signup_creates_user_and_sends_email`: valid signup creates a `User`, logs in, and triggers `send_mail` (patched).
    - `AuthViewsTests`:
      - `test_login_success_redirects`: posts valid credentials and expects redirect to `marketplace`.
      - `test_login_invalid_shows_error`: invalid credentials renders `login` with an error message.
      - `test_logout_redirects_home`: authenticated user logout redirects to `home`.
    - `EmailFunctionTests`:
      - `test_send_signup_confirmation_email`: patches `send_mail` and asserts it's called with the new user's email.
    - `AuthCheckTests`:
      - `test_authcheck_anonymous`: `authCheck` returns `False` for anonymous users.
      - `test_authcheck_authenticated`: `authCheck` returns `True` for authenticated users.
  - Important dependencies: `core.views` (forms and helpers), Django `User` model, `django.test.Client`, `django.test.RequestFactory`, and the URL names `signup`, `login`, `logout`, `marketplace`, and `home`.

- **Account tests**: [account/tests.py](account/tests.py#L1-L60)
  - Purpose: Unit and integration tests for user account features — profile rendering, wishlist behaviour, and creator account metadata.
  - Key test classes & cases:
    - `CreatorAccountModelTests`:
      - `test_str`: `CreatorAccountModel.__str__` contains the owner's username.
    - `WishlistViewTests`:
      - `test_add_to_wishlist_creates_item_and_prevents_duplicates`: a logged-in user can add a `Sneaker` to their wishlist; duplicate adds are prevented.
      - `test_remove_from_wishlist_deletes_item_or_errors`: removing a wishlist item deletes it; attempting to remove a non-existent item redirects with an error.
    - `AccountPageTests`:
      - `test_account_page_permission_denied_for_other_user`: users cannot view other users' account pages and are redirected to a permission error.
      - `test_account_page_renders_for_owner`: owners can access their account page and receive the expected context variables (e.g., `available_sneakers`).
  - Important dependencies: `account.views` (profile and wishlist views), `account.models.WishlistItem`, `CreatorAccountModel`, `marketplace.models.Sneaker`, `checkout.models.Order`, and URL names `account` / `wishlist_add` / `wishlist_remove` / `sneaker_detail`.

- **Checkout tests**: [checkout/tests.py](checkout/tests.py#L1-L200)
  - Purpose: Unit and integration tests for the checkout flow — validating `Order`/`OrderItem` model behaviour, `CheckoutForm` rendering, and the `checkoutView` POST flow including email sending and cart handling.
  - Key test classes & cases:
    - `CheckoutFormTests`:
      - `test_placeholders_and_classes`: form fields include `placeholder` text and the `checkout-input` CSS class.
    - `OrderModelTests`:
      - `test_order_number_generated_on_save`: saving an `Order` generates a unique `order_number`.
      - `test_order_update_total_and_delivery`: `update_total` correctly sums line items, applies delivery rules, and sets `grand_total`.
    - `OrderItemTests`:
      - `test_orderitem_save_sets_line_total`: saving an `OrderItem` sets `line_total` from the linked `Sneaker.price`.
    - `CheckoutViewTests`:
      - `test_checkout_post_creates_order_and_clears_cart`: posting valid checkout data creates an `Order`, persists `OrderItem`s, clears the session cart, and triggers the order confirmation email (email sending is patched in tests).
      - `test_checkout_post_missing_sneaker_redirects_to_cart`: when a sneaker in the cart is missing, the view redirects back to the cart and does not leave a partial order.
  - Important dependencies: `checkout.forms.CheckoutForm`, `checkout.models.Order`, `checkout.models.OrderItem`, `checkout.views.send_order_confirmation_email` (patched), `marketplace.models.Sneaker`, `django.test.Client`, and the `checkout` URL patterns.

### Test Grid

Run the full test suite:

```bash
python manage.py test
```

| App                              | Purpose                                                                      |                                                  Key tests (examples) | Status  | Notes                                                    |
| -------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------: | :-----: | -------------------------------------------------------- |
| Core                             | Authentication/signup forms, helpers, and email utilities                    | CustomerFormTests, AuthViewsTests, EmailFunctionTests, AuthCheckTests | ✅ Pass | All core tests pass locally                              |
| Checkout                         | Checkout flow, `Order`/`OrderItem` behaviour, `CheckoutForm`, view POST flow | CheckoutFormTests, OrderModelTests, OrderItemTests, CheckoutViewTests | ✅ Pass | Checkout tests pass; email sending patched in tests      |
| Account                          | Profile rendering, wishlist add/remove, creator account model                |         CreatorAccountModelTests, WishlistViewTests, AccountPageTests | ✅ Pass | Tests verify permission handling and wishlist uniqueness |
| Marketplace / Listings / Reviews | Models, views, and admin behaviours across marketplace features              |              SneakerModelTests, ListingCreationFormTests, ReviewTests | ✅ Pass | Existing tests included in full run passed               |
| Full Run                         | Run all tests                                                                |                                                                     — | ✅ Pass | 34 tests ran successfully at time of report              |

---

## 🛡️ Defensive Programming

This project follows several defensive-programming practices to reduce bugs, prevent data corruption, and make integrations robust. Key measures and where to find them:

- **Input validation (forms):** use of Django `Form`/`ModelForm` validations and custom `clean_...` methods to validate user input (e.g. email uniqueness and password rules). See `core.views.CustomerUserCreationForm` for examples.
  - File: [core/views.py](core/views.py#L1-L200)

- **Authentication & authorization:** views guarded with `@login_required`, explicit user checks and redirects to permission/error handlers to prevent unauthorized access.
  - Files: [account/views.py](account/views.py#L1-L200), [core/views.py](core/views.py#L1-L200)

- **Error handling & rollback:** use of `get_object_or_404`, try/except blocks, user-facing `messages.error()`, and cleanup (e.g., deleting a partially-created order when an item is missing) to avoid leaving inconsistent state.
  - File: [checkout/views.py](checkout/views.py#L1-L200)

- **Data integrity & constraints:** database-level uniqueness (`unique_together`), typed fields for money (`DecimalField`), and model `save()` overrides that ensure consistent derived fields (e.g., `Order.order_number`).
  - Files: [account/models.py](account/models.py#L1-L200), [checkout/models.py](checkout/models.py#L1-L200)

- **External integration safety:** secrets and keys are read from `settings` (not hard-coded); external calls (email, Stripe) are invoked server-side and are patched/mocked in tests to avoid side effects during CI.
  - Files: [checkout/views.py](checkout/views.py#L1-L200), [core/views.py](core/views.py#L1-L200)

- **Session & CSRF protection:** templates include CSRF tokens for form posts; session modifications are explicit (`request.session.modified = True`) when cart is cleared.
  - Templates and views: `templates/*` (CSRF), [checkout/views.py](checkout/views.py#L1-L200)

- **User feedback & observability:** consistent use of the Django `messages` framework to surface recoverable errors and validation issues to users.
  - Example: [checkout/views.py](checkout/views.py#L1-L200)

- **Defensive tests & mocks:** unit tests cover edge-cases, patch external services (e.g., `send_mail` and Stripe) and use `RequestFactory` and `Client` to validate both view-level and model-level behavior.
  - See test suites: [core/tests.py](core/tests.py#L1-L200), [checkout/tests.py](checkout/tests.py#L1-L200), [account/tests.py](account/tests.py#L1-L200), and [TESTING.md](TESTING.md)

- **Principle of least privilege & ownership checks:** model ownership used to scope actions (e.g., `Sneaker.owner`) and views validate the requesting user's identity before exposing profile or owner-only actions.
  - Files: [marketplace/models.py](marketplace/models.py#L1-L200), [account/views.py](account/views.py#L1-L200)

These measures are intentionally lightweight and idiomatic to Django — they prioritize correct server-side validation, clear user feedback, and testable integration points.

Recommended next steps to strengthen defenses:

- Add end-to-end tests for Stripe webhook handling and seller notifications.
- Add explicit logging around external failures (email, Stripe) and rate-limit sensitive endpoints if exposed via API.
- Introduce schema-level constraints and migrations to enforce invariants where appropriate.

## ⚙️ Installation & Setup

### 1. Clone repository

```bash
git clone https://github.com/ljkkj7/sneakerhub.git
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
