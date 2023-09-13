# Repository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_id** | **object** | The Id of the repository. | 
**owner_id** | **object** | The Id of the owner of the repository. | 
**owner_name** | **object** | The unique name of the owner of the repository. | 
**repository_name** | **object** | The unique name of the repository. | 
**created_at** | **object** | The date and time the repository was created. | 
**updated_at** | **object** | The date and time the repository was last updated. | 
**is_public** | **object** | Whether the repository is public. | 

## Example

```python
from aim_platform_sdk.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print Repository.to_json()

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_form_dict = repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


