# Code

Information about where to find the code associated with a ticket or artifact.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **object** | The userName of the code repository owner. | 
**repo** | **object** | The name of the code repository. | 
**branch** | **object** | The name of the relevant branch in the code repository. | 
**commit** | **object** | The commit hash of the relevant commit in the code repository. | 

## Example

```python
from aim_platform_sdk.models.code import Code

# TODO update the JSON string below
json = "{}"
# create an instance of Code from a JSON string
code_instance = Code.from_json(json)
# print the JSON string representation of the object
print Code.to_json()

# convert the object into a dict
code_dict = code_instance.to_dict()
# create an instance of Code from a dict
code_form_dict = code.from_dict(code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


