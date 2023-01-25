import pyautogui
import time


def rpa_rename(filepath, filename, page_number):
    pyautogui.PAUSE = 1

    '''Opening Adobe Reader'''
    pyautogui.press('winleft')
    pyautogui.write('adobe')
    pyautogui.press('enter')
    time.sleep(1)

    '''Shortcut to "open file"'''
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)

    '''Locating file to rename'''
    pyautogui.write(f'{filepath}{filename}')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    '''Shortcut to "save as"'''
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(1)

    '''Locating and selecting the original folder'''
    tab = ['tab'] * 5
    pyautogui.press(tab)
    pyautogui.press('enter')
    pyautogui.write(filepath)
    pyautogui.press('enter')
    time.sleep(1)

    '''Renaming the file'''
    pyautogui.write(f'Pagina {page_number} - Modificado')
    time.sleep(1)
    pyautogui.press('enter')

    '''Shortcut to "exiting the application"'''
    pyautogui.hotkey('ctrl', 'q')
