# CreateRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **object** | The unique name of the repository. | 
**is_public** | **object** | Whether the repository is public. | 

## Example

```python
from aim_platform_sdk.models.create_repository_request import CreateRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRepositoryRequest from a JSON string
create_repository_request_instance = CreateRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print CreateRepositoryRequest.to_json()

# convert the object into a dict
create_repository_request_dict = create_repository_request_instance.to_dict()
# create an instance of CreateRepositoryRequest from a dict
create_repository_request_form_dict = create_repository_request.from_dict(create_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


