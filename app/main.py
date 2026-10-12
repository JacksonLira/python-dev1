from fastapi import FastAPI

app = FastAPI(
    title="Python Dev Profile",
    description="Minha primeira API profissional com Python",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "API funcionando",
        "project": "Python Dev Profile",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/profile")
def profile():
    return {
        "name": "Seu Nome",
        "role": "Python Developer",
        "location": "Brasil",
        "experience": "Em formação",
    }

@app.get("/skills")
def skills():
    return {
        "backend": [
            "Python",
            "FastAPI",
        ],
        "frontend": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
        ],
        "database": [
            "PostgreSQL",
            "MySQL",
        ],
    }