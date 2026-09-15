# SMARTPARK --- MASTER PROJECT CONTEXT & FINAL DEVELOPMENT GUIDE

**Project:** SmartPark -- Automated Smart Parking Reservation System\
**Student:** G R Govind\
**Academic Level:** MCA Mini Project\
**Document Status:** FINAL BASELINE --- DEVELOPMENT STARTS AFTER THIS
DOCUMENT\
**Primary Purpose:** Long-term source of truth for the student,
Antigravity, Claude, and other coding agents.

------------------------------------------------------------------------

## 1. DOCUMENT PURPOSE

This document is the final project specification and development guide
for SmartPark.

It must be treated as the **source of truth** for:

-   project scope
-   features
-   modules
-   workflows
-   UI/UX
-   frontend technology
-   backend technology
-   database
-   APIs
-   ML functionality
-   security
-   testing
-   diagrams
-   development priorities

Coding agents MUST read this document before implementing major changes.

A short-term `memory.md` may also exist. The master document defines the
stable project specification; `memory.md` records the current
implementation state.

------------------------------------------------------------------------

# 2. PROJECT VISION

SmartPark is a smart parking reservation system that helps users:

1.  Find suitable parking locations.
2.  View current parking availability.
3.  View parking details and map location.
4.  Select a suitable parking slot based on vehicle information.
5.  Reserve a slot.
6.  Make payment.
7.  Receive QR and OTP access credentials.
8.  Enter the parking facility using either QR or OTP.
9.  Exit using QR or OTP.
10. Automatically release the occupied slot after successful exit.
11. View booking history and booking details.
12. Extend an active booking when possible.
13. Receive useful notifications.
14. Use AI/ML-based parking availability prediction.

The system is intended to make parking:

**Discoverable → Reservable → Payable → Accessible → Trackable →
Automated**

------------------------------------------------------------------------

# 3. CORE PROJECT IDEA

Traditional parking systems often require users to physically search for
parking and manually determine whether a slot is available.

SmartPark introduces a centralized digital process:

    Search Parking
          ↓
    Check Availability
          ↓
    Predict Future Availability
          ↓
    Select Vehicle
          ↓
    Find Suitable Slot
          ↓
    Reserve
          ↓
    Pay
          ↓
    Receive QR + OTP
          ↓
    Enter Parking
          ↓
    Slot becomes OCCUPIED
          ↓
    Park
          ↓
    Exit using QR/OTP
          ↓
    Slot becomes AVAILABLE
          ↓
    Booking Completed

------------------------------------------------------------------------

# 4. IMPORTANT BUSINESS MODEL DECISION

SmartPark owns and manages the parking locations represented in the
system.

There are:

-   NO external parking owners
-   NO third-party parking-provider registration
-   NO parking-owner marketplace
-   NO user-created parking locations

Only authorized SmartPark administrators manage:

-   parking locations
-   parking slots
-   availability
-   bookings
-   payments
-   entry/exit records
-   prediction data
-   analytics

------------------------------------------------------------------------

# 5. PROJECT OBJECTIVES

## Primary Objectives

-   Reduce time spent searching for parking.
-   Allow users to reserve parking before arrival.
-   Show current parking availability.
-   Predict future availability using Machine Learning.
-   Match parking slots to vehicle requirements.
-   Enable digital payment.
-   Provide QR/OTP-based entry and exit.
-   Automatically update slot states.
-   Provide administrators with centralized management.
-   Maintain a simple, secure and understandable architecture.

## Academic Objectives

The project should demonstrate:

-   Web application development
-   Flask backend development
-   SQLite database design
-   REST API development
-   CRUD operations
-   Authentication and authorization
-   Database relationships
-   Machine Learning integration
-   Data visualization
-   System automation
-   DFD and workflow design
-   Responsive frontend development
-   Security practices

------------------------------------------------------------------------

# 6. MAIN SYSTEM MODULES

The project has exactly **TWO MAIN APPLICATION MODULES**:

## MODULE 1 --- USER

The user module handles all customer-facing parking operations.

## MODULE 2 --- ADMIN

The admin module handles centralized SmartPark management.

Do not create a third business module for parking owners.

------------------------------------------------------------------------

# 7. USER MODULE

User functionality includes:

-   Registration
-   Login/logout
-   Dashboard
-   Find Parking
-   Parking Details
-   Slot Selection
-   Vehicle Information
-   Booking
-   Payment
-   Booking Success
-   My Bookings
-   Booking Details
-   QR access
-   OTP access
-   Booking extension
-   Notifications
-   Profile

------------------------------------------------------------------------

# 8. ADMIN MODULE

Admin functionality includes:

-   Admin Login
-   Dashboard
-   Parking Locations
-   Parking Slots
-   Users
-   Bookings
-   Payments
-   Entry/Exit
-   AI Predictions
-   Analytics
-   Reports
-   Profile/Settings

------------------------------------------------------------------------

# 9. PUBLIC PAGES

The public website should contain:

-   Home
-   About Us
-   Services
-   Reviews
-   Contact
-   Terms & Conditions
-   Privacy Policy
-   404

The public website should explain the SmartPark concept without
requiring login.

------------------------------------------------------------------------

# 10. AUTHENTICATION PAGES

Authentication:

-   Login
-   Sign Up
-   Logout

Do not ask for vehicle number during registration.

Vehicle information is collected during booking.

------------------------------------------------------------------------

# 11. USER PAGE STRUCTURE

Final user pages:

    /dashboard
    /parking
    /parking/<id>
    /parking/<id>/slots
    /booking
    /payment/<id>
    /booking/<id>/success
    /bookings
    /booking/<id>
    /notifications
    /profile

------------------------------------------------------------------------

# 12. ADMIN PAGE STRUCTURE

Final admin pages:

    /admin/dashboard
    /admin/parking
    /admin/parking/<id>/slots
    /admin/users
    /admin/bookings
    /admin/payments
    /admin/entry-exit
    /admin/predictions
    /admin/analytics
    /admin/reports
    /admin/communication/reviews
    /admin/communication/feedback
    /admin/communication/contact-messages
    /admin/profile

Admin and User login use the same authentication page with role-based
access.

------------------------------------------------------------------------

# 13. NO SEPARATE MY QR PAGE

Do NOT create:

    /my-qr

QR information belongs inside:

    My Bookings
          ↓
    Booking Details

Booking Details must display the QR access information associated with
that booking.

------------------------------------------------------------------------

# 14. NO SEPARATE MY VEHICLES PAGE

Do NOT create:

    /my-vehicles

Vehicle information belongs to a specific booking.

This avoids unnecessary permanent vehicle-profile management.

------------------------------------------------------------------------

# 15. VEHICLE INFORMATION

Vehicle information is collected during booking.

The system must ask:

-   Vehicle Number
-   Vehicle Type

Vehicle types:

-   Bike
-   Car
-   Bus
-   Truck

Vehicle information is required before final slot selection because the
system must determine slot compatibility.

------------------------------------------------------------------------

# 16. VEHICLE-SPECIFIC INFORMATION

## Bike

Collect:

-   Vehicle number
-   Vehicle type

## Car

Collect:

-   Vehicle number
-   Car type/category

Examples:

-   Hatchback
-   Sedan
-   SUV
-   MUV
-   Pickup
-   Other

## Bus

Collect:

-   Vehicle number
-   Bus category
-   Seating capacity where required

Possible categories:

-   Mini Bus
-   20--30 seats
-   31--40 seats
-   41--50 seats
-   50+ seats

## Truck

Collect:

-   Vehicle number
-   Truck category

Examples:

-   Light
-   Medium
-   Heavy

Additional dimensions can be collected only if required by the slot
model.

Do not collect unnecessary vehicle information.

------------------------------------------------------------------------

# 17. VEHICLE-AWARE SLOT SELECTION

Slot recommendation must consider:

-   vehicle type
-   vehicle size/category
-   slot type
-   slot dimensions/capacity
-   current slot status

Example:

    User selects SUV
            ↓
    System checks compatible slots
            ↓
    Remove unavailable slots
            ↓
    Remove incompatible slots
            ↓
    Display suitable slots
            ↓
    User selects slot

The system must never assign an incompatible slot.

------------------------------------------------------------------------

# 18. PARKING LOCATION

Each parking location can contain:

-   Location name
-   Address
-   Latitude
-   Longitude
-   Description
-   Operating status
-   Total slots
-   Available slots
-   Reserved slots
-   Occupied slots
-   Parking facilities/features

SmartPark administrators create and manage locations.

Users cannot create locations.

------------------------------------------------------------------------

# 19. MAPS

Use:

-   OpenStreetMap
-   Leaflet.js

Do not require Google Maps API.

Map responsibilities:

-   show parking locations
-   show location markers
-   help users understand parking position
-   support navigation context

The map is a supporting feature, not the core booking engine.

------------------------------------------------------------------------

# 20. PARKING SLOT

Each slot should have relevant information such as:

-   slot ID
-   parking location
-   slot number
-   vehicle compatibility
-   size/category
-   status
-   optional floor/section

Possible slot statuses:

-   AVAILABLE
-   RESERVED
-   OCCUPIED
-   MAINTENANCE

Core lifecycle:

    AVAILABLE
        ↓
    RESERVED
        ↓
    OCCUPIED
        ↓
    AVAILABLE

Maintenance may temporarily remove a slot from normal allocation.

------------------------------------------------------------------------

# 21. BOOKING

A booking contains:

-   user
-   parking location
-   parking slot
-   booking date
-   start time
-   end time
-   vehicle number
-   vehicle type
-   vehicle-specific information
-   booking status
-   payment status
-   QR credential
-   OTP credential/status
-   timestamps

Booking status examples:

-   PENDING
-   CONFIRMED
-   ACTIVE
-   COMPLETED
-   CANCELLED
-   EXPIRED

------------------------------------------------------------------------

# 22. BOOKING CONFLICT PREVENTION

The system must prevent double booking.

Before confirming:

1.  Check slot exists.
2.  Check slot is compatible.
3.  Check slot is available for the requested period.
4.  Check conflicting bookings.
5.  Validate user.
6.  Calculate fee.
7.  Create reservation.
8.  Mark slot RESERVED.
9.  Process payment.
10. Confirm booking.

A slot must never be assigned to two conflicting active bookings.

------------------------------------------------------------------------

# 23. PAYMENT

Initial implementation:

**Demo Payment**

The system should simulate successful/failed payment states without
requiring a real payment gateway.

Payment should record:

-   booking ID
-   user ID
-   amount
-   payment status
-   transaction/reference ID
-   payment timestamp
-   payment method

Possible statuses:

-   PENDING
-   SUCCESS
-   FAILED
-   REFUNDED

Razorpay may be a future enhancement.

Do not make real payment integration mandatory for the first development
version.

------------------------------------------------------------------------

# 24. BOOKING SUCCESS

After successful payment:

    Payment Success
          ↓
    Booking Confirmed
          ↓
    Slot RESERVED
          ↓
    QR Generated
          ↓
    OTP Generated
          ↓
    Booking Success Page

Booking Success should provide:

-   booking ID
-   parking location
-   slot
-   vehicle
-   date/time
-   amount
-   booking status
-   QR access
-   OTP access
-   link to Booking Details

------------------------------------------------------------------------

# 25. QR AND OTP ACCESS

QR and OTP are **alternative access methods for the same booking**.

The user can enter using:

    QR
    OR
    OTP

The user does not need to use both.

------------------------------------------------------------------------

# 26. QR FLOW

    Booking Confirmed
          ↓
    Generate secure QR credential
          ↓
    Store reference/token
          ↓
    Display in Booking Details
          ↓
    User reaches parking
          ↓
    QR scanned
          ↓
    Verify booking
          ↓
    Verify validity
          ↓
    Verify time/status
          ↓
    Entry approved
          ↓
    Slot = OCCUPIED

QR must not contain unnecessary sensitive information.

------------------------------------------------------------------------

# 27. OTP FLOW

    Booking Confirmed
          ↓
    OTP generated
          ↓
    OTP displayed/sent according to implementation
          ↓
    User reaches parking
          ↓
    Enter OTP
          ↓
    Verify OTP
          ↓
    Verify booking
          ↓
    Verify validity
          ↓
    Entry approved
          ↓
    Slot = OCCUPIED

OTP must be time-bound and invalid after successful use or expiry.

------------------------------------------------------------------------

# 28. ENTRY/EXIT

The same conceptual access mechanism can be used for exit.

## Entry

    QR/OTP
       ↓
    Validation
       ↓
    Successful Entry
       ↓
    Booking ACTIVE
       ↓
    Slot OCCUPIED

## Exit

    QR/OTP
       ↓
    Validation
       ↓
    Successful Exit
       ↓
    Slot AVAILABLE
       ↓
    Booking COMPLETED

Access logs should record:

-   booking
-   user
-   method (QR/OTP)
-   entry/exit
-   timestamp
-   result
-   relevant verification metadata

------------------------------------------------------------------------

# 29. BOOKING EXTENSION

A user can request extension from Booking Details.

Flow:

    Active Booking
          ↓
    Extend Booking
          ↓
    Select additional duration
          ↓
    Check future conflicts
          ↓
    Calculate additional fee
          ↓
    Additional payment
          ↓
    Update booking end time
          ↓
    Confirm extension

Extension must fail if the requested period conflicts with another
reservation.

------------------------------------------------------------------------

# 30. BOOKING CANCELLATION

Cancellation is handled from the Booking Details page.

No separate cancellation page exists.

Flow:

    Booking Details
          ↓
    Cancel Booking
          ↓
    Check cancellation time
          ↓
    Calculate refund
          ↓
    Cancel booking
          ↓
    Release slot

Refund rules:

  Cancellation Time            Refund
  ---------------------------- --------------------------
  \>= 2 hours before parking   75% refund
  1-2 hours before parking     50% refund
  Less than 1 hour             No refund
  After parking starts         Cancellation unavailable

# 30. NOTIFICATIONS

Notifications may include:

-   booking confirmed
-   payment successful
-   upcoming booking
-   entry successful
-   exit successful
-   extension successful/failed
-   booking cancelled
-   OTP-related information
-   system alerts

Notifications belong to the user module.

------------------------------------------------------------------------

# 31. USER DASHBOARD

Dashboard should prioritize:

-   current/active booking
-   upcoming booking
-   nearby/find parking action
-   current availability summary
-   booking statistics
-   quick access to My Bookings
-   useful parking information

Do not overcrowd the dashboard.

------------------------------------------------------------------------

# 32. ADMIN DASHBOARD

Admin dashboard should summarize:

-   total users
-   total parking locations
-   total slots
-   available slots
-   reserved slots
-   occupied slots
-   active bookings
-   completed bookings
-   payments
-   entry/exit activity
-   prediction overview
-   useful analytics

Charts should be used only where they communicate information clearly.

------------------------------------------------------------------------

# 33. ADMIN PARKING MANAGEMENT

Admin can:

-   create parking location
-   edit parking location
-   deactivate location
-   view location details
-   create slots
-   edit slots
-   change slot status where appropriate
-   view occupancy

Users cannot modify parking infrastructure.

------------------------------------------------------------------------

# 34. ADMIN USER MANAGEMENT

Admin can:

-   view users
-   inspect user status
-   activate/deactivate where required
-   view booking-related information

Admin should not expose unnecessary sensitive data.

------------------------------------------------------------------------

# 35. ADMIN BOOKING MANAGEMENT

Admin can:

-   view bookings
-   filter bookings
-   inspect booking details
-   view status
-   view payment status
-   inspect entry/exit history
-   handle administrative cases

------------------------------------------------------------------------

# 36. ADMIN PAYMENT MANAGEMENT

Admin can:

-   view payments
-   filter by status
-   view booking relation
-   view transaction/reference information
-   inspect successful/failed payments

------------------------------------------------------------------------

# 37. AI / MACHINE LEARNING

Machine Learning is a supporting feature of SmartPark.

However, ML has a **specific responsibility**:

> Predict parking availability.

ML must NOT control deterministic security or transaction operations
such as:

-   authentication
-   payment verification
-   QR validation
-   OTP validation
-   booking conflict prevention
-   slot state verification

Those functions must remain deterministic.

------------------------------------------------------------------------

# 38. SELECTED ML ALGORITHM

Primary algorithm:

**Linear Regression**

Libraries:

-   scikit-learn
-   pandas
-   numpy
-   joblib

The model predicts future availability/occupancy from historical parking
data.

------------------------------------------------------------------------

# 39. POSSIBLE ML FEATURES

Input features may include:

-   date
-   hour
-   day of week
-   current occupancy
-   historical occupancy
-   total slots
-   historical bookings
-   historical available slots

Output:

-   predicted occupancy
-   predicted available slots
-   availability trend

The exact final feature set can be refined during implementation based
on the available dataset.

------------------------------------------------------------------------

# 40. ML WORKFLOW

    Historical Parking Data
             ↓
       Data Cleaning
             ↓
       Feature Preparation
             ↓
       Train/Test Split
             ↓
      Linear Regression
             ↓
       Model Evaluation
             ↓
        Save Model
             ↓
      Future Prediction
             ↓
     Display Prediction

Use `joblib` for model persistence where appropriate.

------------------------------------------------------------------------

# 41. AI PREDICTION PAGE

Admin should be able to view:

-   prediction date/time
-   expected occupancy
-   expected available slots
-   prediction trend
-   model-related summary
-   relevant historical comparison

User-facing prediction can be simplified to:

-   likely available
-   moderately busy
-   likely busy

Avoid exposing unnecessary ML complexity to normal users.

------------------------------------------------------------------------

# 42. ANALYTICS VS AI

These are different concepts.

## Analytics

Uses actual/current/historical data to show:

-   occupancy
-   booking count
-   utilization
-   payments
-   trends

## AI/ML

Uses historical data to estimate:

-   future availability
-   future occupancy

Do not label ordinary charts as AI.

------------------------------------------------------------------------

# 43. TECHNOLOGY STACK --- FINAL

## Frontend

-   HTML5
-   Tailwind CSS
-   JavaScript
-   Leaflet.js
-   Charting library where useful

## Backend

-   Python
-   Flask
-   Flask Blueprints
-   REST API

## Database

**SQLite**

## ML

-   Python
-   pandas
-   numpy
-   scikit-learn
-   joblib

## Maps

-   OpenStreetMap
-   Leaflet.js

------------------------------------------------------------------------

# 44. WHY TAILWIND CSS

Tailwind CSS is now the official frontend styling technology.

Benefits:

-   rapid UI development
-   consistent spacing
-   responsive utilities
-   reusable design patterns
-   easier adaptive layouts
-   fewer large custom CSS files
-   easy component-level styling

Do not build the project around a separate heavy UI framework unless
explicitly required.

Tailwind should be used consistently instead of mixing many unrelated
styling systems.

------------------------------------------------------------------------

# 45. FRONTEND DESIGN PRINCIPLES

The interface should feel:

-   smart
-   clean
-   modern
-   premium
-   calm
-   precise
-   trustworthy
-   easy to understand

Avoid:

-   excessive gradients
-   excessive glass effects
-   unnecessary animations
-   clutter
-   tiny text
-   oversized decorative elements
-   complicated navigation

SmartPark should look like a serious intelligent mobility product.

------------------------------------------------------------------------

# 46. RESPONSIVE DESIGN

The frontend must support:

-   Desktop
-   Tablet
-   Mobile

Do not simply shrink desktop layouts.

## Desktop

Can use:

-   sidebar
-   multi-column dashboard
-   larger maps
-   larger charts

## Tablet

Use:

-   reduced columns
-   adaptive navigation
-   appropriately sized cards

## Mobile

Use:

-   compact navigation
-   bottom navigation where appropriate
-   single-column cards
-   large touch targets
-   simple booking flow
-   full-width actions
-   readable maps
-   minimal text

------------------------------------------------------------------------

# 47. FRONTEND COMPONENT PRINCIPLES

Prefer reusable UI patterns:

-   Navbar
-   Sidebar
-   Mobile navigation
-   Cards
-   Status badges
-   Buttons
-   Form controls
-   Modal
-   Toast/alert
-   Loading state
-   Empty state
-   Error state
-   Parking cards
-   Slot cards
-   Booking summary
-   Payment summary
-   QR display
-   OTP display
-   Map container
-   Chart container

Do not duplicate identical markup unnecessarily.

------------------------------------------------------------------------

# 48. FRONTEND DATA FLOW

General pattern:

    User Action
        ↓
    JavaScript
        ↓
    Fetch API
        ↓
    Flask REST API
        ↓
    Validation
        ↓
    Business Logic
        ↓
    SQLite
        ↓
    JSON Response
        ↓
    JavaScript
        ↓
    UI Update

------------------------------------------------------------------------

# 49. BACKEND ARCHITECTURE

Use a simple layered Flask architecture.

    Frontend
       ↓
    Flask Routes / REST API
       ↓
    Authentication & Validation
       ↓
    Business Logic
       ↓
    ML / Prediction Services where required
       ↓
    Data Access
       ↓
    SQLite

Keep the architecture understandable for an MCA mini project.

Do not introduce microservices.

------------------------------------------------------------------------

# 50. FLASK BLUEPRINT STRUCTURE

Suggested structure:

    routes/
        auth.py
        user.py
        admin.py
        booking.py
        parking.py
        payment.py
        prediction.py
        qr.py

The exact file split may be adjusted if the existing implementation
benefits from a simpler structure.

Avoid duplicate route ownership.

------------------------------------------------------------------------

# 51. REST API ORGANIZATION

Suggested API groups:

    /api/auth
    /api/parking
    /api/bookings
    /api/payment
    /api/prediction
    /api/qr
    /api/otp
    /api/admin

Example endpoints:

    GET  /api/parking
    GET  /api/parking/<id>
    GET  /api/parking/<id>/slots

    POST /api/bookings
    GET  /api/bookings
    GET  /api/bookings/<id>

    POST /api/payment

    GET  /api/prediction

    POST /api/qr/verify
    POST /api/otp/verify

Use appropriate HTTP methods.

------------------------------------------------------------------------

# 52. DATABASE --- SQLITE

SQLite is the final selected database for the current project.

Reasons:

-   simple setup
-   zero separate database server
-   easy local development
-   easy demonstration
-   suitable for a focused MCA mini project
-   easy backup and portability

SQLite is intentionally selected over PostgreSQL for this final
development baseline.

Do not switch to PostgreSQL/MySQL unless the project scope is explicitly
changed.

------------------------------------------------------------------------

# 53. DATABASE TABLES

Suggested core tables:

1.  users
2.  admins
3.  parking_locations
4.  parking_slots
5.  bookings
6.  payments
7.  parking_prediction_data
8.  notifications
9.  access_logs

Additional tables may be introduced only when genuinely required by an
approved feature.

------------------------------------------------------------------------

# 54. USERS TABLE

Possible fields:

-   id
-   name
-   email
-   phone
-   password_hash
-   is_verified
-   status
-   created_at
-   updated_at

Do not store plain-text passwords.

------------------------------------------------------------------------

# 55. ADMINS TABLE

Possible fields:

-   id
-   name
-   email
-   password_hash
-   status
-   created_at
-   updated_at

Admin authentication must be separated from normal user authorization.

------------------------------------------------------------------------

# 56. PARKING_LOCATIONS TABLE

Possible fields:

-   id
-   name
-   address
-   latitude
-   longitude
-   description
-   total_slots
-   status
-   created_at
-   updated_at

------------------------------------------------------------------------

# 57. PARKING_SLOTS TABLE

Possible fields:

-   id
-   parking_location_id
-   slot_number
-   vehicle_type
-   vehicle_category
-   status
-   section/floor if required
-   created_at
-   updated_at

------------------------------------------------------------------------

# 58. BOOKINGS TABLE

Possible fields:

-   id
-   user_id
-   parking_location_id
-   parking_slot_id
-   booking_date
-   start_time
-   end_time
-   vehicle_number
-   vehicle_type
-   vehicle_category
-   vehicle_capacity/size where applicable
-   booking_status
-   payment_status
-   qr_token/reference
-   otp_hash/reference
-   created_at
-   updated_at

Vehicle data belongs here because it describes the vehicle used for that
booking.

------------------------------------------------------------------------

# 59. PAYMENTS TABLE

Possible fields:

-   id
-   booking_id
-   user_id
-   amount
-   payment_method
-   transaction_reference
-   status
-   paid_at
-   created_at

------------------------------------------------------------------------

# 60. PREDICTION DATA TABLE

Possible fields:

-   id
-   parking_location_id
-   timestamp/date
-   hour
-   day_of_week
-   total_slots
-   occupancy
-   available_slots
-   predicted_occupancy
-   predicted_available_slots
-   created_at

The exact schema can be refined after the ML dataset is finalized.

------------------------------------------------------------------------

# 61. NOTIFICATIONS TABLE

Possible fields:

-   id
-   user_id
-   title
-   message
-   type
-   is_read
-   created_at

------------------------------------------------------------------------

# 62. ACCESS LOGS TABLE

Possible fields:

-   id
-   booking_id
-   user_id
-   access_type
-   action
-   verification_status
-   timestamp
-   metadata/reference

Examples:

    access_type = QR / OTP
    action = ENTRY / EXIT

------------------------------------------------------------------------

# 63. DATABASE RELATIONSHIPS

Conceptual relationship:

    USER
      │
      ├── BOOKINGS
      │      │
      │      ├── PAYMENT
      │      ├── ACCESS LOGS
      │      ├── PARKING LOCATION
      │      └── PARKING SLOT
      │
      └── NOTIFICATIONS

    PARKING LOCATION
      │
      ├── PARKING SLOTS
      ├── BOOKINGS
      └── PREDICTION DATA

    ADMIN
      │
      └── manages system resources

Foreign keys should maintain data integrity.

------------------------------------------------------------------------

# 64. ENTITY RELATIONSHIP DIAGRAM

Conceptual ER structure:

    +-------------+
    |    USERS    |
    +-------------+
           |
           | 1:N
           v
    +-------------+
    |  BOOKINGS   |
    +-------------+
       |    |    |
       |    |    +----------------+
       |    |                     |
       |    v                     v
       | PAYMENT              ACCESS_LOGS
       |
       +----------------------+
                              |
                              v
                     PARKING_LOCATIONS
                              |
                              | 1:N
                              v
                       PARKING_SLOTS

    PARKING_LOCATIONS
            |
            | 1:N
            v
    PREDICTION_DATA

    USERS
      |
      | 1:N
      v
    NOTIFICATIONS

    ADMINS manage the administrative resources.

------------------------------------------------------------------------

# 65. SYSTEM ARCHITECTURE DIAGRAM

    ┌──────────────────────────────┐
    │          USER / ADMIN        │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Frontend                     │
    │ HTML + Tailwind + JavaScript │
    │ Leaflet + Charts             │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ Flask REST API               │
    │ Blueprints + Authentication  │
    └──────────────┬───────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
    ┌─────────────┐   ┌──────────────┐
    │ Business    │   │ ML Prediction│
    │ Logic       │   │ Service      │
    └──────┬──────┘   └──────┬───────┘
           │                 │
           └────────┬────────┘
                    ▼
             ┌─────────────┐
             │    SQLite   │
             └─────────────┘

------------------------------------------------------------------------

# 66. DFD LEVEL 0 --- CONTEXT DIAGRAM

External entities:

-   User
-   Admin

Central process:

**SmartPark**

Data flows:

    User
      │
      │ registration, search,
      │ booking, payment,
      │ QR/OTP, profile requests
      ▼
    ┌──────────────────────┐
    │     SmartPark     │
    └──────────────────────┘
      ▲
      │ booking status,
      │ parking information,
      │ payment status,
      │ QR/OTP, notifications
      │
     User


    Admin
      │
      │ manage locations,
      │ slots, users, bookings,
      │ payments, predictions
      ▼
    ┌──────────────────────┐
    │     SmartPark     │
    └──────────────────────┘
      ▲
      │ reports, analytics,
      │ system status
      │
     Admin

------------------------------------------------------------------------

# 67. DFD LEVEL 1

Main processes:

1.  Authentication
2.  Parking Search & Availability
3.  Parking Reservation
4.  Payment
5.  QR/OTP Access
6.  Parking Entry/Exit
7.  AI Availability Prediction
8.  User Management
9.  Admin Management
10. Notifications

Data stores:

-   D1 Users
-   D2 Parking Locations
-   D3 Parking Slots
-   D4 Bookings
-   D5 Payments
-   D6 Prediction Data
-   D7 Notifications
-   D8 Access Logs

Conceptual flow:

    USER
      |
      v
    [1 Authentication]
      |
      v
    D1 Users

    USER
      |
      v
    [2 Search & Availability]
      |
      +----> D2 Parking Locations
      +----> D3 Parking Slots
      |
      v
    Parking Results

    USER
      |
      v
    [3 Reservation]
      |
      +----> D4 Bookings
      +----> D3 Parking Slots

    USER
      |
      v
    [4 Payment]
      |
      +----> D5 Payments
      |
      v
    Booking Confirmation

    USER
      |
      v
    [5 QR/OTP Access]
      |
      +----> D4 Bookings
      +----> D8 Access Logs
      |
      v
    [6 Entry/Exit]
      |
      +----> D3 Parking Slots
      +----> D4 Bookings

    D6 Prediction Data
          |
          v
    [7 AI Prediction]
          |
          v
    Availability Prediction

    ADMIN
      |
      v
    [8/9 Administration]
      |
      +----> Users
      +----> Locations
      +----> Slots
      +----> Bookings
      +----> Payments

    [10 Notifications]
          |
          v
       D7 Notifications

------------------------------------------------------------------------

# 68. DFD LEVEL 2 --- BOOKING PROCESS

Process 3 can be decomposed as:

    User
      ↓
    3.1 Select Parking Location
      ↓
    3.2 Select Date/Time
      ↓
    3.3 Enter Vehicle Details
      ↓
    3.4 Check Slot Compatibility
      ↓
    3.5 Check Slot Availability
      ↓
    3.6 Calculate Fee
      ↓
    3.7 Create Booking
      ↓
    3.8 Reserve Slot
      ↓
    3.9 Send to Payment
      ↓
    3.10 Confirm Booking
      ↓
    QR + OTP
      ↓
    User

------------------------------------------------------------------------

# 69. DFD LEVEL 2 --- ENTRY/EXIT PROCESS

    User
      ↓
    QR or OTP
      ↓
    6.1 Receive Credential
      ↓
    6.2 Validate Credential
      ↓
    6.3 Validate Booking
      ↓
    6.4 Validate Time/Status
      ↓
    ┌───────────────┐
    │ Entry or Exit │
    └───────┬───────┘
            │
       ┌────┴────┐
       ▼         ▼
     ENTRY      EXIT
       │         │
       ▼         ▼
    OCCUPIED   AVAILABLE
       │         │
       └────┬────┘
            ▼
       Access Log

------------------------------------------------------------------------

# 70. DFD LEVEL 2 --- AI PREDICTION PROCESS

    Historical Data
          ↓
    7.1 Data Collection
          ↓
    7.2 Data Cleaning
          ↓
    7.3 Feature Preparation
          ↓
    7.4 Linear Regression
          ↓
    7.5 Prediction
          ↓
    Predicted Availability
          ↓
    Admin/User Interface

------------------------------------------------------------------------

# 71. COMPLETE USER WORKFLOW

    Open SmartPark
          ↓
       Sign Up
          ↓
     OTP Verify
          ↓
        Login
          ↓
      Dashboard
          ↓
    Find Parking
          ↓
    Select Location
          ↓
    View Details
          ↓
    Select Date/Time
          ↓
    Enter Vehicle Details
          ↓
    Find Compatible Slots
          ↓
    Select Slot
          ↓
    Review Booking
          ↓
       Payment
          ↓
    Booking Confirmed
          ↓
      QR + OTP
          ↓
     My Bookings
          ↓
    Booking Details
          ↓
      Reach Parking
          ↓
    QR OR OTP Entry
          ↓
     Slot OCCUPIED
          ↓
       Parking
          ↓
    QR OR OTP Exit
          ↓
     Slot AVAILABLE
          ↓
    Booking COMPLETED

------------------------------------------------------------------------

# 72. BOOKING WORKFLOW

    Find Parking
        ↓
    Parking Details
        ↓
    Date + Time
        ↓
    Vehicle Details
        ↓
    Compatibility Check
        ↓
    Availability Check
        ↓
    Slot Selection
        ↓
    Fee Calculation
        ↓
    Payment
        ↓
    Booking Confirmation
        ↓
    QR + OTP Generation

------------------------------------------------------------------------

# 73. ADMIN WORKFLOW

    Admin Login
        ↓
    Admin Dashboard
        ↓
    Manage Parking Locations
        ↓
    Manage Parking Slots
        ↓
    Manage Users
        ↓
    Manage Bookings
        ↓
    Manage Payments
        ↓
    Entry/Exit Monitoring
        ↓
    AI Predictions
        ↓
    Analytics
        ↓
    Reports
        ↓
    Profile/Settings

------------------------------------------------------------------------

# 74. PARKING SEARCH WORKFLOW

    User opens Find Parking
            ↓
    Search/filter location
            ↓
    Retrieve parking locations
            ↓
    Show map/list
            ↓
    Select parking
            ↓
    View current availability
            ↓
    View predicted availability
            ↓
    Continue booking

------------------------------------------------------------------------

# 75. SLOT ALLOCATION WORKFLOW

    Vehicle Information
          ↓
    Determine vehicle category
          ↓
    Retrieve candidate slots
          ↓
    Remove incompatible slots
          ↓
    Remove unavailable slots
          ↓
    Check booking conflicts
          ↓
    Display suitable slots
          ↓
    User selects slot
          ↓
    Final availability check
          ↓
    Reserve

------------------------------------------------------------------------

# 76. PAYMENT WORKFLOW

    Booking Review
         ↓
    Calculate Amount
         ↓
    Demo Payment
         ↓
    Payment Result
      /        \

Success Failure ↓ ↓ Confirm Retry/Cancel Booking

------------------------------------------------------------------------

# 77. EXTENSION WORKFLOW

    Booking Details
         ↓
    Extend Booking
         ↓
    Select New End Time
         ↓
    Check Conflict
      /       \

Valid Conflict ↓ ↓ Calculate Reject Fee ↓ Additional Payment ↓ Update
Booking ↓ Extension Confirmed

------------------------------------------------------------------------

# 78. ENTRY WORKFLOW

    User arrives
        ↓
    Present QR OR OTP
        ↓
    Verify credential
        ↓
    Verify booking
        ↓
    Verify status/time
        ↓
    Approve entry
        ↓
    Booking ACTIVE
        ↓
    Slot OCCUPIED
        ↓
    Log entry

------------------------------------------------------------------------

# 79. EXIT WORKFLOW

    User leaves
        ↓
    Present QR OR OTP
        ↓
    Verify credential
        ↓
    Verify active booking
        ↓
    Approve exit
        ↓
    Slot AVAILABLE
        ↓
    Booking COMPLETED
        ↓
    Log exit

------------------------------------------------------------------------

# 80. NOTIFICATION WORKFLOW

    System Event
        ↓
    Determine notification type
        ↓
    Create notification
        ↓
    Store notification
        ↓
    User opens notifications
        ↓
    Mark as read

------------------------------------------------------------------------

# 81. SECURITY REQUIREMENTS

The system must implement:

-   password hashing
-   secure sessions
-   environment variables
-   protected routes
-   admin authorization
-   user ownership validation
-   booking ownership validation
-   input validation
-   parameterized database operations
-   CSRF protection where applicable
-   safe QR credential handling
-   hashed/secure OTP handling where appropriate
-   session expiry/secure cookie settings
-   no hard-coded production secrets

Never commit real passwords, API keys or secret credentials.

------------------------------------------------------------------------

# 82. QR SECURITY

QR credentials should:

-   be unpredictable
-   not expose passwords
-   not expose unnecessary personal information
-   be tied to a booking
-   be validated server-side
-   respect booking status
-   respect access timing
-   be invalidated when no longer valid

Do not trust data supplied directly by the browser.

------------------------------------------------------------------------

# 83. OTP SECURITY

OTP should:

-   be sufficiently random
-   expire
-   have limited attempts
-   be associated with the correct booking
-   be invalidated after successful use where appropriate
-   be verified server-side

Avoid storing plain OTP values when a secure hash/reference approach is
practical.

------------------------------------------------------------------------

# 84. FUNCTIONAL REQUIREMENTS

## User

-   Register
-   Verify OTP
-   Login
-   Logout
-   View dashboard
-   Search parking
-   View parking details
-   View availability
-   View predictions
-   Enter vehicle details
-   Select slot
-   Book parking
-   Make demo payment
-   View booking success
-   View bookings
-   View booking details
-   Access QR/OTP
-   Extend booking
-   View notifications
-   Manage profile

## Admin

-   Login
-   Dashboard
-   Manage locations
-   Manage slots
-   Manage users
-   Manage bookings
-   Manage payments
-   Monitor entry/exit
-   View AI predictions
-   View analytics
-   View reports
-   Manage profile/settings

------------------------------------------------------------------------

# 85. NON-FUNCTIONAL REQUIREMENTS

## Usability

The system should be easy for first-time users.

## Performance

Common pages should load quickly and avoid unnecessary database queries.

## Security

Authentication, authorization and validation must be enforced
server-side.

## Reliability

Booking and slot-state changes must maintain consistent data.

## Maintainability

Use clear modules and understandable code.

## Responsiveness

The interface must work on desktop, tablet and mobile.

## Scalability

The architecture should remain reasonably extensible without introducing
unnecessary complexity.

------------------------------------------------------------------------

# 86. ERROR HANDLING

Handle:

-   invalid login
-   invalid registration
-   OTP failure
-   unavailable slot
-   conflicting booking
-   payment failure
-   expired booking
-   invalid QR
-   invalid OTP
-   unauthorized access
-   missing record
-   invalid vehicle data
-   database failure
-   API failure

User-facing messages must be understandable.

Do not expose internal stack traces to users.

------------------------------------------------------------------------

# 87. API ERROR FORMAT

Use a consistent JSON style such as:

    {
      "success": false,
      "message": "Parking slot is no longer available"
    }

Success example:

    {
      "success": true,
      "message": "Booking confirmed",
      "data": {}
    }

The exact response structure may be standardized during implementation.

------------------------------------------------------------------------

# 88. TESTING REQUIREMENTS

Test at minimum:

### Authentication

-   registration
-   duplicate email
-   OTP verification
-   login
-   logout
-   unauthorized access

### Parking

-   location listing
-   location details
-   slot listing
-   slot status

### Booking

-   valid booking
-   conflicting booking
-   incompatible slot
-   expired booking
-   cancellation if implemented
-   extension

### Payment

-   successful payment
-   failed payment
-   duplicate payment handling

### QR/OTP

-   valid QR
-   invalid QR
-   expired QR
-   valid OTP
-   invalid OTP
-   expired OTP
-   wrong booking
-   entry
-   exit

### Slot State

-   AVAILABLE → RESERVED
-   RESERVED → OCCUPIED
-   OCCUPIED → AVAILABLE

### ML

-   dataset loading
-   preprocessing
-   model training
-   prediction
-   invalid input handling

### Admin

-   admin authorization
-   location management
-   slot management
-   user management
-   booking management

### Security

-   user data isolation
-   route protection
-   input validation
-   password hashing

------------------------------------------------------------------------

# 89. ACADEMIC DIAGRAM REQUIREMENTS

The final project documentation should include:

1.  System Architecture Diagram
2.  ER Diagram
3.  DFD Level 0
4.  DFD Level 1
5.  DFD Level 2
6.  User Workflow
7.  Booking Workflow
8.  Admin Workflow
9.  QR/OTP Entry Workflow
10. Exit Workflow
11. ML Prediction Workflow
12. Use Case Diagram
13. Activity Diagram where required
14. Sequence Diagram where required

Diagrams should be readable and academically appropriate.

Do not overload diagrams with implementation-level details.

------------------------------------------------------------------------

# 90. USE CASE DIAGRAM --- CONCEPT

## Actor: User

Use cases:

-   Register
-   Verify OTP
-   Login
-   Search Parking
-   View Parking Details
-   View Availability
-   View Prediction
-   Enter Vehicle Details
-   Select Slot
-   Book Parking
-   Make Payment
-   View Booking
-   Access QR
-   Access OTP
-   Enter Parking
-   Exit Parking
-   Extend Booking
-   View Notifications
-   Manage Profile

## Actor: Admin

Use cases:

-   Login
-   Manage Parking Locations
-   Manage Parking Slots
-   Manage Users
-   Manage Bookings
-   Manage Payments
-   Monitor Entry/Exit
-   View Predictions
-   View Analytics
-   View Reports
-   Manage Profile

------------------------------------------------------------------------

# 91. SEQUENCE --- BOOKING

    User
      |
      | booking request
      v
    Frontend
      |
      | POST /api/bookings
      v
    Flask API
      |
      | validate user
      | validate vehicle
      | check slot
      v
    Booking Logic
      |
      | reserve slot
      v
    SQLite
      |
      | booking created
      v
    Payment
      |
      | success
      v
    Booking Logic
      |
      | generate QR/OTP
      v
    Frontend
      |
      v
    Booking Success

------------------------------------------------------------------------

# 92. SEQUENCE --- ENTRY

    User
      |
      | QR/OTP
      v
    Frontend/Scanner
      |
      v
    Flask API
      |
      | validate credential
      v
    Booking
      |
      | validate status/time
      v
    SQLite
      |
      | successful
      v
    Slot State
      |
      | OCCUPIED
      v
    Access Log

------------------------------------------------------------------------

# 93. SEQUENCE --- EXIT

    User
      |
      | QR/OTP
      v
    Flask API
      |
      | validate
      v
    Booking
      |
      v
    Slot
      |
      | AVAILABLE
      v
    Access Log
      |
      v
    Booking COMPLETED

------------------------------------------------------------------------

# 94. DEVELOPMENT ORDER --- FINAL

Development must proceed in controlled phases.

## Phase 1 --- Project Foundation

-   project folder
-   Flask setup
-   Tailwind setup
-   base templates
-   static assets
-   configuration
-   environment handling

## Phase 2 --- SQLite Database

-   database initialization
-   schema/models
-   relationships
-   seed/admin setup for development

## Phase 3 --- Authentication

-   registration
-   OTP verification
-   login
-   logout
-   route protection

## Phase 4 --- Parking

-   locations
-   slots
-   availability
-   parking details
-   Leaflet map

## Phase 5 --- Booking

-   vehicle details
-   slot compatibility
-   conflict prevention
-   booking creation
-   booking details

## Phase 6 --- Payment

-   demo payment
-   payment status
-   booking confirmation

## Phase 7 --- QR/OTP

-   QR generation
-   OTP generation
-   verification
-   entry
-   exit
-   access logs
-   slot state transitions

## Phase 8 --- User Features

-   dashboard
-   my bookings
-   booking details
-   extension
-   notifications
-   profile

## Phase 9 --- Admin

-   dashboard
-   locations
-   slots
-   users
-   bookings
-   payments
-   entry/exit
-   reports
-   analytics

## Phase 10 --- ML

-   dataset
-   preprocessing
-   Linear Regression
-   evaluation
-   model persistence
-   prediction API
-   prediction interface

## Phase 11 --- UI/UX Polish

-   responsive design
-   mobile navigation
-   loading states
-   empty states
-   error states
-   accessibility
-   consistency

## Phase 12 --- Testing & Documentation

-   functional testing
-   security testing
-   ML testing
-   integration testing
-   diagrams
-   screenshots
-   project report
-   viva preparation

------------------------------------------------------------------------

# 95. DEVELOPMENT PRIORITY RULE

The priority is:

    Correctness
        ↓
    Database consistency
        ↓
    Backend/API
        ↓
    Core booking workflow
        ↓
    Security
        ↓
    ML
        ↓
    UI polish
        ↓
    Documentation

Do not spend excessive time on visual polish before the booking and
database logic works.

------------------------------------------------------------------------

# 96. FOLDER STRUCTURE

Recommended structure:

    smartpark/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ├── memory.md
    │
    ├── database/
    │   ├── database.db
    │   ├── schema.sql
    │   └── seed.py
    │
    ├── models/
    │   ├── user.py
    │   ├── admin.py
    │   ├── parking.py
    │   ├── booking.py
    │   ├── payment.py
    │   ├── prediction.py
    │   └── notification.py
    │
    ├── routes/
    │   ├── auth.py
    │   ├── user.py
    │   ├── admin.py
    │   ├── parking.py
    │   ├── booking.py
    │   ├── payment.py
    │   ├── prediction.py
    │   └── qr.py
    │
    ├── services/
    │   ├── booking_service.py
    │   ├── payment_service.py
    │   ├── access_service.py
    │   └── prediction_service.py
    │
    ├── ml/
    │   ├── dataset/
    │   ├── train.py
    │   ├── predict.py
    │   └── model/
    │
    ├── templates/
    │   ├── public/
    │   ├── auth/
    │   ├── user/
    │   └── admin/
    │
    └── static/
        ├── js/
        ├── images/
        └── css/

The structure may be simplified if implementation complexity does not
justify all folders.

------------------------------------------------------------------------

# 97. MEMORY.MD RULE

`memory.md` is required as the short-term implementation memory.

It should contain:

-   current development phase
-   completed features
-   current routes
-   current database status
-   current UI status
-   known bugs
-   recent decisions
-   pending tasks
-   testing status

After meaningful implementation changes, coding agents should update
`memory.md`.

Do not rewrite the entire project context into memory.md.

------------------------------------------------------------------------

# 98. ANTIGRAVITY / CODING AGENT MASTER RULES

Before making changes:

1.  Read this master document.
2.  Read `memory.md` if present.
3.  Inspect the current project structure.
4.  Inspect relevant source files.
5.  Understand existing implementation before editing.
6.  Make the smallest appropriate change.
7.  Preserve working features.
8.  Test the affected feature.
9.  Update `memory.md`.
10. Update this master document only when a stable project decision
    changes.

Never blindly regenerate the entire application.

------------------------------------------------------------------------

# 99. SCOPE CONTROL

Do not add features because they sound impressive.

Every feature must have:

-   clear purpose
-   clear module
-   clear data flow
-   clear UI location
-   clear backend responsibility

Avoid:

-   duplicate pages
-   duplicate APIs
-   unnecessary frameworks
-   unnecessary libraries
-   microservices
-   unnecessary real-time systems
-   unnecessary cloud infrastructure
-   unnecessary AI features

If a new idea is outside scope:

**classify it as FUTURE ENHANCEMENT.**

------------------------------------------------------------------------

# 100. DO NOT BREAK EXISTING FUNCTIONALITY

Before changing a feature:

-   understand dependencies
-   check routes
-   check database references
-   check frontend API calls
-   check templates
-   check JavaScript
-   test related functionality

A visually improved page is not considered successful if it breaks
booking, authentication, APIs or database operations.

------------------------------------------------------------------------

# 101. BEGINNER-FRIENDLY DEVELOPMENT STYLE

The project must remain understandable to an MCA student.

Prefer:

-   clear variable names
-   small functions
-   comments where useful
-   simple Flask patterns
-   straightforward SQL/database operations
-   clear API responses
-   understandable folder structure

Avoid unnecessary advanced abstractions.

The project should be easy to explain in a viva.

------------------------------------------------------------------------

# 102. PERFORMANCE PRINCIPLES

Avoid:

-   repeated database queries
-   unnecessary API calls
-   loading large datasets into every page
-   unnecessary ML predictions
-   unnecessary map operations
-   repeated DOM rebuilding

Use:

-   efficient queries
-   pagination where required
-   appropriate indexes
-   cached/static assets where useful
-   lazy loading where useful

Do not introduce Redis or complex infrastructure without a real
requirement.

------------------------------------------------------------------------

# 103. ACCESSIBILITY

The interface should include:

-   readable contrast
-   visible focus states
-   semantic HTML
-   labels for forms
-   keyboard accessibility where practical
-   adequate touch targets
-   meaningful error messages
-   accessible status indicators

Do not communicate important state only through color.

Example:

Instead of only green:

    AVAILABLE

Use:

    ● AVAILABLE

with appropriate text.

------------------------------------------------------------------------

# 104. FINAL NAVIGATION

## Public

    Home
    About
    Services
    Contact
    Terms
    Privacy

## User

    Dashboard
    Find Parking
    My Bookings
    Notifications
    Profile

Booking-specific screens are reached through the booking flow.

## Admin

    Dashboard
    Parking Locations
    Parking Slots
    Users
    Bookings
    Payments
    Entry/Exit
    AI Predictions
    Analytics
    Reports
    Profile/Settings

------------------------------------------------------------------------

# 105. FINAL BUSINESS RULES

1.  SmartPark manages its own parking locations.
2.  Users cannot create parking locations.
3.  Vehicle number is NOT collected during registration.
4.  Vehicle information is collected during booking.
5.  Vehicle type affects slot compatibility.
6.  A booking cannot use an incompatible slot.
7.  A slot cannot have conflicting active reservations.
8.  Confirmed booking reserves a slot.
9.  Successful entry changes slot to OCCUPIED.
10. Successful exit changes slot to AVAILABLE.
11. QR and OTP are alternative access methods.
12. QR/OTP access belongs in Booking Details.
13. There is no separate My QR page.
14. There is no separate My Vehicles page.
15. Booking extension requires conflict checking and additional payment.
16. Initial payment is Demo Payment.
17. ML is used for availability prediction.
18. Linear Regression is the selected baseline ML algorithm.
19. ML does not control security or booking validation.
20. SQLite is the final current database.
21. Tailwind CSS is the final frontend styling technology.
22. Leaflet + OpenStreetMap is the map solution.
23. Flask is the backend framework.
24. The system has two main application modules: User and Admin.

------------------------------------------------------------------------

# 106. TECHNOLOGIES NOT SELECTED

The following are not required for the current implementation:

-   React
-   Next.js
-   Django
-   FastAPI
-   PostgreSQL
-   MySQL
-   MongoDB
-   GraphQL
-   gRPC
-   WebSockets
-   Redis
-   Google Maps API
-   Razorpay as a mandatory dependency
-   LLM-based recommendations

This does not mean these technologies are bad.

They are simply unnecessary for the current project baseline.

------------------------------------------------------------------------

# 107. FUTURE ENHANCEMENTS

Possible future features:

-   real payment gateway
-   mobile application
-   IoT parking sensors
-   automated barrier hardware
-   ANPR/license plate recognition
-   dynamic pricing
-   advanced ML models
-   real-time sensor feeds
-   navigation integration
-   EV charging reservation
-   multi-branch SmartPark deployment
-   cloud database migration
-   advanced predictive analytics

These are future enhancements, not mandatory current features.

------------------------------------------------------------------------

# 108. FINAL PROJECT DEFINITION

SmartPark is a Flask-based smart parking web application using:

    HTML5
          +
    Tailwind CSS
          +
    JavaScript
          +
    Leaflet.js
          +
    Flask
          +
    SQLite
          +
    scikit-learn
          +
    pandas
          +
    numpy
          +
    joblib

The system enables users to discover parking, inspect current and
predicted availability, provide vehicle details, select compatible
slots, reserve parking, make demo payments, receive QR/OTP access
credentials, enter and exit parking, extend bookings, and track
bookings.

Administrators centrally manage the SmartPark parking infrastructure and
monitor users, bookings, payments, entry/exit activity, analytics and ML
predictions.

The project is intentionally designed to be:

-   practical
-   explainable
-   secure
-   maintainable
-   responsive
-   academically defensible
-   beginner-friendly
-   realistic for an MCA mini project

------------------------------------------------------------------------

# 109. FINAL DEVELOPMENT CHECKLIST

Before considering the project complete:

## Foundation

-   [ ] Flask application runs
-   [ ] SQLite initializes
-   [ ] Tailwind loads correctly
-   [ ] Base layout works
-   [ ] Responsive navigation works

## Authentication

-   [ ] Registration
-   [ ] OTP
-   [ ] Login
-   [ ] Logout
-   [ ] Route protection

## Parking

-   [ ] Locations
-   [ ] Slots
-   [ ] Availability
-   [ ] Map
-   [ ] Parking details

## Booking

-   [ ] Vehicle information
-   [ ] Compatibility
-   [ ] Slot selection
-   [ ] Conflict prevention
-   [ ] Booking creation
-   [ ] Booking details
-   [ ] Extension

## Payment

-   [ ] Demo payment
-   [ ] Payment status
-   [ ] Confirmation

## Access

-   [ ] QR
-   [ ] OTP
-   [ ] Entry
-   [ ] Exit
-   [ ] Access logs
-   [ ] Slot state updates

## User

-   [ ] Dashboard
-   [ ] My Bookings
-   [ ] Notifications
-   [ ] Profile

## Admin

-   [ ] Dashboard
-   [ ] Locations
-   [ ] Slots
-   [ ] Users
-   [ ] Bookings
-   [ ] Payments
-   [ ] Entry/Exit
-   [ ] Predictions
-   [ ] Analytics
-   [ ] Reports
-   [ ] Settings

## ML

-   [ ] Dataset
-   [ ] Preprocessing
-   [ ] Linear Regression
-   [ ] Evaluation
-   [ ] Model saving
-   [ ] Prediction
-   [ ] UI

## Security

-   [ ] Password hashing
-   [ ] Secure sessions
-   [ ] Authorization
-   [ ] Validation
-   [ ] QR security
-   [ ] OTP security
-   [ ] No secrets in repository

## Documentation

-   [ ] Introduction
-   [ ] Problem Statement
-   [ ] Existing System
-   [ ] Drawbacks
-   [ ] Proposed System
-   [ ] Objectives
-   [ ] Modules
-   [ ] Architecture
-   [ ] Database
-   [ ] ER Diagram
-   [ ] DFD Level 0
-   [ ] DFD Level 1
-   [ ] DFD Level 2
-   [ ] Workflow Diagrams
-   [ ] Use Case Diagram
-   [ ] Activity Diagram
-   [ ] Sequence Diagram
-   [ ] ML Methodology
-   [ ] Testing
-   [ ] Limitations
-   [ ] Future Enhancements
-   [ ] Conclusion

------------------------------------------------------------------------

# 110. SOURCE OF TRUTH PRIORITY

When documents or instructions conflict, use this priority:

1.  Explicit latest project decision from the user
2.  This master project document
3.  `memory.md` for current implementation state
4.  Existing working code
5.  Older drafts
6.  General assumptions

Never silently override an explicit project decision.

------------------------------------------------------------------------

# 111. FINAL MASTER INSTRUCTION TO ANTIGRAVITY AND OTHER CODING AGENTS

You are working as the lead developer and technical implementation
assistant for:

**SmartPark -- Automated Smart Parking Reservation System**

Treat this document as the project's stable source of truth.

Before coding:

-   read this document
-   read `memory.md`
-   inspect the existing code
-   identify the current implementation state
-   understand dependencies

During coding:

-   use Flask
-   use Tailwind CSS
-   use JavaScript
-   use SQLite
-   use Leaflet/OpenStreetMap
-   use Linear Regression for availability prediction
-   preserve the two-module structure: User and Admin
-   keep vehicle information in bookings
-   keep QR/OTP inside Booking Details
-   support QR OR OTP as alternative access methods
-   maintain the slot lifecycle
-   prevent booking conflicts
-   keep payment as Demo Payment initially
-   use secure authentication and validation
-   keep the implementation beginner-friendly
-   avoid feature creep
-   avoid unnecessary technologies
-   do not create duplicate pages
-   do not create duplicate modules
-   do not switch databases/frameworks without explicit approval

After coding:

-   test the changed functionality
-   verify related functionality
-   update `memory.md`
-   document important stable decisions
-   report any unresolved issue clearly

Never claim a feature works without testing it.

Never replace working functionality merely to make the code look
different.

Never add an impressive feature merely because it is technically
possible.

The goal is not to build the largest parking application.

The goal is to build a **coherent, intelligent, automated, secure,
responsive and academically strong MCA mini project**.

------------------------------------------------------------------------

# 112. DEVELOPMENT STARTING POINT

This document is now the **FINAL BASELINE PROJECT GUIDE**.

After this document is accepted:

    STOP MAJOR REQUIREMENT CHANGES

and begin implementation in this order:

    1. Project foundation
    2. Tailwind frontend foundation
    3. SQLite database
    4. Authentication
    5. Parking locations and slots
    6. Booking
    7. Demo payment
    8. QR/OTP
    9. Entry/Exit
    10. User module completion
    11. Admin module
    12. ML prediction
    13. Testing
    14. Documentation
    15. Final UI polish
    16. Deployment

Any new idea discovered during development must first be classified as:

    CURRENT SCOPE
    or
    FUTURE ENHANCEMENT

Do not silently expand the project.

------------------------------------------------------------------------

# END OF SMARTPARK MASTER PROJECT CONTEXT

------------------------------------------------------------------------

# UI/UX DESIGN SYSTEM & DASHBOARD DESIGN GUIDELINES

## Design Inspiration

SmartPark UI/UX will take inspiration from the provided premium
editorial dashboard design analysis.

The design inspiration will be used for:

-   Layout structure
-   Visual hierarchy
-   Typography approach
-   Dashboard organization
-   Spacing system
-   Component design
-   Animation style

The design will be adapted to SmartPark and will not directly copy the
reference project.

------------------------------------------------------------------------

# Overall Design Identity

SmartPark will follow:

**Premium Mobility Platform + Neo-Brutalist Dashboard Design**

Core characteristics:

-   Minimal and structured layouts
-   Strong typography hierarchy
-   Professional dashboard experience
-   High contrast visual system
-   Purpose-driven components
-   Clean spacing and alignment

Avoid:

-   Excessive card layouts
-   Generic SaaS templates
-   Unnecessary illustrations
-   Heavy gradients
-   Visual clutter

------------------------------------------------------------------------

# SmartPark Color System

## Primary

Deep Navy:

    #0B132B

Used for:

-   Sidebar
-   Headers
-   Primary branding

## Background

Soft White:

    #FAFAF9

## Surface

Light Gray:

    #F1F5F9

## Text

Primary:

    #0F172A

Secondary:

    #475569

## Accent

Electric Blue:

    #2563EB

Used for:

-   Active navigation
-   Primary actions
-   Selected parking slots
-   Important interactions

## Status Colors

Available:

    #16A34A

Occupied:

    #DC2626

Warning:

    #F59E0B

------------------------------------------------------------------------

# Typography

Typography is a major visual element.

Recommended fonts:

-   Inter
-   Plus Jakarta Sans

Hierarchy:

## Hero/Public Pages

Large editorial headings:

    text-6xl
    md:text-7xl
    lg:text-[6rem]

## Dashboard Headings

    text-3xl
    font-bold
    tracking-tight

## Labels

Small uppercase labels:

    text-xs
    tracking-widest
    uppercase

------------------------------------------------------------------------

# Layout System

## Public Website

Use:

-   Maximum width containers (1200px - 1400px)
-   Large vertical spacing
-   Clear section separation
-   Border-based layouts

Avoid unnecessary floating cards.

------------------------------------------------------------------------

# Dashboard Layout

Both User and Admin modules use a professional left sidebar dashboard
layout.

Structure:

    ------------------------------------------------
    | Sidebar              | Main Content           |
    |                      |                        |
    | SmartPark Logo       | Header                 |
    | Dashboard            |                        |
    | Parking              | Page Content           |
    | Bookings             |                        |
    | Notifications        |                        |
    | Profile              |                        |
    ------------------------------------------------

------------------------------------------------------------------------

# User Module UI Direction

The user experience is inspired by BookMyShow's discovery and booking
flow.

Main goal:

    Open App
       ↓
    Find Parking
       ↓
    Book Slot
       ↓
    Manage Parking

------------------------------------------------------------------------

# User Sidebar

    SMARTPARK

    Dashboard

    Find Parking

    My Bookings

    Current Parking

    Notifications

    Review & Feedback

    Profile

------------------------------------------------------------------------

# User Dashboard Design

Dashboard contains:

## Parking Search

Primary action:

    Where do you want to park?

    [ Search parking location ]

## Current Parking

Shows:

-   Parking location
-   Slot
-   Remaining time
-   Extend option

## Upcoming Booking

Shows:

-   Parking location
-   Date
-   Time
-   Slot
-   Booking status

## Parking Discovery

Optional sections:

-   Nearby Parking
-   Popular Locations
-   Recently Viewed Parking

------------------------------------------------------------------------

# User Booking Experience

Flow:

    Find Parking

          ↓

    Select Location

          ↓

    Parking Details

          ↓

    Vehicle Details

          ↓

    Slot Selection

          ↓

    Booking Summary

          ↓

    Payment

          ↓

    QR + OTP

------------------------------------------------------------------------

# Admin Dashboard UI Direction

Admin uses the same visual language but focuses on management and data.

Sidebar:

    SMARTPARK ADMIN

    Dashboard

    Parking Management
        Locations
        Slots

    Users

    Bookings

    Payments

    Entry / Exit

    Intelligence
        Predictions
        Analytics
        Reports

    Communication
        Reviews
        Feedback
        Contact Messages

    Profile

------------------------------------------------------------------------

# Admin Dashboard Content

Use structured sections instead of excessive cards.

Display:

-   Total users
-   Active bookings
-   Available slots
-   Revenue
-   Occupancy overview

Analytics sections use Chart.js.

------------------------------------------------------------------------

# Prediction Page Design

Prediction is an intelligence feature.

It displays:

-   Expected occupancy
-   Expected available slots
-   Peak parking hours
-   Availability trends

ML does not control:

-   Slot allocation
-   Booking approval
-   Payments
-   OTP verification

------------------------------------------------------------------------

# Component Design

## Buttons

Style:

-   Clean
-   Strong contrast
-   Slight hover scaling
-   Clear action hierarchy

## Cards

Use minimal bordered surfaces:

-   Light borders
-   Small radius
-   Limited shadows

Avoid making every section a card.

## Tables

Admin tables should include:

-   Clean borders
-   Sticky headers
-   Status badges
-   Search/filter options

------------------------------------------------------------------------

# Motion Design

Use smooth premium animations:

    cubic-bezier(0.16,1,0.3,1)

Animations:

-   Fade up
-   Slide reveal
-   Staggered loading
-   Hover micro-interactions

------------------------------------------------------------------------

# Glass Effects

Use only where required:

Allowed:

-   Sidebar overlays
-   Navigation elements

Avoid:

-   Glass effect on every card
-   Excessive blur

------------------------------------------------------------------------

# Responsive Design

Desktop:

    Sidebar + Content

Mobile:

    Collapsed sidebar
    Bottom navigation

Typography and layouts should scale responsively.

------------------------------------------------------------------------

# SmartPark Design DNA

    Premium Mobility Dashboard

    +
    BookMyShow-inspired user discovery

    +
    Neo-brutalist editorial structure

    +
    Professional admin management interface

Core principles:

1.  Strong typography
2.  Spacious layouts
3.  Left sidebar navigation
4.  Minimal cards
5.  Clear user actions
6.  Data-focused admin design
7.  Smooth micro-interactions
8.  Consistent visual system
