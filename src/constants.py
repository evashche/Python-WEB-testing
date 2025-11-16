from enum import Enum

BASE_URL = "http://instagram.com/"
SIGN_UP_URL = f"{BASE_URL}accounts/emailsignup/"
LOGIN_URL = f"{BASE_URL}accounts/login/"

REQUIRED_FIELD_ERROR = "This field is required."
PASSWORD_ERROR = "This password is too easy to guess. Please create a new one."

class ButtonsSignIn(Enum):
  LOGIN = "Log in with Facebook"
  SIGN_UP = "Sign up"

class ButtonsLogIn(Enum):
  LOGIN = "Log in"
  LOGIN_FACEBOOK = "Log in with Facebook"

class ButtonsLocal(Enum):
  EN = [button.value for button in ButtonsSignIn]
  UK = ["Увійти через Facebook", "Зареєструватися"]

class FieldsLogin(Enum):
  MOBILE_OR_EMAIL = "Phone number, username, or email"
  PASSWORD = "Password"

class FieldsSignIn(Enum):
  MOBILE_OR_EMAIL = "Mobile Number or Email"
  PASSWORD = "Password"
  FULL_NAME = "Full Name"
  USERNAME = "Username"

class FieldsSignInLocal(Enum):
  EN = [field.value for field in FieldsSignIn]
  DE = ["Handynummer oder E-Mail-Adresse", "Passwort", "Vollständiger Name", "Benutzername"]

class FieldsLoginLocal(Enum):
  EN = [field.value for field in FieldsLogin]
  DE = ["Telefonnummer, Benutzername oder E-Mail-Adresse", "Passwort"]

class Links(Enum):
  META = "Meta"
  ABOUT = "About"
  BLOG = "Blog"
  JOBS = "Jobs"
  HELP = "Help"
  API = "API"
  PRIVACY = "Privacy"
  TERMS = "Terms"
  LOCATIONS = "Locations"
  INSTAGRAM_LITE = "Instagram Lite"
  META_AI = "Meta AI"
  META_AI_ARTICLES = "Meta AI Articles"
  THREADS = "Threads"
  CONTACT_UPLOADING = "Contact Uploading & Non-Users"
  META_VERIFIED = "Meta Verified"

class Icons(Enum):
  LIKE = "Like"
  COMMENT = "Comment"
  SHARE = "Share"
  SAVE = "Save"
