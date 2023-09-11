# CreateArtifactRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_id** | **object** | The Id of the bid the artifact is for. | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the artifact. | 
**draft** | **object** | Optional. Defaults to false. Draft artifacts are only visible to their authors. | [optional] 

## Example

```python
from openapi_client.models.create_artifact_request import CreateArtifactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateArtifactRequest from a JSON string
create_artifact_request_instance = CreateArtifactRequest.from_json(json)
# print the JSON string representation of the object
print CreateArtifactRequest.to_json()

# convert the object into a dict
create_artifact_request_dict = create_artifact_request_instance.to_dict()
# create an instance of CreateArtifactRequest from a dict
create_artifact_request_form_dict = create_artifact_request.from_dict(create_artifact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


