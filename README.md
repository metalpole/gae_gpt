# gce_gpt

Things tried:
1) Deployed telegram bot to Heroku. Realized that there is not enough space to load GPT-2.
2) Thought of putting the model on Google App Engine using Flask, and then let the telegram bot on Heroku communicate with it. Spent days trying to deploy on GAE before realizing that there is not enough memory as well.
3) After 5 days since I started, I am going to put everything on Google Compute Engine.