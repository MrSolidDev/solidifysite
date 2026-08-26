def project_payload(publication_status: str = "draft") -> dict:
    return {
        "slug": "duit",
        "name": "DUIT",
        "tagline": "Producto de prueba",
        "short_description": "Descripción corta",
        "full_description": "Descripción completa",
        "status": "Activo",
        "featured": True,
        "publication_status": publication_status,
        "technology_ids": [],
    }


def test_liveness(client):
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_admin_routes_require_authentication(client):
    response = client.get("/api/admin/projects")
    assert response.status_code == 401


def test_admin_mutation_requires_csrf(admin_client):
    client, _headers = admin_client
    response = client.post("/api/admin/projects", json=project_payload())
    assert response.status_code == 403


def test_draft_is_hidden_and_published_project_is_public(admin_client):
    client, headers = admin_client
    draft = client.post("/api/admin/projects", json=project_payload(), headers=headers)
    assert draft.status_code == 201
    assert client.get("/api/projects").json() == []

    project_id = draft.json()["id"]
    published = client.patch(
        f"/api/admin/projects/{project_id}",
        json={"publication_status": "published"},
        headers=headers,
    )
    assert published.status_code == 200

    public = client.get("/api/projects/duit")
    assert public.status_code == 200
    assert public.json()["name"] == "DUIT"


def test_duplicate_slug_returns_conflict(admin_client):
    client, headers = admin_client
    assert client.post("/api/admin/projects", json=project_payload(), headers=headers).status_code == 201
    assert client.post("/api/admin/projects", json=project_payload(), headers=headers).status_code == 409


def test_published_case_study_includes_project(admin_client):
    client, headers = admin_client
    project = client.post("/api/admin/projects", json=project_payload("published"), headers=headers).json()
    response = client.post(
        "/api/admin/case-studies",
        headers=headers,
        json={
            "project_id": project["id"],
            "slug": "duit-case",
            "title": "Caso DUIT",
            "challenge": "Un reto concreto",
            "solution": "Una solución concreta",
            "results": "Un resultado medible",
            "publication_status": "published",
        },
    )
    assert response.status_code == 201
    public = client.get("/api/case-studies/duit-case")
    assert public.status_code == 200
    assert public.json()["project"]["name"] == "DUIT"
    product = client.get("/api/projects/duit")
    assert product.status_code == 200
    assert product.json()["case_studies"][0]["slug"] == "duit-case"

    second = client.post(
        "/api/admin/case-studies",
        headers=headers,
        json={
            "project_id": project["id"],
            "slug": "duit-case-two",
            "title": "Segundo caso DUIT",
            "challenge": "Otro reto",
            "solution": "Otra solución",
            "results": "Otro resultado",
            "publication_status": "published",
        },
    )
    assert second.status_code == 201
    product = client.get("/api/projects/duit")
    assert len(product.json()["case_studies"]) == 2
