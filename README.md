![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to the Retro Vinyl Store!

Bugs: 

Don't know if I imagined it since I can't find the reference again, but I was at first under the impression that it was a good idea to name the bucket in AWS
the same way as the heroku-app. Turns out that was a bad idea...when the bucket has a .com or another TLD component in the name, the deployed site complains about
the certificate not being valid and the site refuses to load say css-files or images stored in the bucket. Creating a duplicate bucket with another name solved
the issue.

Removed .vscode and sqlitebb

Couldn't get gmail working at first. It kept complaining about bad credentials when username and password was in env.py but worked fine when set explicitly
in settings.py. Not sure what the problem was, since the code looks the same now except now it works...

Some overflow issues that showed up on real mobile but wasn't visible in devtools

Products page looked too cramped when in two columns

Fullname did not show up in user-menu. Forgot to make sure fname and lname is set on all accounts. Fixed by making custom signup form

Custom signup form was hard to get the fields in the order I wanted them. 

The css to remove the bullet points from the li on the privacy page hit too wide. Fixed by altering the css

NOTES

Keep summernote / crispyforms in config for now. In case they will be needed. If not needed, remove at the end
Maybe remove popper js? Keep for now

.nu tld means now in Swedish so if the site were to be deployed live it would be on a .nu domain

fix border-end on index. Fixed by jquery
name standard for css/js files that are app-specific

Special deals - some sort of continues loading?

Comments

every html-comment in the templates are encapsulated within djano comment-tags to make them invisible when in view source. Not strictly necessary
but I like to do it that way because:
1. I can easily spot the comments because of the color coding in Vstudio
2. I can add comments there to remind me of something without having to worry about a curious end-user to see it.

Db

Moved some models to the products app

Moved custom class used as mixin to mixin.py in core app. All other apps imports it in view.py
Slightly breaks the idea that apps should be self-contained but keeps to the DRY philosophy better.
Apps are not all that selfcontained in an e-commerce django-site anyway

Apps:

Core: main-site
bag: shopping-bag
checkout: used by stripe
webauth: used by allauth - REMOVED
staff: used to provide admin-functionality for staff (update stock with new items for example)
about: credits and about-text

Credits:

lp-image  

Photo by <a href="https://unsplash.com/@ekrull?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Eric Krull</a> on <a href="https://unsplash.com/photos/black-vinyl-record-on-black-vinyl-record-fi3_lDi3qPE?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  