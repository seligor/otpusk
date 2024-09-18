# otpusk
Мини бот, который автоматически отвечает всем в личные сообщения о том, что я нахожусь в отпуске

Для установки бота 
```
git clone https://github.com/seligor/otpusk.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

chmod 755 START.sh
chmod 755 start.sh
```
Получение API ключей для работы бота

Перейдите на сайт my.telegram.org и войдите в систему, используя свой номер телефона.
Выберите "API development tools" и заполните форму для регистрации нового приложения.
Запишите api_id и api_hash и phone_number в файле main.py
