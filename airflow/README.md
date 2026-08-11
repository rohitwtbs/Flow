# Local Apache Airflow Docker Setup

This repository provides a complete, production-aligned local **Apache Airflow 2.10.0** setup powered by **Docker Compose**, configured with **CeleryExecutor**, **PostgreSQL 15**, and **Redis 7**.

---

## 🛠️ Architecture & Services

The Docker Compose configuration includes the following containers:
- **`airflow-webserver`**: Airflow Web UI & REST API (`http://localhost:8080`)
- **`airflow-scheduler`**: DAG scheduler monitoring workflow triggers
- **`airflow-worker`**: Celery worker executing tasks in parallel
- **`airflow-triggerer`**: Supports async / deferrable operators
- **`airflow-flower`**: Celery monitoring dashboard (`http://localhost:5555`)
- **`airflow-init`**: One-off database migration & admin user initialization container
- **`postgres`**: PostgreSQL database backend
- **`redis`**: Redis broker for Celery task message queue

---

## 🚀 Quickstart Guide

### 1. Set File Permissions & Environment Variables (Linux / macOS)

On Linux/macOS, match the user ID of your local host machine to avoid file permission issues in mounted directories (`dags/`, `logs/`, `plugins/`):

```bash
echo -e "AIRFLOW_UID=$(id -u)" >> .env
```

Create the required mount directories if they do not exist:

```bash
mkdir -p ./dags ./logs ./plugins ./config
```

---

### 2. Initialize Database & Create Admin User

Run the initialization service:

```bash
docker compose up airflow-init
```

Once `airflow-init` exits with code `0`, your PostgreSQL database and default admin user are ready.

---

### 3. Start Airflow Services

Start all services in detached mode:

```bash
docker compose up -d
```

Check the status of running containers:

```bash
docker compose ps
```

---

## 🌐 Accessing the Dashboards

- **Airflow Web UI**: [http://localhost:8080](http://localhost:8080)
  - **Username**: `admin`
  - **Password**: `admin`
- **Celery Flower Dashboard**: [http://localhost:5555](http://localhost:5555)

---

## 🧪 Testing Your First DAG

1. A sample DAG [`example_dag.py`](file:///home/rohitwtbs/Documents/github/Flow/airflow/dags/example_dag.py) is included in `./dags`.
2. Open [http://localhost:8080](http://localhost:8080), unpause `local_quickstart_dag`, and trigger a run.
3. Check task logs in the UI or examine the local `./logs` directory.

---

## 🧹 Useful Commands

| Action | Command |
| :--- | :--- |
| **View Service Logs** | `docker compose logs -f` |
| **Stop All Containers** | `docker compose stop` |
| **Stop & Remove Containers** | `docker compose down` |
| **Reset Database & Clean Volumes** | `docker compose down --volumes --remove-orphans` |
| **Install Additional PyPI Packages** | Add package names to `_PIP_ADDITIONAL_REQUIREMENTS` in `.env` and restart containers. |
