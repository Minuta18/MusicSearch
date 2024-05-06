import pytest
import httpx
import main
from tests import conftest

client = httpx.AsyncClient(
    app=main.fastapi_app, 
    base_url=f'http://127.0.0.1:6002{main.app.PREFIX}/{main.app.SERVICE_NAME}'
)

@pytest.mark.asyncio
async def create_track_test():
    responce = await client.post('/create', json={
        'title': 'Created track',
        'description': 'Created track description',
        'author_id': 1,
        'origin_url': 'https://this.is.link/something/okay/nu_ok?ok=true',
    })

    assert responce.status_code == 201

    responce_json = responce.json()
    
    assert responce_json['error'] == False
    assert responce_json['track']['id'] is not None
    assert responce_json['track']['name'] == 'Created track'
    assert responce_json['track']['description'] == 'Created track description'
    assert responce_json['track']['download_link'] is None
    assert responce_json['track']['length'] is None
    assert responce_json['track']['origin_url'] == \
        'https://this.is.link/something/okay/nu_ok?ok=true'
    assert responce_json['track']['short_origin_url'] == \
        'is.link/something/okay/nu_ok'
    
    responce2 = await client.post('/create', json={
        'title': 'Create Track',
        'description': 'Another description',
        'author_id': 1,
        'origin_url': 'https://this.is.also.link',
    })
    
    assert responce2.status_code == 201
    
    responce2_json = responce2.json()
    
    assert responce2_json['error'] == False
    assert responce2_json['track']['id'] is not None
    assert responce2_json['track']['id'] != responce_json['track']['json']
    assert responce2_json['track']['description'] == 'Another description'
    assert responce2_json['track']['download_link'] is None
    assert responce2_json['track']['length'] is None
    assert responce2_json['track']['origin_url'] == \
        'https://this.is.also.link'
    assert responce2_json['track']['short_origin_url'] == \
        'this.is.also.link'
    