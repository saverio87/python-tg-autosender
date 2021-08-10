import os
import time
import socks
import credentials
import random
from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeVideo
from telethon.tl.types import Chat


# Remember to use your own values from my.telegram.org!
client = TelegramClient('anon', credentials.api_id, credentials.api_hash, proxy=(
    socks.SOCKS5, '127.0.0.1', 7890))

prod = False


async def send_template_a(chat):

    if prod:
        try:
            await client.send_message(chat, "What's up")
        except:
            pass

        # Template for sending media:
        # await client.send_file(username, 'media/namefile.jpg', attributes=(DocumentAttributeVideo(0, 0, 0),))

    else:
        print('send_template_b ad_1')


async def send_template_b(chat):

    if prod:
        try:
            await client.send_message(chat, "I'm gay")
        except:
            pass

        # Template for sending media:
        # await client.send_file(username, 'media/namefile.jpg', attributes=(DocumentAttributeVideo(0, 0, 0),))
    else:
        print('send_template_b ad_2')


async def send_template_c(chat):

    if prod:
        try:
            await client.send_message(chat, "I got rekt")
        except:
            pass

        # Template for sending media:
        # await client.send_file(username, 'media/namefile.jpg', attributes=(DocumentAttributeVideo(0, 0, 0),))

    else:
        print('send_template_b ad_3')

templates = {'message_1': send_template_a,
             'message_2': send_template_b, 'message_3': send_template_c}
templatesList = list(templates)


async def main():

    print("Starting")

    chats = await client.get_dialogs()
    for chat in chats:
        # We only want to send messages to groups
        if isinstance(chat.entity, Chat):

            templateKey = templatesList[random.randrange(
                0, len(templatesList))]
            start_time = time.time()
            print('- Sending', templateKey, 'to group id ',
                  chat.entity.id, " - ", chat.entity.title)
            template = templates[templateKey]

            try:
                await template(chat)
                print('- Sent success, sleep a while')
                time.sleep(5)
                end_time = round(time.time() - start_time, 2)
                print('- Sent success in ' + str(end_time) + ' seconds')
            except Exception as e:
                print('- Sent failed, bummer', chat.id, "Error: ", e)
                templateKey = 'error'


with client:
    client.loop.run_until_complete(main())
