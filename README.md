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
  - [Agile Planning Enviroment](#)
  - [Design](#)
    - [GinAmore Design Principles](#)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Wireframes](#)
    - [Desktop Wireframes](#)
    - [Mobile Wireframes](#)
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

### Viewing and Navigation

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|1| Shopper | View a list of all Gin products | Select which ones I want to purchase | -- | --|
|2| Shopper | View individual Gin details | Identify the price, description and product rating of each product | -- | -- |
|3| Shopper | Be able to quickly see the total cost of all my products | Avoid spending too much | -- | -- |
|4| Shopper | Identify any deals and special offers quickly on the page | Take advantage of special offers | -- | -- |

### Registration and Verification

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|5| Site User | Easily register for an account | View my personal profile information | -- | --|
|6| Site User | Easily login/logout of my account | Access my personal account | -- | -- |
|7| Site User | Easily recover my password if I forget it | Recover access to my account | -- | -- |
|8| Site User | Be able to personalise my user profile | Verify my account is set up | -- | -- |
|9| Site User | Identify any deals and special offers quickly on the page | View my basket, order information and payment information | -- | -- |

### Sorting and Searching

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|10| Shopper | Be able to sort through the Gin products | Easily see the best rated, best priced items | -- | --|
|11| Shopper | Be able to sort based on the Gin category | Sort Gin items based on the type of Gin I prefer | -- | -- |
|12| Shopper | Search a product by name and description | Find a specific Gin I would like to purchase | -- | -- |
|13| Shopper | Easily see what I have searched for and the results | Quickly decide which product I would like to purchase | -- | -- |

### Purchasing and Checkout

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|14| Shopper | View items in my bag to be purchased | Check total cost and the items that I will be purchasing | -- | --|
|15| Shopper | Receive an email to verify my order | Feel more secure that my payment has gone through | -- | -- |
|16| Shopper | View an order confirmation when my order is complete | Check my order is correct without mistakes | -- | -- |
|17| Shopper | Feel my personal payment information is protected | Confidently prodive payment details to purchase an item | -- | -- |
|18| Shopper | Easily enter my payment information | Check out quickly without hassle | -- | -- |
|19| Shopper | Adjust the quantity of items in my bag | Easily adjust the quantity for my own preference | -- | -- |
|20| Shopper | Easily select the quantity of the product I want | I am able to get the amount of Gin I require | -- | -- |

### Admin and Store Management

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|21| Store Owner | Add a Product | Add new products to my store | -- | --|
|22| Store Owner | Edit/Update a Product | Change details of a product including description and price | -- | -- |
|23| Store Owner | Delete a Product | Remove any discontinued products | -- | -- |

### Product Review and Screening

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|24| Shopper | Leave a Product Review | Advise other shoppers on their purchases | -- | --|
|25| Store Owner | Screen/delete reviewed comments | Allowing reviews to be monitored and deleted if needed | -- | -- |

### Wishlist Functionality

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|26| Shopper | Like products so they appear in my wish list | Easily find items later on to purchase them quickly | -- | --|
|27| Shopper | Remove items from my wish list if I change my mind | Keep my wish list basket up to date with things I love | -- | -- |

### Cocktails Review and Screening

| ID | As A |I want to be able to...|So that I can...|Story Points|MoSCoW|
|----|------|-----------------------|----------------|------------|------|
|28| Site User | Leave comments on cocktail recipes  | Communicate with other site users and leave reviews and advice on recipes | -- | --|
|29| Site Admin | Screen/delete comments  | Ensure that they are appropriate | -- | -- |

# Colour Scheme

The colours within the site were carefully selected to mirror the premium products sold at GinAmore. The dark regal blue contrasts against the light pink making elements of importance stand out on the page. These colours were initially selected from the sites main banner image using DEV tools, allowing for all colours within the page to compliment eachother nicely.

![Colour-Scheme](static/images/color-scheme.PNG)

# Wire Frames

Although the wireframes for site users and site admin are similar there are a few subtle differences between some pages to help admin modify, add and delete products and cocktails. Extra wireframes were created to account for these differences below:

## Desktop Wire Frames (Site Users)

[Homepage](static/images/homepage_desktop.PNG)

[Our Story](static/images/aboutus_desktop.PNG)

[Contact Us](static/images/contact_desktop.PNG)

[Gin Page](static/images/gin_desktop.PNG)

[Gin Detail Page](static/images/gin_detail_desktop.PNG)

[Cocktail Page](static/images/cocktail_desktop.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_desktop.PNG)

## Desktop Wire Frames (Site Admin)

[Gin Page](static/images/gin_admin_desktop.PNG)

[Gin Detail Page](static/images/gin_detail_admin_desktop.PNG)

[Cocktail Page](static/images/cocktails_admin_desktop.PNG)

[Cocktail Detail Page](static/images/cocktail_detail_admin_desktop.PNG)