# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** | The Id of the user. | 
**user_name** | **object** | The unique name of the user. | 
**email** | **object** | The email address of the user. | 
**created_at** | **object** | The date and time the user was created. | 
**updated_at** | **object** | The date and time the user was last updated. | 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


