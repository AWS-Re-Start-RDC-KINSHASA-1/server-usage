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

    # Conversion de disk_usage en gigaoctets
    disk_usage_gb = {
        "total": disk_usage.total / (1024**3),  # Conversion de bytes en gigaoctets
        "used": disk_usage.used / (1024**3),
        "free": disk_usage.free / (1024**3),
        "percent": disk_usage.percent
    }

    # Conversion de mem_percent en gigaoctets
    mem_percent_gb = mem_percent / (1024**3)  # Conversion de bytes en gigaoctets

    # Mise à jour de monitoring_data avec les nouvelles valeurs en gigaoctets
    
    monitoring_data_gb = {
        "cpu_percent": cpu_percent,
        "disk_usage": disk_usage_gb,
        "mem_percent": mem_percent_gb
    }

    return monitoring_data_gb

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)