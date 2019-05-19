import random
import re
import logging
import sample_model
import interact_model
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Waiting message
wait_msg = {1:'Please wait for my very good brain...', 2:'Working my good brain genes...', 3:'Generating my BS...', \
    4:'My father gave me a good brain with high IQ...', 5:'Coming up with the best words...'}

alphabet = 'abcdefghijklmnopqrstuvwxyzAEIOU'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Send a word or phrase as a primer to get rolling')

def echo(update, context):
    """Echo the user message."""
    # Waiting message
    update.message.reply_text(wait_msg[random.randint(1,len(wait_msg))])
    with open('primers.txt', 'a') as f:
        f.write(update.message.text+'\n')

    # Generate conditional sample
    reply = interact_model.interact_model(raw_text=(update.message.text))
    reply = ''.join(reply.split("<|endoftext|>"))

    # Remove remaining characters from partial <|endoftext|>
    reply = reply.split("<")[0].rstrip()

    # Fix ending (last char not punctuation, and last word not handle)
    while (reply[-1] not in '.!?$\"') and ('@' not in reply.split()[-1]) and ('#' not in reply.split()[-1]):
        reply = reply[:-1]

    # Fix punctuation (.!?)
    # Full stop
    stops = re.split(r'\.', reply)
    new_stops = [stops[0]]
    for sentence in stops[1:]:
        new_stops.append(' ' + sentence.lstrip())
    reply = '.'.join(new_stops)
    # Exclaimation mark
    exclaim = re.split(r'!', reply)
    new_exclaim = [exclaim[0]]
    for sentence in exclaim[1:]:
        new_exclaim.append(' ' + sentence.lstrip())
    reply = '.'.join(new_exclaim)
    # Question mark
    quest = re.split(r'\?', reply)
    new_quest = [quest[0]]
    for sentence in quest[1:]:
        new_quest.append(' ' + sentence.lstrip())
    reply = '.'.join(new_quest)

    # Add spelling error (50% chance). Random word, random letter, random insertion
    #if random.randint(1,2) == 1:    Try spelling error with every response
    word_list = reply.split()
    n = random.randint(0, len(word_list))
    word = list(word_list[n])
    word.insert(random.randint(1, len(word)), random.choice(alphabet))
    word_list[n] = ''.join(word)
    reply = ' '.join(word_list)

    # Reply user with response
    update.message.reply_text(update.message.text + reply)
    
    # Generate random sample
#    update.message.reply_text(sample_model.sample_model())
#    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("666218025:AAFOzCAxqnxwZcZsoq4P0kjPZrB-5UehMWA", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()