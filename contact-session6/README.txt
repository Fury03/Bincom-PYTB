Session 6: host the multimedia website (contact-session5/multimedia_site) on GitHub and Heroku.

GitHub:
  cd contact-session5/multimedia_site
  git init && git add . && git commit -m "Multimedia website"
  (create an empty repo on github.com, then)
  git remote add origin <your-repo-url>
  git push -u origin main

Heroku:
  heroku login
  heroku create <app-name>
  heroku config:set SECRET_KEY=<any-long-random-string> DEBUG=False
  git push heroku main
  heroku run python manage.py migrate
  heroku open     <- this is the URL to submit
