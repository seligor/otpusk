# otpusk
![Static Badge](https://img.shields.io/badge/seligor-otpusk-otpusk)
![GitHub top language](https://img.shields.io/github/languages/top/seligor/otpusk)


![image](https://github.com/user-attachments/assets/cb1e617a-7deb-48fc-8ca7-f070be742c0e)


Мини бот, который автоматически отвечает всем в личные сообщения о том, что я нахожусь в отпуске
По умолчанию он отвечает всем, кто напишет в личные сообщения. Игнорирует групповые чаты. 
Отправляет сообщение только арз в сутки. На случай перезапуска - запоминает кому отвечал в бд sqlite


## Для установки бота 
```
git clone https://github.com/seligor/otpusk.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

chmod 755 START.sh
chmod 755 start.sh
```
## Получение API ключей для работы бота

Перейдите на сайт my.telegram.org и войдите в систему, используя свой номер телефона.
Выберите "API development tools" и заполните форму для регистрации нового приложения.
Запишите api_id и api_hash и phone_number в файле main.py


START.sh - оснойной файл запуска. Однако я предпочитаю использовать screen. Поэтому start.sh запускает screen, создаёт именнованную сессию по имени директории откуда он запущен
после этого запускает SATRT.sh. 
Далее можно нажать Ctrl+a, Ctrl+d - это деаттачит вас отсессии. При этом она остаётся работать. Если требуется вернуться к сессии - просто запустите снова start.sh и если именованная сессия существует - вернётесь в неё. Если не существует - запустите бота. На мой взгляд удобное поведение. 
