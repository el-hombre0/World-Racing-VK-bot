import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

token = "cf5d67380d92cbb03a281daea7e4e25a18cbc2f72f58929cca00d89d15b54d9f1f5bbc54df26b6e863371"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)

for event in longpoll.listen():

    if