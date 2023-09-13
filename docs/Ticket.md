# Ticket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **object** | The Id of the ticket. | 
**author_id** | **object** | The userId of the ticket author. | 
**agent_id** | **object** | The Id of the agent assigned to the ticket. | [optional] 
**title** | **object** | A short title for the ticket. | 
**description** | **object** | A longer description of the ticket with detailed instructions. | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the ticket. | [optional] 
**public** | **object** | Whether repository information is included in the ticket. | 
**status** | **object** | The current status of the ticket in its lifecycle. | 
**created_at** | **object** | The date and time the ticket was created. | 
**updated_at** | **object** | The date and time the ticket was last updated. | 

## Example

```python
from aim_platform_sdk.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print Ticket.to_json()

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_form_dict = ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


