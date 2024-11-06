import tkinter as tk

result_file = 'clear_text.txt'

# Функція для видалення зайвих пробілів та збереження результату у файл
def clear_spaces():
    # Отримуємо текст з віджета Text
    text = text_widget.get("1.0", tk.END)
    # Видаляємо зайві пробіли
    cleared_text = ' '.join(text.split())

    # Записуємо очищений текст у файл
    with open(result_file, "w", encoding="utf-8") as file:
        file.write(cleared_text)

    # Оновлення Label з повідомленням про успішне збереження
    result_label.config(text=f"Текст очищено і збережено у {result_file}")

# Створення основного вікна
root = tk.Tk()
root.title("Очищення зайвих пробілів")
root.geometry("400x300")

# Додавання віджета Label
label = tk.Label(root, text="Введіть текст із зайвими пробілами:")
label.pack(pady=10)

# Додавання віджета Text
text_widget = tk.Text(root, width=40, height=10)
text_widget.pack(pady=10)

# Додавання кнопки для очищення пробілів
clear_button = tk.Button(root, text="Очистити пробіли", command=clear_spaces)
clear_button.pack(pady=10)

# Додавання Label для повідомлення про успіх
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()