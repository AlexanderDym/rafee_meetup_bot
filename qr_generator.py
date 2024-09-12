import qrcode
import os
from qrcode.image.svg import SvgPathImage  # Для генерации SVG

# Название вашего Telegram бота
bot_name = 'trafee_meetup_bot'

# Список участников с уникальными токенами
participants = [
    {"name": "Kostiantyn Dotsenko", "token": "token_kostiantyn"},
    {"name": "Mariia", "token": "token_mariia"},
    {"name": "Joanna Marinova", "token": "token_joanna"},
    {"name": "Daiana", "token": "token_daiana_b"},
    {"name": "Daiana Imlive", "token": "token_daiana_imlive"},
    {"name": "Artem", "token": "token_artem"},
    {"name": "Anastasiia", "token": "token_anastasiia"},
    {"name": "Olga", "token": "token_olga"},
    {"name": "Sebastien BALESTAS", "token": "token_sebastien"},
    {"name": "Nikita", "token": "token_nikita"},
    {"name": "Anton", "token": "token_anton"},
    {"name": "Sasha", "token": "token_sasha"},
    {"name": "Shawn Herron", "token": "token_shawn"},
    {"name": "cybermike", "token": "token_cybermike"},
    {"name": "Vitaliy", "token": "token_vitaliy"},
    {"name": "Николай", "token": "token_nikolay"},
    {"name": "Vladyslav Haiduk", "token": "token_vladyslav"},
    {"name": "Slava", "token": "token_slava"},
    {"name": "Roman", "token": "token_roman"},
    {"name": "Tomáš Vítek", "token": "token_tomas"},
    {"name": "Pavel", "token": "token_pavel"},
    {"name": "Kira", "token": "token_kira"},
    {"name": "Snezhana Fed", "token": "token_snezhana"},
    {"name": "Maksym", "token": "token_maksym"},
    {"name": "Igor Aleksandrov", "token": "token_igor"},
    {"name": "Andrii Cherepanskyi", "token": "token_andrii"},
    {"name": "Nazar", "token": "token_nazar"},
    {"name": "Sebastian Prekop", "token": "token_sebastian"},
    {"name": "Tobias Andersen", "token": "token_tobias_andersen"},
    {"name": "Daria", "token": "token_daria"},
    {"name": "Kian Mir", "token": "token_kian"},
    {"name": "Alessandro Polidoro", "token": "token_alessandro"},
    {"name": "Tobias Andersen (Endorphina)", "token": "token_tobias_endorphina"},
    {"name": "Andrii", "token": "token_andrii_stat"},
    {"name": "Inna", "token": "token_inna"},
    {"name": "Muhammad Ulil Nuha", "token": "token_muhammad"},
    {"name": "Pentil_dawa", "token": "token_pentil"},
    {"name": "Sergey", "token": "token_sergey"},
    {"name": "Ilya", "token": "token_ilya"}
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
