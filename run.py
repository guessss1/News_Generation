from typing import List
import openai
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

# Установите API-ключ OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


# Функция для взаимодействия с GPT
def ask_chatgpt(messages: List[dict]) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content


# Роль ассистента
prompt_role = '''Вы — ассистент для журналистов.
Ваша задача — писать статьи на основе ФАКТОВ, которые вам предоставлены.
Вы должны соблюдать указанные инструкции: ТОН, ДЛИНА и СТИЛЬ.
Ответ давайте на русском языке.'''


# Основная функция для помощи журналисту
def assist_journalist(
        facts: List[str],
        tone: str,
        length_words: int,
        style: str
) -> str:
    # Формируем факты и параметры запроса
    facts = ", ".join(facts)
    prompt = (f'{prompt_role}\nФАКТЫ: {facts}\n'
              f'ТОН: {tone}\n'
              f'ДЛИНА: {length_words} слов\n'
              f'СТИЛЬ: {style}')

    # Отправляем запрос в GPT
    return ask_chatgpt([{"role": "user", "content": prompt}])


# Пример вызова функции
if __name__ == "__main__":
    result = assist_journalist(
        ['Небо синее', 'Трава зелёная'],
        'неформальный', 100, 'блоговый стиль'
    )
    print(result)
