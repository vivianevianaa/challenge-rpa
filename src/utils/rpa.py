import pyautogui
import time
import pyperclip


def rpa_rename(filepath, filename, page_number):
    '''The macro function that calls the micro functions'''
    open_file()
    locating_file(filepath, filename)
    open_save_as_window()
    select_original_folder(filepath)
    renaming_file(page_number)
    close_adobe_file()


def open_adobe_reader():
    '''Opening Adobe Reader'''
    pyautogui.PAUSE = 0.5
    pyautogui.press('winleft')
    pyautogui.write('adobe')
    pyautogui.press('enter')
    time.sleep(1)


def close_adobe_reader():
    '''Shortcut to "exiting the application"'''
    pyautogui.hotkey('ctrl', 'q')


def open_file():
    '''Shortcut to "open file"'''
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)


def locating_file(filepath, filename):
    '''Locating file to rename'''
    pyautogui.PAUSE = 1
    pyautogui.write(f'{filepath}{filename}')
    time.sleep(1)
    pyautogui.press('enter')


def open_save_as_window():
    '''Shortcut to "save as"'''
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(1)


def select_original_folder(filepath):
    '''Locating and selecting the original folder'''
    tab = ['tab'] * 5
    pyautogui.press(tab)
    pyautogui.press('enter')
    pyautogui.write(filepath)
    pyautogui.press('enter')
    time.sleep(1)


def renaming_file(page_number):
    '''Renaming the file'''
    pyautogui.PAUSE = 1
    pyperclip.copy(f'Página {page_number} - Modificado')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')


def close_adobe_file():
    '''Closing the file'''
    pyautogui.hotkey('ctrl', 'w')
