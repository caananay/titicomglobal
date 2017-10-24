##ABOUT THE PROJECT:

Titicom Global Photography is a web app designed for a company selling photo and photography tools and blogging to their followers about photography.

##TECHNOLOGIES USED:

The website was designed using the following technologies:

HTML: is used to build the webpages

Bootstrap and CSS: this was used for the page layout design, look and feel of the website.

Django: is a Python framework and was used to build the backend of the project, to link the frontend with the database.

Postgressql DB: is an SQL database, which has been used in this project to store the data.

##APP FUNCTIONALITY:

1. BLOG
	a. Share blog post link via email
	b. if user is logged in user details are prepopulate in the share link form (but hidden from user)
	c. Pagination on the blog post list page
	d. Comment using DISQUS
2. ESTORE
	a. User login required to purchase from store
	b. Cart provided for shopper
	c. logged in user details prepopulated on the purchase order form
	d. logged in user can review a product
	e. email sent to user when a purchase is successful
	f. Admin can download pdf files from orders interface
3. PAYPAL
	a. payment on the estore is done with paypal 
4. AWS
	a. Serving STATIC and MEDIA files using AWS
5. Flatpages
	a. Terms page
	b. Policy page
	

##TESTING:

   The application was tested manually on the following internet browsers Chrome, safari, IE and Firefox using inspect, heroku logs, Pycharm, command prompt to debug any errors on the code. The application was also tested on the following mobile devices ipad and an andriod mobile phone (samsung note3) for responsiveness.

##DEPLOYMENT:

   The project was deployed using Heroku.

##THIRD PARTY APPLICATIONS USED:

*django-taggit app: To add tags to my blog posts I used the django-taggit app (https://django-taggit.readthedocs.io/en/latest/)

*DISQUS: for adding comments to the blog posts

##LESSONS LEARNED/DEBUGGING:

The following issues were encountered when developing and deploying the app.

1. Integrating Disqus to the app: 

   Eventhough Disqus was integrated with the Titicom Global web app as taught in the lessons and after extensive research on the internet, incorporting all my findings and debugging. I was still unable to get it to work in my app. Eventually, I had to implement the disqus code directly into my website and it worked.

2. Hiding Email/AWS settings:

   Initially, I tried to mask the settings from public view by creating a separate file named 'secret_keys.py' which held both settings and putting the file in the gitignore file.  so that when pushing to github the file would be excluded. Then I removed the file from gitignore and pushed to heroku. However, at some point during the push back and forth to github and heroku, the file ended up being exposed on github.

   To address this issue, I have put these settings on heroku config vars settings and I call these variables from my settings file. This way the sensitive information is not exposed on the web.

3. Issues serving MEDIA and STATIC files from Heroku

   Using Amazon Web Services AWS for serving MEDIA and STATIC files
