from paddleocr import PaddleOCR

# Inicializar PaddleOCR com otimizações para GPU
ocr = PaddleOCR(
    use_angle_cls=True,  # Desativa classificação de rotação para ganho de velocidade
    lang='en', 
    use_gpu=True, 
    rec_batch_num=64,  # Processa múltiplas regiões de texto ao mesmo tempo
    precision='fp16',  # Usa FP16 para melhor desempenho na GPU
    gpu_mem=6000,  # Limite de memória da GPU para evitar estouro
    max_batch_size=32,  # Tamanho máximo do lote para inferência
)

def detect_text(image):
    # Realizar OCR na imagem
    result = ocr.ocr(image, cls=False, det=True)
    
    # Extrair apenas o texto das detecções
    text_only = []
    if result and result[0]:  # Verifica se há alguma detecção
        for line in result[0]:
            text = line[1][0]  # [1][0] contém o texto detectado
            # Converter para maiúsculas e remover caracteres não alfanuméricos
            text = ''.join(c for c in text.upper() if c.isalnum())
            if text:  # Adiciona apenas se houver texto
                text_only.append(text)
    
    return text_only
