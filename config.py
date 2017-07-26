# Application settings
APP_NAME = "fp"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "e3ea9526f9c148f5858b25a8475d9e05"

# Secret key for signing cookies
SECRET_KEY = "e3ea9526f9c148f5858b25a8475d9e05"
