# CreateBenchmarkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **object** | A short title for the benchmark task. | 
**description** | **object** | A longer description of the benchmark with detailed instructions. | 
**link** | **object** | A link to the original benchmark design (e.g. github). | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the benchmark. | 
**public** | **object** | Optional. Defaults to false. Whether repository information is included in the benchmark. | [optional] 
**difficulty** | **object** | The difficulty of the benchmark. | 

## Example

```python
from aim_platform_sdk.models.create_benchmark_request import CreateBenchmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBenchmarkRequest from a JSON string
create_benchmark_request_instance = CreateBenchmarkRequest.from_json(json)
# print the JSON string representation of the object
print CreateBenchmarkRequest.to_json()

# convert the object into a dict
create_benchmark_request_dict = create_benchmark_request_instance.to_dict()
# create an instance of CreateBenchmarkRequest from a dict
create_benchmark_request_form_dict = create_benchmark_request.from_dict(create_benchmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


