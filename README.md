## Grocery E-Commerce Web Application

A full-stack grocery e-commerce platform developed using Python and Django, featuring multiple user modules, product recommendations via FastAPI, and chatbot integration for enhanced user experience.

---

Features by Module

## Guest
- Category-wise product browsing
- Search and filter products
- Product detail page
- Signup / Login / Forgot Password
- Chatbot (via BotPress)
- Static pages: About, Contact, Terms, Privacy, FAQ

## Registered User
- User profile with edit option
- Wishlist functionality
- Cart and Checkout
- Order tracking and order history
- Multiple address support (Add/Edit/Delete)
- Payment options: Razorpay UPI & Cash on Delivery
- Secure logout

## Admin
- Dashboard displaying:
  - Total users
  - Total products
  - Monthly sales
  - Pending requests
- Admin management tools:
  - User Management (with search & filter)
  - Product Management (add/edit/delete with filter/search)
  - Order Management
  -  Order History (with search & filter)
  - Request Management

## FastAPI
- Homepage “Best Offer” product recommendations
- Product Details Page “Similar Products” recommendation engine

---

## Video


## Tech Stack

- **Backend:** Python, Django, FastAPI
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** PostgreSQL
- **Chatbot:** BotPress
- **Libraries & Tools:**  
  Font Awesome, Bootstrap Icons, jQuery, Google Fonts, SweetAlert2, Notyf 3

## Future Plans

- Integrate inventory management using FastAPI
- Protect all admin URLs with `@login_required`
- Build and expose RESTful APIs
