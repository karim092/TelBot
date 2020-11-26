import telebot
from telebot.types import LabeledPrice, ShippingOption

token = '1088507126:AAF6k3_GIhAcClpMOzyTjtKSrFxMIuGI3Ow'
provider_token = '1234567890:TEST:AAAABBBBCCCCDDDD'  # @BotFather -> Bot Settings -> Payments
bot = telebot.TeleBot(token)

# More about Payments: https://core.telegram.org/bots/payments

prices = [LabeledPrice(label='Working Time Machine', amount=5950), LabeledPrice('Gift wrapping', 500)]

shipping_options = [
    ShippingOption(id='instant', title='WorldWide Teleporter').add_price(LabeledPrice('Teleporter', 1000)),
    ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]


@bot.message_handler(commands=['start'])
def command_start(message):
    bot.send_message(message.chat.id,
                     "Hello, I'm the demo merchant bot."
                     " I can sell you a Time Machine."
                     " Use /buy to order one, /terms for Terms and Conditions")

@bot.message_handler(commands=['buy'])
def command_pay(message):
    bot.send_message(message.chat.id,
                     "Real cards won't work with me, no money will be debited from your account."
                     " Use this test card number to pay for your Time Machine: `4242 4242 4242 4242`"
                     "\n\nThis is your demo invoice:", parse_mode='Markdown')
    bot.send_invoice(message.chat.id, title='Working Time Machine',
                     description='Want to visit your great-great-great-grandparents?'
                                 ' Make a fortune at the races?'
                                 ' Shake hands with Hammurabi and take a stroll in the Hanging Gardens?'
                                 ' Order our Working Time Machine today!',
                     provider_token='381764678:TEST:20843',
                     label='Гоба',
                     amount=50000,
                     currency='rub',
                     photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
                     photo_height=512,  # !=0/None or picture won't be shown
                     photo_width=512,
                     photo_size=512,
                     is_flexible=False,  # True If you need to set up Shipping Fee
                     prices=prices,
                     start_parameter='time-machine-example',
                     invoice_payload='HAPPY FRIDAYS COUPON')

bot.skip_pending = True
bot.polling(none_stop=True, interval=0)




