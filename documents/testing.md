# Testing 
<span id="testing"></span>

## Table of Contents 
> - [User Stories Testing](#userstories)
> - [Code Validation](#validation)
>   - [HTML](#html)
>   - [CSS](#css)
>   - [JavaScript](#js)
>   - [Python](#py)
>   - [error](#error)
> - [Responsive Testing](#responsive)

<span id ="userstories"></span>

## User Story Testing
### Anonymous user
#### View the site on all screen sizes
* Site tested on all screen sizes as shown in [the responsive testing section](#responsive)
#### understand what the site is about from landing page
- **Testing:** Used the [deployed site url](https://purity-mxhaib.herokuapp.com/) and clicked enter, The page opened showing the landing page instantly showing a welcome to message.
  - [Adding url to navbar]() > [Home page showing welcome message]()
#### easily navigate around the site
- The site contains mutlitple ways to navigate, for example the navbar is fixed so no matter how far down a page the menu dropdown is available. The footer also container links around the site and multiple pages throughout the site has back buttons implemented. The home page also has a button strait away with easy navigation to the treatments page. 
- **Testing:** From the landing page I used the dropdown menu and tested all links, using the footer I clicked all link, all links were correct. From the home page I clicked 'take a look button' this correctly opened the treatments page. Throughout the site I tested back buttons for example the treatment details and blog details page.
  - [Menu dropdown links]() > [Footer links]() > ['take a look' button test]() > [Treatment details back button]() > [Blog details back button]()
#### search for treatments
- **Testing:** On the treatments page I used the search bar to search treatments by name and description to check correct results was returned. Using the search bar I put in a treatment that did not exist, the correct result showed.
  - [Search by name]() > [Search by description]() > [Searh a treatment that does not exist]()
#### filter my search results
- **Testing:** Searched for a treatment then using the 'sort by..' dropdown tested options.
  - [Use sort by dropdown]()
#### read details about the treatments
- **Testing:** On the treatments page I clicked a treatment to test the treatment details page opened.
  - [Treatments page]() > [Treatment details page]()
#### add treatments into my cart
- **Testing:** On the treatment details page I selected a quantity and clicked 'add to cart' button, checked the total was displayed at the top right of the navbar, checked toast showed when adding the treatment. Clicked 'go to cart' button to make sure the treatment was located inside of the cart page.
  - [Clicked add to cart button]() > [Cart total showing correctly]() > [Cart success toast shows]() > [Cart page showing treatment in cart]()
#### understand why I should sign up
- The aim of the site is for all users to be able to make purchases but there are two reasons for a user to sign up. 1) To save billing information for next time checkout. 2) To add a rating on a treatment that is purchased.
- **Testing:** On the checkout page I checked non-logged in users could not save there information and that logged in users could. On the treatment details page I checked that non-logged in users could not add a rating and a message was shown, that logged in users who have purchased the treatment could.
  - [Non-logged in user on checkout]() > [Logged in users in the checkout]() > [Logged in users saved info in the profile]() > [non-logged in user not able to add rating]() > [Logged in user who purchased the treatment can add a rating]()
#### gain access to the companys social media
- **Testing:** Using the social media icons in the footer, I clicked all social media links checking they opened in a new page.
  - [Social media icons in the footer]() > [Social media site open in new page]()
#### register for a user profile account by choosing a username and password
- **Testing:** Using the sign up page I filled information wrong by including spaces to check validation worked correctly, I then put information of another user in to check the validation worked there, worked successfully. I then put new user details in the check a user was successfully created.
  - [Wrong information]() > [Already signed up user]() > [New user]()
#### able to view blog/updates for the company
- **Testing:** On the blog page I checked all users had access then clicked a blog to make sure the blog details page opened correctly.
  - [blog page]() > [blog details page]()

### Registered User
#### log in and log out of my account
- **Testing:** First I put wrong information in checking form validation worked. Then using previous sign up details I went to the login page and put details in checked I was logged in correctly.
  - [Wrong information]() > [Correct details]()
#### update my billing information
- **Testing:** First I went to the checkout page and filled in billing information making sure the save information checkbox was selected then made the purchase. From there I went to my profile and checked my details were showing successfully, then I made changes to the information in the profile clicked 'Update Information', I went back to the checkout to check information was changed successfully.
  - [Checkout page adding information]() > [Profile page checking information is there]() > [Changed information and clicked update button]() > [Checkout page showing updated information]()
#### store my order history and check previous order recipts
- **Testing:** Made a purchase then went to my profile, checked the order number was matching the purchase and that the recipt showed when clicked.
  - [Make a purchase get order number]() > [Profile check order is in there correctly]() > [Clicked order check recipt shows]()
#### Add ratings to orders I purchased
- **Testing:** Made a puchase, then went back to the same treatment details to make sure 'add rating' button showed. Then I clicked the button to make sure the rating form opens, I chose a rating and clicked add rating, making sure the rating was added.
  - [Made a purchase]() > [Add Rating button showing]() > [Add rating form opens]() > [Check rating was added successfully]()

### Site admin/superuser
#### add new treatments to the site
- **Testing:** I clicked treatment management link to check it opened the add treatment form. I filled in the form with the correct details and added it, I then checked it was added to the site.
  - [Treatment management link]() > [Add Treatment form]() > [Fill treatment form and add to site]() > [Check treatment was added to site]()
#### edit treatment
- **Testing:** Going to an added treatment I clicked the edit button and made sure the edit treatment form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
  - [Edit button]() > [Edit form]() > [Make changes and click update]() > [Check changes were applied]()
#### delete treatments
- **Testing:** Click on a treatment and check the delete button is displayed, I then clicked the delete button making sure the are you sure delete modal opened. Once opened I clicked delete, then checked the treatment was gone.
  - [Delete button]() > [Delete modal]() > [Delete treatment check it has gone]()
#### add blogs to the site
- **Testing:** I clicked blog management link to check it opened the add blog form. I filled in the form with the correct details and added it, I then checked it was added to the site.
  - [Blog management link]() > [Add Blog form]() > [Fill blog form and add to site]() > [Check blog was added to site]()
#### edit blogs
- **Testing:** Going to an added blog I clicked the edit button and made sure the edit blog form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
  - [Edit button]() > [Edit form]() > [Make changes and click update]() > [Check changes were applied]()
#### delete blogs
- **Testing:** Click on a blog and check the delete button is displayed, I then clicked the delete button making sure the are you sure delete modal opened. Once opened I clicked delete, then checked the blog was gone.
  - [Delete button]() > [Delete modal]() > [Delete blog check it has gone]()

## Code Validation
#### HTML
#### CSS
#### JavaScript
#### Python
- Autopepe8 installed as a dependency for checking code as written, all python ran through.
###### [ExtendsClass](https://extendsclass.com/python-tester.html) Python Syntax Checker used to check all python files syntax
- **Blog App Syntax Check**
  - admin.py [Passed Validation Image](testing-images/blog-admin-validation.png)
  - apps.py [Passed Validation Image](testing-images/blog-apps-validation.png)
  - forms.py [Passed Validation Image](testing-images/blog-forms-validation.png)
  - models.py [Passed Validation Image](testing-images/blog-models-validation.png)
  - tests.py [Passed Validation Image](testing-images/blog-tests-validation.png)
  - urls.py [Passed Validation Image](testing-images/blog-urls-validation.png)
  - views.py [One Error](testing-images/blog-urls-error-validation.png)
- **Cart App Syntax Check**
  - apps.py [Passed Validation Image](testing-images/cart-apps-validation.png)
  - contexts.py [Passed Validation Image](testing-images/cart-contexts-validation.png)
  - urls.py [Passed Validation Image](testing-images/cart-urls-validation.png)
  - views.py [One Error](testing-images/cart-views-error-validation.png)
- **Checkout App Syntax Check**
  - admin.py [Passed Validation Image](testing-images/checkout-admin-validation.png)
  - apps.py [Passed Validation Image](testing-images/checkout-apps-validation.png)
  - forms.py [One Error](testing-images/checkout-forms-error-validation.png)
  - models.py [One Error](testing-images/checkout-models-error-validation.png)
  - signals.py [Passed Validation Image](testing-images/checkout-signals-validation.png)
  - urls.py [Passed Validation Image](testing-images/checkout-urls-validation.png)
  - views.py [Passed Validation Image](testing-images/checkout-views-validation.png)
  - webhook_handler.py [One Error](testing-images/checkout-webhookh-error-validation.png)
  - webhooks.py [Passed Validation Image](testing-images/checkout-webhooks-validation.png)
- **Home App Syntax Check**
  - apps.py [Passed Validation Image](testing-images/home-apps-validation.png)
  - urls.py [Passed Validation Image](testing-images/home-urls-validation.png)
  - views.py [Passed Validation Image](testing-images/home-views-validation.png)
- **Profiles App Syntax Check**
  - apps.py [Passed Validation Image](testing-images/profiles-apps-validation.png)
  - forms.py [One Error]() []()
  - models.py [Passed Validation Image](testing-images/profiles-apps-validation.png)
  - urls.py [Passed Validation Image](testing-images/profiles-urls-validation.png)
  - views.py [One Error](testing-images/profiles-views-error-validation.png)
- **Purity App Syntax Check**
  - settings.py [One Error]() []()
  - urls.py [Passed Validation Image](testing-images/purity-urls-validation.png)
- **Treatments App Syntax Check**
  - admin.py [Passed Validation Image](testing-images/treatments-admin-validation.png)
  - apps.py [Passed Validation Image](testing-images/treatments-apps-validation.png)
  - forms.py [Passed Validation Image](testing-images/treatments-forms-validation.png)
  - models.py [Passed Validation Image](testing-images/treatments-models-validation.png)
  - urls.py [Passed Validation Image](testing-images/treatments-urls-validation.png)
  - views.py [One Error](testing-images/treatments-views-error-validation.png)
  - widgets.py [Passed Validation Image](testing-images/treatments-widgets-validation.png)
- **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**

## Stripe Tests
* Using stripe dashboard in the webhooks section I checked my site returned webhooks correctly. **Worked**

## Responsive Tests
- DevTools - Devices tested across a range of widths:
  - Mobiles: iphone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:
  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px) | Very Large Desktop screen (1440px)

- Viewed site on above range (including Responsive mode) on various browsers: >   - Google Chrome
  - Firefox
  - Opera
  - Safari

## Known Bugs & Issues

## Deployment
* Ensured deployed page on Heroku loads up correctly.
* Ensured Debug variable in app.py file is set to False.
* Confirmed that there is no difference between the deployed version and the development version.
