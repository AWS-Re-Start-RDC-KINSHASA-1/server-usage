from fastapi import FastAPI
import psutil

app = FastAPI()

# Route pour obtenir les informations de surveillance
@app.get("/monitoring")
async def get_monitoring():
    # Utilisation du CPU en pourcentage
    cpu_percent = psutil.cpu_percent(interval=1)

    # Utilisation du disque
    disk_usage = psutil.disk_usage("/")

    # Utilisation de la mémoire
    mem = psutil.virtual_memory()
    mem_percent = mem.percent

    # Création du dictionnaire de résultats
    monitoring_data = {
        "cpu_percent": cpu_percent,
        "disk_usage": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent
        },
        "mem_percent": mem_percent
    }

    return monitoring_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)