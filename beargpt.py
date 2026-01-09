# beargpt.py
import requests
import time
import sys

class BearGPT:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.chat_id = None
        
    def _print_slow(self, text, speed=0.008):
        """Красивая печать текста"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()
    
    def _create_chat(self, chat_name):
        """Создает чат и возвращает его ID"""
        response = self.session.post(
            "https://hm337566.webhm.pro/ai/beargpt/api.php",
            json={"action": "create_chat", "message": chat_name}
        )
        data = response.json()
        if data.get('success'):
            return data['chat_id']
        return None
    
    def start(self, language='ru'):
        """Запускает чат на указанном языке"""
        
        # Тексты на разных языках
        texts = {
            'ru': {
                'name_prompt': "🎯 Название чата: ",
                'created': "✅ Чат создан! Готов к общению.",
                'your_turn': "👤 Вы: ",
                'ai_name': "🤖 ",
                'exit_commands': ['выход', 'exit'],
                'bye': "👋 До свидания!",
                'error': "❌ Ошибка: ",
                'empty': "Сообщение не может быть пустым"
            },
            'en': {
                'name_prompt': "🎯 Chat name: ",
                'created': "✅ Chat created! Ready to chat.",
                'your_turn': "👤 You: ",
                'ai_name': "🤖 ",
                'exit_commands': ['exit', 'quit'],
                'bye': "👋 Goodbye!",
                'error': "❌ Error: ",
                'empty': "Message cannot be empty"
            }
        }
        
        # Выбираем тексты для текущего языка
        t = texts.get(language, texts['ru'])
        
        # Создаем чат
        self._print_slow(t['name_prompt'], 0.02)
        chat_name = input().strip()
        if not chat_name:
            chat_name = "Мой чат" if language == 'ru' else "My Chat"
        
        self.chat_id = self._create_chat(chat_name)
        if not self.chat_id:
            print(t['error'] + "Failed to create chat")
            return
        
        self._print_slow(t['created'] + f"\n", 0.02)
        
        # Цикл общения
        while True:
            try:
                # Ввод пользователя
                user_input = input("\n" + t['your_turn']).strip()
                
                # Проверка на выход
                if user_input.lower() in t['exit_commands']:
                    self._print_slow("\n" + t['bye'], 0.02)
                    break
                
                # Проверка пустого сообщения
                if not user_input:
                    print(t['empty'])
                    continue
                
                # Отправка сообщения
                response = self.session.post(
                    "https://hm337566.webhm.pro/ai/beargpt/api.php",
                    json={
                        "action": "send_message",
                        "chat_id": self.chat_id,
                        "message": user_input
                    }
                )
                
                data = response.json()
                
                # Вывод ответа
                if data.get('success'):
                    print("\n" + t['ai_name'], end="")
                    self._print_slow(data['response'].strip(), 0.008)
                else:
                    self._print_slow(t['error'] + data.get('error', 'Unknown error'), 0.02)
                    
            except KeyboardInterrupt:
                self._print_slow("\n\n" + t['bye'], 0.02)
                break
            except Exception as e:
                self._print_slow(t['error'] + str(e), 0.02)

# Функция для импорта
def start(language='ru'):
    """Запускает BearGPT чат на указанном языке
    
    Args:
        language (str): 'ru' для русского, 'en' для английского
    """
    gpt = BearGPT()
    gpt.start(language)

# Если файл запущен напрямую
if __name__ == "__main__":
    # По умолчанию русский, но можно передать язык как аргумент
    import argparse
    
    parser = argparse.ArgumentParser(description='BearGPT Chat Client')
    parser.add_argument('--lang', '-l', default='ru', choices=['ru', 'en'], 
                       help='Language: ru (Russian) or en (English)')
    
    args = parser.parse_args()
    start(args.lang)