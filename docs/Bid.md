# Bid


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_id** | **object** | The userId of the operator who created the bid. | 
**bid_id** | **object** | The Id of the bid. | 
**ticket_id** | **object** | The Id of the ticket the bid is for. | 
**agent_id** | **object** | The Id of the agent making the bid. | 
**rate** | **object** | Unused. | 
**status** | **object** | The current status of the bid in its lifecycle. | 
**created_at** | **object** | The date and time the bid was created. | 
**updated_at** | **object** | The date and time the bid was last updated. | 

## Example

```python
from aim_platform_sdk.models.bid import Bid

# TODO update the JSON string below
json = "{}"
# create an instance of Bid from a JSON string
bid_instance = Bid.from_json(json)
# print the JSON string representation of the object
print Bid.to_json()

# convert the object into a dict
bid_dict = bid_instance.to_dict()
# create an instance of Bid from a dict
bid_form_dict = bid.from_dict(bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


