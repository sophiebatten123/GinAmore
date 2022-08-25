[GinAmore Live Link](https://ginamore.herokuapp.com/)
[Github Repository](https://github.com/sophiebatten123/GinAmore)

# GinAmore

(Developer: Sophie Batten)

![Am I Responsive?](static/images/am_i_responsive.PNG)

GinAmore is an ecommerce website built using Django, Python, HTML, CSS and Javascript as part of the Code Institute Diploma in Full Stack Software Development.

## Aim
GinAmore aims to provide users with the ability to easily purchase premium flavoured gin. It does this by providing clear and consice site navigation and checkout functionality throughout the site. GinAmore encourages users to make informed purchases allowing them to favourite items and revist them later inside their personalised wishlist. Users are given cocktail ideas that compliment with the sites products, enncouraging them to make purchases and revisit the site more regularly. Moreover, GinAmore prides itself on transpency allowing users to write reviews on products, increasing trust between the company and its clients.

# Table of Contents:

- [UX](#)
  - [User Stories](#)
  - [Agile Planning Enviroment](agile-planning-enviroment)
  - [Design](#)
    - [GinAmore Design Principles](#)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Wireframes](wireframes)
    - [Desktop Wireframes](desktop-wireframes)
    - [Mobile Wireframes](mobile-wireframes)
  - [Features](#)
  - [Future Features](#)
  - [Functionality](#)
    - [Fixed Bugs and Errors](#)
    - [Technologies Used](#)
    - [Programs Used](#)
  - [Data Schema](#)
    - [Logic Flowchart](#)
    - [Entity Relationship Diagram](#)
- [Testing](#)
    - [Manual Testing](#)
    - [Automated Testing](#)
- [Future Features](#)
- [Deployment](#)
- [Credits](#)

## User Stories

### EPIC: Viewing and Navigation (Products)

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|1| Shopper | View a list of all Gin products | Select which ones I want to purchase | 8 | Mo |
|2| Shopper | View individual Gin details | Identify the price, description and product rating of each product | 5 | Mo |
|3| Shopper | Identify any deals and special offers quickly on the page | Take advantage of special offers | 1 | Mo |

### EPIC: Registration and Verification

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|4| Site User | Easily register for an account | View my personal profile information | 3 | Mo |
|5| Site User | Easily login/logout of my account | Access my personal account | 3 | Mo |
|6| Site User | Easily recover my password if I forget it | Recover access to my account | 2 | Mo |
|7| Site User | Receive an email to verify I have created an account | Verify my account is set up. | 2 | S |
|8| Site User | Register/login to an account via social media | Login to my account quicker | 5 | Co |
|9| Site User | Confirm I am of legal age to drink | Use the site effectively and purchase items | 3 | Mo |


### EPIC: Sorting and Searching

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|10| Shopper | Sort through all Gin products | Easily see the best rated, best priced items | 3 | Mo |
|11| Shopper | Sort based on the Gin category | Sort Gin items based on the type of Gin I prefer | 3 | Mo |
|12| Shopper | Search a product by name and description | Find a specific Gin I would like to purchase | 3 | Mo |
|13| Shopper |  See search results quickly and easily  | Quickly decide which product I would like to purchase | 2 | Mo |

### EPIC: Purchasing and Checkout

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|14| Shopper | View items in my bag to be purchased | Check total cost and the items that I will be purchasing | 2 | Mo |
|15| Shopper | Receive an email to verify my order | Feel more secure that my payment has gone through | 3 | S |
|16| Shopper | View an order confirmation when my order is complete | Check my order is correct without mistakes | 2 | S |
|17| Shopper | Securely provide payment details | Confidently provide payment details to purchase an item | 5 | Mo |
|18| Shopper | Enter payment information quickly  | Check out quickly without hassle | 3 | Mo |
|19| Shopper | Adjust the quantity of items in my bag | Easily adjust the quantity for my own preference | 2 | Mo |
|20| Shopper | Select the quantity of product to add to shopping bag | I am able to get the amount of Gin I require | 3 | Mo |
|21| Shopper | Quickly see the total cost of all my products | Avoid spending too much | 2 | Mo |

### EPIC: Admin and Store Management

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|22| Store Owner | Easily Add Cocktail Recipes | Keep recipes interesting and new to users | 5 | Co |
|23| Store Owner | Edit/Update Cocktail Recipes | Ensure the cocktail information is up to date | 3 | Co |
|24| Store Owner | Add a Product | Add new products to my store | 3 | Mo |
|25| Store Owner | Edit/Update a Product | Change details of a product including description and price | 3 | Mo |
|26| Store Owner | Delete a Product | Remove any discontinued products | 1 | Mo |

### EPIC: Product and Cocktail Reviews

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|27| Shopper | Rate and Review Cocktail Recipes | Communicate with others on the site | 5 | Co |
|28| Store Owner | Delete a Review |  Filter the content shown to customer | 1 | S |
|29| Shopper | Leave a Product Review | Advise other shoppers on their purchases | 3 | S |
|30| Shopper | Submit cocktail recipe ideas | Contribute to the site and feel in contact with other cocktail makers | 5 | W |

### EPIC: Wishlist Functionality

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|31| Shopper | Add items to my wish list | Easily find items later on to purchase them quickly | 3 | S |
|32| Shopper | Remove items from my wish list | Keep my wish list basket up to date with things I love | 1 | S |

### EPIC: Viewing and Navigation (Cocktails)

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|33| Shopper | View individual cocktail recipes | Learn how to make individual cocktails | 5 | S |
|34| Shopper | View cocktail recipes based on their category | Choose which recipe I would like to make | 2 | Co |

# Agile Planning Enviroment

The story point allocation above is based upon a 100 point iteration and uses the Fibonacci Sequence. Using the MoSCoW method each user story was then been labeled as being either 'Must Have', 'Should Have', 'Could Have' or 'Wont Have', based upon its importance to the project whilst following the 60:20:20 MoSCoW format. Note that the 'Wont Have' User Story below was excluded from the 60:20:20 MoSCoW allocation.

![Acceptance Criteria](static/images/agile-screenshot.PNG)

## Acceptance Criteria

Each of the user stories was given acceptance criteria, an example of this can be seen below:
 
![Acceptance Criteria](static/images/acceptance-criteria.PNG)

This helped to ensure all tasks were completed before the user story was marked as done and ensured the website was fully functional. I also used the acceptance criteria to guide the manual testing that was performed throughout the project.

# Features

## Existing Features

## Future Features

# Site Map Wireframe

The following site map was created to help understand the flow of the website prior to development. This helped in understanding the links between pages and ensured pages were easily accessed by users.

![Site Map Wireframe](static/images/site_map.PNG)

# Database Schema

Entity Relationship Databases (ERD) were created to help develop this project. These were seperated into seperate database schemas: 'Gin Products' and 'Cocktail Products' due to them not being related to each other directly.

***

![Entity Relationship Database: Products](static/images/erd_products.PNG)

***

![Entity Relationship Database: Cocktails](static/images/erd_cocktails.PNG)

# Marketing

# Search Engine Optimization

The site was optimized by careful selection of keywords. The following steps were taken to do this:

1. The entire table consists of important relevant topics based upon my initial understanding of the buissness.
2. Using these topics a 'brain dump' of keywords was made orientated around common topics and themes within the buissness.
3. Topics and keywords were then tried out on Google and the relevant suggestions it gave were added to the keyword list.
2. Words crossed out in red were removed due to too having too much competition using [Wordtracker](https://www.wordtracker.com/?fpr=refer&fp_sid=bingof).
3. Words crossed out in blue were removed due to the lack of relevance and not being specific to the site.

Words in Yellow denote the sites **"Short Tail Keywords"**

Words in Green denote the sites **Long Tailed Keywords"**

![Site Optimization Keyword Selection](static/images/site_optimization.PNG)

## SEO Implementations in HTML
  - Words/phrases included within semantic HTML elements were optimized using the keywords above.
  - Careful consideration was given to the words chosen to avoid 'keyword stuffing'.
  - Keywords were used within links, urls and aria labels.
  - Social network links include **rel="noopener"** to not affect the assessment of the webpage.
  - Image description alt tags contain the keywords chosen above.
  - External reliable links were included within the site to improve SEO, these include:
    - Charities that the company supports.
    - Reccomended mixer brands.
    - Useful tips/advice on drinking sensibly.
  - Within the META data (screenshot)

***
## sitemap.xml
***

A sitemap was made to list the websites important URL's to ensure that search engines are able to easily navigate through the site and understand its structure. This was made using [XML-sitemaps.com](https://www.xml-sitemaps.com/) using the following steps:

1. Paste the URL of the deployed site into XML-sitemaps.
2. Download the XML sitemap file.
3. Drag and drop this files into the projects root folder, and ensure it is labeled **sitemap.xml**

***
## robots.txt
***

A robots.txt file was created to tell search engines where not to allowed go on the site and increase the quality of the site, ultimetly improving the SEO rating. The following steps were taken to creat this:

1. A file was added named **robots.txt**.
2. The following code was written into this file, adding in your personalised sitemap url:

```
  User-agent: *
  Disallow:
  Sitemap: YOUR_SITEMAP_URL
```

The final steps for working with these two files requires a DNS certificate for a deployed custom domain. This project did not require a custom domain and so has been temporarily left out.

***
## Improving Google Metrics

| Expertise | Authoritiveness | Trustworthiness |
|-----------|-----------------|-----------------|
| Creating engaging content to meet the users needs. | Including clear steps and examples within the recipe section of the site. | Content is proffesional and avoids typos and spelling mistakes. |
| Included an FAQS page for users. |  | Links to privacy statements and terms and conditions is provided at the bottom. |
| High quality images were included within the site. |  | Reviews are included on all products and cocktails. |

Google metrics were considered when developing the site, including: 

- Click Through Rate (CTR)
  - The title and Meta data of the website were optimized with both short and long tailed keywords.
- Bounce Rate
  - The homepage of the site has been made engaging for the user.
- Dwell Time
  - Content on the homepage is interesting and engaging to users.
- Session Time
  - It is made easy for users to discover more content through 'reccomneded items" sections on the page.
- Pages Per Session
  - Links were regularly included throughout the webiste to encourage users to navigate through the website more and engage with more of the content.

# Business Model

The business model used for the GinAmore store would be a B2C (Business to Customer), this is due to the business selling products directly to the customer through the platform.

# Colour Scheme

The colours within the site were carefully selected to mirror the premium products sold at GinAmore. The dark regal blue contrasts against the light pink making elements of importance stand out on the page. These colours were initially selected from the sites main banner image using DEV tools, allowing for all colours within the page to compliment eachother nicely.

![Colour-Scheme](static/images/color-scheme.PNG)

# Wireframes

Although the wireframes for site users and site admin are similar there are a few subtle differences between some pages to help admin modify, add and delete products and cocktails. Extra wireframes were created to account for these differences below:

## Desktop Wireframes

***
### Site Users
***

[Homepage](static/images/homepage_desktop.PNG)

[Our Story](static/images/aboutus_desktop.PNG)

[Contact Us](static/images/contact_desktop.PNG)

[Gin Page](static/images/gin_desktop.PNG)

[Gin Detail Page](static/images/gin_detail_desktop.PNG)

[Cocktail Page](static/images/cocktail_desktop.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_desktop.PNG)

[Wishlist](static/images/wishlist_desktop.PNG)

[Shopping Bag](static/images/bag_desktop.PNG)

[Checkout Page](static/images/checkout_desktop.PNG)

[Checkout Success Page](static/images/checkout_success_desktop.PNG)

***
### Site Admin
***

[Gin Page](static/images/gin_admin_desktop.PNG)

[Gin Detail Page](static/images/gin_detail_admin_desktop.PNG)

[Cocktail Page](static/images/cocktails_admin_desktop.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_admin_desktop.PNG)

[Add Product Page](static/images/add_product_desktop.PNG)

[Edit Product Page](static/images/edit_product_desktop.PNG)

## Mobile Wireframes

***
### Site Users
***

[Homepage](static/images/home_mobile.PNG)

[Our Story](static/images/about_us_mobile.PNG)

[Contact Us](static/images/contact_us_mobile.PNG)

[Gin Page](static/images/gin_mobile.PNG)

[Gin Detail Page](static/images/gin_detail_mobile.PNG)

[Cocktail Page](static/images/cocktails_mobile.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_mobile.PNG)

[Wishlist](static/images/wishlist_mobile.PNG)

[Shopping Bag](static/images/bag_mobile.PNG)

[Checkout Page](static/images/checkout_mobile.PNG)

[Checkout Success Page](static/images/checkout_success_mobile.PNG)

***
### Site Admin
***

[Gin Page](static/images/gin_admin_mobile.PNG)

[Gin Detail Page](static/images/gin_detail_admin_mobile.PNG)

[Cocktail Page](static/images/cocktails_admin_mobile.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_admin_mobile.PNG)

[Add Product Page](static/images/add_product_mobile.PNG)

[Edit Product Page](static/images/edit_product_mobile.PNG)

# Technologies Used

***
### Coding Languages
***

* [HTML]()
  * HTML is the main language used accross the site and completes the structure of the webpages.

* [CSS]()
  * CSS is used throughout to create custom styling to elements accross the site.

* [Javascript]()
  * Javascript is used within the checkout template to help with form submission and to verify the users age.
  * [JQuery]() is used within the following webpages:
    * To update item quantity within the bag template and to update the form.
    * To display success and fail messages within form submission.

* [Python]()
  * Python was used extensively on the site to handle back-end functionality.

***
### Frameworks and Platforms
***

* [Django]()
  * The project was created using Django as a framework to help handle back-end functionality. 

* [Github]()
  * Github was the hosting site for the project code.

* [Gitpod]()
  * Gitpod has been used to commit and push code within the GitHub repository.

* [Bootstrap]()
  * Bootstrap was used within the site to help format the layout of elements and improve the responsiveness of the site.

* [Google Fonts]()
  * Google Fonts was used to select the typography type for the website and imported within CSS.

* [AWS S3 Buckets]()
  * AWS S3 Buckets provide storage for static and media files within the deployed Heroku site.

* [Heroku]()
  * Heroku was used as a platform to deploy the site.

* [Google Chrome Developer Tools]()
  * Google Chrome's Developer Tools were used to help debug errors within the code and to help style the site through the colour selector.

* [Uizard Wireframe Generator]()
  * Wireframes were created and generated through Uizard.

* [Font Awesome]()
  * Icons used accross the site were imported from Font Awesome.

* [Am I Responsive]()
  * The site Mock Up image was generated using Am I Responsive.

[Back to top ⇧](#ginamore)

# Testing

## Manual and Automated Testing

### HTML & CSS: W3C Validation

HTML and CSS was checked using an online W3C Validator to ensure there were no errors within the code. 
When the site was ran through the validators there were no errors at the point of deployment.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- [WSC HTML Validator](https://validator.w3.org/)

### Javascript: JShint

JavaScript code was tested regularly both manually and automatically through [JShint](https://jshint.com/) and the [DevTools](https://developer.chrome.com/docs/devtools/). DevTools allowed me to test responses using the console log function and jShint enabled me to ensure that my code was hitting the style guidelines. Upon the launch of my project jShint showed no errors or warnings with my code.

### Wave Testing: Accessibility

- Improved alt labels on images
- Added labels to input buttons
- Headers run in order

### Lighthouse Reports

A lighthouse report was generated on each page of the site and the following steps were taken to improve sections based on the feedback it provided:
- Performance 
  - Images were convered from jpg files into webp files using:
  - Images were reduced in size using:
  - Unnecessary script tags were removed from the sites base.html file.
- Accessibility
  - White font colour within the pink banners were changed to blue.
  - Missing labels were added to input form elements.
  - Missing alt tags were added to images.
  - Headers within the site were ordered based upon hierachy.
- SEO
  - Buttons were increased in size.
- Best Practices

### Automated Testing Reports

Attached below is a screenshot of the HTML & CSS Validator and Lighthouse Reports for each page of the site:

<details>
    <summary>Home Page: Automated Testing Report</summary>
    <img src="static/images/home_html.PNG" width="500">
    <img src="static/images/css_home.PNG" width="500">
    <img src="static/images/lighthouse_home.PNG" width="500">
</details>

<details>
    <summary>Products: Automated Testing Report</summary>
    <img src="static/images/products_html.PNG" width="500">
    <img src="static/images/css_products.PNG" width="500">
    <img src="static/images/lighthouse_products.PNG" width="500">
</details>

<details>
    <summary>Product Detail: Automated Testing Report</summary>
    <img src="static/images/product_detail_html.PNG" width="500">
    <img src="static/images/css_product_detail.PNG" width="500">
    <img src="static/images/lighthouse_product_detail.PNG" width="500">
</details>

<details>
    <summary>Add Product: Automated Testing Report</summary>
    <img src="static/images/add_product_html.PNG" width="500">
    <img src="static/images/css_add_product.PNG" width="500">
    <img src="static/images/lighthouse_add_product.PNG" width="500">
</details>

<details>
    <summary>Edit Product: Automated Testing Report</summary>
    <img src="static/images/edit_product_html.PNG" width="500">
    <img src="static/images/css_edit_product.PNG" width="500">
    <img src="static/images/lighthouse_edit_product.PNG" width="500">
</details>

<details>
    <summary>Cocktails: Automated Testing Report</summary>
    <img src="static/images/cocktails_html.PNG" width="500">
    <img src="static/images/css_cocktails.PNG" width="500">
    <img src="static/images/lighthouse_cocktails.PNG" width="500">
</details>

<details>
    <summary>Cocktail Details: Automated Testing Report</summary>
    <img src="static/images/cocktail_detail_html.PNG" width="500">
    <img src="static/images/css_cocktail_detail.PNG" width="500">
    <img src="static/images/lighthouse_cocktail_detail.PNG" width="500">
</details>

<details>
    <summary>Add Cocktail: Automated Testing Report</summary>
    <img src="static/images/add_cocktail_html.PNG" width="500">
    <img src="static/images/css_add_cocktail.PNG" width="500">
    <img src="static/images/lighthouse_add_cocktail.PNG" width="500">
</details>

<details>
    <summary>Edit Cocktail: Automated Testing Report</summary>
    <img src="static/images/edit_cocktail_html.PNG" width="500">
    <img src="static/images/css_edit_cocktail.PNG" width="500">
    <img src="static/images/lighthouse_edit_cocktail.PNG" width="500">
</details>

<details>
    <summary>Our Story: Automated Testing Report</summary>
    <img src="static/images/ourstory_html.PNG" width="500">
    <img src="static/images/css_our_story.PNG" width="500">
    <img src="static/images/lighthouse_ourstory.PNG" width="500">
</details>

<details>
    <summary>Contact Us: Automated Testing Report</summary>
    <img src="static/images/contact_html.PNG" width="500">
    <img src="static/images/css_contact.PNG" width="500">
    <img src="static/images/lighthouse_contact.PNG" width="500">
</details>

<details>
    <summary>Wishlist: Automated Testing Report</summary>
    <img src="static/images/wishlist_html.PNG" width="500">
    <img src="static/images/css_wishlist.PNG" width="500">
    <img src="static/images/lighthouse_wishlist.PNG" width="500">
</details>

<details>
    <summary>Profile: Automated Testing Report</summary>
    <img src="static/images/profile_html.PNG" width="500">
    <img src="static/images/css_profile.PNG" width="500">
    <img src="static/images/lighthouse_profile.PNG" width="500">
</details>

<details>
    <summary>Bag: Automated Testing Report</summary>
    <img src="static/images/bag_html.PNG" width="500">
    <img src="static/images/css_bag.PNG" width="500">
    <img src="static/images/lighthouse_bag.PNG" width="500">
</details>

<details>
    <summary>Checkout: Automated Testing Report</summary>
    <img src="static/images/checkout_html.PNG" width="500">
    <img src="static/images/css_checkout.PNG" width="500">
    <img src="static/images/lighthouse_checkout.PNG" width="500">
</details>

## Python Testing

### Manual Python Testing

Python code was tested to ensure that it met [PEP8](https://pep8.org/) style guidelines. This was done within the terminal console using the command **python3 -m flake8**, which displayed errors and warnings within the code. All errors that were not a result of autogenerated packages installed from Code Institute's Boutique Ado Walkthrough project were removed upon deployment. The autogenerated warnings are:

  - Linting Issue: Importing checkout.signals in the checkout.apps.py file.
  - Linting Issue: handler 404 error in urls.py file.
  - Linting Issue: Line too long in settings.py file.
  - Linting Issue: Webhook and validator errors with e being assigned but never used.
  - Linting Issue: arctictern.py file as part of Code Institues template file.

Furthermore, using the MVC framework I was able to keep track of the changes made and ensure that they had the desired output. After each change made to the Postgres Database I referred directly to it to track the changes, ensuring that upon ‘trial runs’ information was being successfully displayed and filters were displaying alongside.

### Automated Python Testing

# Fixed Bugs and Errors

| Bug/Error Identified | Reason for the Error | Fix for the Error |
|-----------|-----------------|-----------------|
|  |  |  |

# Deployment

## Github
  * Created a new GitHub repository page using the 'Code Institute Template'.
  * Opened the new repository by clicking on the 'Gitpod' button.
  * Installed the relevant apps and packages needed to deploy to HEROKU.

## Django and Heroku

Deployment of my project was scaffolded using the Code Institute's [Django Blog Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf). Furthermore, the following steps were taken to deploy the project to Heroku from the GitHub repository:

1. Create the Heroku App:
    - Before creating the Heroku app make sure your project has the following files:
        - requirements.txt to create this type the following within the terminal: **pip3 freeze --local > requirements.txt**.
        - Procfile to create this type the following within the terminal: **python run.py > Procfile**.
    - Select "Create new app" within Heroku.
2. Attach the Postgres database:
    - Search "Postgres" within the Resources tab and select the Heroku Postgres option.
3. Create the settings.py file:
    - In Heroku navigate to the Settings tab, click on Reveal Config Vars and copy the DATABASE_URL.
    - Within the GitPod workspace, create an env.py file within the main directory.
    - Import the env.py file within the settings.py file.
    - Create a SECRET_KEY value within the Reveal Config Vars in Heroku.
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Run the following command in your terminal **python3 manage.py migrate**.
    - Add the CLOUDINARY_URL to the Reveal Config Vars in Heroku and add this to your settings.py file.
    - Add the following sections to your settings.py file:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILES_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com','localhost']
4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the top level directory: media, storage and templates.
    - Create a file named "Procfile" in the main directory and ass the following: [web: gunicorn project-name.wsgi].
    - Login to Heroku within the terminal window using **heroku login -i**
    - Run the following command in the terminal window: **heroku git:remote -a your_app_name_here**. By doing this you will link the app to your GidPod terminal.
    - After linking the app you can deploy new versions to Heroku by running the command **git push heroku main**.
  
[Back to top ⇧](#ginamore)

***
### Allauth

Within the Django Framework, Allauth a package that handles registration and login details was installed. More information on how this was installed can be found here: [Django Allauth Installation](https://django-allauth.readthedocs.io/en/latest/installation.html).
****

## Forking the Repository

  * Log in to GitHub and locate the required GitHub repository.
  * At the top of the Repository, above the **"Settings"** button, locate the button labeled **"Fork"**.
  * You should now have a copy of the original repository within your GitHub account.
  * You can make changes to this new version whilst keeping the original version safe.

## Cloning the Repository

  * Ensure that you are logged into GitHub and locate the required GitHub repository.
  * Click the dropdown button labelled **'Code'** above the file list.
  * Copy the URL for the required repository.
  * Open Git Bash on your device.
  * Change the current working directory to the location where you want the cloned directory.
  * Type git clone in the CLI and then paste the URL you copied earlier. This is what it should look like: $ git clone https://github.com/sophiebatten123/ginamore
  * Press Enter to create your local clone.

  For more information on how to clone a repository read GitHubs [Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) document.

[Back to top ⇧](#ginamore)

# AWS S3 Bucket Set Up

The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://portal.aws.amazon.com/billing/signup#/start/email).
2. Login to your account and within the search bar type in **S3**.
3. Within the S3 page click on the button that says **Create Bucket**.
4. Name the bucket and select the region which is closest to you.
5. Underneath **Object Ownership** select **ACLs enabled**.
6. Uncheck **Block Public Access** and acknowledge that the bucket will be made public, then click **Create Bucket**.
7. Inside the created bucket click on the **Properties** tab. Below **Static Website Hosting** click **Edit** and change the Static website hosting option to **Enabled**. Copy the default values for the index and error documents and click **Save Changes**.
8. Click on the **Permissions** tab, below **Cross-origin Resource Sharing (CORS)**, click **Edit** and then paste in the following code:

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

9. Within the **Bucket Policy** section. Click **Edit** and then **Policy Generator**. Click the **Select Type of Policy** dropdown and select **S3 Bucket Policy** and within **Principle** allow all principals by typing *.
10. Within the **Actions** dropdown menu select **Get Object** and in the previous tab copy the **Bucket ARN number**. Paste this within the policy generator within the field labeled **Amazon Resource Name (ARN)**.
11. Click **Add statement > Generate Policy** and copy the policy that's been generated and paste this into the **Bucket Policy Editor**.
12. Before saving, add /* at the end of your **Resource Key**, this will allow access to all resources within the bucket.
13. Once saved, scroll down to the **Access Control List (ACL)** and click **Edit**.
14. Next to **Everyone (public access)**, check the **list** checkbox and save your changes.

[Back to top ⇧](#ginamore)

# IAM

1. Search for IAM within the AWS navigation bar and select it.
2. Click **User Groups** that can be seen in the side bar and then click **Create group** and name the group 'manage-your-project-name'.
3. Click **Policies** and then **Create policy**.
4. Navigate to the JSON tab and click **Import Managed Policy**, within here search **S3** and select **AmazonS3FullAccess** followed by **Import**.
5. Navigate back to the recently created S3 bucket and copy your **ARN Number**. Go back to **This Policy** and update the **Resource Key** to include your ARN Number, and another line with your ARN followed by a /*. Below is an example of what this should look like:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```

6. Ensure the policy has been given a name and a short description, then click **Create Policy**.
7. Click **User groups**, and then the group you created earlier. Under permissions click **Add Permission** and from the dropdown click **Attach Policies**.
8. Select **Users** from the sidebar and click **Add User**.
9. Provide a username and check **Programmatic Access**, then click 'Next: Permissions'.
10. Ensure your policy is selected and navigate through until you click **Add User**.
11. Download the **CSV file**, which contains the user's access key and secret access key.

[Back to top ⇧](#ginamore)

# Connecting AWS to Django

1. Within your terminal install the following packages by typing 

```
  pip3 install boto3
  pip3 install django-storages 
```  

2. Freeze the requirements by typing 

```
pip3 freeze > requirements.txt
```

3. Add **storages** to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
5. Add the following keys within Heroku: **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY**. These can be found in your CSV file.
6. Add the key **USE_AWS**, and set the value to True within Heroku.
6. Remove the **DISABLE_COLLECTSTAIC** variable from Heroku.
7. Within your settings.py file inside the code just written add: 

```
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
8. Inside the settings.py file inside the bucket config if statement add the following lines of code:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

9. In the root directory of your project create a file called **custom_storages.py**. Import the following at the top of this file and add the classes below:

```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

10. Navigate back to you AWS S3 Bucket and click on **Create Folder** name this folder **media**, within the media file click **Upload > Add Files** and select the images for your site.
11. Under **Permissions** select the option **Grant public-read access** and click **Upload**.

[Back to top ⇧](#ginamore)

# Stripe Payments

To handle payments within the website ensure that you have set this up a guide on how this can be done can be found [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details).



# Credits

- The images used on my site were taken from [Shutterstock](https://www.shutterstock.com/).
- Images and video clips were also used from [Pexels](https://www.pexels.com/).
- The icons included throughout the website were taken from [Font-Awesome](https://fontawesome.com/).
- The colour theme was chosen using [coolors](https://coolors.co/).
- Help and support was given by the Code Institute Tutors.

Thank you to the tutors of code institute for the help given throughout this project.