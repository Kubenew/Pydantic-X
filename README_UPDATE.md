# Pydantic-X Examples Update Pack

This ZIP contains:
- docker-compose.yml (runs demo in Python container)
- examples/demo_full.py (sanitizers + schema migration)
- examples/fastapi_validation_demo.py (FastAPI integration example)

## How to use

1. Extract into repo root.
2. Run:

```bash
docker compose up --build
```

Or run FastAPI demo manually:

```bash
pip install fastapi uvicorn
uvicorn examples.fastapi_validation_demo:app --reload --port 8001
```
