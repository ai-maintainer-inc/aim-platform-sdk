# CreateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **object** | The unique name of the user. | 
**email** | **object** | The email address of the user. | 
**password** | **object** | The password of the user. | 

## Example

```python
from openapi_client.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserRequest.to_json()

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_form_dict = create_user_request.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


