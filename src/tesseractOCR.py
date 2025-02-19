import cv2
import pytesseract
import numpy as np

# Configuração para Windows (descomente se necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_text(image):
    # Pré-processamento da imagem para melhorar o OCR
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Configuração do Tesseract
    config = (
        '--psm 7 '              # Modo de segmentação para uma única linha de texto
        '--oem 3 '              # Motor OCR mais avançado
        '-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # Filtra caracteres
    )
    
    # Executa o OCR
    text = pytesseract.image_to_string(thresh, config=config, lang='eng')
    
    # Processa o texto extraído
    text = text.strip().replace('\n', ' ').replace('\x0c', '')
    return [text] if text else []