# 📦 Subscription Service Microservice

A simple, clean microservice for managing user subscriptions and plans in a SaaS platform.  
Built with **Flask**, **SQLAlchemy**, **JWT** auth, and **SQLite** (zero-config DB).  

---

## 📝 Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Environment Variables](#environment-variables)  
   - [Initialize Database](#initialize-database)  
   - [Run the Service](#run-the-service)  
4. [API Documentation](#api-documentation)  
   - [Authentication](#1-authentication)  
   - [Plans](#2-plans)  
   - [Subscriptions](#3-subscriptions)  
5. [Demo GIF / Video](#demo-gif--video)  
6. [Future Enhancements](#future-enhancements)  
7. [License](#license)  

---

## 🚀 Features

- **JWT Authentication**  
- **Plan Management**: create & list subscription plans  
- **Subscription CRUD**: subscribe, retrieve, update, cancel  
- **Status Handling**: ACTIVE, CANCELLED (plus `end_date`)  
- **Zero-config DB**: uses SQLite file `subscriptions.db`  
- **Clean Architecture**: Flask blueprints, SQLAlchemy models, Marshmallow schemas  
- **Error Handling & Validation** with Marshmallow  

---

## 🛠 Tech Stack

- **Framework**: Flask  
- **ORM**: Flask-SQLAlchemy  
- **Auth**: Flask-JWT-Extended  
- **Validation**: Marshmallow  
- **DB**: SQLite (via SQLAlchemy)  
- **Config**: python-dotenv  

---

## 🏁 Getting Started

### Prerequisites

- Python 3.8+ installed  
- Git (to clone repo)  
- (optional) Virtual environment tool  

