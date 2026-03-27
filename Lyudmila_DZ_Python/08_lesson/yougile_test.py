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
    resp = requests.put(base_url + 'projects/{id}', json=body, headers=my_h)
    
    
def test_put_project_id_negative():
    body = {"title": "ГосУслуги"}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.post(base_url + 'projects', json=body, headers=my_h)        
    response_body = resp.json()
    id = response_body["id"]       
    resp = requests.put(base_url + 'projects/{id}', json=body, headers=my_h) 
    assert resp.status_code == 404
 
       
def test_get_project_id_negative():   
    body = {}
    my_h = {'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.get(base_url + 'projects/{id}', json=body, headers=my_h)        
    response_body = resp.json()
    projects_id= [""]
    assert resp.status_code == 404   


def test_get_project_id_positive():   
    body = {"id": " "}
    my_h = { 'Authorization': f"Bearer {token}", 'Content-Type':'application/json'}
    resp = requests.get(base_url + 'projects/{id}', json=body, headers=my_h)        
    response_body = resp.json()
    projects_id= [""]
    resp.status_code == 200
    