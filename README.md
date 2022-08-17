[GinAmore Live Link](https://ginamore.herokuapp.com/)
[Github Repository](https://github.com/sophiebatten123/GinAmore)

# GinAmore

(Developer: Sophie Batten)

![Am I Responsive?]()

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

# Forking the Repository

  * Log in to GitHub and locate the required GitHub repository.
  * At the top of the Repository, above the **"Settings"** button, locate the button labeled **"Fork"**.
  * You should now have a copy of the original repository within your GitHub account.
  * You can make changes to this new version whilst keeping the original version safe.

# Cloning the Repository

  * Ensure that you are logged into GitHub and locate the required GitHub repository.
  * Click the dropdown button labelled **'Code'** above the file list.
  * Copy the URL for the required repository.
  * Open Git Bash on your device.
  * Change the current working directory to the location where you want the cloned directory.
  * Type git clone in the CLI and then paste the URL you copied earlier. This is what it should look like: **$ git clone https://github.com/sophiebatten123/ginamore**
  * Press Enter to create your local clone.