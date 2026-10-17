import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# សូមជំនួស 'YOUR_BOT_TOKEN_HERE' ដោយ Token ដែលអ្នកទទួលបានពី BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(BOT_TOKEN)

# ដំណើរការនៅពេលអ្នកប្រើប្រាស់វាយបញ្ជា /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # បង្កើតផ្ទាំងប៊ូតុង
    markup = InlineKeyboardMarkup()
    
    # បង្កើតប៊ូតុង "1 គណនី"
    button_account = InlineKeyboardButton("👤 1 គណនី", callback_data='account_1')
    markup.add(button_account)
    
    # ផ្ញើសារស្វាគមន៍ភ្ជាប់ជាមួយប៊ូតុង
    bot.send_message(
        message.chat.id, 
        "សួស្តី! នេះជា Telegram Bot សម្រាប់គ្រប់គ្រង GitHub Runner របស់អ្នក។\nសូមជ្រើសរើសជម្រើសខាងក្រោម៖", 
        reply_markup=markup
    )

# ដំណើរការនៅពេលអ្នកប្រើប្រាស់ចុចលើប៊ូតុងណាមួយ
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'account_1':
        # បង្ហាញសារពេលចុចប៊ូតុងរួច
        bot.answer_callback_query(call.id, "អ្នកបានជ្រើសរើស 1 គណនី!")
        
        # ផ្ញើសារតបទៅកាន់ការជជែក (អ្នកអាចសរសេរកូដភ្ជាប់ទៅ GitHub API / Runner នៅទីនេះ)
        bot.send_message(
            call.message.chat.id, 
            "✅ កំពុងរៀបចំ និងដំណើរការទិន្នន័យសម្រាប់ 1 គណនី (GitHub Runner)..."
        )

if __name__ == '__main__':
    print("🤖 Bot កំពុងដំណើរការ...")
    bot.infinity_polling()
