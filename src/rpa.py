import pyautogui
import time
import pyperclip


def rpa_rename(filepath, filename, page_number):
    """
    Opens, renames and saves the file.
    """
    pyautogui.PAUSE = 1
    try:
        open_file()
        locating_file(filepath, filename)
        open_save_as_window()
        select_destiny_folder(filepath)
        renaming_file(page_number)
        close_adobe_file()
    except Exception as e:
        print(f"Something went wrong: {e}")


def open_adobe_reader():
    """
    Opening Adobe Reader
    """
    pyautogui.PAUSE = 0.5
    pyautogui.press('winleft')
    pyautogui.write('adobe acrobat')
    pyautogui.press('enter')
    time.sleep(1)


def close_adobe_application():
    pyautogui.hotkey('ctrl', 'q')


def open_file():
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)


def locating_file(filepath, filename):
    pyautogui.PAUSE = 1
    pyautogui.write(f'{filepath}{filename}')
    time.sleep(0.5)
    pyautogui.press('enter')


def open_save_as_window():
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(1)


def select_destiny_folder(filepath):
    tab = ['tab'] * 5
    pyautogui.press(tab)
    pyautogui.press('enter')
    pyautogui.write(filepath)
    pyautogui.press('enter')
    time.sleep(1)


def renaming_file(page_number):
    pyautogui.PAUSE = 1
    pyperclip.copy(f'Página {page_number} - Modificado')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')


def close_adobe_file():
    pyautogui.hotkey('ctrl', 'w')
