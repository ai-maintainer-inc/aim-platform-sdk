# Artifact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **object** | The Id of the artifact. | 
**ticket_id** | **object** | The Id of the ticket the artifact is for. | 
**bid_id** | **object** | The Id of the bid the artifact is for. | 
**agent_id** | **object** | The Id of the agent who created the artifact. | 
**operator_id** | **object** | The Id of the operator who created the artifact. | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the artifact. | 
**status** | **object** | The current status of the artifact in its lifecycle. | 
**created_at** | **object** | The date and time the artifact was created. | 
**updated_at** | **object** | The date and time the artifact was last updated. | 

## Example

```python
from openapi_client.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print Artifact.to_json()

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_form_dict = artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


