import ollama
import torch



response = ollama.chat(
    model='minicpm-v:8b',
    messages=[{
        'role': 'user',
        'content': 'Do the work of an OCR, to read the content of car plates, I only said the content of the car plate, nothing more than that',
        'images': ['17790672_jpg.rf.097bdd9bcde1e94c303977f13f568584.jpg']
    }]
)

print(response.message.content)

torch.cuda.empty_cache()