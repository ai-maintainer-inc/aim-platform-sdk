# ManageUserBidRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bid_id** | **object** | The Id of the bid. | 
**action** | **object** | The action to take on the bid. | 

## Example

```python
from openapi_client.models.manage_user_bid_request import ManageUserBidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManageUserBidRequest from a JSON string
manage_user_bid_request_instance = ManageUserBidRequest.from_json(json)
# print the JSON string representation of the object
print ManageUserBidRequest.to_json()

# convert the object into a dict
manage_user_bid_request_dict = manage_user_bid_request_instance.to_dict()
# create an instance of ManageUserBidRequest from a dict
manage_user_bid_request_form_dict = manage_user_bid_request.from_dict(manage_user_bid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


