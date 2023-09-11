# BenchmarkTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_ticket_id** | **object** | The Id of the benchmark ticket. | 
**benchmark_id** | **object** | The Id of the benchmark. | 
**ticket_id** | **object** | The Id of the ticket. | 
**agent_id** | **object** | The Id of the agent. | 
**attempt** | **object** | The attempt number of the benchmark ticket. | 
**created_at** | **object** | The date and time the benchmark ticket was created. | 
**updated_at** | **object** | The date and time the benchmark ticket was last updated. | 

## Example

```python
from openapi_client.models.benchmark_ticket import BenchmarkTicket

# TODO update the JSON string below
json = "{}"
# create an instance of BenchmarkTicket from a JSON string
benchmark_ticket_instance = BenchmarkTicket.from_json(json)
# print the JSON string representation of the object
print BenchmarkTicket.to_json()

# convert the object into a dict
benchmark_ticket_dict = benchmark_ticket_instance.to_dict()
# create an instance of BenchmarkTicket from a dict
benchmark_ticket_form_dict = benchmark_ticket.from_dict(benchmark_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


