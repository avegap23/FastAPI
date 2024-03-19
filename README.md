## 1. Create virtual environment:
```
py -m venv .venv
```

## 2. Activate virtual environment:
On Powershell:
```
.\.venv\Scripts\Activate.ps1
```

On Command Prompt:
```
.\.venv\Scripts\activate.bat
```

On Linux/macOS:
```
source .venv/bin/activate
```

## 3. Install requirements (dependencies):
```
pip install -r requirements.txt
```

## 4. Start server with main.py:
```
uvicorn main:app --reload
```
