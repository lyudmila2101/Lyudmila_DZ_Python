import requests

base_url = "https://ru.yougile.com/api-v2/"
token = "pG0namDifosJoTYq5MKHk9f9wsO0RB1iLc82RmI7KDyiJBJKGAGD9kgPmgYO1R9B"



def test_post_project_positive():
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.post(base_url + 'projects', json=body, headers=my_h)    
    response_body = resp.json() 
    assert response_body["id"] is not None  
    assert resp.status_code == 201
    

def test_post_project_negative():
    body = {"title": ""}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.post(base_url + 'projects', json=body, headers=my_h)    
    response_body = resp.json()     
    assert resp.status_code == 400


def test_put_project_id_positive():
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.post(base_url + 'projects', json=body, headers=my_h)        
    response_body = resp.json()
    id = response_body["id"]  
    assert resp.status_code == 201
    body = {"title": "фнс"}
    resp = requests.put(f'{base_url}projects/{id}', json=body, headers=my_h)
    assert resp.status_code == 200
    # получаем проект по id
    resp = requests.get(f'{base_url}projects/{id}', headers=my_h)
    response_body = resp.json()
    assert response_body["title"] == "фнс"
    
    
def test_put_project_id_negative():
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.post(base_url + 'projects', json=body, headers=my_h)        
    response_body = resp.json()
    id = response_body["id"]  
    assert resp.status_code == 201
    body = {"title": ""}
    resp = requests.put(f'{base_url}projects/{id}', json=body, headers=my_h)
    assert resp.status_code == 400
    # получаем проект по id
    resp = requests.get(f'{base_url}projects/{id}', headers=my_h)
    response_body = resp.json()
    assert response_body["title"] == "ГосУслуги"
    
 
       
def test_get_project_id_negative(): 
    '''запрос проекта без ключа''' 
    # формируем заголовки и тело
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    # создаём проект
    resp = requests.post(base_url + 'projects', json=body, headers=my_h) 
    # запоминаем id       
    response_body = resp.json()
    id = response_body["id"]  
    assert resp.status_code == 201    
    # получаем проект по id
    my_h = {'Content-Type':'application/json'}
    resp = requests.get(f'{base_url}projects/{id}', headers=my_h)
    assert resp.status_code == 401

def test_get_project_id_positive():   
    '''запрос проекта без ключа''' 
    # формируем заголовки и тело
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    # создаём проект
    resp = requests.post(base_url + 'projects', json=body, headers=my_h) 
    # запоминаем id       
    response_body = resp.json()
    id = response_body["id"]  
    assert resp.status_code == 201        
    # получаем проект по id
    resp = requests.get(f'{base_url}projects/{id}', headers=my_h)
    response_body = resp.json()
    assert resp.status_code == 200
    assert response_body["title"] == "ГосУслуги"
    