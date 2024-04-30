<h1 align="center">Spotted City Guide Membership Club</h1>

[View the live project here.](https://)

<h2 align="center"><img src="https://"></h2>

## User Experience (UX)

 ### User stories

 ### Testing User Stories from User Experience (UX) Section

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
        -   The Montserrat font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat is a clean font used frequently in programming, so it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

*   ### Wireframes

    -   Page Wireframe - [View](resources_readme/1.jpg)
                       - [View](resources_readme/2.jpg)
                       - [View](resources_readme/3.jpg)

*   ### ERDS

#### ERD Post model
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



![Logo](https://)

# Spotted members city guide

An insider membership guide to Stockholm.
In this section, you will include one or two paragraphs providing an overview of your project. Essentially, this part is your sales pitch. At this stage, you should have a name for your project so use it! Don’t introduce the project as a Portfolio project for the diploma. In this section, describe what the project hopes to accomplish, who it is intended to target and how it will be useful to the target audience. 

For example; Love Running is a site that hopes to help keep people motivated to meet up for runs on a regular basis in Dublin, Ireland. The site will be targeted toward runners who are looking for a way to socialise and keep themselves fit. Love Running will be useful for runners to see exactly when and where they should be to join the running club. 

![Responsice Mockup](https://github.com/lucyrush/readme-template/blob/master/media/love_running_mockup.png)

## Features 

-   Responsive on all device sizes

-   Interactive elements

In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

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
 
![Events Page](https://)
![Events Detail Page](https://)

- __Restaurants & Bars, What's On, & Things to do page__

  - These apges displays posts for the relevant subjects and allows the uer to brows restaurants, bars, things to do, things that are happening in the city. Posts are added daily to give the members/users value and and incentive to keep being members.

![Post List page](https://)
![Post Detail page](https://)


- __Neighbourhoods Page__

  - The Neighbourhoods page displays by bneighbourhood, to make it easier for uers to find what is going on around where they live or work.

![Neighbourhoods](https://)

- __Perks Page__

  - This displays a post list of the perks available to members.

![Perks](https://)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Spotted. The links will open to a new tab to allow easy navigation for the user. 
  - the footer also inclued lnks to About (contactinfo), Become a member and
 Partnerships pages.  

![Footer](https://)


- __The Sign Up Page__

  - This page allows users to get signed up to the membersite. The user will also be able specify their interest and let the site know which neighbourhood they live in. The user will be asked to submit their full name, a username, email address choose a password.

![Sign Up](https://)


- __The Profile Page__

  - This page allows users to see their personal info. and profile choices, as wella s their saved posts.

![Profile](https://)

- __The Login Page__

  - 

![Log In](https://)

- __The Logout Page__

  - 

![Logout](https://)



- __The Change Email__

  - 

![Change email](https://)

- __The Change Password__

  - 

![Change password](https://)


- __The Delete Account Page__

  - 

![Delete](https://)


### Features Left to Implement

- Another feature idea

# Testing 


## Unit testing 

### Testing Forms

- UpdateUserProfileForm

- UserProfileForm

- UpdateUserForm

- DeleteAccountForm

| Syntax | Description |   |
| ----------- | ----------- |  ----------- |
| SignUpForm|  |  |
| | |   |
|  | | |

| Syntax | Description | Testing |
| ----------- | ----------- | ----------- |
| RSVP-form| the user can chose yes or no  <br> and the number of guests <br> and then click the RSVP button | The user can change thir response  <br> by changing their answer and number of guests  <br> and submit again | The users response gets sent  <br> to the database and appears in the admin panel|

## Testing other Features

### Buttons ### (not part of any form)

| Syntax | Description |
| ----------- | ----------- |
| Like-button | icon/button for liking and unliking posts | likes or unlikes the post when clicked and returns a Json response |
| Save-button | icon/button for saving and unsaving posts | Saves or unsaves the post to the profile and returns a Json response  |
| Save-button | icon/button for saving and unsaving posts | Saves or unsaves the post to the profile and returns a Json response  |

### Navbar & dropdowns
| Syntax | Description |
| ----------- | ----------- |
| First navbar| icon/button for liking and unliking posts | likes or unlikes the post when clicked and returns a Json response |
| Second navbar| icon/button for saving and unsaving posts | Saves or unsaves the post to the profile and returns a Json response  |
| Dropdowns | icon/button for saving and unsaving posts | Saves or unsaves the post to the profile and returns a Json response  |


## Lighthouse

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator]()
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator]()
- CI Python Linter [(https://pep8ci.herokuapp.com/)]()


### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

- I used the I Think Therefore I Blog walkthrough as a guide to get my project set up and get me started. And I refered back to it throughout the project.


### Content 

- The content for the posts and pages were generated with the help of AI.
- The icons used in the project were taken from [Font Awesome](https://fontawesome.com/)


- How to extend the Django user model:
[https://simpleisbetterthancomplex.com](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
-  Creating a like function:
[StackOverflow](https://stackoverflow.com/search?q=creating+a+like+function+in+Django)
-- Liking/unliking posts without refreshing the page
[StackOverflow](https://stackoverflow.com/questions/63081738/like-unlike-a-post-without-refreshing-the-page)

- Using Ajax with Django:
[StackOverflow](https://stackoverflow.com/questions/20306981/how-do-i-integrate-ajax-with-django-applications/20307569#20307569)
- Prevent default event:
[StackOverflow](https://stackoverflow.com/questions/7056669/how-to-prevent-default-event-handling-in-an-onclick-method)
- Let user delete their account:
[StackOverflow](https://stackoverflow.com/questions/54864355/django-user-account-delete-and-then-return-redirect-and-render)
(https://stackoverflow.com/questions/65510305/django-how-to-enable-users-to-delete-their-account)
(https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth)
- Overlay for frontpage:
 [Overlay](https://www.w3schools.com/howto/howto_css_overlay.asp)

 - Setting up email allAuth:
 [https://florianbgt.com/](https://florianbgt.com/posts/django_allauth_email_login)

### Media

- The logo and favicon was created by my husband.

- The images for posts, events and pages were downloaded from free imgaes on [Unsplash](https://unsplash.com/)

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

