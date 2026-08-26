import flet as ft
import sqlite3

def init_db():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clicks (id INTEGER PRIMARY KEY, count INTEGER)")
    cursor.execute("INSERT OR IGNORE INTO clicks (id, count) VALUES (1, 0)")
    conn.commit()
    conn.close()

def get_count():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("SELECT count FROM clicks WHERE id = 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 0

def update_count(new_count):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clicks SET count = ? WHERE id = 1", (new_count,))
    conn.commit()
    conn.close()

def main(page: ft.Page):
    page.title = "Flet Test App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    init_db()
    current_count = get_count()

    count_text = ft.Text(value=f"تعداد کلیک: {current_count}", size=30, weight=ft.FontWeight.BOLD)

    def button_click(e):
        nonlocal current_count
        current_count += 1
        update_count(current_count)
        count_text.value = f"تعداد کلیک: {current_count}"
        page.update()

    page.add(
        ft.Text("تست بیلد اندروید با Flet", size=24),
        count_text,
        ft.Button("افزایش شمارنده و ذخیره در SQLite", on_click=button_click, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE)
    )

ft.app(target=main)
