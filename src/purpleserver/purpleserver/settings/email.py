from decouple import config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='admin@purplship.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)

EMAIL_PAGE_DOMAIN = config('DOMAIN', default='https://app.purplship.com')
EMAIL_FROM_ADDRESS = config('EMAIL_FROM_ADDRESS', default='noreply@purplship.com')

EMAIL_SERVER = EMAIL_HOST
EMAIL_ADDRESS = EMAIL_HOST_USER
EMAIL_PASSWORD = EMAIL_HOST_PASSWORD

EMAIL_ACTIVE_FIELD = 'is_active'
EMAIL_MAIL_SUBJECT = 'Purplship - Verify Your New Account Email'
EMAIL_MAIL_HTML = 'registration/registration_confirm_email.html'
EMAIL_PAGE_TEMPLATE = 'registration/registration_confirm_done.html'


EMAIL_ENABLED = False
