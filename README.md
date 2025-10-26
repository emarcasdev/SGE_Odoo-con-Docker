# Odoo con Docker

Despliegue rápido de **Odoo** + **PostgreSQL** utilizando Docker Compose.

## Requisitos

* Tener instalado **Docker Desktop**
* Obtener las imágenes de Odoo y PostgreSQL en **Docker Hub**

## Estructura

```
.
├─ backups/            # Copias de seguridad
├─ config/             # Configuración
└─ docker-compose.yaml
```

## Primer uso

```bash
git clone https://github.com/emarcasdev/SGE_Odoo-con-Docker.git   # Clona el repositorio
cd SGE_Odoo-con-Docker                                            # Entra en el directorio
docker compose up -d --build                                      # Clona el repositorio
```

Puedes acceder al Odoo entrando en: **[http://localhost:8069](http://localhost:8069)**

## Comandos útiles

```bash
# VER ESTADO
docker ps                      # Contenedores en ejecución

# LOGS
docker compose logs -f odoo    # Logs de Odoo en vivo
docker compose logs -f db      # Logs de Postgres en vivo
docker compose logs -f         # Todos los servicios

# CICLO DE VIDA
docker compose up              # Levantar mostrando los logs
docker compose up -d           # Levantar sin mostrar los logs
docker compose up -d --build   # Levantar reconstruyendo imágenes
docker compose restart         # Reiniciar todos los servicios
docker compose stop            # Detener
docker compose start           # Arrancar servicios detenidos
docker compose down            # Parar y eliminar contenedores + red
docker compose down -v         # Parar y eliminar contenedores + red + volúmenes

```

## Backups

**Crear dump**:

```bash
docker exec -t postgres pg_dump -U odoo_admin -F c -b -v -f /var/lib/postgresql/data/backup_odoo_yyyymmdd.dump postgres
```

**Restaurar**:

```bash
docker exec -t postgres pg_restore -U odoo_admin -d postgres --clean --if-exists -v /var/lib/postgresql/data/backup_odoo_yyyymmdd.dump
```
