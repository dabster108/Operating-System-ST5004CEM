# Operating System & Networking Projects

A comprehensive collection of Python projects demonstrating fundamental networking concepts including **socket programming** (TCP/UDP), **REST API development** with Flask and FastAPI, and **client-server architecture**.

## 📚 Project Overview

This repository contains four main projects that progressively demonstrate networking concepts:

| Project | Protocol | Type | Key Concept |
|---------|----------|------|-------------|
| **TCP Socket** | TCP | Connection-Oriented | Reliable, ordered communication |
| **UDP Socket** | UDP | Connectionless | Fast, unreliable communication |
| **Flask REST API** | HTTP | Framework | Lightweight API framework |
| **FastAPI REST API** | HTTP | Modern Framework | High-performance async API |

---

## 🛠️ Prerequisites

- **Python 3.7+**
- **pip** (Python package manager)

---

## 📦 Installation

### Install Required Packages

```bash
pip install Flask FastAPI uvicorn
```

Or if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Projects

### 📡 TCP Socket Programs

TCP (Transmission Control Protocol) provides **reliable, ordered, connection-oriented** communication.

#### Navigate to the TCP directory:
```bash
cd tcp/
```

#### Start the TCP server in one terminal:
```bash
python server.py
```
> The server will start listening on a specific port (e.g., 12345)

#### Run the TCP client in another terminal:
```bash
python client.py
```
> The client will connect to the server, establishing a connection and enabling bidirectional communication

---

### 📨 UDP Socket Programs

UDP (User Datagram Protocol) provides **fast, connectionless** communication without guaranteed delivery.

#### Navigate to the UDP directory:
```bash
cd udp/
```

#### Start the UDP server in one terminal:
```bash
python server.py
```

#### Run the UDP client in another terminal:
```bash
python client.py
```

> **Note:** UDP is connectionless, so the order of execution may vary compared to TCP. Messages are not guaranteed to arrive in order or at all.

---

### 🌐 Flask REST API

Flask is a lightweight, flexible framework for building simple web applications and APIs.

#### Navigate to the Flask API directory:
```bash
cd rest-apis/flask-api/
```

#### Set the Flask app environment variable:

**MacOS/Linux:**
```bash
export FLASK_APP=server-flask.py
```

**Windows:**
```bash
set FLASK_APP=server-flask.py
```

#### Run the Flask development server:
```bash
flask run
```

> By default, the server runs at `http://127.0.0.1:5000`

#### Access the API:
- Use your browser, `curl`, or **Postman** to interact with endpoints
- Example: `curl http://127.0.0.1:5000/api/endpoint`

---

### ⚡ FastAPI REST API

FastAPI is a modern, high-performance framework with automatic interactive documentation.

#### Navigate to the FastAPI directory (if exists):
```bash
cd rest-apis/fastapi/
```

#### Launch the FastAPI server using Uvicorn:
```bash
uvicorn server-fastapi:app --reload
```

> The `--reload` flag enables automatic reloading on code changes

#### Access the application:

- **API Base URL:** `http://127.0.0.1:8000`
- **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`
- **Alternative Docs (ReDoc):** `http://127.0.0.1:8000/redoc`

---

## 🎯 Learning Outcomes

After working with these projects, you will gain practical experience in:

| Concept | Skills Acquired |
|---------|-----------------|
| **TCP vs UDP** | Understand connection-oriented vs connectionless communication, reliability differences, and use cases for each protocol |
| **Client-Server Architecture** | Implement both client and server components for network communication |
| **Socket Programming** | Create low-level network applications using Python's `socket` library |
| **REST API Development** | Design and build RESTful APIs with proper endpoints and HTTP methods (GET, POST, PUT, DELETE) |
| **Framework Comparison** | Contrast Flask's simplicity with FastAPI's performance and automatic documentation generation |
| **HTTP Protocol** | Handle different HTTP methods, status codes, and request/response patterns |
| **Error Handling** | Implement robust error handling in network applications |
| **Asynchronous Programming** | Learn async/await patterns with FastAPI |

---

## 📂 Project Structure

```
Operating-System-Networking/
├── README.MD                          # This file
├── tcp/
│   ├── client.py                      # TCP client implementation
│   └── server.py                      # TCP server implementation
├── udp/
│   ├── client.py                      # UDP client implementation
│   └── server.py                      # UDP server implementation
└── rest-apis/
    ├── client.py                      # Generic REST client
    ├── server.py                      # Generic REST server
    └── flask-api/
        ├── client-flask.py            # Flask REST client
        └── server-flask.py            # Flask REST server
```

---

## 🔍 Quick Start Guide

### For Beginners
Start with **TCP Socket Programs** to understand basic networking:
```bash
cd tcp/
python server.py &  # Run server in background
python client.py    # Run client in foreground
```

### For Intermediate Learners
Compare TCP and UDP to understand the trade-offs:
```bash
# Terminal 1: TCP Server
cd tcp/ && python server.py

# Terminal 2: UDP Server
cd ../udp/ && python server.py

# Terminal 3: Test both clients
cd ../tcp/ && python client.py
cd ../udp/ && python client.py
```

### For Advanced Learners
Build and test REST APIs:
```bash
# Terminal 1: Flask
cd rest-apis/flask-api/ && flask run

# Terminal 2: Test API endpoints
curl http://localhost:5000/api/endpoint
```

---

## 💡 Tips & Best Practices

- **Firewall Issues?** Ensure ports are not blocked by your firewall
- **Port Already in Use?** Modify the port number in the server code if you encounter address already in use errors
- **Testing APIs?** Use tools like:
  - `curl` (command-line)
  - **Postman** (GUI)
  - **VS Code REST Client** extension
- **Debugging?** Add print statements or use Python's `logging` module
- **Production Use?** Use proper web servers like Gunicorn for Flask, and production-grade configurations for FastAPI

---

## 📖 Resources

- [Python Socket Library](https://docs.python.org/3/library/socket.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [TCP/IP Protocol Guide](https://en.wikipedia.org/wiki/Internet_protocol_suite)
- [REST API Best Practices](https://restfulapi.net/)

---

## 📝 License

This project is open-source and available for educational purposes.

---

## ✨ Happy Learning!

Feel free to modify the code, experiment with different protocols, and build upon these projects to deepen your understanding of networking concepts.
