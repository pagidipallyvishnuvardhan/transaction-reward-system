# Transaction Reward System

## Overview

Transaction Reward System is a full-stack web application built using FastAPI, SQLite, HTML, CSS, and JavaScript.

The application allows users to:

* Add transactions
* Track user transaction summaries
* View rankings based on reward scores
* Prevent duplicate transaction processing

---

## Technology Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* HTML
* CSS
* JavaScript

---

## API Endpoints

### POST /transaction

Creates a new transaction.

Example Request:

{
"userId": "101",
"amount": 500,
"transactionId": "TXN001"
}

Features:

* Validates input
* Prevents duplicate transaction IDs
* Updates user statistics
* Recalculates score

---

### GET /summary/{user_id}

Returns user statistics.

Example Response:

{
"userId": "101",
"totalAmount": 1500,
"totalTransactions": 2,
"score": 190
}

---

### GET /ranking

Returns all users sorted by score.

Example Response:

[
{
"rank": 1,
"userId": "102",
"score": 360
}
]

---

## Ranking Logic

Score Calculation:

score = (total_amount × 0.1) + (total_transactions × 20)

This rewards both:

* Transaction volume
* Transaction frequency

---

## Duplicate Request Prevention

Each transaction uses a unique transactionId.

Before inserting a transaction, the system checks:

* If transactionId already exists
* If found, returns HTTP 400 Bad Request

This prevents duplicate processing and ranking manipulation.

---

## How To Run

### Backend

cd backend

pip install -r requirements.txt

uvicorn main:app --reload

Backend URL:

Backend URL:
https://transaction-reward-system.onrender.com

---

### Frontend

Open:

frontend/index.html

or run using VS Code Live Server.
https://pagidipallyvishnuvardhan.github.io/transaction-reward-system/

---

## Future Improvements

* PostgreSQL integration
* User authentication
* Advanced ranking algorithms
* Transaction history dashboard
* Deployment using Render and Vercel
