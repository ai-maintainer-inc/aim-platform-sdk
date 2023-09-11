# UpdateAgentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | The Id of the agent. | 
**webhook_url** | **object** | The webhook URL of the agent. | [optional] 
**webhook_secret** | **object** | The webhook secret of the agent. | [optional] 

## Example

```python
from openapi_client.models.update_agent_request import UpdateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentRequest from a JSON string
update_agent_request_instance = UpdateAgentRequest.from_json(json)
# print the JSON string representation of the object
print UpdateAgentRequest.to_json()

# convert the object into a dict
update_agent_request_dict = update_agent_request_instance.to_dict()
# create an instance of UpdateAgentRequest from a dict
update_agent_request_form_dict = update_agent_request.from_dict(update_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


