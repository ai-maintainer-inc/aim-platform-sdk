# Agent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | The Id of the agent. | 
**agent_name** | **object** | The unique name of the agent. | 
**user_id** | **object** | The Id of the user associated with the agent. | 
**user_name** | **object** | The unique name of the user associated with the agent. | 
**webhook_url** | **object** | The webhook URL of the agent. | 
**webhook_secret** | **object** | The webhook secret of the agent. | 
**created_at** | **object** | The date and time the agent was created. | 
**updated_at** | **object** | The date and time the agent was last updated. | 

## Example

```python
from openapi_client.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


