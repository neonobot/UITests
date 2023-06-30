import os

import requests

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"


def send_message():
    chat_id = "-1001936386729"
    total_tests = os.environ.get('TOTAL_TESTS', 'N/A')
    passed_tests = os.environ.get('PASSED_TESTS', 'N/A')
    failed_tests = os.environ.get('FAILED_TESTS', 'N/A')
    skipped_tests = os.environ.get('SKIPPED_TESTS', 'N/A')
    allure_report = os.environ.get('Allure Report', 'N/A')

    message = f"Результаты выполнения UI тестов:\n" \
              f"Всего тестов: {total_tests}\n" \
              f"Пройдено: {passed_tests}\n" \
              f"Провалено: {failed_tests}\n" \
              f"Пропущено: {skipped_tests}\n" \
              f"Отчет: {allure_report}"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, params=payload)
    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения:", response.status_code)


send_message()
