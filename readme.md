# RealtorHub

A Django + Electron desktop application for managing real estate deals. RealtorHub lets realtors, buyers, and sellers store and organise property listings locally — no internet connection required.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [URL Routes](#url-routes)
- [Data Model](#data-model)
- [Notable Implementation Details](#notable-implementation-details)

---

## Features

- **Add property listings** — record Agriculture Land, House, Flat, or Shop entries with full details
- **Track parties** — up to 5 buyers, 1 seller, and 2 dealers per listing
- **Property details** — name, type, size (length × breadth), marla, state, city, address, and nearby landmarks
- **Financial details** — total amount, rate, SAI, and expenses displayed in Indian number format (e.g. ₹12,34,567)
- **Registry date picker** — calendar widget for selecting the registration date
- **Multi-line payment conditions** — newlines are preserved when viewing a listing
- **Sort listings** — by most recent, name A–Z / Z–A, or registry date ascending / descending
- **Search** — find listings by property name (prefix match, case-insensitive)
- **Edit & Delete** — both actions require JavaScript confirmation before proceeding
- **User authentication** — register, login, and logout; each user sees only their own listings
- **Offline-ready** — Bootstrap assets are bundled locally
- **Desktop app** — wraps the Django server in an Electron window (Windows & Linux)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django 5.0.6 |
| Frontend | HTML, Bootstrap (local), JavaScript |
| Desktop shell | Electron 32 (via Node.js / npm) |
| Database | SQLite (default Django DB) |

---

## Project Structure

```
RealtorHub/
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies (Django)
├── package.json            # Node.js dependencies (Electron)
├── index.js                # Electron main process — loads localhost:8000
├── realtor.bat             # Windows launcher
├── realtor.sh              # Linux/macOS launcher
├── realtorspace/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
└── realtorhub/             # Main Django application
    ├── models.py           # User and Property models
    ├── views.py            # All view functions
    ├── forms.py            # PropertyForm (ModelForm)
    ├── urls.py             # URL patterns
    ├── templatetags/
    │   └── custom_filters.py   # intcomma_in — Indian number formatting
    ├── templates/realtorhub/   # HTML templates
    └── static/                 # CSS, JS, Bootstrap assets
```

---

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.10 or later |
| Django | 5.0.6 (installed via pip) |
| Node.js & npm | LTS recommended |
| Electron | installed automatically via npm |

---

## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Sanyam-bot/RealtorHub.git
   cd RealtorHub
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies** *(only needed for the desktop app)*

   ```bash
   npm install
   ```

4. **Apply database migrations**

   ```bash
   python manage.py migrate
   ```

---

## Running the Application

### As a Desktop App (Electron)

The launcher scripts start the Django development server and then open Electron.

**Windows:**
```bat
realtor.bat
```

**Linux / macOS:**
```bash
bash realtor.sh
```

### As a Web App Only

No Node.js or Electron required.

```bash
python manage.py runserver
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `index` | Dashboard — list all property listings |
| `/add` | `add_property` | Add a new property listing |
| `/property/<id>` | `property` | View details of a listing; POST to delete it |
| `/edit/<id>` | `edit` | Edit an existing listing |
| `/search` | `search` | Search listings by property name |
| `/login` | `login_view` | Login page |
| `/logout` | `logout_view` | Logout and redirect to index |
| `/register` | `register` | Register a new account |

---

## Data Model

### `Property`

| Field | Type | Notes |
|---|---|---|
| `user` | ForeignKey | Owner of the listing |
| `property_name` | CharField | Auto title-cased on save |
| `type` | CharField | `agriculture`, `house`, `flat`, or `shop` |
| `buyer_1` … `buyer_5` | CharField | Up to five buyers |
| `seller` | CharField | |
| `dealer_1`, `dealer_2` | CharField | Up to two dealers |
| `state`, `city`, `address1`, `nearby` | CharField | Location fields |
| `total_amount`, `expenses`, `sai` | IntegerField | Shown in Indian number format |
| `rate` | CharField | Rate per unit |
| `size` | CharField | Format: `Length x Breadth` |
| `marla` | IntegerField | Area in marla |
| `registry_date` | DateField | Chosen via calendar widget |
| `payment_condition` | TextField | Newlines preserved as `<br>` in detail view |

---

## Notable Implementation Details

### Indian Number Format (`templatetags/custom_filters.py`)
The custom `intcomma_in` template filter displays integers in the Indian numeral system (e.g. `1234567` → `12,34,567`). Numbers with three or fewer digits are returned as-is; for longer numbers the last three digits are separated first, then remaining digits are grouped in pairs from right to left.

### Hardware Acceleration Disabled (`index.js`)
`app.disableHardwareAcceleration()` is called before the Electron window is created. This ensures compatibility with older or integrated GPUs that do not fully support Electron's GPU compositing.

### Payment Condition Newline Handling (`views.py` — `add_property`)
Before saving a new listing, newline characters (`\n`) in the `payment_condition` field are replaced with `<br>` so that line breaks entered by the user are preserved when the listing is displayed in the browser.

### Search Algorithm (`views.py` — `search`)
The search performs a case-insensitive prefix match: the query is title-cased and compared character-by-character against each `property_name`. A listing is included in the results only if every character of the query matches the corresponding position in the property name.