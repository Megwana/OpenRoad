# **OPEN ROAD**

## Conceptualisation

Welcome to Open Road , a website for visitors with a passion for travel to seek inspiration and plan their road trips specifically around Northern America.

I love to travel and know many others also hold this passion, to seek new adventures and learn new things. 

I think so much more can be learnt and experienced from driving from place to place as opposed to flying. You gain much more of a feel for a place, when traveling by car and hold much more flexibility in your timings and destinations of where you want to go. 

Therefore, I wanted to create a website dedicated to road trips specifically. The term 'road trip' has been coined by northern americans and holds large association with the USA. I decided it was much better to begin with one country that has the capacity for a variety of road trips with the ability to expand with time. 

![Open Road Media Image]()

LINK TO DEPLOYED APP

![Last Commit]()
![Language Count]()
![Top Language]()
![Contributors]()

<details>
<summary>
Table of Contents - Click for full list
</summary>

- [UX Development](#ux-development)
- [Technologies Applied](#technologies-applied)
- [Features](#features)
- [Testing](#testing) 
- [Deployment](#deployment--local-development)
- [Credits & Acknowledgments](#credits--acknowledgments)
</details>

# UX Development

## Strategy

### Project Goals

* To create an App where users can find North American road trip routes.

* Guest users who do not have an account, are able to preview routes by seeing the first two. 

* Users who have created an account are able to have access to more road trips. In addition, they are able to add their own trip notes. Whether this be a journal documentation as they travel. Or they wish to take planning notes. 

* Display the information of the site in a user-friendly way.

* To inspire users to travel with beautiful images across the road trip destinations. 

* Give guest users the ability to create an account. 

* Give users (registered members) access the CR functionality. 

* Display success and error messages when signing up or logging in, to provide users with an understanding of different actions or etc. why they may not have been able to sign up successfully.

* Give users the ability to make notes and for other users not see their notes. Their trip notes are solely viewed through their logged in user account. 

### Demographic

* Ages 18 and above for viewing, signing up  and documenting/ using the trip notes platform. 

* Visitors who are interest in road trips, traveling or the USA. 

### User stories

#### First-time Visitor Goals
I want users to be able to:

* Understand the purpose of the website and how to use it. 

* View the preview selection of the road trips to give them an idea before creating an account. 

* Navigate easily to the sign up page.

#### Account User Goals
I want users to be able to:

* View more Road trips now that they are able to access these as a logged in user. 

* Add travel notes, plans. 

* Be able to log out with ease. 

## Scope
### Feature Ideas
During the planning process, I created an Importance viability analysis of the features:

| # | Feature | Importance | Viability |
| --- | --- | --- | --- |
| 1 | View Road Trips | 5 | 5 |
| 2 | View and Create Trip Notes | 5 | 5 |
| 3 | Edit and Delete Trip Notes | 4 | 3 |
| 4 | Create, Edit and Delete Account | 4 | 3 |
| 5 | Login and Logout to Account | 5 | 5 |
| 6 | Moderate Content posted by Account Users | 4 | 1 |
| 7 | Receive Notifications on users activities | 2 | 2 |
| 8 | Search Different Road Trips | 3 | 1 |
| 9 | Share Road trips on Social Media | 2 | 3 |
| 10 | Show alert messages to communicate Log Authentication to user  | 4 | 5 |

Based on the results of the Feature Ideas Planning, I have decided to attempt to implement Features numbers 1, 2, 5 and 10 for this production release and park the remaining features due to time limitations.

- feature ideas planning
- functionality
Structure
- Topology (navigating through python element)
* Guest User
* Sign in User 
* schema
## Skeleton
- wireframes 
### Design

[Bootstrap5](https://getbootstrap.com/) was used and customised for the front-end development of the application.

#### Color scheme

#### Typography

[Bootstrap5](https://getbootstrap.com/) was used and customised for the Typography of the application.

# Technologies Applied 

* Languages:
1. HTML 
2. CSS
3. JavaScript
4. Python

1. Flask
2. Postgres
3. pip
4. Jinja
5. Git 
6. Google Chrome
7. Werkzeug
8. Flask_login
9. Heroku
10. Github
11. SQLAlchemy
12. Bootstrap
13. Font Awesome 
14. Python Checker https://www.pythonchecker.com/
# Features
- Future Features
- Defensive (login required)
- functionality routes check if logged in 
- error 

# Testing
(Bugs)

# Deployment & Local Development 

## Deployment to Heroku

I used Heroku to deploy this project. The deployed version is the same as the repository which is stored in GitHub.

Deployment steps:

1. In GitPod CLI, the root directory of OpenRoad, run: 
pip3 freeze --local > requirements.txt to create a requirements.txt file holding project dependencies. 
2. In the root directory of Open Road, create a new file called 'Procfile'.
3. Login to Heroku/ Create an account. 
4. Once logged in, select Create New App.
5. Add the name of your app (no spaces). Select your closest region US or Europe. 
6. Go to the Deploy Tab on the Heroku Dashboard and select Github.
7. Search for Open Road by its repository name and select connect. 
8. Go to the settings tab, click reveal config vars and input the following: 

# Credits & Acknowledgments

I would like to Credit:

https://www.roadtripusa.com/the-oregon-trail/ For the Road Trip content. 





