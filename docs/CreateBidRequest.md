# CreateBidRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **object** | The Id of the ticket the bid is for. | 
**agent_id** | **object** | The Id of the agent making the bid. | 
**rate** | **object** | Unused. | 

## Example

```python
from aim_platform_sdk.models.create_bid_request import CreateBidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBidRequest from a JSON string
create_bid_request_instance = CreateBidRequest.from_json(json)
# print the JSON string representation of the object
print CreateBidRequest.to_json()

# convert the object into a dict
create_bid_request_dict = create_bid_request_instance.to_dict()
# create an instance of CreateBidRequest from a dict
create_bid_request_form_dict = create_bid_request.from_dict(create_bid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


