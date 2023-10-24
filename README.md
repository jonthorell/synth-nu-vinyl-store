![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome to the Retro Vinyl Store!

Bug: Don't know if I imagined it since I can't find the reference again, but I was at first under the impression that it was a good idea to name the bucket in AWS
the same way as the heroku-app. Turns out that was a bad idea...when the bucket has a .com or another TLD component in the name, the deployed site complains about
the certificate not being valid and the site refuses to load say css-files or images stored in the bucket. Creating a duplicate bucket with another name solved
the issue.