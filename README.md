# Custom Django Authentication

A custom authentication system built with Django, featuring login, signup, password reset via email, and session management.

## Features

- Login with Email or Username
- Signup with Email verification ready
- Password Reset via Email (Ethereal SMTP for testing)
- Session Timeout (Auto Logout)
- Bootstrap 5 UI with form-floating fields
- Show/Hide Password toggle
- Success & Error messages

## Tech Stack

- Python 3.12
- Django 6.0
- Bootstrap 5.3
- Ethereal Email (Testing)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/custom-auth-django.git
cd custom-auth-django
```

### 2. Virtual Environment Banao
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

## Email Testing — Ethereal

1. Go To [ethereal.email](https://ethereal.email) 
2. Create Account 
3. Add Credentials in `.env` 
4. Password reset karo — email **Messages tab** 
5. Rendered HTML Message 

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `MAIL` | Ethereal email address |
| `MAIL_PASSWORD` | Ethereal SMTP password |

## Settings

| Setting | Value |
|---|---|
| `SESSION_COOKIE_AGE` | 1800 (30 min auto logout) |
| `PASSWORD_RESET_TIMEOUT` | 3600 (1 hour) |
| `LOGIN_REDIRECT_URL` | home |
| `LOGOUT_REDIRECT_URL` | login |

## Pages

| URL | Page |
|---|---|
| `/` | Home |
| `/accounts/login/` | Login |
| `/accounts/signup/` | Signup |
| `/accounts/logout/` | Logout |
| `/accounts/password_reset/` | Forgot Password |

---

## Author

Muhammad Waqas Khan
