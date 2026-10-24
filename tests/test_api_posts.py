
import requests
import pytest
from jsonschema import validate, ValidationError
from schemas import POST_SCHEMA
from test_data import NUEVO_POST


@pytest.mark.parametrize("id_post", [1, 2, 3])
def test_obtener_post(base_url, id_post):
    url = f"{base_url}/posts/{id_post}"

    
    try:
        respuesta = requests.get(url, timeout=10)

    except requests.exceptions.Timeout:
        pytest.fail(
            f"Timeout: la API tardó demasiado "
            f"al consultar el post {id_post}"
        )

    except requests.exceptions.ConnectionError as error:
        pytest.fail(
            f"Error de conexión al consultar "
            f"el post {id_post}: {error}"
        )


    # Validar el codigo HTTP
    assert respuesta.status_code == 200, (
    f"Error al consultar el post {id_post}. "
    f"Se esperaba HTTP 200, pero se recibió HTTP {respuesta.status_code}. "
    f"Respuesta: {respuesta.text[:200]}"
)

    # Validar que la respuesta contiene JSON
    assert "application/json" in respuesta.headers["Content-Type"]

    # Validar el contenido JSON
    datos = respuesta.json()

    assert datos["id"] == id_post
    assert datos["userId"] == 1
    assert isinstance(datos["title"], str)
    assert isinstance(datos["body"], str)



def test_obtener_post_inexistente(base_url):
    url = f"{base_url}/posts/999999"

    respuesta = requests.get(url, timeout=10)

    # Verificar que el recurso no existe
    assert respuesta.status_code == 404



def test_crear_post(base_url):
    url = f"{base_url}/posts"

    respuesta = requests.post(
        url,
        json=NUEVO_POST,
        timeout=10
    )

    # Validar codigo HTTP
    assert respuesta.status_code == 201

    # Validar los datos recibidos
    datos = respuesta.json()

    assert datos["title"] == NUEVO_POST["title"]
    assert datos["body"] == NUEVO_POST["body"]
    assert datos["userId"] == NUEVO_POST["userId"]
    assert "id" in datos



def test_actualizar_post(base_url):
    url = f"{base_url}/posts/1"

    post_actualizado = {
        "id": 1,
        "title": "Post actualizado por QA",
        "body": "Prueba automatizada del metodo PUT",
        "userId": 1
    }

    respuesta = requests.put(
        url,
        json=post_actualizado,
        timeout=10
    )

    # Validar el codigo HTTP
    assert respuesta.status_code == 200

    # Validar el contenido actualizado
    datos = respuesta.json()

    assert datos["id"] == 1
    assert datos["title"] == post_actualizado["title"]
    assert datos["body"] == post_actualizado["body"]
    assert datos["userId"] == 1


def test_eliminar_post(base_url):
    url = f"{base_url}/posts/1"

    respuesta = requests.delete(
        url,
        timeout=10
    )

    # Validar que la API acepta la eliminación
    assert respuesta.status_code == 200




@pytest.mark.parametrize("id_post", [1, 2, 3])
def test_validar_schema_post(base_url, id_post):
    url = f"{base_url}/posts/{id_post}"

    respuesta = requests.get(url, timeout=10)

    # Validar codigo HTTP
    assert respuesta.status_code == 200

    # Obtener datos JSON
    datos = respuesta.json()

    # Validar estructura utilizando JSON Schema
    validate(instance=datos, schema=POST_SCHEMA)

    # Validar que recibimos el post solicitado
    assert datos["id"] == id_post



def test_schema_rechaza_datos_invalidos():
    # Simular una respuesta JSON incorrecta
    post_invalido = {
        "userId": 1,
        "id": 1,
        "title": 12345,
        "body": "Contenido de prueba"
    }

    # Verificar que el esquema detecta el error
    with pytest.raises(ValidationError):
        validate(
            instance=post_invalido,
            schema=POST_SCHEMA
        )
