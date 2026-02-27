import re

def analyze_text(text):
    """
    Анализирует текст и возвращает словарь со статистикой.
    """
    # Проверка на пустую строку
    if not text or not text.strip():
        return {
            "word_count": 0,
            "unique_words": 0,
            "longest_word": ""
        }
    
    # Удаляем знаки препинания и получаем список слов
    words = re.findall(r'\b\w+\b', text)
    
    if not words:
        return {
            "word_count": 0,
            "unique_words": 0,
            "longest_word": ""
        }
    
    # Общее количество слов
    word_count = len(words)
    
    # Уникальные слова (без учёта регистра)
    words_lower = [word.lower() for word in words]
    unique_words = len(set(words_lower))
    
    # Самое длинное слово
    longest_word = max(words, key=len)
    
    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "longest_word": longest_word
    }


# Пример использования
if __name__ == "__main__":
    result = analyze_text("Привет, мир! Привет, чудесный мир программирования.")
    print(result)