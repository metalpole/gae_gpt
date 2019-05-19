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

19th May 2019
- BOOSTED DATASET WITH TRANSCRIPTS OF HIS SPEECHES FROM 2016 CAMPAIGN

**Stuff to make it better**
1) Clean up tweets dataset; remove undesirable elements
   - ~~Drop URLs, no RTs~~ (13/05/2019)
   - ~~Situation where too many twitter user handles are being generated in a single response. Remove tweets with more than 2 handles (1247 tweets)~~ (14/05/2019)
   - ~~Remove '[VIDEO]', 'Video'~~ (14/05/2019)
   - ~~Remove tweets for event announcements with words like 'join', 'tomorrow', 'Tune', '#MakeAmericaGreatAgain, 'Just arrive'; they are clearly not written by him~~ (18/05/2019)
   - ~~Remove tweets from iPhone with 'Thank you'~~ (18/05/2019)
   - ~~Remove manual retweets. They start with the user handle of the person he's retweeting, followed by @realdonaldtrump~~ (18/05/2019)
   - Remove tweets from [iPhone](http://varianceexplained.org/r/trump-tweets/). Apparently he only writes his more hyperbolic ones from Android. They are also more likely to contain just his words, with no links or hashtags. The iPhone is also clearly responsible for event announcements. 
   *Update: I think this might not be applicable in the more recent years, since I can easily spot nonsense coming from an iPhone source. Maybe only remove iPhone tweets from before he became president since the article only analyzes tweets till 2016. Apparently, the iPhone tweets only started in 2014, and seem to be purely used by a staff. Since 2016, I think it's not as easy to separate the tweets based purely on the source alone.*
2) Post-processing on generated text before sending response back to user
   - ~~Spelling errors~~ (19/05/2019)
   - Random/full caps
   - ~~Avoid repeated twitter handles~~ (18/05/2019)
   - ~~Deal with <|endoftext|>~~ (15/05/2019)
   - ~~Puncutation spacing errors~~ (19/05/2019)
   - ~~End response properly~~ (19/05/2019)
3) Added new data from 2016 campaign speeches MAJOR BOOST (19/05/2019)

**Currently 20952 tweets in dataset. Didn't count for transcripts, but it's a major addition.**

**Latest model: 1015 epochs**

**Other stuff to consider**
1) Length of response
2) Temperature, top_k
3) Greater pool of hard-coded responses
4) Faster VM
5) Training epochs

**What's next? _Trump_ with _Shakespeare_?!**

*Bot built using the sick [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library, deployed on Google Compute Engine. GPT-2 model released by [OpenAI](https://github.com/openai/gpt-2), scripts for retraining by [nshepperd](https://github.com/nshepperd/gpt-2), fine-tuned on Google Colab. Tweets archived by [bpb27](https://github.com/bpb27/trump_tweet_data_archive), original tweets created by [the stable genius](https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor). Speech transcripts from [ryanmcdermott repo](https://github.com/ryanmcdermott/trump-speeches).*