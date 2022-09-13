import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

from vk_bot import VkBot

def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})

token = "cf5d67380d92cbb03a281daea7e4e25a18cbc2f72f58929cca00d89d15b54d9f1f5bbc54df26b6e863371"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)
print("Server started\n")

for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print("New message")
            print(f'For me by: {event.user_id}', end='')
            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
            print("Text: ", event.text)