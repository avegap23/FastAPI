## 1. Crear entorno virtual:
```
py -m venv .venv
```

## 2. Activar entorno virtual:
Powershell:
```
.\.venv\Scripts\Activate.ps1
```

Command Prompt:
```
.\.venv\Scripts\activate.bat
```

Linux/macOS:
```
source .venv/bin/activate
```

## 3. Instalar requirements (dependencias):
```
pip install -r requirements.txt
```

## 4. Iniciar servidor con main.py:
```
uvicorn main:app --reload
```
