# UpdateRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **object** | The unique name of the repository. | 
**is_public** | **object** | Whether the repository is public. | 

## Example

```python
from openapi_client.models.update_repository_request import UpdateRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRepositoryRequest from a JSON string
update_repository_request_instance = UpdateRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRepositoryRequest.to_json()

# convert the object into a dict
update_repository_request_dict = update_repository_request_instance.to_dict()
# create an instance of UpdateRepositoryRequest from a dict
update_repository_request_form_dict = update_repository_request.from_dict(update_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


