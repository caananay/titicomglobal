ABOUT THE PROJECT:

Titicom Global Photography is a web app designed for a company selling photo and photography tools and blogging to their followers about photography.

TECHNOLOGIES USED:

The website was designed using the following technologies:

HTML: is used to build the webpages

Bootstrap and CSS: this was used for the page layout design, look and feel of the website.

Django: is a Python framework and was used to build the backend of the project, to link the frontend with the database.

Postgressql DB: is an SQL database, which has been used in this project to store the data.

APP FUNCTIONALITY:

1. BLOG
	a. Share blog post link via email
	b. if user is logged in user details are prepopulate in the share link form
	c. Pagination on the blog post list page
2. ESTORE
	a. User login required to purchase from store
	b. Cart provided for shopper
	c. logged in user details prepopulated on the purchase order form
	d. logged in user can review a product
3. PAYPAL
	a. payment on the estore is done with paypal 
4. AWS
	a. Serving STATIC and MEDIA files using AWS
	

TESTING:

The application was tested manually on the following internet browsers Chrome, safari, IE and Firefox using inspect to debug any errors on the code. The application was also tested on the following mobile devices ipad and an andriod mobile phone for responsiveness.

DEPLOYMENT:

The project was deployed using Heroku.

THIRD PARTY APPLICATIONS USED:

django-taggit app: To add tags to my blog posts I used the django-taggit app (https://django-taggit.readthedocs.io/en/latest/)

django-disqus: To add comments to blog posts I used the django-disqus app (https://django-disqus.readthedocs.io/en/latest/)

LESSONS LEARNED:

The following issues were encountered when developing and deploying the app.

1. Integrating Disqus to the app: 

Eventhough Disqus was integrated with the Titicom Global web app as taught in the lessons and after extensive research on the internet, incorporting all my findings and debugging. I was still unable to get it to work in my app.

2. Hiding Email settings:

For this project I have chosen to create a dummy email account to use as the email settings, so that the app can send email notifications to a user. The email settings are in the settings.py file

However, if this were to be used for a real company, there would be a need to mask the email settings to prevent unauthorised access. One way to achieve this is to put the settings in a separate file, e.g. secret_settings.py that will be in .gitignore, and then in the main settings file do `import * from secret_settings.py`. This means that one can create the *secret_settings.py* file with the real values, and then add it to gitignore. This will allow you to then make any changes you'd like to the file locally (and on heroku), without them being noticed by git if pushed to github.
