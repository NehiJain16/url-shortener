**URL Shortener Backend**


A production-ready URL shortener service built with FastAPI, featuring Base62 hashing, Redis-based rate limiting, analytics tracking, and unit-tested REST APIs.
Deployed on Render with environment-driven configuration.


**Live Demo:**

• Swagger UI- https://url-shortener-2x68.onrender.com/docs

• Example Short URL- https://url-shortener-2x68.onrender.com/b


**Tech Stack:**

• Backend- Python, FastAPI 

• Database- SQLite (SQLAlchemy ORM)

• Caching / Rate Limiting- Redis (managed, env-configured)

• Testing- pytest, FastAPI TestClient (mocked Redis)

• Deployment- Render

• Version Control- Git, GitHub


**Features:**

• Create short URLs from long URLs

• Redirect short URLs to original destinations

• Analytics tracking (click count per URL)

• Distributed rate limiting using Redis

• Unit-tested APIs with mocked external dependencies

• Environment-based configuration for production readiness


**System Design Highlights:**

• Base62 Encoding- Generates compact, URL-friendly short codes from database IDs

• Indexed Lookups- Optimized retrieval using indexed short_code column

• Distributed Rate Limiting- Redis counters with TTL prevent abuse under concurrent traffic

• Scalability- Stateless API design allows horizontal scaling

• Test Isolation- Redis mocked in tests to ensure deterministic behavior


**Testing:**

Unit tests are written using pytest and FastAPI TestClient, with Redis mocked to isolate external dependencies. All core flows are covered- URL creation, Redirection behavior, Analytics tracking, Rate-limit safety


**Local Setup:**

• git clone https://github.com/NehiJain16/url-shortener.git
  
• cd url-shortener

• python -m venv venv
  
• venv\Scripts\activate

• python -m pip install -r requirements.txt
  
• uvicorn app.main:app --reload


  **Environment Variables:**

• REDIS_URL- Redis connection string for rate limiting


  **Future Enhancements:** 
  
  • URL expiration (TTL)
    
  • Custom aliases
    
  • Persistent analytics storage
    
  • Dockerized deployment
    
  • CI pipeline for automated testing


  **Author:**
  Nehi Jain,
  Software Engineer

  **Why This Project?**  
  This project demonstrates backend engineering fundamentals;API design, database modeling, caching, testing, and cloud deployment aligned with real world Software Engineer responsibilities.
