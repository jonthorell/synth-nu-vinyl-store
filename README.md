# Synth.Nu

The aim of this project to build an e-commerce site that aims to sell music on vinyl to lovers of a specific genre, namely synthmusic (and subgenres).

The .nu top-level-domain means now in Swedish so if the site were to be deployed live it would be on a .nu domain. So the name of the site is literally
Synth.now.

The site is by its nature B2C centered.

The project is live 
[here](https://synth-vinyls-e3c70f9ba271.herokuapp.com/)

![mockup-picture](https://synth-jt.s3.eu-north-1.amazonaws.com/static/images/readmes/01-landing-page.png?raw=true)

# Background and use-case

The site is for all intentents and purposes a fully working e-commerce site although limited in scale.
Customers can search for what they are interested in purchasing in a varierty of ways (full text search and drop-down menues
for example), add said products to a shopping bag (and remove if they change their mind), and fullfill the purchase with the
aid of stripe. If they want to, they can create an account for themselves although not mandatory. 

If they do create an account, they can provide shipping details and payment details in their profile so they don't have to
enter those details if they come back for another purchase.

If logged in, the site will provide the prices in the currency the customer choses. Otherwise it defaults to USD.

Staff-members can update stock, add new products, change descriptions, handle incoming questions from a contact-form and
similar tasks without having to use the django-admin site. The only thing django-admin is required for is to change
group-member ship of people (that is, if they should be considered staff or not).

The screen is divided into three parts.

At the top,

![navbar](https://synth-jt.s3.eu-north-1.amazonaws.com/static/images/readmes/02-header.png?raw=true)

Genre and Mediatype are drop-down menues showing the different genres (such as EBM, Synthpop) and mediatypes shows album, single, and
so on. Sort have a few pre-selected sort options, and more will be provided if you first select say a genre.

Contact will direct you to a contact-form, and everything sent in using that form will be logged in the database so customer
service can deal with the issue. About shows a short description of what the site is about as well as credits.

The rounded field on the right shows how much more you have to spend to get free shipping. The search field naturally lets
you search. The shopping cart is a link to view what is in your bag, and it also provides a visual clue of how many items
are already in it.

The padlock is the user-menu. It will look different depending on who is logged in (user can decide), and it provides
links to among other things login, logout, create account, delete account, manage stock (for staff).

The middle looks like this:

![middle-part](https://synth-jt.s3.eu-north-1.amazonaws.com/static/images/readmes/04-middle.png?raw=true)

Example picture shows how it looks when you've selected a genre, or in this case: all genres.

Apart from seach, everything happens on this part of the screen. Adding items to the bag, reviewing items, entering login-details
and so on. On some pages this part is more clearly divided into two columns (such as the landing page). In the example picture
above, it is not.

And finally, at the bottom. A footer with copyright information.

![footer](https://synth-jt.s3.eu-north-1.amazonaws.com/static/images/readmes/03-footer.png?raw=true)

# Design considerations (visual). CHANGE!

1. Colors and other graphical elements have been "stolen" or mimicked from AmigaOS as much as possible. 
2. The beachball at the top-left is a sort-of unofficial logo.
3. The grey background is the default background color of the GUI.
4. The navbar uses the same white as the AmigaOS menubar.
5. The black text is the default font-color.
6. The orange text comes from the "fuel-gauge" that indicates how full a disk is (from an earlier version of AmigaOS).
7. The black background and the blinking graphics on the 403 page is how the Amiga indicates it has run into a dead-end software failure.
8. The site should be fully responsive.

# Technologies used

1. HTML
2. CSS (with classes from MaterializeBootstrap as well as my own)
3. Javascript
4. Django
5. Python
6. Git (from within Visual Studio), pushed to GitHub. UserStories and Kanban board is also hosted at GitHub.
7. Postgres SQL
8. jQuery

# Design considerations (code)

1. Since it is a django-project, configuation is done in settings.py, forms.py, & urls.py
2. The project consists of several apps.
Core: main-site
bag: shopping-bag
checkout: used by stripe
staff: used to provide admin-functionality for staff (update stock with new items for example)
about: credits and about-text
Point one applies here as well.
3. The main code is in views.py and "scattered" in the django template files as well such as the articles_by_author file. In the latter case it stuff like this:
```django
{% if profile.user.is_active %}
{% endif %
```
4. The code also uses context processors to access variables and models across the site. This means the app are not completely abiding by the self-containment principle, but I decided
it was more important to stick to the DRY principle in order to make it easier to not forget making changes in several places if need be. Besides, it would be hard to stick to
self-containment in a site like this. With that I mean a checkout app will by necessity require a products app as well as a shopping bag app if you do not want to write the whole thing as a monolith.
4. Comments are used in both the python code and the template files. In the latter case, it is html-comments surrounded by the django comment-tags. The purpose for doing it twice is that the html-comment sticks out color-wise in the code editor and the django-tags make sure commens are not visible in view source. I like having them invisible there since it makes it more "safe" to keep notes formyself in the code while developing.
5. It uses a mix of class-based views and function-based, depending on what made most sense for the particular view. Helper-functins are function based.
6. Custom javascript and custom css classes used only in one app or even on just one page of an app are stored in separate files rather than in a generic script.js and style.css and
then "injected" into the template that needs it. The reason is to make it easier to locate the code in question should you need to change it, and lessen the risk of the "wrong"
class being applied.
7. In the folder synth (the project-level core-folder) contains a utils.py file. It contains some helper-classes that other apps are using. Those are imported in the core-site.
This is mainly due to those classes are pretty static and a way to organize the code so you don't have to see them unless you really need to. 

# Design considerations (user classes)

Every user belongs to one or more classes of user. This is implemented using django groups.

1. Admin. Or superusers. They can do anything.
2. Staff. Has the ability to maintain stock and so on.
3. Members. Used to provide a profile for the user. When someone sign up, they are automatically added to this group. If they need to be in another group (say editors) an admin has to add them there manually.
4. Anonymous users (or not logged in users). Can purchase but not provide testimonials.

# External APIs used

1. Stripe for payment processing
2. FreeCurrecnyAPI for online currecy conversion

# Deployment

All coding takes place in Visual Studio and regularily pushed to the repo at GitHub. There are some "hidden" environmental variables in a file called env.py that is excluded from git
pushes. Those variables are used when running locally. The variables in question are:

* DATABASE_URL
* SECRET_KEY
* DEVELOPMENT
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* STRIPE_WH_SECRET
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* CURRENCY_API_KEY

# Deployment to Heroku

In order to deploy something to Heroku, several steps needs to be taken care of.

This is taken for granted that the project is already hosted at GitHub.

Code changes are regularily pushed into that repository using either Visual Studio or the cli command git using:

1. git add .
2. git commit -m "commit message"
3. git push

The steps for deployment to Heroku are:

1. Create an account at Heroku.
2. Create an app in Heroku, with a unique name and a region
3. Under settings, create the same environment variables as above
4. Add an additional environment variable with the name PORT and value of 8000 as well as an USE_AWS variable set to True
5. Create an account at AWS
6. Create a bucket in the AWS account.
7. Follow the instructions in the aws.pdf to set correct rights on the bucket.
8. In your development environment, do: pip freeze > requirements.txt to add the requirements needed to build the project at heroku.
Things installed, if any, locally will be added to the requirements file, to make sure everything necessary will be available when deployed.
This might include things not necessarily referenced, but it will make sure the build will be complete.
9. Make sure there's a file named Procfile in the root of your repo with this line: web: web: gunicorn synth.wsgi
10. Under deployment, connect the github account to the heroku-account
11. Under deployment method, connect the app to the correct github repository
12. Decide if you want the deployment to be automatic or manual. That is a matter of preference. For now, I have opted to make it manual.

# Database design CHANGE!

Since the entire site is built around three apps, there is a possibility to use models in three different places.

App: FAQ

Uses one very simple model called __Terminology__. It has four fields (5 if you count the automatically created id/pk field).

* Name: Charfield, max 40 characters in length. Can not be blank and must be unique. It must be unique because it is used as a title in the display and I do not want to confuse the user with having the same name twice or more.
* Created_on: Datefield, is automatically filled in.
* Slug: filled automatically using the third-party django-autoslug package. In the end I ended up not using slugs to create more intuiative urls since I could not quite get it to work the way I wanted, but left the field if I want to extend the site later on.
* Description: Charfield, max length 3000, must not be empty. Used to provide the "meat" of the terminology so the user can get more information.

There are no relations to other models. Also, this particular model needs to be populated from django-admin.

The output of this model looks like this:



App: Credits

Does not use a model.

App: Retro

The main app, uses the following models:

The default django user-model

+the following (all uses the default id/pk field)

__Category__

* Name: Name of category. Charfield, max_length 40 and must be unique and not null
* Created_on: created by default with the current time-stamp
* Slug: see above regarding slugs
* Description: Description of the category. Max_length 200 (can be seen in all-categories boxes), must not be null
* Avatar: filename of category-image (can be seen in categories menu). Max-length 60, must not be null. File is pulled from static/categories

Does not refer to any other model, but others refer to this.

__Article__

* Category: refers to the id of category model so the article is linked to one category.
* Slug: see above regarding slugs
* Title: name of the article. Charfield, maxlength 60. Must not be null
* Content: main body of the article. Max length 200, must not be null and is linked to a summernote field
* updated_on/created_on: DateTimeField, updated automatically
* excerpt: short description of article. 
* status: published or not (integer). 1=published, which is the default
* user: refers to the id of the user in the usertable so the article is linked to one user (=owner)

Both user and category has on_delete CASCADE so if the user or category is deleted, so is the article

__Link__

* Name. Charfield, Name of the link, max_length 60, must be unique and not null
* Slug: see above regarding slugs
* URL: max length 255, must be unique and not null
* Description: Charfield, max length 255. Must not be null. A short description of the url.
* Alt: Charfield. Maxlength 255, not null. Provides the alt= text

Link model is self-contained and does not refer to any other models or is referred to one.

__Comment__

* Article. Refers to the article model to keep track of which article it is a comment on.
* Name. Refers to the user model to keep track of who wrote the comment
* Body. Textfield, maxlength 200. Can not be null
* Slug. See above regarding slugs
* Created_on: DateTimeField, updated automatically
* Approved. Boolean. Comments needs to be approved by an admin before they are visible so set to False automatically so admin needs to approve it.
* Status. Integer. Either 0 (not published, or invisible) or 1 (published and visible). 

Article and name are set on_delete CASCADE so if the article or user the comment belongs to is deleted, so is the comment

__Profile__

In django-admin, this one is not listed as a model on its own. Instead the fields show up if one clicks on a user. It is sort of an extension of the user model.

* Short_description. Charfield, maxlength 60. Not null.
* Description. Charfield, max 2000. Not null. Longer description. A biography if you will.
* updated on/created on. DateTimeField. Added automatically
* slug. See above regarding slugs.
* user. Refers to the id of the user in the user model.
* avatar. Charfield, maxlength 60. Not null. See under categories. Same principle, except the picture is fetched from static/avatars. Can be null in principle but gets a default on creation.
* conputer. Textfield, maxlength 400. A computer oriented site needs to let the user describe their setup, right?

User has on_delete CASCADE set so if user is deleted, so is the profile

# Bugs encountered and fixed
1. Navbar did not list genres for all pages at first. I had the same issue in the RetroLoversUnited project, but used a context-processor this time around instead of a mixin. This approach
has the added benefit that it also works on function-based views such as the ones for allauth
2. Problem finding a way of getting the group for the current user. The solution found is not as elegant as I would like, but it works.
3. Spacing issue between cover-image and the text on the product_details view. Fixed using custom css
4. Some layout issues in "Add to bag" form. Changing the css solved the issue.
5. Don't know if I imagined it since I can't find the reference again, but I was at first under the impression that it was a good idea to name the bucket in AWS
the same way as the heroku-app. Turns out that was a bad idea...when the bucket has a .com or another TLD component in the name, the deployed site complains about
the certificate not being valid and the site refuses to load say css-files or images stored in the bucket. Creating a duplicate bucket with another name solved
the issue.
6. The vertical line dividing the columns on the landing page made the page look weird on lower resoltions. Fixed by using jQuery to remove/add the classes based on the resolution.
7. Couldn't get the gmail integration working at first. It kept complaining about bad credentials when username and password was in env.py but worked fine when set explicitly
in settings.py. Not sure what the problem was, since the code looks the same now except now it works...I suspect some typo crept in somewhere.
8. Some overflow issues that showed up on real mobile but wasn't visible in devtools. Seems to work now, so I suspect it was a cached css-file that was the culprit.
9. Products page looked too cramped when in two columns. Fixed by removing some details and keeping that to the product_details page
10. Fullname did not show up in user-menu. Forgot to make sure fname and lname is set on all accounts. Fixed by making a custom signup form
11. Custom signup form was hard to get the fields in the order I wanted them. It took a while to find out you needed both the Meta class and field_order to make it work.
12.The css to remove the bullet points from the li on the privacy page hit too wide. Fixed by altering the css.
13. Update/remove links in bag did not work. Turned out it did not load the js-file correctly. Fixed.
14. Got a bunch of unbound errors when submitting the order into the database. I used the boutique ado code as a base but with some modifications. The problem was that in boutique ado the 
model was named Products (capital P) but mine is called products (lowercase P). Python and/or Django got confused by this:
```
order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                    )
```

The solution was to replace the variable product with the shortened prod.
15. The Add-staff link to menu did not work properly. Removed check if user is superuser. Superfluos since it is only the group membership that is important
16. The new image field in profile model introduced an error in profile-view. Fixed by altering the form.
17. Update in bag template should take current stock into consideration. Shouldn't be possible to add you want to buy 7 items if only 2 are in stock. Now prevented by some if-statements.
18. Stripe input box is not rendered?? Silly mistake with an underscore in the block where it was supposed to go.
19. Profile view showed an generic "server error" if you were not logged in. Fixed by wrapping it in a decorator so the error is more meaningful
20. When viewing bag-contents and one product does not contain an image, the site crashes with "The 'image' attribute has no file associated with it". The if-statement to check whether the product has an associated image was wrong.
21. The "Shop some more" text in the button should not be underlined. Fixed. It was missing a class.
22. The "sort by" needs to be styled to be more inline with the rest of the site. Fixed by applying the right classes.
23. The image field in the profile model is not being updated when a user tries to upload an image. The post method missed request.FILES, fixed.
24. The add product, edit product, add genre, and add news item only used the left column. Fixed by aligning the divs and their classes properly
25. Not necessarily a big bug but an annoyance. When viewing a past order, it still said thank you in the header which is not really appropriate. Fixed by adding a if-statement to check if the user comes from the profile or not
26. Accidentally used static instead of MEDIA_URL to access default avatar images in menu. Fixed
27. The ordernumber in the toast when successfully bought something flowed out of the toast on smaller devices such as mobile phones."Fixed" by removing that from the toast. The information is present in the page below anyway.
28. Toasts are kinda cramped on mobile. Rewrote how big they are to rectify that.
29. Text sometimes spilled out of the button on smaller resolutions. First noticed on the newsletter subscription form. Fixed by adding a no-overflow class that sets the property to hidden. Will be added to remaining buttons as well.
30. The buttons on top of the all products view got a strange layout on lower resolutions. Fixed by adding so they are stacked on those resolutions. A bit of a tradeof when that happens so there is no wasted screen real estate on larger resolutions. Settled for d-sm as the breaking point. Should be added elsewhere there are buttons present as well.


# Bugs encountered but not fixed yet

1. Search-field yields strange results if artist name contain space(s)
2. App-specific css-files refuses to work from the app's static/css folder. It does work for js though. Temporary workaround: keep css-files in the global static/css folder
9. About css file refuses to load from the correct app. Workaround: putting it in the core app
10. Webhooks do not work all the way. Money is being drawn but order not fulfilled if user closes the browser
11. Emails do not work from webhook
12. Right column on product_details is "cut off" on mobile.
13. Whenever a genre is added, the view to products becomes wrong. The reason is I am using a ?genre= construct to show the shortcut buttons from many links. Need to find a way to make that
more generic and work regardless of what genres are present in the db



# To Do

Update stock when an order has been completed
Staff view - in progress
Double check if I've understood webhooks. Should'nt an order be placed even if something goes wrong if the payment.intent succeeded?

Check everything!

# Things for the future

The newsletter works fine given its limited scope. It is perfectly possible to add oneself to the mailing list and remove oneself again. However, since it is a non-vital
part of the site (although nice to have) I decided to not implement checks to see if it is the right individual that has entered the adress. For a live site that would
of course not do. In such a case something like an e-mail being sent out to verify the intent at the very least would need to be in place. Just because there are no such
checks and that it is a non-vital part of the site, I decided that the newsletter functions will not send out any e-mails at this point. The only notification the user
will get is on the page itself.

# Testing

Testing has been done manually in selecting the different menu entries, trying to get an unauthorized user getting the possibility to edit something, and trying to get user
A to be able to edit/delete something belonging to user B, among other things. I have not been able to trigger errors
of that sort but get the proper error message as expected.

## Lighthouse

One Lighthouse screenshot per view. In All cases Lighthouse complains about missing explicit size-tags (not surprising since it is in a header.html that in turn is included in base.html). However,
the error is misleading. The width and height attributes are set using css-classes which lighthouse does not pick up upon.

Lighthouse also complains about things I can not do much about without re-rewriting the front-end framework that is being used (Materialize bootstrap).

In this example for instance.

![lighthouse-error](https://github.com/jonthorell/RetroLoversUnited/blob/main/static/images/readme-files/lighthouse/error-lh.PNG?raw=true)

The buttons are created on the fly by the classname added and the data-* fields needed for the class to work. In some cases there might be work-arounds for it, but not always.


As can be seen, the values from lighthouse are fairly consistant across the board. But see above for a partial explantion of what could potentially
lower the scores. Some of them are, as far as I can tell, out of my control at this point. I could have found out about those issues earler on and
found ways to fix it, but I did not spot the issues in time.


## HTML validation

The different pages have been validated through 

[validator](https://validator.w3.org)

In order to not get complaints about Django-tags, the "view source" output for every page has been pasted into the validator. 

I got the following result for the pages listed below (listed this way to make it more digestable).

## Manual Tests

1. Adding procuts to the bag and adjusting items already in the bag should only accept values between 1 and whatever is in stock. 
Expected behavior: it is impossible to add more items of a given product than is currently in stock.
This has been tested by checking that the up and down arrows next to the input fields stops when you've reaced the limits, and this has been done on multiple products. 
Also, if the user enters a number manually the site should throw an error saying there is not enough in stock. This has also been done on several products, and I have 
been unable to fool the site into adding more than what is possible. This does not apply to products that are out of stock since in that case you do not even get the 
form in the first place. Works as intended.

## Credit cards

Has been tested with these two fake credit cards

4000007520000008
4242424242424242

csv and expiredate can be anything

Those were used for successful orders.

These were used for testing specific use cases:
Generic decline	4000000000000002	card_declined	generic_decline
Insufficient funds decline	4000000000009995	card_declined	insufficient_funds
Lost card decline	4000000000009987	card_declined	lost_card
Stolen card decline	4000000000009979	card_declined	stolen_card
Expired card decline	4000000000000069	expired_card	n/a
Incorrect CVC decline	4000000000000127	incorrect_cvc	n/a
Processing error decline	4000000000000119	processing_error	n/a
Incorrect number decline	4242424242424241	incorrect_number	n/a
Exceeding velocity limit decline	4000000000006975	card_declined	card_velocity_exceeded

As well as 4000002760003184 to test 3D Secure