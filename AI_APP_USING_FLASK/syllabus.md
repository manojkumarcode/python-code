# Course Syllabus

## Module 1: Python Coding Practices and Packaging Concepts
- **Lesson 1:** Application Development and Packaging using Python

## Module 2: Web App Deployment using Flask
- **Lesson 1:** Web application deployment using Flask

## Module 3: Creating AI Application and Deploy using Flask
- **Lesson 1:** Practice Project
- **Lesson 2:** Final Project
- **Lesson 3:** Course Wrap-up

---

## Learning Path: Flask vs FastAPI vs Django

For a beginner, the honest answer is: learn Flask first, then move to FastAPI or Django. Not because Flask is what you'll use professionally, but because it teaches you what a web framework actually does instead of hiding it.

Here's the order that works:

1. **Python fundamentals first.** Functions, classes, decorators, virtual environments, pip. Decorators especially — Flask and FastAPI both use them everywhere, and if `@app.route` looks like magic, you'll never debug confidently.

2. **HTTP itself, before any framework.** Request/response cycle, methods, status codes, headers, JSON. Half of "framework problems" beginners hit are actually HTTP misunderstandings. An afternoon with curl or Postman pays for itself.

3. **Flask, small.** Build three or four tiny things: a JSON API, a form that saves to a database, something with login. You'll hand-write routing, request parsing, and templates — that's the point. You learn what the framework is doing for you and what it isn't.

4. **Databases and SQL.** Real SQL before an ORM. `SELECT`, `JOIN`, indexes, why an unindexed query is slow. Then SQLAlchemy. Beginners who learn the ORM first end up unable to explain why their app is slow.

5. **Then pick your direction.**
   - APIs and ML services → **FastAPI** (async, Pydantic, typing)
   - Full products with admin screens and user management → **Django** (ORM, auth, admin, migrations all included)

   At this point you'll understand why they made the choices they did, which you can't appreciate coming in cold.

6. **The stuff nobody teaches but everyone needs.** Git, environment variables and secrets, writing tests with pytest, reading a stack trace properly, Docker basics, deploying one thing to a real server. This is the gap between "can build a tutorial app" and "employable."
