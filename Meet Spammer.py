import pyautogui, time
print("Time to begin >:D")
time.sleep(3)
while True:
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(688, 772)
    pyautogui.click(770, 770)
    pyautogui.click(1270, 600)
    time.sleep(1)