<h1 align="center">Spotted City Guide Membership Club</h1>

[View the live project here.](https://)

<h2 align="center"><img src="images/SpottedJournal_Logo3.webp"></h2>

# Spotted members city guide

An insider membership guide to Stockholm.
This is a memberships site with the purpose of prividing members - people living in Stockholm - with a comprehensive guide of everything going on in the city as well as some perks for members making it good value for money. The site intends to includs everything from bars and restaurants, to things tod do, events, musical festivals etc.

## User Experience (UX)

#### First Time Visitor Goals

    1. As a First Time Visitor (non-logged-in), I want to easily understand the main purpose of the site and learn more about the benefits.

        1. Upon entering the site, users are greeted with a clean and easily readable navigation bar and a section briefly explaining what the site is about and the possibility of trying a membership for for free by clicking the button, or follow a link to read more.
        2. A non logged-in user can have a look around, see the posts with the excerpts, click the nav-links to the other pages, but not click the post links. The non-logged in user has the option to sign-up or read more about the membership.
        3. There is also a seperate navbar for logging in and signing up. This navbar dropsdown on smaller screens.

    2. As a First Time Visitor and returning visitor (logge-in), I want to be able to easily be able to navigate throughout the site to find content and administrating my account.

        1. The site has been designed to be fluid and has a content navbar at the top of every page, to never to entrap the user. At the top of each page there is a clean navigation bar with links to each content page, the links are cleary and simly described so uers know whre it will take them.
        2. On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.
        3. As a logged in user I can access the first navbar, a dropdown here I can access my profile (where I also find my saved post). Via this dropdown-navbar I can also access the pages for changing my email, password, logout and deleting my account.

   
-   #### Returning Visitor Goals

    1. As a Returning Visitor I want to see what new posts and events have been added to the site.
        1. These can be found in the first section on the index-page in the section The Latest.
        2. The Latest section is clearly visible on the first page.

    2. As a First time and Returning Visitor, I want to find out more about which events are coming-up and I want to be able to RSVP to the event.

        1. The events link is crealy visible in the navbar.
        2. On the event-detail page the uer can read more about the event and when and where it is taking place.
        3. The event-detail page also includes a simåle form to let the uer RSVP.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

-   ### Design
    -   #### Colour Scheme
        -   The three main colours used are black, white and green.

    -   #### Typography
        -   The Playfair Display font is the main font, together with Poppins used throughout the whole website with Serif and Sans Serif as the fallback fonts in case for any reason the font isn't being imported into the site correctly. 

    -   #### Imagery
        -   Imagery is important. The large, top image is designed to be striking and catch the user's attention. The post and events images are choosen to give the site a vibrant, fun and energetic feeling.

*   ### Wireframes

    -   Page Wireframe - [View](resources_readme/1.jpg)
                       - [View](resources_readme/2.jpg)
                       - [View](resources_readme/3.jpg)

*   ### ERDS for models

#### ERD Post model
| FK | Heading | Heading Model|
| ----------- | ----------- | ----------- |
| | title | charfield |
| | image |CloudinaryField |
| | Content | textField  |
| | slug | slugfield |
| | excerpt | textField  |
| | tag| charfield  |
| | status | small Integerfield |
| | start date |  |
| | end date|  |
| | Neighbourhood| TextField  |

#### ERD Event model
| FK | Heading | Heading Model|
| ----------- | ----------- | ----------- |
| | title | charfield |
| | image |img  |
| | description | text  |
| | slug | slugfield |
| | excerpt | text  |
| | tag| charfield  |
| | status | small Integerfield |
| | start date |  |
| | end date|  |

#### ERD Saved Post Model
| FK | Post| Post Model|
| ----------- | ----------- | ----------- |
| | title | charfield |
| | image |img  |
| | description | text  |
| | slug | slugfield |
| | excerpt | text  |
| | tag| charfield  |
| | status | small Integerfield |
| | start date |  |
| | end date|  |

#### ERD Liked Post Model
| FK | Post | Post Model|
| ----------- | ----------- | ----------- |
| | title | charfield |
| | image |img  |
| | description | text  |
| | slug | slugfield |
| | excerpt | text  |
| | tag| charfield  |
| | status | small Integerfield |
| | start date |  |
| | end date|  |

#### ERD RSVP Model
| FK | Event | Event Model|
| ----------- | ----------- | ----------- |
| FK | User| User Model|
| | Response  |CharField |
| | num_guests |Charfield |


#### ERD UserProfile Model
| FK | User | User Model| OntoOneField |
| ----------- | ----------- | ----------- | ----------- |
| | Neighbourhood | CharField |
| | Interests |ArrayField |
| | City | Charfield  |


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Bootstrap]
-   [Django]
-   [Javascript]


### Frameworks, Libraries & Programs Used

1. [Bootstrap 5:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitPod.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo.
1. [Canva:](https://canva.com/)
    - Canva was used to create the [wireframes](https://github.com/) during the design process and [ERD-Tables](https://github.com/)
2. [Tiny PNG](https://tinypng.com/)
- Tiny PNG was used to compress the images
3. [cloudconvert][https://cloudconvert.com/jpg-to-webp]
- Cloudconvert was used to convert the images to webp.



## Features 

-   Responsive on all device sizes

-   Interactive elements

### User stories
User stories are evaluated against test below.

 - Kanban Board: <img src="resources_readme/Skärmavbild 2024-05-02 kl. 15.21.49.png">

**USER STORY: Create and Manage content on the site**
As a site administrator I can create, update and delete content so that I can manage the site.

AC1 As a logged in user, they can create content.
AC2 As a logged in user, they can read content.
AC3 As a logged in user, they can update content.
AC4 As a logged in user, they can delete content.

**The requirements are met**

**USER STORY: Account registration and user authentication**

As a user I want to be able register for an account so that I access the members only content.

AC1 A user can easily register an account and fill in their account information.
AC2 When the user is logged-in they can access the members-only content.

**The requirements are met**

**USER STORY: Login, logout**
AC1 As a logged-in user, I want to easily be able to log out of my account when I'm finished.
AC2 As a user/member I can easily and securely logg-in.

**The requirements are met**

**USER STORY: Send email to users**

AC1 When they sign-up, update and when they forgotten their password

**The requirements are met** but isn't connected and can only be accessed in the terminal.

**USER STORY: Home page access**
As a home page visitor I can want to access the home page so that I can learn about the site.

AC1 As a first time visitor I want to be able to understand what the site is about and what benefits
AC2 As a logged-in user I want to be able to access members-only information relevant to my profile.

**The requirements are met**

**USER STORY: Opening and reading posts**

AC1 As a logged in user/member I want to be able to open and read posts about restaurants, bars, events etc.

**The requirements are met**

**USER STORY: Reading and updating**

AC1 As a logged-in user I want to easily be able to update my account information.

**The requirements are met**

**USER STORY: Saving posts and showing them in the user account**

**The requirements are met**

**Events, access and RSVP**

AC1 As a logged in user I want to be able to access the events page and RSVP to events.
AC2 As an admin I want to be able to create events and display them on the events page.
AC2 As an admin I want to be able to administer rsvps.
AC4 As an admin I want to be able to respond to users who have rsvp:ed to events.

**All the requirements have been met apart from the last one which as not been implemented yet**

**Deleting account and account information**
AC1 As a logged-in user I want to easily be able to delete my account information, and my account.

**The requirements are met**

**USER STORY: Liking posts and showing the likes in when the user is logged in (change colour of like icon)**

AC1 As a logged-in user I want to easily be able to delete my account information, and my account.

**The requirements are met**

**USER STORY: Liking posts and showing the likes in when the user is logged in (change colour of like icon)**

AC1 As a logged in user I want to be able to like posts about restaurants, bars etc and se my liked posts/articles.
AC2 As a logged in user I want to be able to like and unlike posts.
AC3 As a logged in user I want to save posts to my profile so I can locate them later.

**Not all of the rquirements ahve been met. Posts can be liked/un-liked saved/un-saved and the colour of the heart icon changes but isn't saved.**

 ### Testing User Stories from User Experience (UX) Section

### Existing Features, Testing & unit testing

- __Navigation Bar__

  - Featured on all pages, the full responsive navigation bar includes links to the Logo (which is also a linked to the home-page), Restaurants & Bars, Things To Do, What's On, Events, Neighbourhoods, Perks and Sign and Sign Up (when logged out) and a dropdown with profile, logout, change password and change email when logged in. The navbar page and is identical on each page to allow for easy navigation.
  - This section will allow the user (logged in and non-autenticated) to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

![Nav Bar](https://)

- __The landing page image__

  - The landing page for non logged in users give the users an overview of the site but the posts are unclickable as they are only for logged in users. 
  - The Latest section show the uers the latest from all categories/pages: restaurants & bars, things to do, what's on etc.

![Landing Page](https://)

- __The Events page__

  - The Events page give the user an overview of the events available will allow the user to see the benefits of signing up as a member.
  - The listed events are cklickable and takes the user to a details page with more information about the eve, it also includes a function for the member to RSVP to events and let the arrangers know how many gusets they will be bringing.

| Form | Description | Testing | Comment | Result |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **RSVP-form**, App: rsvp, Template: event_detail.html| Gives the uer the ability to RSVP for psoted events. <br> The RSVP-form is part of the event_detail page. The user can chose yes or no <br> and the number of guests <br> and then click the RSVP button. | The user can change their response <br> by changing their answer and number of guests <br> and submiting again. | The user's response gets sent  <br> to the database and is also whown in the admin panel| OK |
 
![Events Page](https://)
![Events Detail Page](https://)

- __Restaurants & Bars, What's On, & Things to do page__

  - These apges displays posts for the relevant subjects and allows the uer to brows restaurants, bars, things to do, things that are happening in the city. Posts are added daily to give the members/users value and and incentive to keep being members.

![Post List page](https://)
![Post Detail page](https://)


- __Neighbourhoods Page__

  - The Neighbourhoods page displays by neighbourhood, to make it easier for users to find what is going on around where they live or work.

![Neighbourhoods](https://)

- __Perks Page__

  - This displays a post list of the perks available to members.

![Perks](https://)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Spotted. The links will open to a new tab to allow easy navigation for the user. 
  - the footer also inclued links to About (inkl. contactinfo), Become a member and
 Partnerships pages.  

![Footer](https://)


- __The Sign Up Page__

  - This page allows users to get signed up to the membersite. The user will also be able specify their interest and let the site know which neighbourhood they live in. The user will be asked to submit their full name, a username, email address choose a password.

| Form | Description | Testing |
| ----------- | ----------- |  ----------- |
| **SignUpForm**, App: Core, Template: register.html <br> (inludes user and profile form)| Gives the user the ability signup to the site. The user can fill in the form, chosing a username and password and then clicking the signup button. | User info. and details are saved to the database. | Both the email and usermail needs to be unique<br> and trying  to use the same email and user mail <br> and email will return the form with an error message. |

![Sign Up](https://)


- __The Profile Page__

  - This page allows users to see their personal info. and profile choices, as well as their saved posts.
| Form| Description | Testing  | Comment | Result |
| ----------- | ----------- |  ----------- | ----------- | ----------- |
| **UpdateUserProfileForm**, App: Core, Template: profile.html | Gives user the ability to change their details and preferences. <br>The user can update their profile <br> by changing and confirming <br> email and user name. The form is pre-populated <br> with existing details. | The user can also change <br> their neighbourhood and interest choices. <br> The membership is only available in Stockholm, <br>otherwise they would also be able to choose another city. <br> The email, username and passwords have to match <br> otherwise the form want sign the user up but will return the <br> form to correct the errors, that are marked. | | OK |

![Profile](https://)


- __The Signin Page__

  - Registered users can login.

| Form | Description | Testing  | Comment | Result |
| ----------- | ----------- |  ----------- |  ----------- |  ----------- |
| **SignIn**, Form App: Core, Template: login.html | Gives the user the ability to signin with their email and password. The user can fill in their email and password to sign in. <br> There is also an option to click remember me. | When the user fills in their login info correctly <br> and clicks the button <br> they are logged in and authorised access the whole site. <br> They will then be taken directly to the landing page for logged in users. | | OK|

![Log In](https://)

- __The Logout Page__

  - Users can logout

![Logout](https://)


- __The Change Email__

  - Registered users can change/update their email.

| Form | Description | Testing   | Comment |Result |
| ----------- | ----------- |  ----------- | ----------- | ----------- |
| **Change email**, AllAuth, email.html|  |  |
| | |   |

![Change email](https://)


- __The Change Password__

  - Gives the user the ability to change their password. Registered users can change their password.

| Form | Description | Testing  | Comment | Result |
| ----------- | ----------- |  ----------- | ----------- | ----------- |
| **Change password**, AllAuth, password_change.html|  |  |
| | |   |


![Change password](https://)


- __The Delete Account Page__

  - Gives the user the ability to easily delete their account. Registered users/members can delete their account and all associated information.

| Form | Description | Testing  |Comment | Result|
| ----------- | ----------- |  ----------- | ----------- | ----------- |
| **DeleteAccountForm**, App: Core, delete_account.html | The user gets to the Delete account page by clicking the link in the frist/dropdown navbar. Here the user can delete their account. <br> Confirming by checking the box <br> and then clicking delete account. | The user, user info and any profile information <br> related to the user is deleted from the admin panel and the database. |  OK |

![Delete](https://)


### Features Left to Implement

- Navigation directly between posts without having to back out to the post_list.
- Navigation directly between events without having to back out to the event_list.
- At the moment the email feature only runs in the terminal, and email verification isn't required to sign up. Connecting the email and sending actual emails, and email verficatiosn is a feature that should be implemented.
- More filtering functions, and more tags.


## Testing other Features

### Logout
| Function | Description | Result   |
| ----------- | ----------- |  ----------- |
| **Signout**, App: Core, Template: login.html | When the Signout link in the first navbar (dropdown) is clicked <br> it takes the user to the signout page.<br> Where they can click the signout button <br> that signs them out and returns them to <br> the logged out version of the index page.| ok |


| Feature| Description | Testing | Comment | Result|
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Like-icon**, App: content_management, Template: all templates displaying post lists. | Icon/button for liking and unliking posts | Likes or unlikes the post <br> when clicked and returns a Json response  <br>in the form of an alert | Saves the instance of the post-like to the database, so that when it is ckicked again there is a Json response telling the uer that tey have already liked it and it is now unliked. | OK |
| **Save-icon**, App: content_management, Template: all templates displaying post lists. | Icon for saving and unsaving posts. | Saves or unsaves the post <br> to the database. Saved posts are shown in the user profile. It returns a Json response telling the user they have saved the post. When they click the save icon again thre is a message telling users they have now unsaved he post. <br> Message in the form of an alert.  | Saves the instance of the post to the database. | OK |


### Buttons ### (not part of any form)

### Navbar & dropdowns
| Feature | Description | Testing | Comment | Result|
| ----------- | ----------- | ----------- | ----------- | ----------- |
| First navbar| Links to all signup and profile <br> related functions and pages.  | All page links were tested and worked. | OK |
| Second navbar| Links to all content pages | All page links were tested and worked.  | OK |
| Dropdowns | As above but for small screens | All links ere tesed and worked.  | OK |


## Lighthouse

- Results:

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.

### Validator Testing 

- HTML
  - Stray end tags were flagged for when checking code when non.logged in, this is because the some links are only available to authorized users, which means the link isn't visible when logged out. The link wraps a card so the end tag is visible to the browser. When checking the same html when logged in it passes validation. 
 -  Summernote is causing issues by rendering code inte white spaces on the details_templates. This throw error when validating the HTML for these pages.
-  No other errors were returned when passing through the official [W3C validator]()

- No errors were found when passing through the official [(Jigsaw) validator]()
- CI Python Linter [(https://pep8ci.herokuapp.com/)]()
- JS Hint [(https://jshint.com/)] No error were found when passing the code through JSHint.


### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

Cloudinary

## Deployment

## Creating the Heroku app, deploying to Heroku

Steps to follow for deployment to Heroku:

### In GitHub.
1. Navigate to the repository for the project. 

### In Heroku

1.	Go to Heroku, create account, if you don't have one, and log in.
2.	Go to the dashboard and click New after which you click Create new app
3.	Choose name and region. Click Create app
4.	Go to Settings, under the "Config Vars" set your Key/Value Pairs.
    You must then create a _Config Var_ called `PORT`. Set this to `8000`
    If you have credentials, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.
    When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:
    1. `heroku/python`
    2. `heroku/nodejs`

5.	In the Buildpacks section, add buildpacks. Note order in which you add buildpacks: Python first and nodejs.
6.	No go to Deployment. In deployment method click on "GitHub"(for repository)
7.	The connect to GitHub, find your repository and click  connect.
8.	Under connect to GitHub-section, you can either chose automatic deploys with Enable Automatic Deploys or Manual Deploy, to deploy manually.
    
    **Now you can view the deployed app.**


## Credits 

- I used the I Think Therefore I Blog walkthrough as a guide to get my project set up and get me started. And I refered back to it throughout the project.

- How to extend the Django user model:
[https://simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
-  Creating a like function:
[StackOverflow](https://stackoverflow.com/search?q=creating+a+like+function+in+Django)
- Liking/un-liking posts, saving/un-saving posts:
(https://stackoverflow.com/questions/14007453/my-own-like-button-django-ajax-how)
- [StackOverflow](https://stackoverflow.com/questions/14007453/my-own-like-button-django-ajax-how)
- [StackOverflow](https://stackoverflow.com/questions/63081738/like-unlike-a-post-without-refreshing-the-page)

- Using Ajax with Django:
[StackOverflow](https://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications/20307569#20307569)
- Prevent default event:
[StackOverflow](https://stackoverflow.com/questions/7056669/how-to-prevent-default-event-handling-in-an-onclick-method)
- Let user delete their account:
- [StackOverflow](https://stackoverflow.com/questions/54864355/django-user-account-delete-and-then-return-redirect-and-render)
(https://stackoverflow.com/questions/65510305/django-how-to-enable-users-to-delete-their-account)
(https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth)
- Overlay for frontpage:
 [Overlay](https://www.w3schools.com/howto/howto_css_overlay.asp)

Exists/ Doesnotexist:
- [StackOverflow](https://stackoverflow.com/questions/40910149/django-exists-versus-doesnotexist)

 - Setting up email allAuth:
 [https://florianbgt.com/](https://florianbgt.com/posts/django_allauth_email_login)

 - Filter if tag:
- [StackOverflow](https://stackoverflow.com/questions/5923676/template-filter-if-tag)


### Content 

- The text content for the posts and pages were generated with the help of AI.
- The icons used in the project were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The logo and favicon was created by my husband.

- The images for posts, events and pages were downloaded from free images on [Unsplash](https://unsplash.com/)



