# FastAPI Best Practices

Hi there, 👋

Welcome to **my past mistakes** and the architecture that helped me overcome them. This repository is the result of solving real engineering problems that once cost me **time, energy, and clarity** — and it's now shaped into a reusable, modular FastAPI backend template.

---

## 🚀 What is This?

This repository contains **battle-tested best practices** for building FastAPI-based microservices that are **production-ready**, **scalable**, and **developer-friendly**.

It combines the **most modern tech stacks** and **clean architecture principles** to give you a foundation that:

* Avoids spaghetti code
* Encourages clean separation of concerns
* Works well in **CI/CD**, **Docker**, and **cloud environments**

---

## 🧱 Features

* ✅ **FastAPI** (async-first, modern REST API)
* ✅ **SQLAlchemy (async)** with **PostgreSQL**
* ✅ **Ruff**, **Pytest**, **Pyright**, **GitHub Actions**
* ✅ **DTO-based architecture** for type safety
* ✅ Clean **Dependency Injection** layering
* ✅ Full support for **Redis**, **RabbitMQ**, **Kafka** (optional)
* ✅ Pluggable microservice-ready structure
* ✅ **Modular Config Management** with `.env` per domain
* ✅ Clean separation between `infrastructure`, `use_cases`, `dto`, and `query`

---

## 📁 Folder Structure

```
alembic/

secrets/
    app/
        logging/
            .env
        database/
            .env
        domain/
            .env
    shared/
        auth/
            .env
            public.pem
        xss/
            .env

src/
    project-name/
        api/
            routers.py

        app/
            main.py
            loader.py

        services/
            di.py
            use_cases/
    
            http/
                service_http_service.py
            queries/
                users.py
            dto/
                schemas/
                    domain.py
                    users.py  # here is schema for http clients
                parameters/
                    use_cases/
                        foo.py
                    http/
                        foo_service.py
                responses/
                    use_cases/
                        foo.py
                    http/
                        foo_service.py

        infrastructure/
            database/
                setup.py
                setup_tools.py
                di.py
            kafka/
                setup.py
                setup_tools.py
                di.py
            rabbitmq/
            redis/

        config/
            base.py
            logging_conf.py
            database_conf.py
            redis_conf.py
            utils.py

        models/
            __init__.py
            domain.py

        utils/
        misc.py

    shared/
        auth/
            src/
                di.py
                decorators.py
                middlewares.py
                utils/
                    misc.py
                ...
        ...

tests/
    conftest.py
    unit/
        shared/
        src/
            services/
                ...
            ...
    integration/
        ...

.github/workflows/
    CI.yaml
    CD.yaml

scripts/
    ci.py

pyproject.toml
alembic.ini
pytest.ini
ruff.toml
.venv
```

---

## 💡 Philosophy

* **One source of truth** for schemas, injected everywhere as DTOs
* Services **don't rely on central auth logic** — everything is cleanly separated
* Use cases are **independent**, reusable, and testable
* **Query layer** holds raw SQLAlchemy logic, not business logic
* Supports **x-service-key** pattern for inter-service auth
* Structured for real-world async services running via **Gunicorn** or **Uvicorn**

---

## 🛠 Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
* [PostgreSQL](https://www.postgresql.org/)
* [Alembic](https://alembic.sqlalchemy.org/)
* [Redis](https://redis.io/) / [RabbitMQ](https://www.rabbitmq.com/) / [Kafka](https://kafka.apache.org/)
* [Pytest](https://docs.pytest.org/)
* [Ruff](https://docs.astral.sh/ruff/)
* [Pyright](https://github.com/microsoft/pyright)
* [GitHub Actions](https://github.com/features/actions)

---

## 🤝 Contributing

This template is a living thing. Feel free to fork, submit PRs, or just steal the best ideas. You’re welcome to contribute your own clean patterns.

---

## 📧 Contact

Need advice or want to collaborate? [fazliddin1801@gmail.com](mailto:fazliddin1801@gmail.com)
Or better you can find me from telegram at [@abdurahimov_f18][https://t.me/abdurahimov_f18]

---

## 🏁 Final Words

If you're tired of monolith frameworks, unclear file structures, or hard-to-scale applications — this repo might save you months of future refactors.

Happy coding 👨‍💻⚡
