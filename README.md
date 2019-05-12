# gce_gpt

Things tried:
4th May 2019
- Deployed telegram bot to Heroku. Realized that there is not enough space to load GPT-2.
- Thought of putting the model on Google App Engine using Flask, and then let the telegram bot on Heroku communicate with it. Spent days trying to deploy on GAE before realizing that there is not enough memory as well.

9th May 2019
- After 5 days since I started, I am going to put everything on Google Compute Engine. Learnt how to deploy a basic bot on GCE. Managed to integrate GPT-2's code with the bot to generate random samples.

12th May 2019
- Integrated script for conditional sample generation after debugging. User is now able to send text via telegram and receive a response generated based on the text.

