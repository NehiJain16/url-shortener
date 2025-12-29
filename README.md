# URL-Shortener-Service
Scalable URL Shortener Backend | FastAPI, SQLAlchemy, Redis, Pytest

# URL Shortener Backend Service

This project implements a **production-ready URL shortener backend** that allows users to generate short URLs, perform fast redirections, track usage analytics, and prevent abuse using **distributed rate limiting**, following real-world **software engineering best practices**.

---

## Project Overview

- **Goal**: Design and deploy a scalable backend system for URL shortening.
- **Focus Areas**: Backend APIs, system design fundamentals, data persistence, caching, testing, and cloud deployment.
- **Deployment**: Live backend deployed on cloud with environment-based configuration.

---

## Tech Stack

- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Caching / Rate Limiting**: Redis (managed, environment-configured)
- **Testing**: pytest, FastAPI TestClient (mocked Redis)
- **Deployment**: Render (API), Railway (Redis)
- **Version Control**: Git, GitHub

---

## Backend Architecture & Design

- **Base62 Encoding**
  - Generates compact, URL-friendly short codes from database IDs
  - Ensures uniqueness while keeping URLs short and readable

- **Database Indexing**
  - Indexed `short_code` column for fast lookup during redirection
  - Optimized for high-frequency read operations

- **Distributed Rate Limiting**
  - Redis-based counters with TTL
  - Prevents abuse and supports horizontal scalability

- **Stateless API Design**
  - Enables multiple backend instances behind a load balancer
  - Redis used for shared state across instances

---

## Core API Endpoints

### Create Short URL
- Endpoint: `POST /shorten`
- Request body example: `{ "original_url": "https://www.google.com" }`
- Response example: `{ "short_url": "https://url-shortener-2x68.onrender.com/b" }`

---

### Redirect to Original URL
- Endpoint: `GET /{short_code}`
- Redirects to the original URL
- Increments click count for analytics

---

### Analytics Endpoint
- Endpoint: `GET /analytics/{short_code}`
- Response example:
  - original_url: https://www.google.com
  - click_count: 3

---

### Delete Short URL
- Endpoint: `DELETE /{short_code}`

---

## Testing Strategy

- Unit tests implemented using **pytest** and **FastAPI TestClient**
- Redis dependency is **mocked** to ensure deterministic and isolated tests
- Coverage includes:
  - URL creation
  - Redirection behavior
  - Analytics tracking
  - Rate-limiting logic

To run tests locally:
- Activate virtual environment
- Run: `python -m pytest`

---

## Deployment

- Backend deployed on **Render**
- Redis hosted on **Railway**
- Environment-driven configuration used for production readiness

### Environment Variables

- `REDIS_URL` — Redis connection string for distributed rate limiting

---

## Key Engineering Learnings

- Designed RESTful APIs with clear separation of concerns
- Applied **DSA concepts** such as hashing, encoding, and indexing in backend systems
- Implemented **distributed rate limiting** using Redis
- Debugged production issues using cloud logs
- Wrote testable, modular backend code with mocked external dependencies
- Deployed and maintained a cloud-hosted backend service

---

## Future Enhancements

- URL expiration (TTL)
- Custom short aliases
- Asynchronous analytics aggregation
- Dockerized deployment
- CI pipeline for automated testing

---

## About Me

**Nehi Jain**  
Software Engineer

- 1+ years of experience in software development
- Strong interest in backend engineering and system design
- Experience building scalable, data-driven applications

LinkedIn: https://www.linkedin.com/in/nehijain

---

### Why This Project?

This project demonstrates **backend engineering skills expected from a Software Engineer**, including API design, database modeling, caching, testing, debugging, and cloud deployment—closely aligned with real-world production systems.
