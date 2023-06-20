
# get,post,put,delete,patch

import requests
import json

base_url="https://petstore.swagger.io/v2/pet/"

GET_PET_BY_STATUS="findByStatus?status={}"
GET_PET_BY_TAGS="findByTags?tags={}"


pet_status=["available","sold","unavailable","pending","newstatus"]
pet_tags=["string"]

# Verify pet by status
# for status in pet_status:
#     response=requests.get(url=base_url+GET_PET_BY_STATUS.format(status))
#
#     json_data=json.loads(response.text)
#     # assert actual_data == expected_data ,"If you want to provide any msg"
#
#     assert  response.status_code == 200
#
#     print("****Veryfying test data for the status {}".format(status))
#     for record in json_data:
#         assert record[
#                    'status'] == status, "status is not correct for id {} status should be available but showing {}".format(
#             record["id"], record["status"])


#Verify pet by tag
# for tag in pet_tags:
#     response = requests.get(url=base_url + GET_PET_BY_TAGS.format(tag))
#
#     json_data=json.loads(response.text)
#     # assert actual_data == expected_data ,"If you want to provide any msg"
#
#     assert  response.status_code == 200
#
#     print("****Veryfying test data for the tag {}".format(tag))
#     for record in json_data:
#         assert record[
#                    'tags'][0]['name'] == tag, "status is not correct for id {} tag should be {} but showing {}".format(
#             tag,record["id"], record["tags"][0]['name'])


# Create pet using post method
import random
id=random.randrange(1,1000**3)
name="test_data"
body={
  "name": "{}",
  "photoUrls": [
    "dolore Excepteur est",
    "consequat in labore"
  ],
  "id": id,
  "category": {
    "id": -29245128,
    "name": "incididunt"
  },
  "tags": [
    {
      "id": -55902183,
      "name": "Lorem laboris nulla"
    },
    {
      "id": 67424482,
      "name": "incididunt ipsum eiusmod"
    }
  ],
  "status": "{}"
}

headers={"Content-Type":"application/json"}


# for status in pet_status:
#     body['status']=status
#     response = requests.post(url=base_url, json=body, headers=headers)
#     response.status_code=200
#     assert response.status_code == 200 ,"status is not as per expectation"
#     json_data=json.loads(response.text)
#     assert json_data['status']==status


body['status']='available'
body['name']=name
#create pet
response = requests.post(url=base_url, json=body, headers=headers)
response.status_code=200

#verify pet is created in get response using petid
response=requests.get(base_url+str(id))
response.status_code=200
json_data=json.loads(response.text)
#name #status #id
assert json_data['status']=='available'
assert json_data['name']==name
assert json_data['id']==id

name='updated_pet_name'
body['name']=name
body['status']='sold'

response = requests.put(url=base_url, json=body, headers=headers)
response.status_code=200

#verify pet is created in get response using petid
response=requests.get(base_url+str(id))
response.status_code=200
json_data=json.loads(response.text)
assert json_data['status']=='sold'
assert json_data['name']==name
assert json_data['id']==id

#verify if pet is deleted
response=requests.delete(base_url+str(id))
assert response.status_code==200

response=requests.get(base_url+str(id))
assert response.status_code==404

#create pet
#verify pet is created in get response using petid
#Update pet using put
#delete that pet
#verify if pet is deleted

#oops concepts + pytest framework

#pytest,robot,nose2,behave,unittest,testng,cucumber,junit,nunit,pytest-bdd,hpQTP

#BDD,TDD,keyword