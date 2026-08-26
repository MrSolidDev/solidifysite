"""Carga contenido inicial de forma idempotente.

Ejecutar después de las migraciones con: python -m scripts.seed
"""
from datetime import UTC, datetime

from sqlalchemy import select

from app.database import SessionLocal
from app.models import CaseStudy, Project, PublicationStatus, Technology

TECHNOLOGIES = ["Vue 3", "TypeScript", "Python", "AWS", "SAP OData", "Raspberry Pi", "Node.js"]
PROJECTS = [
    {
        "slug": "ollin-pulse",
        "name": "Ollin Pulse",
        "tagline": "Concursos interactivos para eventos en vivo",
        "short_description": "Software para producir concursos por equipos con control centralizado, pantalla pública y puntuación automatizada.",
        "full_description": "Convierte una dinámica de preguntas y respuestas en una experiencia visual con ritmo de programa de televisión.",
        "status": "Producto disponible",
        "featured": True,
        "technologies": ["Vue 3", "TypeScript", "Node.js"],
    },
    {
        "slug": "ollin-media",
        "name": "Ollin Media",
        "tagline": "Contenido digital administrado desde un solo lugar",
        "short_description": "Plataforma para administrar, programar, distribuir y monitorear contenido en redes de pantallas.",
        "full_description": "Transforma pantallas en canales de comunicación inteligentes con administración centralizada.",
        "status": "Producto disponible",
        "featured": True,
        "technologies": ["Vue 3", "TypeScript", "AWS"],
    },
    {
        "slug": "plataforma-financiera-sap",
        "name": "Plataforma financiera SAP",
        "tagline": "Operación financiera conectada",
        "short_description": "Plataforma interna para centralizar y procesar información financiera.",
        "full_description": "Caso de implementación empresarial conectado con SAP y servicios de AWS.",
        "status": "Caso documentado",
        "featured": False,
        "technologies": ["Vue 3", "TypeScript", "SAP OData", "AWS"],
        "publication_status": PublicationStatus.published,
    },
    {
        "slug": "experiencia-retail-interactiva",
        "name": "Experiencia retail interactiva",
        "tagline": "Contenido que responde al visitante",
        "short_description": "Experiencia física conectada con sensores y contenido dinámico.",
        "full_description": "Solución interactiva preparada para replicarse en distintos espacios.",
        "status": "Caso documentado",
        "featured": False,
        "technologies": ["Raspberry Pi", "Node.js"],
        "publication_status": PublicationStatus.published,
    },
    {
        "slug": "preventa-tecnologica-b2b",
        "name": "Preventa tecnológica B2B",
        "tagline": "De una necesidad ambigua a una propuesta ejecutable",
        "short_description": "Proceso de discovery, prototipado y arquitectura para proyectos empresariales.",
        "full_description": "Acompañamiento para convertir necesidades de negocio en una ruta técnica viable.",
        "status": "Caso documentado",
        "featured": False,
        "technologies": ["Vue 3", "Python", "AWS"],
        "publication_status": PublicationStatus.published,
    },
]

CASE_STUDIES = [
    {
        "project_slug": "plataforma-financiera-sap",
        "slug": "finanzas-sap",
        "title": "Control empresarial conectado con SAP y AWS",
        "challenge": "La información financiera vivía en distintos puntos y requería seguimiento manual para completar procesos internos.",
        "solution": "Una plataforma web modular conectada a servicios OData y funciones en AWS para consultar, validar y procesar información.",
        "architecture": "Frontend Vue, integración SAP OData y funciones de backend desplegadas en AWS.",
        "results": "Flujos más claros, datos centralizados y una base reutilizable para nuevas herramientas operativas.",
    },
    {
        "project_slug": "experiencia-retail-interactiva",
        "slug": "retail-interactivo",
        "title": "Contenido que reacciona a cada interacción",
        "challenge": "Las pantallas mostraban contenido estático y no respondían a la presencia o acciones de los visitantes.",
        "solution": "Una experiencia basada en sensores y controladores para activar contenido, iluminación y secuencias en tiempo real.",
        "architecture": "Reproductores de contenido conectados con sensores, Raspberry Pi y controladores locales.",
        "results": "Una experiencia diferenciada, administrable y preparada para replicarse en nuevos espacios.",
    },
    {
        "project_slug": "preventa-tecnologica-b2b",
        "slug": "preventa-b2b",
        "title": "De necesidades ambiguas a propuestas ejecutables",
        "challenge": "Los proyectos comenzaban con ideas amplias, múltiples involucrados y poca definición técnica.",
        "solution": "Un proceso de discovery, prototipado y documentación para convertir necesidades en alcances, demos y rutas de implementación.",
        "architecture": "Discovery funcional, prototipos navegables, arquitectura de referencia y roadmap de implementación.",
        "results": "Mejor alineación entre negocio y tecnología, menos incertidumbre y decisiones de inversión más claras.",
    },
]


def slugify(value: str) -> str:
    return value.lower().replace(" ", "-").replace(".", "")


def run() -> None:
    with SessionLocal() as db:
        technology_by_name: dict[str, Technology] = {}
        for name in TECHNOLOGIES:
            technology = db.scalar(select(Technology).where(Technology.name == name))
            if not technology:
                technology = Technology(name=name, slug=slugify(name))
                db.add(technology)
            technology_by_name[name] = technology
        db.flush()

        project_by_slug: dict[str, Project] = {}
        for item in PROJECTS:
            project_data = item.copy()
            project = db.scalar(select(Project).where(Project.slug == project_data["slug"]))
            if project:
                if "publication_status" in project_data:
                    project.publication_status = project_data["publication_status"]
                project_by_slug[project.slug] = project
                continue
            technology_names = project_data.pop("technologies")
            publication_status = project_data.pop("publication_status", PublicationStatus.published)
            project = Project(
                **project_data,
                publication_status=publication_status,
                published_at=datetime.now(UTC),
                technologies=[technology_by_name[name] for name in technology_names],
            )
            db.add(project)
            project_by_slug[project.slug] = project
        db.flush()

        for item in CASE_STUDIES:
            study_data = item.copy()
            if db.scalar(select(CaseStudy).where(CaseStudy.slug == study_data["slug"])):
                continue
            project_slug = study_data.pop("project_slug")
            db.add(CaseStudy(
                **study_data,
                project=project_by_slug[project_slug],
                publication_status=PublicationStatus.published,
                published_at=datetime.now(UTC),
            ))
        db.commit()


if __name__ == "__main__":
    run()
