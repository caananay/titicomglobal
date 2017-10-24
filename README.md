[About the project](#about-the-project)
[Technologies used](#technologies-used)
[APP Functionality](#app-Functionality)
[Testing](#testing)
[Deployment](#deployment)
[Third Party Applications Used](#third-party-applications-used)
[Lessons Learned](#lessons-learned)

### ABOUT THE PROJECT:

Titicom Global Photography is a web app designed for a company selling photo and photography tools and blogging to their followers about photography.

### TECHNOLOGIES USED:

   The website was designed using the following technologies:

   *HTML*: is used to build the webpages

   *Bootstrap and CSS*: this was used for the page layout design, look and feel of the website.

   *Django*: is a Python framework and was used to build the backend of the project, to link the frontend with the database.

   *Postgressql DB*: is an SQL database, which has been used in this project to store the data.

### APP FUNCTIONALITY:

1. BLOG
	* Share blog post link via email
	* if user is logged in user details are prepopulate in the share link form (but hidden from user)
	* Pagination on the blog post list page
	* Comment using DISQUS
2. ESTORE
	* User login required to purchase from store
	* Cart provided for shopper
	* logged in user details prepopulated on the purchase order form
	* logged in user can review a product
	* email sent to user when a purchase is successful
	* Admin can download pdf files from orders interface
3. PAYPAL
	* payment on the estore is done with paypal 
4. AWS
	* Serving STATIC and MEDIA files using AWS
5. Flatpages
	* Terms page
	* Policy page
	

### TESTING:

   The application was tested manually on the following internet browsers Chrome, safari, IE and Firefox using inspect, heroku logs, Pycharm, command prompt to debug any errors on the code. The application was also tested on the following mobile devices ipad and an andriod mobile phone (samsung note3) for responsiveness.

#### TEST SCENERIOS:
   A visitor is defined as a person is not registered on the website or logged on to the website.

   1. A visitor to the site should be able to register, and once registered are automatically logged on to the website.

   2. A registered user should be able to log on and log off to the website at any time.

   3. A visitor to the website is redirected to a log in page at the point of checkout from the estore.

   4. A user of the website can share a blog post with anybody by clicking on the share post button of a post.

   5. A logged on user can pay for items at checkout using paypal. 

   6. A user can comment on a blog post using DISQUS.

   7. A logged on user can review a product in the estore.

   8. Static and media files used by the website must be available and visible to the user at all times. AWS was used to make this possible on heroku.

   9. Logged in user details such as name and email address are persisted on share blog post, checkout and product review page and are subsequently stored on the database if form is submitted.

   10. Footer must remain at bottom of page regardless of the length of the page.

   11. No footer on home page.

   12. Responsiveness of website across some devices (laptops, ipad and samsung note3) and major browsers.

   13. Collapsible navigation menu on mobile devices.

### DEPLOYMENT:

   The project was deployed using Heroku.

### THIRD PARTY APPLICATIONS USED:

   [django-taggit app:](https://django-taggit.readthedocs.io/en/latest/) To add tags to my blog posts I used the django-taggit app 

   [DISQUS:](www.disqus.com) for adding comments to the blog posts

### LESSONS LEARNED:

The following issues were encountered when developing and deploying the app.

1. Integrating Disqus to the app: 

   Eventhough Disqus was integrated with the Titicom Global web app as taught in the lessons and after extensive research on the internet, incorporting all my findings and debugging. I was still unable to get it to work in my app. Eventually, I had to implement the disqus code directly into my website and it worked.

2. Hiding Email/AWS settings:

   Initially, I tried to mask the settings from public view by creating a separate file named 'secret_keys.py' which held both settings and putting the file in the gitignore file.  so that when pushing to github the file would be excluded. Then I removed the file from gitignore and pushed to heroku. However, at some point during the push back and forth to github and heroku, the file ended up being exposed on github.

   To address this issue, I have put these settings on heroku config vars settings and I call these variables from my settings file. This way the sensitive information is not exposed on the web.

3. Issues serving MEDIA and STATIC files from Heroku

   Using Amazon Web Services AWS for serving MEDIA and STATIC files
