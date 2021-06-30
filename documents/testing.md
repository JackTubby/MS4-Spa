# Testing 

## User Story Testing
### Anonymous user
#### View the site on all screen sizes
* Site tested on all screen sizes as described in the responsive testing section.
#### understand what the site is about from landing page
- **Testing:** Used the [deployed site url](https://purity-mxhaib.herokuapp.com/) and clicked enter, The page opened showing the landing page instantly showing a welcome to message.
  - [Home page showing welcome message](testing-images/home-page-1.png)
#### easily navigate around the site
- The site contains mutlitple ways to navigate, for example the navbar is fixed so no matter how far down a page the menu dropdown is available. The footer also container links around the site and multiple pages throughout the site has back buttons implemented. The home page also has a button strait away with easy navigation to the treatments page. 
- **Testing:** From the landing page I used the dropdown menu and tested all links, using the footer I clicked all link, all links were correct. From the home page I clicked 'take a look button' this correctly opened the treatments page. Throughout the site I tested back buttons for example the treatment details and blog details page.
  - [Menu dropdown links](testing-images/menu-dropdown-2.png) > [Footer links](testing-images/footer-links-2.png) > ['take a look' button test](testing-images/take-a-2.png) > [Treatment details back button](testing-images/treatment-details-2.png) > [Blog details back button](testing-images/blog-details-2.png)
#### search for treatments
- **Testing:** On the treatments page I used the search bar to search treatments by name and description to check correct results was returned. Using the search bar I put in a treatment that did not exist, the correct result showed.
  - [Search by name](testing-images/search-by-3.png) > [Search by description](testing-images/search-description-3.png) > [Searh a treatment that does not exist](testing-images/search-a-3.png)
#### filter my search results
- **Testing:** Searched for a treatment then using the 'sort by..' dropdown tested options.
  - [Use sort by dropdown](testing-images/use-sort-4.png)
#### read details about the treatments
- **Testing:** On the treatments page I clicked a treatment to test the treatment details page opened.
  - [Treatments page](testing-images/treatments-page-5.png) > [Treatment details page](treatment-details-5.png)
#### add treatments into my cart
- **Testing:** On the treatment details page I selected a quantity and clicked 'add to cart' button, checked the total was displayed at the top right of the navbar, checked toast showed when adding the treatment. Clicked 'go to cart' button to make sure the treatment was located inside of the cart page.
  - [Clicked add to cart button](testing-images/clicked-add-6.png) > [Cart total showing correctly](testing-images/cart-total-6.png) > [Cart success toast shows](testing-images/cart-success-6.png) > [Cart page showing treatment in cart](testing-images/cart-page-6.png)
#### understand why I should sign up
- The aim of the site is for all users to be able to make purchases but there are two reasons for a user to sign up. 1) To save billing information for next time checkout. 2) To add a rating on a treatment that is purchased.
- **Testing:** On the checkout page I checked non-logged in users could not save there information and that logged in users could. On the treatment details page I checked that non-logged in users could not add a rating and a message was shown, that logged in users who have purchased the treatment could.
  - [Non-logged in user on checkout](testing-images/non-logged-7.png) > [Logged in users in the checkout](testing-images/logged-in-checkout-7.png) > [Logged in users saved info in the profile](testing-images/logged-in-profile-7.png) > [non-logged in user not able to add rating](testing-images/non-logged-rating-7.png) > [Logged in user who purchased the treatment can add a rating](testing-images/logged-in-rating-7.png)
#### gain access to the companys social media
- **Testing:** Using the social media icons in the footer, I clicked all social media links checking they opened in a new page.
  - [Social media icons in the footer](testing-images/social-media-8.png) > [Social media site open in new page](testing-images/social-media-page-8.png)
#### register for a user profile account by choosing a username and password
- **Testing:** Using the sign up page I filled information wrong by including spaces to check validation worked correctly, I then put information of another user in to check the validation worked there, worked successfully. I then put new user details in the check a user was successfully created.
  - [Wrong information](testing-images/wrong-info-9.png) > [Already signed up user](testing-images/already-signed-9.png) > [New user](testing-images/new-user-9.png)
#### able to view blog/updates for the company
- **Testing:** On the blog page I checked all users had access then clicked a blog to make sure the blog details page opened correctly.
  - [blog page](testing-images/blog-page-10.png) > [blog details page](testing-images/blog-details-10.png)

### Registered User
#### log in and log out of my account
- **Testing:** First I put wrong information in checking form validation worked. Then using previous sign up details I went to the login page and put details in checked I was logged in correctly.
  - [Wrong information](testing-images/wrong-info-sign-11.png) > [Correct details](testing-images/correct-details-sign-11.png)
#### update my billing information
- **Testing:** First I went to the checkout page and filled in billing information making sure the save information checkbox was selected then made the purchase. From there I went to my profile and checked my details were showing successfully, then I made changes to the information in the profile clicked 'Update Information', I went back to the checkout to check information was changed successfully.
  - [Checkout page adding information](testing-images/checkout-page-adding-12.png) > [Profile page checking information is there](testing-images/checkout-page-checking-12.png) > [Changed information and clicked update button](testing-images/changed-information-checkout-12.png) > [Checkout page showing updated information](testing-images/checkout-page-updated-12.png)
#### store my order history and check previous order recipts
- **Testing:** Made a purchase then went to my profile, checked the order number was matching the purchase and that the recipt showed when clicked.
  - [Profile check order is in there correctly](testing-images/check-ordernumber-13.png) > [Clicked order check recipt shows](testing-images/check-ordernumber-receipt-13.png)
#### Add ratings to orders I purchased
- **Testing:** Made a puchase, then went back to the same treatment details to make sure 'add rating' button showed. Then I clicked the button to make sure the rating form opens, I chose a rating and clicked add rating, making sure the rating was added.
  - [Add Rating button showing](testing-images/check-add-rating-14.png) > [Add rating form opens](testing-images/add-rating-form-14.png) > [Check rating was added successfully](testing-images/rating-add-successfully-14.png)

### Site admin/superuser
#### add new treatments to the site
- **Testing:** I clicked treatment management link to check it opened the add treatment form. I filled in the form with the correct details and added it, I then checked it was added to the site.
  - [Add Treatment form](testing-images/treatment-management-form-15.png) > [Fill treatment form and add to site](testing-images/fill-treatment-15.png) > [Check treatment was added to site](testing-images/treatment-added-15.png)
#### edit treatment
- **Testing:** Going to an added treatment I clicked the edit button and made sure the edit treatment form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
  - [Edit form](testing-images/treatment-edit-16.png) > [Make changes and click update](testing-images/treatment-edit-change-16.png) > [Check changes were applied](testing-images/treatment-edit-applied-16.png)
#### delete treatments
- **Testing:** Click on a treatment and check the delete button is displayed, I then clicked the delete button making sure the are you sure delete modal opened. Once opened I clicked delete, then checked the treatment was gone.
  - [Delete button](testing-images/delete-btn-17.png) > [Delete modal](testing-images/delete-modal-17.png) > [Delete treatment check it has gone](testing-images/treatment-deleted-17.png)
#### add blogs to the site
- **Testing:** I clicked blog management link to check it opened the add blog form. I filled in the form with the correct details and added it, I then checked it was added to the site.
  - [Add Blog form](testing-images/add-blog-form-18.png) > [Fill blog form and add to site](testing-images/blog-filled-18.png) > [Check blog was added to site](testing-images/add-blog-18.png)
#### edit blogs
- **Testing:** Going to an added blog I clicked the edit button and made sure the edit blog form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
  - [Edit form](testing-images/edit-blog-form-19.png) > [Check changes were applied](testing-images/edit-blog-addded-19.png)
#### delete blogs
- **Testing:** Click on a blog and check the delete button is displayed, I then clicked the delete button making sure the are you sure delete modal opened. Once opened I clicked delete, then checked the blog was gone.
  - [Delete button](testing-images/blog-delete-20.png) > [Delete modal](testing-images/blog-delete-modal-20.png) > [Delete blog check it has gone](testing-images/blog-removed-20.png)

## Code Validation
#### HTML
###### [HTML Validator](https://validator.w3.org/) used to check HTML. 
- 9 errors
- 4 warnings
#### CSS
###### [CSS Validator](https://jigsaw.w3.org/css-validator/) used to check CSS. 
- 3 errors > base.css error fixed > two other errors are bootstrap errors so can be ignored.
- All warnings mostly come from Django & Bootstrap so can be ignored.
- [CSS Validation Image](image-validation/css-validation.png)
#### JavaScript
###### [JSHint](https://jshint.com/) used to check JavaScript syntax.
- Cart.html script | Issues - [3 Warnings](image-validation/cart-js.png) > All fixed apart from 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- Stripe_elements.js | Issues - [3 Warnings](image-validation/stripe-elements-js.png) > All fixed apart from 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- Countryfield.js | Issues - [2 Warnings](image-validation/countryfield-js.png) > All fixed apart from 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- Treatments.html | Issues - [1 Warning](image-validation/treatments-js.png) > All fixed.
- quantity_input_script.html | Issues - [3 Warnings](image-validation/quantity-input-script-js.png) > No fixes required for 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- edit_treatment.html | Issues - [1 Warning](image-validation/edit-treatment-js.png) > No fixes required for 'template literal syntax' is only available in ES6 (use 'esversion: 6').
- add_treatments.html | Issues - [1 Warning](image-validation/add-treatments-js.png) > No fixes required for 'template literal syntax' is only available in ES6 (use 'esversion: 6').

#### Python
- Autopepe8 installed as a dependency for checking code as written, all python ran through.
###### [ExtendsClass](https://extendsclass.com/python-tester.html) Python Syntax Checker used to check all python files syntax
- **Blog App Syntax Check**
  - admin.py [Passed Validation Image](image-validation/blog-admin-validation.png)
  - apps.py [Passed Validation Image](image-validation/blog-apps-validation.png)
  - forms.py [Passed Validation Image](image-validation/blog-forms-validation.png)
  - models.py [Passed Validation Image](image-validation/blog-models-validation.png)
  - tests.py [Passed Validation Image](image-validation/blog-tests-validation.png)
  - urls.py [Passed Validation Image](image-validation/blog-urls-validation.png)
  - views.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
- **Cart App Syntax Check**
  - apps.py [Passed Validation Image](image-validation/cart-apps-validation.png)
  - contexts.py [Passed Validation Image](image-validation/cart-contexts-validation.png)
  - urls.py [Passed Validation Image](image-validation/cart-urls-validation.png)
  - views.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
- **Checkout App Syntax Check**
  - admin.py [Passed Validation Image](image-validation/checkout-admin-validation.png)
  - apps.py [Passed Validation Image](image-validation/checkout-apps-validation.png)
  - forms.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - models.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - signals.py [Passed Validation Image](image-validation/checkout-signals-validation.png)
  - urls.py [Passed Validation Image](image-validation/checkout-urls-validation.png)
  - views.py [Passed Validation Image](image-validation/checkout-views-validation.png)
  - webhook_handler.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - webhooks.py [Passed Validation Image](image-validation/checkout-webhooks-validation.png)
- **Home App Syntax Check**
  - apps.py [Passed Validation Image](image-validation/home-apps-validation.png)
  - urls.py [Passed Validation Image](image-validation/home-urls-validation.png)
  - views.py [Passed Validation Image](image-validation/home-views-validation.png)
- **Profiles App Syntax Check**
  - apps.py [Passed Validation Image](image-validation/profiles-apps-validation.png)
  - forms.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - models.py [Passed Validation Image](image-validation/profiles-apps-validation.png)
  - urls.py [Passed Validation Image](image-validation/profiles-urls-validation.png)
  - views.py [One Error](image-validation/profiles-views-error-validation.png)
- **Purity App Syntax Check**
  - settings.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - urls.py [Passed Validation Image](image-validation/purity-urls-validation.png)
- **Treatments App Syntax Check**
  - admin.py [Passed Validation Image](image-validation/treatments-admin-validation.png)
  - apps.py [Passed Validation Image](image-validation/treatments-apps-validation.png)
  - forms.py [Passed Validation Image](image-validation/treatments-forms-validation.png)
  - models.py [Passed Validation Image](image-validation/treatments-models-validation.png)
  - urls.py [Passed Validation Image](image-validation/treatments-urls-validation.png)
  - views.py **One Error** f strings **Errors found are all due to f strings after further investigations it is a issue with ExtendsClass**
  - widgets.py [Passed Validation Image](image-validation/treatments-widgets-validation.png)
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
* Users are getting emails when they sign up and change password, but not when making an order. Due to time limitations I could not fix this but have added a message saying 'We have recieved your order a memeber of staff will be in contact with you to confirm your booking and give you your recipt'. Meaning it will be manual for now but would like to add this feature next.
* The cart success message when updating the quantity has to close buttons, this is a minor issue and causes no real problems. Did not have time to fix.

## Deployment
* Ensured deployed page on Heroku loads up correctly.
* Ensured Debug variable in app.py file is set to False.
* Confirmed that there is no difference between the deployed version and the development version.
