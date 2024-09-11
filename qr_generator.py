import qrcode
import os

# Название вашего Telegram бота
bot_name = 'trafee_meetup_bot'

# Список участников с уникальными токенами
participants = [
    {"name": "Maksym", "token": "unique_token_1"},
    {"name": "Nikita", "token": "unique_token_2"},
    {"name": "Solomia", "token": "unique_token_3"},
    {"name": "Anton", "token": "unique_token_4"},
    {"name": "Sasha", "token": "unique_token_5"}
]

# Папка для сохранения QR-кодов
output_dir = "./qrcodes/"
os.makedirs(output_dir, exist_ok=True)

# Функция для генерации QR-кодов
def generate_qr_code(link, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_path = os.path.join(output_dir, f"{filename}.png")
    img.save(img_path)
    print(f"QR-код для {filename} успешно сохранен по пути: {img_path}")

# Генерация уникальных ссылок и QR-кодов для каждого участника
for participant in participants:
    unique_link = f"https://t.me/{bot_name}?start={participant['token']}"
    print(f"Уникальная ссылка для {participant['name']}: {unique_link}")

    # Генерация QR-кода для уникальной ссылки
    generate_qr_code(unique_link, participant['name'])
