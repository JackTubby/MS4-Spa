# Under Development
# Purity - Spa Website

## Table of Contents


### User Stories
- I want users to be able to find treatments and see more details about them
- I want users to be able to easily navigate around the site
- I want users to be able to add treatments to there basket 
- I want users to be able to purchase treatments
- I want users to be able to get in contact using a contact page
- I want users to be able to leave the spa reviews/testimonials
- I want users to be able to sign up/ login
- I want users to be able to use an offers page only when logged in
- I want users to to be able to sign up to the new letter
- I want admin users to add/edit/delete treatments and offers
- I want admin users to be able to post blog updates


|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| Anonymous user       | view the site on all screen sizes;                                       | visit the site using my mobile and/or tablet device           |
| Anonymous user       | understand the what the site is for from the homepage;                   | to make sure the website fits my needs                        |
| Anonymous user       | easily navigate around the site;                                         | find what I am looking for quickly and easily                 |
| Anonymous user       | search for treatments;                                                   | browse for treatments instead of scrolling through them all   |
| Anonymous user       | filter my search results;                                                | see the range of prices & categorys                           |
| Anonymous user       | read details about the treatments;                                       | to understand what the treatment provides                     |    
| Anonymous user       | add treatments into my cart;                                             | add a treatment whilst looking at more                        |
| Anonymous user       | understand why I should sign up;                                         | understand the benifits of signing up                         |
| Anonymous user       | gain access to the companys social media;                                | visit you social media pages                                  |
| Anonymous user       | register for a user profile account by choosing a username and password; | save billing details & gain access to offers, ratings         |
| Anonymous user       | able to view blog/updates for the company;                               | understand what's new in the company & there aims             |
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and log out of my account;                                        | safeguard all my information whilst not active on the site    |
| Registered user      | update my billing information;                                           | update any new detials I obtain                               |
| Registered user      | access to special offers/packages;                                       | get great deals on treatments                                 |
| Registered user      | store my order history;                                                  | gain access to previous treatment orders                      |
|          ---         |                                    ---                                   |                              ---                              |
| Site admin/superuser | add new treatments to the site;                                          | always make new treatments avaliable for users                |
| Site admin/superuser | add blogs to the site;                                                   | update users on any new updates with the company              |
| Site admin/superuser | delete treatments;                                                       | delete treatments that are no longer provided                 |
| Site admin/superuser | edit treatment                                                           | make changes to any added treatments                          |
| Site admin/superuser | delete blogs;                                                            | delete any updates that may not be needed anymore             |
| Site admin/superuser | edit blogs;                                                              | edit blogs for any mistakes/changes on the updates            |
|                      |                                                                          |                                                               |

## UX

### Project Goals
* Ease of use.
* Look at the stores treatments.
* Able to purchase treatments in a simple process.
* Full authentication functionality.
* CRUD functionality for store owners to add blogs & treatments.
* Users who purchase a treatment able to set a rating.

### Scope
* Allow users to make purchases on the site.
* Allow users to set ratings on treatments they have purchased.
* Allow users to register for an account & change password when needed.
* Allow Admins to use CRUD functionality to add treatments & blogs.
* Create the site using FullStack development skills.

### Structure
* Fixed navigation bar, This will increase UI/UX for all users on a wide range of devices. For example small screens can easily navigate from anywhere in the page.
* The navigation bar will contain a drop down menu containing page links and the website title. Also located in the navigation bar will be a profile dropdown containing login/signup or profile for logged in users, admins will have a link to add a treatment or blog. The final link in the navbar will be a link to the cart also showing the cart total.
* The top right just below the navbar will show all toast messages.
* Every page will contain a footer which will consist of the company address, links, contact details and social media links.

### Surface
#### Colours
I have chosen a wide range of colours for my website:
* #9eb4a7 This light shade of green was used to give a calm and relaxing feeling to the site. It was used mainly on buttons and on some backgrounds making the text stand out more.
* #f3c1a4 A mix of orange and beige complimenting the overall theme of the site, this was mainly used on buttons and background colours.
* White was used alot over the site giving it a clean and calm feel inline with the sites goal. White was used on a lot of backgrounds and used on some text when on a dark background.
* Black was used for text to make it stand out on lighter backgrounds and catch the users eye.
* Any other colours where chosen through development, a case of this may be when using a previously chosen colour the text did not stand out enough so the colour was changed to match this.
#### Icons
In the project, icons were obtained from [Font Awesome](https://fontawesome.com/). Icons were used for different settings, for example they was used for social media icons but also to help users understand details. An example of this is the checkout button showing a locked lock to give the feel this is the final step to take payment.
#### Typography
* "Lato" used as a base font as it is readable and simple.
* "Dancing Script" An elegant font fitting the clean and fancy theme, mainly used for headings.
* "Courgette" Also an elegant font fitting the clean and fancy theme, mainly used for headings.
* "Monstratt" Used alongside "Lato" it is a clean and readble font perfect for getting information to the user.
#### Imagery
When choosing imagery I used [Pexels](https://www.pexels.com/). Images were used mainly for background images in the site as well as a fallback image if user's uploaded image is not avaliable.
#### Information Architecture
###### Database
SQLite3 was used during development which is included in the default Django installation. Heroku Postgres is used in the production site.
###### Apps and Models used
- Blog App
- Cart App
- Checkout App
- Home App
- Profiles App
- Treatments App

#### Wireframes
TO ADD

## Features
### Existing Features
* Created with HTML5, CSS3, JavaScript, jQuery, Bootstrap, Django, Python.
* Responsive design.
* Home/Index page for users to understand what the site is.
* Footer with social media links, navigation links, address and contact details.
* CRUD functionality for admin users to create treatments or blogs edit and delete them, with any user being able to be read them.
* Rating system where users who purchase the treatment can set a rating and it works out the average.
* Full Stripe payment system implemented to purchase treatments.
* Full user authentications system.
* Profile page showing users previous orders, save billing information and change password.
* Treatment search functionality, searching by name and description.
* Treatment sort by choices.

### Features Left To Implement
* A future feature I would like to implement would be a discount feature where admin users can run offers on treatments.
* A future feature I would like to implement would be a booking system, so users can book a date and time for there treatment.

## Technologies Used
* HTML5
* CSS3
* JavaScript
* Python
* Bootstrap
* FontAwesome
* Google Fonts
* jQuery
* Django
* Git
* Heroku 
* GitHub
* AWS S3 bucket

## Testing


## Deployment
# Deployment

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

---

## Resources
* [Stack Overflow]()
* [Code Institute Course](https://codeinstitute.net/)
* [YouTube]()
* [Balsamiq]()
* [Am I Responsive]()
* [TinyPNG]()

## Credits

### Media

### Acknowledgements

### Support