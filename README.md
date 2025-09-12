# kinesis-cloudformation

## 📌 Project Description
This project is the implementation of streaming data ingestion from a public source.  

The goal is to design and implement a **...** that:
1. a
2. b
3. c
4. d

**Assumptions**
1. a
2. b 
3. c
4. d


The solution also includes:
- a
- b
- c
- d

---

## 🚀 Features
- **xxx**
- **xxx** 
- **xxx** 
- **xxx**

---

## 🛠 Tech Stack
**Programming Language**
- [Python 3.x](https://www.python.org/)

**Frameworks & Libraries**
- [FastAPI](https://fastapi.tiangolo.com/) – REST API framework with automatic Swagger docs.
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database modeling and queries.
- [Pandas](https://pandas.pydata.org/) – CSV parsing and data manipulation.
- [Pytest](https://docs.pytest.org/) – Testing framework.

**Database**  
- [xxx](https://www.) – xxx

**Containerization**
- [](https://www.) – xxx

**Cloud Services**
- [](https://aws.amazon.com/) – xxx

---

## Deployment

- xxx


---

## Project Structure

```text 
kinesis-cloudformation/
├──.github/ # Github Actions
│ ├── workflows/
│ │  ├── deploy.yml
├── scripts/ 
├── app/ # Source code 
│ ├── delivery/
│ │  ├── binance_event_handler.py
│ ├── lambda_handlers/
│ │  ├── stream_processor.py
│ ├── models/
│ ├── processing/
│ │  ├── duration_filter_tester.py
│ │  ├── uptime_filter_tester.py
│ ├── producers/
│ │  ├── kinesis_publiser.py
│ ├── schemas/
│ │  ├── binance_trade_schema.py
│ ├── services/
│ ├── sources/
│ │  ├── binance_ws_client.py
│ ├── observability/
│ ├── utils/
│ │  ├── schema_validator.py
│ │  ├── websocket_payload_parser.py 
│ └── main.py
├── config/
│ ├── __init__.py
│ ├── base_config.py
│ ├── secrets_loader.py
├── iac/
| ├── infra-basica.yml
| ├── infra-secundaria.yml
├── tests/ # Automated test files
│   └── __init__.py
│   ├── test_kinesis_publisher.py
│   ├── test_websocket_payload_parser.py
├──.dockerignore
├──.gitignore
├──dockerfile 
├──README.md # This file 
├──requirements-dev.txt # Python dependencies
└──requirements.txt # Python dependencies
```

---


## Design Decisions

- **High cohesion**: xxx

- **Modularity**: xxx

- **Low coupling**: xxx

- **Organized tests**: xxx

- **Clear separation**: xxx


---


## 🏗 Architecture Overview

xxx

---

## 🔮 Possible Future Improvements

xxx

---

## 📌 Payload

```text
{
  "e": "trade",
  "E": 1756827687988,
  "s": "BTCUSDT",
  "t": 5210041330,
  "p": "111018.01000000",
  "q": "0.00005000",
  "T": 1756827687987,
  "m": false,
  "M": true
}
```

```text
| Key   | Meaning                                      | Type     | Example             |
|-------|----------------------------------------------|----------|---------------------|
| e     | Event type                                   | string   | "trade"             |
| E     | Event timestamp (ms)                         | int      | 1756827688115       |
| s     | Trading pair symbol                          | string   | "BTCUSDT"           |
| t     | Unique trade ID                              | int      | 5210041384          |
| p     | Price at which the trade was executed        | string   | "111022.09000000"   |
| q     | Quantity traded                              | string   | "0.00005000"        |
| T     | Trade timestamp (ms)                         | int      | 1756827688115       |
| m     | Was the seller the maker?                    | bool     | false               |
| M     | Reserved flag (always true)                  | bool     | true                |
```

---

## ☁️ AWS SERVICE

- xxx


---
## ✉️ Contact / Author

- **Name:** Camilo Gálvez Zúñiga  
- **Email:** cgalvezz@udd.cl  
- **LinkedIn:** (https://www.linkedin.com/in/camilogalvez12/)