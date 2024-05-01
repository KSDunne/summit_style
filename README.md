# Summit Style

(Developer: Katie Dunne)

![AmIResponsive Image](docs/readme_images/amiresponsive.PNG)

## Live website

Link to live website: [Summit Style](https://summit-style-b727a186ee80.herokuapp.com/)

## Purpose of the project

Here is an eCommerce website, for a fictitious business called Summit Style. This is a full stack website built using the Django web framework. This business sells adventure clothing, equipment and short educational courses based on outdoor skills. There is a star rating feature on all products and courses. There is a app for testimonals which shows 3 testimonials on the front end, with an option to submit testimonials using a form. There is also a contact tab.

## Table of contents

## User experience (UX)

### Key project goals

### Target audience

- Users that are interested in outdoor and adventure hobbies
- Users that want to buy clothes that are specifically made with outdoor functionality (e.g. fleece, coats, base layers, wetsuits)
- Users that are interested in equipment for outdoor and adventure hobbies (e.g. tents, sleeping bags)
- Users that would like to learn about outdoors and adventure hobbies through short courses

### User requirements and expectations

## Epics and user stories

### Epics

1. Viewing and navigation of products and courses
2. Registration and user accounts
3. Sorting and searching
4. Purchasing and checkout
5. Store management
6. Rating and review feature
7. Testimonials app
8. Contact app

### User stories

- As a website user, I want to be able to:

1.	View a list of clothing products so that I can select some to buy
2.	View a list of outdoor equipment products so that I can select some to buy
3.	View a list of short courses so that I can select some to buy
4.	View a specific category of products or courses, so that I can quickly find what I'm interested in
5.	View individual product details so that I am informed of price, description and product rating
6.	View individual course details so that I am informed of price, description and rating
7.	Identify sale items easily, so that I can take advantage of savings on products I want to buy
8.	See the total of my purchases at any time to avoid overspending
9.	Register for an account so that I can have a profile that is specific to me
10.	Easily log in and out to access my personal account information and to protect it once I’m finished interacting with it
11.	Easily recover my password if I forget it so that I can recover access to my account
12.	Receive an email confirmation after registering to verify my account registration was successful
13.	Have a personalised user profile so that I can view my order history, order confirmations and save payment information
14.	Quickly separate a list of clothing products from a list of equipment and a list of courses
15.	Sort the list of offerings (clothes, equipment or courses) so that I can easily distinguish the best rated, the best priced or categorically sort products
16.	Sort a specific category of product or course, so that I can find the best rated or best priced in a specific category
17.	Search for a product or course by name or description so that I can find a specific product or course
18.	Easily see what I've searched for and the number of results so that I can quickly see if the product or course I want is available here
19.	Easily select the size of a product when purchasing it so that I don’t accidentally order the wrong size of clothing
20.	View items in my cart to be purchased so that I’m aware of the total cost of items and all the items that I will receive after checkout
21.	Adjust the quantity of individual items in my cart so that I can make changes to my order before checkout if I wish to do so
22.	Easily enter my personal payment information so that I can checkout quickly
23.	Feel that my personal and payment information is safe so that I can confidentially provide the information to make a purchase
24.	View an order confirmation after checkout so that I can verify that I haven’t made any mistakes
25.	Receive an email confirmation after I make a purchase so that I can keep the confirmation for my own records
26. See average star ratings on products quickly and easily, so that I don't have to go searching for ratings and I can buy a reliable product or course
27. Submit my star rating so that I can give a vote on how good the product or course is
28. Read reviews that other customers have submitted so that I feel I am purchasing a reliable product
29. Submit a review using a front end form with fields for title, star rating and review text
30. Edit the review I gave, in case I change my mind on how good a product or course is
31. Delete a review I submitted in case I rate the wrong product or I change my mind about giving my opinion
32. Read testimonials from other customers so that I feel like I am making a reliable purchase
33. Submit a testimonial of my own so that I can give my opinion on my purchase from this company
34. Find the contact page easily, so that I don't get frustrated trying to contact the company
35. Contact summit style using a contact form and recieve feedback that my query has been stored and the company will respond in a few days

- As a store owner, I want to be able to:

36.	Add a product or course so that I can add new offerings as they become available for me to sell
37.	Edit or update a product or course information so that I can change product and course prices, descriptions and images if needed
38.	Delete a product or course so that I can remove items that are no longer for sale

## Sprints

1. Development environment setup
2. Design (wireframes and colors)
3. Data mapping of entity relationship diagrams
4. Viewing and navigation of products and courses
5. Registration and user accounts
6. Sorting and searching
7. Purchasing and checkout
8. Store management
9. Add rating feature
10. Testimonials app
11. Contact app
12. Testing
13. Project sunset

## Features

### Logo and navigation bar

#### Mobile navigation using burger menu

#### Monitor navigation bar

On monitor size screens, this is split into 2 divs. The top nav which contains the logo, a search bar, an account dropdown menu and a shopping cart logo with link to the shopping cart. This shopping cart also shows a running total of the users spend. The second part is the main site navigation bar. This main navbar contains downdown menus and links with titles; all products, clothes, equipment, courses, testimonials and contact.

### Hero image

The index page hero image was chosen because it fits the theme of the website. There is a man with hiking gear looking at some mountains in the distance. The colors of this image also align with the theme and design of the overall website.

### Shop now button

This is a call to action on the index page

### We're green section on the index page

### Newsletter sign up on the index page

### Average star rating and reviews

### Footer

### Custom 404 page

### MoSCoW

## Three custom models

1. Average Star Rating and Reviews

This has FE CRUD functionality for your rating and reviews

2. Testimonials App

This is on a testimonials app with tab of its own. This has 3 showing at the top half of the page and the ability to submit a testimonial through a form at the bottom half of the page

3. Record user contact requests in the database

This is on a contact app with tab of its own

## Future features

## Design

### Color

#### Color palette 1

![Accessible color palette 1](docs/readme_images/color_palette_1.PNG)

#### Color palette 2

![Accessible color palette 2](docs/readme_images/color_palette_2.PNG)

## Wireframes

### Index page wireframes

#### Mobile

![Index iPhone SE](docs/readme_images/Home_Page.png)

#### Tablet

![Index Tablet](docs/readme_images/Tablet_Home.png)

#### Monitor

![Index Monitor](docs/readme_images/Monitor_Home.png)

### Product detail page

#### Mobile

![Product Detail iPhone SE](docs/readme_images/Product_Detail_Page.png)

#### Tablet

![Product Detail Tablet](docs/readme_images/Tablet_Product_Detail.png)

#### Monitor

![Product Detail Monitor](docs/readme_images/Monitor_Product_Detail.png)

## Database schema

### Entity relationship diagram

### Entity relationship tables

Please find a screenshot of tables below. These tables are in preparation for the final entity relationship diagram (ERD).

![ERD](docs/readme_images/erd1_300424.PNG)

## Technology Used

### Languages and framework

- [HTML5](https://developer.mozilla.org/en-US/docs/Learn/HTML "link to html mozilla documentation")
  was used to create content and structure
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS "link to css mozilla documentation")
  was used to add custom styles
- [Django 4.2.10](https://www.djangoproject.com/ "link to django docs homepage") was the python framework used to develop the site

### Database

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/ "link to postgresql from code institute") was used as the PostgreSQL database for this project

### Technologies and tools

- [Django allauth](https://docs.allauth.org/en/latest/ "link to official allauth documentation") addresses authentication, registration and account management

## Testing

Detailed testing documentation can be found

### Fixed bugs

Leaving this here as a reminder for me to come back to it later:

1. Webhook handler handling profiles
2. wh handler key and testing

### Unfixed bugs

### Supported screens and browsers

#### Screens

- iPhone SE, 375px wide. Also looks good down to 300px according to devtools
- iPad Mini, 768px wide
- Nest Hub Max, 1280px wide

#### Browsers

- Chrome
- Firefox
- Safari
- Edge
- Opera

## Deployment

### Pre deployment

### Stripe setup

This project used [Stripe](https://stripe.com) to handle all payments.

- Log in to [Stripe](https://stripe.com)
- Go to the developers section. The link is located in the top right of the page
- Go to API keys tab and copy the PUBLIC_KEY and SECRET_KEY and add them to your env.py file
- `STRIPE_PUBLIC_KEY` = starts with **pk**
- `STRIPE_SECRET_KEY` = starts with **sk**
- Go to the Webhooks tab and click on add endpoint
- Here you will need to give a link to the deployed application. The link should look like this: https://your_website.herokuapp.com/checkout/wh/
- Choose the events the webhook should receive and add endpoint
- You'll be given another key, the stripe webhook secret
- `STRIPE_WH_SECRET` = starts with **wh**
- When the application is deployed, run a test purchase to ensure the webhooks are working
- Go back to the webhooks page to check the events

### AWS setup

### Deploying with heroku

### Fork this repository:

### Clone

The repository can be cloned by following these steps:

- Go to the [GitHub repository](https://github.com/KSDunne/summit_style)
- Click the Code button near the top of the page
- Select 'HTTPS', 'SSH', or 'Github CLI', depending on how you would like to clone
- Click the copy button to copy the URL to your clipboard
- Open Git Bash
- Change the current working directory to where you want the cloned directory
- Type git clone and paste the URL ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
- Press enter to create your clone locally

## Credits

### Code

[Star rating tutorial](https://medium.com/p/e1deff03bb1c)

### Media

### Inspiration from real world ecommerce websites

## Acknowledgements

Thank you to family, friends and pets for the support. Also thank you to my mentor and CI cohort facilitator :sparkles:
