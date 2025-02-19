import easyocr

reader = easyocr.Reader(['en'], gpu=True);
allowlist_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def detect_text(image):
    
    result = reader.readtext(
        image,
        decoder='beamsearch',       # Decodificador mais preciso
        beamWidth=10,
        batch_size=32,               # Processa mais rápido com maior memória
        allowlist=allowlist_str,  # Restrito a caracteres de interesse
        detail=0,
        min_size=60                # Ignorar textos pequenos
        )
    
    # Extraindo apenas o texto detectado
    text_only = [item for item in result]

    return text_only
