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

### Viewing and Navigation (Products)

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|1| Shopper | View a list of all Gin products | Select which ones I want to purchase | M | --|
|2| Shopper | View individual Gin details | Identify the price, description and product rating of each product | M | -- |
|3| Shopper | Identify any deals and special offers quickly on the page | Take advantage of special offers | S | -- |

### Registration and Verification

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|4| Site User | Easily register for an account | View my personal profile information | M | --|
|5| Site User | Easily login/logout of my account | Access my personal account | M | -- |
|6| Site User | Easily recover my password if I forget it | Recover access to my account | M | -- |
|7| Site User | Receive an email to verify I have created an account | Verify my account is set up. | S | -- |
|8| Site User | Register/login to an account via social media | Login to my account quicker | C | -- |
|9| Site User | Confirm I am of legal age to drink | Use the site effectively and purchase items | M | -- |


### Sorting and Searching

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|10| Shopper | Sort through all Gin products | Easily see the best rated, best priced items | M | --|
|11| Shopper | Sort based on the Gin category | Sort Gin items based on the type of Gin I prefer | M | -- |
|12| Shopper | Search a product by name and description | Find a specific Gin I would like to purchase | M | -- |
|13| Shopper |  See search results quickly and easily  | Quickly decide which product I would like to purchase | M | -- |

### Purchasing and Checkout

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|14| Shopper | View items in my bag to be purchased | Check total cost and the items that I will be purchasing | M | --|
|15| Shopper | Receive an email to verify my order | Feel more secure that my payment has gone through | S | -- |
|16| Shopper | View an order confirmation when my order is complete | Check my order is correct without mistakes | S | -- |
|17| Shopper | Securely provide payment details| Confidently provide payment details to purchase an item | M | -- |
|18| Shopper | Enter payment information quickly  | Check out quickly without hassle | M | -- |
|19| Shopper | Adjust the quantity of items in my bag | Easily adjust the quantity for my own preference | S | -- |
|20| Shopper | Select the quantity of product to add to shopping bag | I am able to get the amount of Gin I require | M | -- |
|21| Shopper | Quickly see the total cost of all my products | Avoid spending too much | m | -- |

### Admin and Store Management

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|22| Store Owner | Easily Add Cocktail Recipes | Keep recipes interesting and new to users | M | --|
|23| Store Owner | Edit/Update Cocktail Recipes | Ensure the cocktail information is up to date | S | -- |
|24| Store Owner | Add a Product | Add new products to my store | M | --|
|25| Store Owner | Edit/Update a Product | Change details of a product including description and price | M | -- |
|26| Store Owner | Delete a Product | Remove any discontinued products | M | -- |

### Product and Cocktail Reviews

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|27| Shopper | Rate and Review Cocktail Recipes | Communicate with others on the site | C | --|
|28| Store Owner | Delete a Review |  Filter the content shown to customer | S | --|
|29| Shopper | Leave a Product Review | Advise other shoppers on their purchases | S | --|
|30| Shopper | Submit cocktail recipe ideas | Contribute to the site and feel in contact with other cocktail makers | C | --|

### Wishlist Functionality

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|31| Shopper | Add items to my wish list | Easily find items later on to purchase them quickly | C | --|
|32| Shopper | Remove items from my wish list | Keep my wish list basket up to date with things I love | C | -- |

### Viewing and Navigation (Cocktails)

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|33| Shopper | View individual cocktail recipes | Learn how to make individual cocktails | M | --|
|34| Shopper | View cocktail recipes based on their category | Choose which recipe I would like to make | M | -- |

# Agile Planning Enviroment

## Acceptance Criteria

## Epics

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