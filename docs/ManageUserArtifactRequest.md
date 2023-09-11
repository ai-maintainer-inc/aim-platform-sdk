# ManageUserArtifactRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **object** | The Id of the artifact. | 
**action** | **object** | The action to take on the artifact. | 

## Example

```python
from aim_platform_sdk.models.manage_user_artifact_request import ManageUserArtifactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageUserArtifactRequest from a JSON string
manage_user_artifact_request_instance = ManageUserArtifactRequest.from_json(json)
# print the JSON string representation of the object
print ManageUserArtifactRequest.to_json()

# convert the object into a dict
manage_user_artifact_request_dict = manage_user_artifact_request_instance.to_dict()
# create an instance of ManageUserArtifactRequest from a dict
manage_user_artifact_request_form_dict = manage_user_artifact_request.from_dict(manage_user_artifact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


