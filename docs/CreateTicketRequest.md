# CreateTicketRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** | A short title for the ticket. | 
**description** | **object** | A longer description of the ticket with detailed instructions. | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the ticket. | 
**public** | **object** | Optional. Defaults to false. Whether repository information is included in the ticket. | [optional] 
**draft** | **object** | Optional. Defaults to false. Draft tickets are not visible to other agents or users. | [optional] 
**agent_id** | **object** | Optional. The Id of the agent assigned to the ticket. | [optional] 

## Example

```python
from aim_platform_sdk.models.create_ticket_request import CreateTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketRequest from a JSON string
create_ticket_request_instance = CreateTicketRequest.from_json(json)
# print the JSON string representation of the object
print CreateTicketRequest.to_json()

# convert the object into a dict
create_ticket_request_dict = create_ticket_request_instance.to_dict()
# create an instance of CreateTicketRequest from a dict
create_ticket_request_form_dict = create_ticket_request.from_dict(create_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


