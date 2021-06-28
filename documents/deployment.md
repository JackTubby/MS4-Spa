## Deployment
## Heroku Deployment

This project was deployed to Heroku via the following steps:

1. Use `pip3 install` to install **gunicorn**, **psycopg2-binary** and **dj-database-url**

2. Create a requirements.txt file with: `pip3 freeze --local > requirements.txt`

3. Create a Procfile and add `web: gunicorn purity.wsgi:application` then add, commit and push these changes.

4. Log into [Heroku](https://www.heroku.com/), click **New** and **Create New App**. Give the project a unique name, choose the region and click **Create App**.

5. Add **Heroku Postgres** in the Add-ons search bar, select **Free** account and **Submit Order Form** to add to the project.

6. From the **Settings** menu, click **Reveal Config Vars**. Set the variables for:

   * **AWS_ACCESS_KEY_ID** - Your AWS Access Key
   * **AWS_SECRET_ACCESS_KEY** - Your AWS Secret Access Key
   * **DATABASE_URL** - Your Postgres Database URL
   * **SECRET_KEY** - Your Secret Key
   * **STRIPE_PUBLIC_KEY** - Your Stripe Public Key
   * **STRIPE_SECRET_KEY** - Your Stripe Secret Key
   * **STRIPE_WH_SECRET** - Your Stripe WH Key
   * **USE_AWS** - True

   Keys for Stripe and AWS can be found on their respective sites.

7. Select **Github** from the **Deployment Method** section, and select Automatic Deployment.

8. Select your Github user and enter the name of your repo, then select it from the search and click **Connect**.

9. Ensure your **`settings.py`** file is set to:
   ```
   if 'DATABASE_URL' in os.environ:
      DATABASES = {
         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
      }
   else:
      DATABASES = {
         'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': BASE_DIR / 'db.sqlite3',
         }
      }
   ```

10. Use `python3 manage.py makemigrations` and `python3 manage.py migrate` to migrate database models to the Postgres database.

11. Load data fixtures using `python3 manage.py loaddata <fixture>` ensuring fixtures are loaded in the following order:
   * **categories**
   * **products**
   * **portfolio**
   * **testimonials**

12. Create a new superuser using `python3 manage.py createsuperuser` and entering an email, username and password.

13. Ensure **`settings.py`** has `ALLOWED_HOSTS = ['purity-mxhaib.herokuapp.com', 'localhost']`

14. In **Stripe** add the Heroku app checkout URL as the new webhook and update **`settings.py`** with new Stripe environment variables and email settings.

15. Add, commit and push all changed to Heroku.

*If you are using AWS as this guide expects, please continue with the following*

16. On **Amazon Web Services (AWS)**, create an account, locate **S3** and add a new bucket. For more information on this process, please visit [AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

17. Add the following CORS configuration:
   ```
   [
   {
         "AllowedHeaders": [
            "Authorization"
         ],
         "AllowedMethods": [
            "GET"
         ],
         "AllowedOrigins": [
            "*"
         ],
         "ExposeHeaders": []
   }
   ]
   ```

18. With `pip3 install` install **boto3** and **django.storages** and freeze with `pip3 freeze --local > requirements.txt`

19. Add **storages** to the list of **INSTALLED_APPS** in **`settings.py`**

20. Ensure the **`settings.py`** file has the following:
   ```
   if 'USE_AWS' in os.environ:
      # Cache Control
      AWS_S3_OBJECT_PARAMETERS = {
         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
         'CacheControl': 'max-age=94608000',
      }

      # Bucket Config
      AWS_STORAGE_BUCKET_NAME = 'purity-mxhaib'
      AWS_S3_REGION_NAME = 'eu-west-2'
      AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
      AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

      # Static and Media files
      STATICFILES_STORAGE = 'custom_storages.StaticStorage'
      STATICFILES_LOCATION = 'static'
      DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
      MEDIAFILES_LOCATION = 'media'

      # Override static and media URLS in production
      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

   ```

21. Ensure the **`custom_storages.py`** file has the following:
   ```
   from django.conf import settings
   from storages.backends.s3boto3 import S3Boto3Storage


   class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION


   class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
   ```

22. Delete **DISABLE_COLLECTSTATIC** from the Config Vars of Heroku.

23. Add, commit and push all changed to Heroku.


## Running This Project Locally

To run this project locally, you will need to use an IDE such as Gitpod, Visual Studio or PyCharm.

This guide assumes you are using Gitpod:

1. Install the Gitpod Browser Extensions for Chrome and restart your browser.

2. Log into Gitpod and navigate to the [MS4 Spa Project GitHub repository](https://github.com/JackTubby/MS4-Spa).

3. Click the green **"Gitpod"** button at the top of the repository.

* Alternatively, you can open up your repository and use the following command to clone this project. `git clone https://github.com/JackTubby/MS4-Spa.git`

4. Create an **`env.py`** file and add to the **.gitignore** file, and add the following to the **`env.py`** file:

   * import os
   * os.enivron["DEVELOPMENT"] = "True"
   * os.environ["SECRET_KEY"] = Your Secret Key
   * os.environ["STRIPE_PUBLIC_KEY"] = Your Stripe Public Key
   * os.environ["STRIPE_SECRET_KEY"] = Your Stripe Secret Key
   * os.environ["STRIPE_WH_SECRET"] = Your Stripe WH Secret Key

5. Ensure that all the requirements are downloaded by using the following command: `pip3 install -r requirements.txt`

6. Migrate models to the database with: `python3 manage.py makemigrations` and `python3 manage.py migrate`

7. Load data fixtures using `python3 manage.py loaddata <fixture>` ensuring fixtures are loaded in the following order:
   * **categories**
   * **products**
   * **blogs**

8. Create a new superuser using `python3 manage.py createsuperuser` and entering an email, username and password.

9. Run the app in your browser by inputting the following command: `python3 manage.py runserver`
