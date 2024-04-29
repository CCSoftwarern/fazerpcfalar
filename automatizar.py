import pyautogui
import time

nome = input("Digite no nome da pessoa: ")
texto = input("Digite um texto: ")
automatizar = pyautogui
automatizar.PAUSE = 1

automatizar.moveTo(26,882)
automatizar.click(26,882)
automatizar.moveTo(489,291)
automatizar.click(489,291)
automatizar.write(nome)
automatizar.moveTo(240,177)
automatizar.click(240,177)
automatizar.write(texto)
automatizar.hotkey('enter')
automatizar.moveTo(1583,18)
automatizar.click(1583,18)
