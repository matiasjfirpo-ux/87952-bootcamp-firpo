*Codigo original para editar en cloude
```
from transformers import pipeline
classifier = pipeline("sentiment-analysis",
                      model="distilbert-base-uncased-finetuned-sst-2-english",
                      cache_dir="/content/modelos_hf")
result = classifier("This is excelent")
print(result)
```

*Codigo hecho por cloude IA

```

from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      model="distilbert-base-uncased-finetuned-sst-2-english",
                      cache_dir="/content/modelos_hf")

texto = input("Ingresá el texto a analizar: ")
result = classifier(texto)
print(result)
```

[!NOTE] Si quiero que tenga un loop, seria este codigo:
```
from transformers import pipeline

classifier = pipeline("sentiment-analysis",
                      model="distilbert-base-uncased-finetuned-sst-2-english",
                      cache_dir="/content/modelos_hf")

while True:
    texto = input("Ingresá el texto a analizar (o 'salir' para terminar): ")
    if texto.lower() == "salir":
        print("Fin del programa.")
        break
    result = classifier(texto)
    print(result)
```

