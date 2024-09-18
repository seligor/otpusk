import sqlite3
from telethon import TelegramClient, events
from datetime import datetime, timedelta


phone_number = 'XXXXXXXXXXX'
api_id='XXXXXXXX'
api_hash='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'



client = TelegramClient('session_name', api_id, api_hash)

conn = sqlite3.connect('responses.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS responses (user_id INTEGER PRIMARY KEY, last_response_time TEXT)''')
conn.commit()

last_response_time = {}
# указываем user_id, которым не нужно отвечать
excluded_users = {XXXXXXXXXX, XXXXXXXXXX}

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        user_id = event.sender_id
        print(f'user id is: {user_id}')
        if user_id in excluded_users:
            return
        current_time = datetime.now()

        c.execute('SELECT last_response_time FROM responses WHERE user_id = ?', (user_id,))
        row = c.fetchone()
        if row:
            last_time = datetime.fromisoformat(row[0])
#дельта времени(как часто напоминать о том, что я в отпуске, если с первого раза человек не понял
            if current_time - last_time < timedelta(days=1):
                print(f"Мы уже отвечали господину {user_id} в {last_time}")
                return
#текст сообщения, которым нужно отывечать
        await event.reply('Добрый день. С 16.09 по 29.09 я нахожусь в отпуске.')
        c.execute('INSERT OR REPLACE INTO responses (user_id, last_response_time) VALUES (?, ?)', (user_id, current_time.isoformat()))
        conn.commit()


async def main():
    await client.start(phone=phone_number)
    print("Бот запущен. Нажмите Ctrl+C для остановки.")

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
