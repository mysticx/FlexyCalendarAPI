class SecurityConfigurations():
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'flexy_calendar',
            'USER': 'root',
            'PASSWORD': '',
        }
     }
    SECRET_KEY = '(8qem3)&pe^l=(#lb6&-b&)+u&9w_vtket(0f=#gt30i+cfvba'
    CORS_ORIGIN_WHITELIST = (
        'localhost:8000',
        'localhost:8000/',
        'http://localhost:8000',
        'http://localhost:8000/',
        'http://127.0.0.1:8000',
        '127.0.0.1:8000',
        '46.101.163.181:80',
    )