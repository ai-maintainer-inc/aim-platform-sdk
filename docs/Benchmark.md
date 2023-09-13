# Benchmark


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark_id** | **object** | The Id of the benchmark. | 
**title** | **object** | A short title for the benchmark task. | 
**description** | **object** | A longer description of the benchmark with detailed instructions. | 
**link** | **object** | A link to the original benchmark design (e.g. github). | 
**author_id** | **object** | The Id of the author of the benchmark. | 
**author_name** | **object** | The unique name of the author of the benchmark. | 
**public** | **object** | Whether repository information is included in the benchmark. | 
**code** | [**Code**](Code.md) | Information about the code repository associated with the benchmark. | [optional] 
**difficulty** | **object** | The difficulty of the benchmark. | 
**created_at** | **object** | The date and time the benchmark was created. | 
**updated_at** | **object** | The date and time the benchmark was last updated. | 

## Example

```python
from aim_platform_sdk.models.benchmark import Benchmark

# TODO update the JSON string below
json = "{}"
# create an instance of Benchmark from a JSON string
benchmark_instance = Benchmark.from_json(json)
# print the JSON string representation of the object
print Benchmark.to_json()

# convert the object into a dict
benchmark_dict = benchmark_instance.to_dict()
# create an instance of Benchmark from a dict
benchmark_form_dict = benchmark.from_dict(benchmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


