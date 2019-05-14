@stablegeniusbot

**Deployment & Integration Progress:**
4th May 2019
- Deployed telegram bot to Heroku. Realized that there is not enough space to load GPT-2.
- Thought of putting the model on Google App Engine using Flask, and then let the telegram bot on Heroku communicate with it. Spent days struggling to deploy on GAE before realizing that there is not enough memory as well.

9th May 2019
- After 5 days since I started, I am going to put everything on Google Compute Engine. Apparently I can't be a cheapskate as the model itself is simply too big for the lite options. Learnt how to deploy a basic bot on GCE. Managed to integrate GPT-2's code with the bot to generate random samples.

12th May 2019
- Integrated script for conditional sample generation after debugging. User is now able to send text via telegram and receive a response generated based on the text.

13th May 2019
- Downloaded and combined Twitter data from 2009-2019. Did basic parsing/processing to get the texts of relevant tweets. Tried some fine-tuning.

14th May 2019
- Figured out how to do fine-tuning on Google Colab since there is a GPU there, then upload model checkpoints to Cloud Storage which can then be downloaded by Compute Engine VM instance.

**NLP Issues**
*3 avenues of tackling quality of generated text*
1) Clean up tweets dataset; remove undesirable elements
   - ~~Drop URLs, no RTs~~ (13/05/2019)
   - ~~Situation where too many twitter user handles are being generated in a single response. Remove tweets with more than 3 handles (1247 tweets)~~ (14/05/2019)
   - ~~Remove '[VIDEO]', 'Video'~~ (14/05/2019)
2) Remove undesirable elements while the model is still generating
3) Post-processing on generated text before sending response back to user
   - Preferable for response to have a proper ending/no sudden cutoff

*Currently 37525 tweets in dataset*

*Other stuff to consider*
1) Length of response (random or fixed)
2) Temperature, top_k