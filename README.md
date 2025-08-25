---

# 🧠 Sentiment Analysis App (Java + Python AI)
<img width="1536" height="1024" alt="Sentiment Analysis Tech Diagram" src="https://github.com/user-attachments/assets/acac1bf7-399d-44d1-84f4-19b6a2b52ab2" />

A **microservice-based AI application** that combines **Python (AI/ML)** and **Java Spring Boot (API layer)** to deliver real-time **sentiment analysis**.

Users send text to the **Spring Boot API**, which forwards the request to a **Python FastAPI service** running a Hugging Face model. The AI service responds with **Positive / Negative / Neutral** classification and confidence score.

---

## 📌 Features

* ⚡ **Microservices Architecture**: Java (API) + Python (AI)
* 🤖 **AI-powered NLP**: Hugging Face transformer model
* 🌍 **REST APIs**: Exposes sentiment analysis endpoints
* 🐳 **Dockerized**: Run with Docker Compose (Java + Python containers)
* 🔐 **Extensible**: Add DB, OAuth2 security, or frontend later

---

## 🏗️ Project Structure

```
sentiment-analysis-app/
│
├── java-sentiment-app/               # Java Spring Boot microservice
│   ├── src/main/java/com/example/sentiment/
│   │   ├── controller/
│   │   │   └── SentimentController.java
│   │   ├── service/
│   │   │   └── SentimentService.java
│   │   ├── dto/
│   │   │   └── SentimentResponse.java
│   │   └── SentimentApplication.java
│   ├── pom.xml
│   └── Dockerfile
│
├── python-ai-service/                # Python AI microservice
│   ├── app.py                        # FastAPI entrypoint
│   ├── model.py                      # Hugging Face model loader (optional)
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml                # Orchestration for Java + Python services
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2️⃣ Run Locally (Without Docker)

#### Start Python AI Service

```bash
cd python-ai-service
pip install -r requirements.txt
uvicorn app:app --reload --port 5000
```

#### Start Java Spring Boot API

```bash
cd ../java-sentiment-app
./mvnw spring-boot:run
```

---

### 3️⃣ Run with Docker (Recommended)

Build and start both services:

```bash
docker-compose up --build
```

* Java API → [http://localhost:8080/sentiment](http://localhost:8080/sentiment)
* Python AI Service → [http://localhost:5000/predict](http://localhost:5000/predict)

---

## 📡 API Usage

### Java API (User-facing)

```http
POST /sentiment
Content-Type: application/json

{
  "text": "I love Java and Python working together!"
}
```

**Response**

```json
{
  "label": "POSITIVE",
  "score": 0.9983
}
```

---

### Python AI Service (Internal)

```http
POST /predict
Content-Type: application/json

{
  "text": "This project is amazing!"
}
```

**Response**

```json
{
  "label": "POSITIVE",
  "score": 0.9991
}
```

---

## 📦 Tech Stack

* **Java 21 + Spring Boot 3.5** → REST API service
* **Python 3.11 + FastAPI** → AI microservice
* **Hugging Face Transformers** → Pretrained NLP models
* **Docker + Docker Compose** → Container orchestration
* **Maven** → Java build tool

---

## 🛠️ Future Improvements

* [ ] Add **MySQL/Postgres** for storing user queries
* [ ] Implement **OAuth2 (JWT)** for authentication
* [ ] Build a **React frontend** to visualize results
* [ ] Deploy to **Kubernetes / Cloud provider**

---

## 👨‍💻 Author

**Babatunde Ipaye**
📧 [b.tunde.ipaye@gmail.com](mailto:b.tunde.ipaye@gmail.com)
💼 [LinkedIn](https://www.linkedin.com/in/engripayebabatunde)
🐙 [GitHub](https://github.com/engripaye)

---

Do you want me to also generate the **`docker-compose.yml` and Dockerfiles for both Java & Python services** so you can run everything together in one command?
