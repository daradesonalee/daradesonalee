import requests
import json
import yaml
import os
from libs.api_body import ApiBody
import random

class PetLibs(ApiBody):

    def __init__(self):
        file_path="configs/{}.yaml".format(os.environ['TEST_ENV'])
        print("Executing test case on {} environment ".format(os.environ['TEST_ENV']))
        with open(file_path) as f:
            self.configs = yaml.safe_load(f)

        self.base_url=self.configs.get('base_url')


    def get_pet(self,url):
        print("I am in get_pet method")
        response = requests.get(url=self.base_url+url)
        assert response.status_code == 200
        json_data = json.loads(response.text)
        print("Response converted to json")

        return json_data

    def get_pet_by_id(self,id):
        print("I am in get_pet method")
        response = requests.get(url=self.base_url+str(id))
        assert response.status_code == 200
        json_data = json.loads(response.text)
        print("Response converted to json")

        return json_data

    def get_random_id(self):
        id = random.randrange(1, 1000 ** 3)

        return id

    def create_pet(self,name='test_name',status='sold'):
        headers = {"Content-Type": "application/json"}
        body=self.create_pet_body
        pet_id=self.get_random_id()
        body['id']=pet_id
        body['status']=status
        body['name']=name
        response = requests.post(url=self.base_url, json=body, headers=headers)
        assert response.status_code == 200
        print("Pet is created with id {} and with status {} and name is {}".format(pet_id,status,name))

        json_data = json.loads(response.text)
        print("Response converted to json")

        return json_data
