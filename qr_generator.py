import qrcode
import os
from qrcode.image.svg import SvgPathImage  # Для генерации SVG

# Название вашего Telegram бота
bot_name = 'trafee_meetup_bot'

# Список участников с уникальными токенами
participants = [
    {"name": "Igor Ivanovski", "token": "token_igor_ivanovski"},
    
]

# Папка для сохранения QR-кодов
output_dir = "./qrcodes/"
os.makedirs(output_dir, exist_ok=True)

# Функция для генерации QR-кодов в формате SVG
def generate_qr_code(link, filename):
    # Создаем QR-код
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    # Генерируем SVG изображение QR-кода
    img = qr.make_image(image_factory=SvgPathImage)

    # Сохраняем изображение в формате SVG
    img_path = os.path.join(output_dir, f"{filename}.svg")
    with open(img_path, "wb") as f:
        img.save(f)
    print(f"QR-код для {filename} успешно сохранен в формате SVG по пути: {img_path}")

# Генерация уникальных ссылок и QR-кодов для каждого участника
for participant in participants:
    unique_link = f"https://t.me/{bot_name}?start={participant['token']}"
    print(f"Уникальная ссылка для {participant['name']}: {unique_link}")

    # Генерация QR-кода для уникальной ссылки в формате SVG
    generate_qr_code(unique_link, participant['name'])
