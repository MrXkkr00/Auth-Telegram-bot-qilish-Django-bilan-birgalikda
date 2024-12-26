from django.core.management import BaseCommand
import telebot
import environs
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from ...utils import generate_code
from django.core.cache import cache
# Initialize the environment variables
env = environs.Env()
env.read_env()

# Read environment variables
DEBUG = env.bool("DEBUG", default=False)
TOKEN = env.str('TOKEN')

# Initialize the Telegram bot
bot = telebot.TeleBot(token=TOKEN)


class Command(BaseCommand):
    help = "Run the Telegram bot"  # Description for the management command

    def handle(self, *args, **options):
        self.stdout.write("Starting the Telegram bot...")
        try:
            bot.infinity_polling()  # Keep the bot running
        except KeyboardInterrupt:
            self.stdout.write("\nBot stopped manually.")
        except Exception as e:
            self.stderr.write(f"An error occurred: {e}")

def get_contact_button():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    contact = KeyboardButton(text='Kontactni yuborish', request_contact=True)
    button.add(contact)
    return button


# Define message handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = (f"Salom rasmiy botga hush kelib siz\n"
           f"Kontaktingizni yuboring")
    bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=get_contact_button())


@bot.message_handler(content_types=['contact'])
def contact_def(message):
    if message.from_user.id == message.contact.user_id:
        code = generate_code()
        user_id = message.from_user.id
        cache.set(code,user_id, timeout=60)
        msg = (f'Sizning Codingiz: \n'
               f'{code}')
        bot.send_message(message.chat.id, msg, reply_markup=ReplyKeyboardRemove())
        bot.send_message(message.chat.id,f"Yangi code olish uchun \login ni boshing")

    else:
        bot.send_message(message.chat.id, f"O'zingiz kantaktingizni yuboring")


#+ 1) /start (Kontact yuboradi) +

#+ 2) send kontact (Tekshiradi shahsiy yoki yo'q) +

#+ 3)send kod (cashga saqlaydi ) +

# 4.Create API, codni olib saqlaydi va user yaratadi

# 5)Generate token (access, refresh)

# 6)
