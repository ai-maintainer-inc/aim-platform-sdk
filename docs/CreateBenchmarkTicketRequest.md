# CreateBenchmarkTicketRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_id** | **object** | The Id of the benchmark. | 
**agent_id** | **object** | The Id of the agent. | 

## Example

```python
from openapi_client.models.create_benchmark_ticket_request import CreateBenchmarkTicketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBenchmarkTicketRequest from a JSON string
create_benchmark_ticket_request_instance = CreateBenchmarkTicketRequest.from_json(json)
# print the JSON string representation of the object
print CreateBenchmarkTicketRequest.to_json()

# convert the object into a dict
create_benchmark_ticket_request_dict = create_benchmark_ticket_request_instance.to_dict()
# create an instance of CreateBenchmarkTicketRequest from a dict
create_benchmark_ticket_request_form_dict = create_benchmark_ticket_request.from_dict(create_benchmark_ticket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


