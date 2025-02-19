# Auto Plate Detection

Este projeto tem como objetivo desenvolver uma solução de Inteligência Artificial para a detecção automática de placas de carro, utilizando YOLO para identificar a região da placa e EasyOCR para extrair o seu conteúdo. O intuito é auxiliar na identificação de possíveis furtos, facilitando o monitoramento de veículos através das placas detectadas.

## Funcionalidades

- **Detecção de Placas:** Utiliza o YOLO para identificar e extrair a região onde a placa está presente.
- **OCR de Placas:** Emprega o EasyOCR para ler o texto presente na placa.
- **Processamento de Vídeo:** Analisa frames de vídeos, aplicando a detecção e leitura de placas, e registra métricas de desempenho.
- **Treinamento do Modelo:** Possibilita o treinamento customizado do modelo YOLO com um dataset específico.
- **Análise de Métricas:** Armazena as métricas de detecção e OCR em arquivos CSV para análises posteriores.

## Estrutura do Projeto

- **src/OCRdetect.py**  
  Contém a função `detect_text(image)` que utiliza EasyOCR para extrair o texto das imagens de placas.

- **notebooks/OCRanalitycs.ipynb**  
  Notebook para processar vídeos. Realiza a detecção de placas com YOLO e a extração do texto via OCR, registrando métricas de processamento e detecções em arquivos CSV.

- **notebooks/treinamento.ipynb**  
  Notebook para treinamento do modelo YOLO com base em um dataset customizado, definindo hiperparâmetros diversos e salvando o modelo treinado.

- **Imagens de Análise (Exemplos de Resultados)**  
  - `auto_Plate_Detectionbottleneck_analysis.png`  
  - `comparacao_validacoes.png`  
  - `validas_vs_invalidas.png`  
  Essas imagens podem ser utilizadas para acompanhar e demonstrar os resultados e análises do desempenho do sistema.

## Requisitos

- Python 3.8 ou superior
- [OpenCV](https://opencv.org/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [PyTorch](https://pytorch.org/)
- [EasyOCR](https://www.jaided.ai/easyocr/)
- Outras dependências podem ser listadas em um arquivo `requirements.txt`, se disponível.

## Como Executar

1. **Instalação das Dependências**

   Instale as dependências necessárias:

```bash
pip install opencv-python-headless
pip install ultralytics
pip install torch torchvision
pip install easyocr
```

2. **Treinamento do Modelo**

   Execute o notebook `treinamento.ipynb` para treinar o modelo:
   - Configure os paths para os dados e o modelo conforme necessário.
   - Siga as instruções do notebook para iniciar o treinamento.

3. **Processamento de Vídeo e OCR**

   Execute o notebook `OCRanalitycs.ipynb` para processar os vídeos:
   - Verifique se o modelo treinado está configurado corretamente.
   - Defina os paths para o vídeo e inicie o processamento.
   - Os resultados serão registrados em arquivos CSV.

## Resultados

Nesta seção, você pode incluir imagens e gráficos que demonstram os resultados e análises do desempenho do sistema. Exemplos de imagens que podem ser adicionadas:

- **Análise de Gargalos:**  
  ![Bottleneck Analysis](https://raw.githubusercontent.com/Natsuzera/SmartPlateDetection/master/notebooks/analise_final/bottleneck_analysis.png)
- **Valida vs. Inválida:**  
  ![Validation Comparison](https://raw.githubusercontent.com/Natsuzera/SmartPlateDetection/master/notebooks/analise_visual/validas_vs_invalidas.png)
- **Comparação de Validações:**  
  ![Valid vs Invalid](https://raw.githubusercontent.com/Natsuzera/SmartPlateDetection/master/notebooks/analise_final/comparacao_validacoes.png)

Atualize esta seção com novas imagens e descrições conforme necessário.

## Objetivos do Projeto

- Automatizar a identificação de veículos suspeitos através da leitura das placas.
- Auxiliar na prevenção de furtos com uma solução escalável de monitoramento.
- Fornecer métricas detalhadas para análise e melhoria do sistema.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões, melhorias ou correções.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para mais informações, acesse o repositório em [github.com/Natsuzera/SmartPlateDetection](https://github.com/Natsuzera/SmartPlateDetection).
