
 

 # AWS_ACCESS_KEY_ID = 'AKIAIQV5OYFEVOZBC5JQ'
# AWS_SECRET_ACCESS_KEY = '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'
 # Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

#Email settings

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'titiphotos593@gmail.com'
EMAIL_HOST_PASSWORD = 'Bl@zetr@il'
EMAIL_PORT = 587
EMAIL_USE_TLS = True