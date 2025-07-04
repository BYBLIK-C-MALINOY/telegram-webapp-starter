import mysql.connector
from fpdf import FPDF

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="bot_db_local"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT category_name, category_description FROM `categories`")
    data = cursor.fetchall()
    conn.close()
    return data


def create_pdf(data, filename="export.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font(fname='DejaVuSans.ttf')
    pdf.set_font('DejaVuSans', size=14)
    pdf.set_text_shaping(True)


    pdf.cell(0, 10, "Экспорт данных из SQL", align="C")

    for row in data:
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln() 

    pdf.output(filename)
    return filename

from telegram import Bot
import os
import logging
import asyncio
from typing import Optional

from pdf import fetch_data, create_pdf  

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def send_pdf(chat_id: str, bot_token: str) -> None:
    bot = Bot(token=bot_token)
    pdf_path: Optional[str] = None  
    try:
        data = fetch_data()
        pdf_path = create_pdf(data)

        with open(pdf_path, "rb") as file:
            await bot.send_document(
                chat_id=chat_id, 
                document=file,
                caption="Ваш PDF файл готов! Вот результаты:"  
            )
        logger.info("PDF успешно отправлен!")

    except FileNotFoundError:
        logger.error("PDF файл не найден!")
        await bot.send_message(chat_id=chat_id, text="Ошибка: не удалось создать PDF файл")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        await bot.send_message(chat_id=chat_id, text=f"Ошибка: {e}")
    finally:
        if pdf_path and os.path.exists(pdf_path):
            os.remove(pdf_path)
            logger.info("Временный PDF файл удален")

async def main():
    await send_pdf(
        chat_id="@Dashatru_bot",  
        bot_token="8140513380:AAHTFVRAMc-38YiCBVk13yD4VMITTmIhwaU"        
    )

if __name__ == "__main__":
    asyncio.run(main())

    data = fetch_data()
if not data:
    raise ValueError("No data fetched")

pdf_path = create_pdf(data)
if not os.path.exists(pdf_path):
    raise FileNotFoundError("PDF was not created")
logger.info(f"Fetched data: {type(data)}, length: {len(data) if hasattr(data, '__len__') else 'N/A'}")
logger.info(f"PDF created at: {pdf_path}")