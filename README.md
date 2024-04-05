## 1. Create virtual environment:
```
py -m venv .venv
```

## 2. Activate virtual environment:
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

## 3. Install requirements:
```
pip install -r requirements.txt
```

## 4. Start server with main.py:
```
uvicorn main:app --reload
```
