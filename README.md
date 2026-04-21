# Pydantic-X ✨

[![PyPI version](https://img.shields.io/pypi/v/pydantic-x.svg)](https://pypi.org/project/pydantic-x/)
[![Downloads](https://static.pepy.tech/badge/pydantic-x)](https://pepy.tech/project/pydantic-x)
[![License: MIT](https://img.shields.io/pypi/l/pydantic-x)](https://github.com/yourname/pydantic-x/blob/main/LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/pydantic-x)](https://pypi.org/project/pydantic-x/)

 About
Pydantic-X enhances Pydantic with:

🔹 Compiled validation (fast)  
🔹 Schema versioning & migration  
🔹 Sanitizers (trim, normalize, strip HTML)  
🔹 Streaming JSON validation  

Perfect for APIs, ETL, and data platforms.
Install
pip install pydantic-x
Example Usage
from pydantic_x import BaseModelX, SchemaVersion

class Person(BaseModelX):
    name: str
    email: str

    class Config:
        sanitize = True
        strip_whitespace = True

print(Person(name=" Alice ", email=" ALICE@EX.COM ").dict())
Schema Versioning
class V1User(BaseModelX, version=1):
    name: str

class V2User(BaseModelX, version=2):
    name: str
    email: str

# auto migrate data from V1 → V2
user = V2User.from_previous({"name": "Bob"})
Features

✔ Faster compiled validation
✔ Schema migrations
✔ Built-in sanitizers
✔ Streaming JSON parsing
✔ Strict types (email, UUID, phone, IBAN)

Contributing

PRs welcome!

License

MIT


---

## 📢 Promotion Templates

### Twitter/X

🚀 Just released **fastapi-xkit** and **pydantic-x** on PyPI!  
🔗 fastapi-xkit – production toolkit for FastAPI  
🔗 pydantic-x – next-gen Pydantic enhancements

✨ Ready for real applications  
💡 Features: JWT auth, RBAC, Redis rate limiting, OpenTelemetry, schema versioning

👇 Try them today!  
https://pypi.org/project/fastapi-xkit/  
https://pypi.org/project/pydantic-x/

---

### Reddit (r/Python / r/FastAPI)

Hi Python community!  
I just published **fastapi-xkit** and **pydantic-x** on PyPI:

🔹 **fastapi-xkit** – FastAPI production toolkit (Redis rate limits, JWT auth, RBAC, audit logs DB, OpenTelemetry)  
🔹 **pydantic-x** – Faster validation + schema versioning + sanitizers

Critiques and feature ideas welcome! 🚀
