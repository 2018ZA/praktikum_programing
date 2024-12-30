import tkinter as tk
from math import cos, sin, pi

# Создаем главное окно
root = tk.Tk()
root.title("Окружность с движущейся точкой")

# Устанавливаем размер окна
canvas_width = 600
canvas_height = 600
root.geometry(f"{canvas_width}x{canvas_height}")

# Создаем холст для рисования
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Координаты центра круга
center_x = canvas_width // 2
center_y = canvas_height // 2

# Радиус окружности
radius = 200

# Функция для анимации точки
def animate_point():
    global angle, direction
    
    # Удаляем старую точку
    canvas.delete(point_id)
    
    # Рассчитываем новые координаты точки
    x = center_x + radius * cos(angle)
    y = center_y + radius * sin(angle)
    
    # Рисуем новую точку
    point_id = canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red", outline="black")
    
    # Обновляем угол
    angle += direction * 0.01
    
    # Повторяем анимацию через 10 мс
    root.after(10, animate_point)

# Начальный угол и направление вращения
angle = 0
direction = 1  # 1 - по часовой стрелке, -1 - против часовой стрелки

# Переменная для хранения идентификатора точки
point_id = None

# Рисуем окружность
canvas.create_oval(center_x - radius, center_y - radius,
                   center_x + radius, center_y + radius,
                   outline="blue", width=2)

# Запускаем анимацию
animate_point()

# Запуск главного цикла
root.mainloop()
