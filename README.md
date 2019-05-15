# Check it out at _@stablegeniusbot_ on Telegram
*(Still in process of improving the quality of the responses)*

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
- Figured out how to do fine-tuning on Google Colab since there is a GPU there, then upload model checkpoints to Cloud Storage which can then be downloaded by Compute Engine VM instance. Learnt to bypass using Google Drive since it does not integrate well with GCP.

**NLP Issues/Stuff to make it better**
*3 avenues of tackling quality of generated text*
1) Clean up tweets dataset; remove undesirable elements
   - ~~Drop URLs, no RTs~~ (13/05/2019)
   - ~~Situation where too many twitter user handles are being generated in a single response. Remove tweets with more than 3 handles (1247 tweets)~~ (14/05/2019)
   - ~~Remove '[VIDEO]', 'Video'~~ (14/05/2019)
2) Remove undesirable elements or add additional tokens while the model is still generating
   - Modify generation script to check that final character is a punction or final word is a twitter handle (no abrupt end to text) 
3) Post-processing on generated text before sending response back to user
   - Make text responses more characteristic of the chief
   - Spelling errors
   - Full caps or capitalize first letter (Maybe not necessary, the model seems capable of reusing such words. Can try to randomly create my own)
   - Avoid repeated twitter handles
   - ~~Deal with <|endoftext|>~~ (15/05/2019)
   - Puncutation spacing errors
   - Drop incomplete sentence if too few words, or use it to continue generating a complete sentence and append to response. If 2 responses required, then maybe append "..." at end of first part

**Currently 37525 tweets in dataset**

**Latest model: 6.5 hrs, 7250 epochs, avg loss 1.35**

**Other stuff to consider**
*1) Length of response (random or fixed)*
*2) Temperature, top_k (find optimal, or allow user to change?)*
*3) Greater pool of hard-coded responses*
*4) Faster VM*
*5) Reduce training. 7250 epochs is definitely too much*

**What's next? _Trump_ with _Shakespeare_?!**

*Bot built using the sick [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library, deployed on Google Compute Engine. GPT-2 model released by [OpenAI](https://github.com/openai/gpt-2), scripts for retraining by [nshepperd](https://github.com/nshepperd/gpt-2), fine-tuned on Google Colab. Tweets archived by [bpb27](https://github.com/bpb27/trump_tweet_data_archive), original tweets created by [the stable genius](https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor).*