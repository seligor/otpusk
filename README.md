# otpusk
![Static Badge](https://img.shields.io/badge/seligor-otpusk-otpusk)
![GitHub top language](https://img.shields.io/github/languages/top/seligor/otpusk)
![GitHub issues](https://img.shields.io/github/issues/seligor/otpusk)

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

__Перейдите на сайт my.telegram.org и войдите в систему, используя свой номер телефона.__

__Выберите "API development tools" и заполните форму для регистрации нового приложения.__

__Запишите api_id и api_hash и phone_number в файле main.py__


_START.sh_ - оснойной файл запуска. Однако я предпочитаю использовать screen. Поэтому _start.sh_ запускает screen, создаёт именнованную сессию по имени директории откуда он запущен
после этого запускает _SATRT.sh_. 
Далее можно нажать _Ctrl+a_, _Ctrl+d_ - это деаттачит вас отсессии. При этом она остаётся работать. Если требуется вернуться к сессии - просто запустите снова _start.sh_ и если именованная сессия существует - вернётесь в неё. Если не существует - запустите бота. На мой взгляд удобное поведение. 
