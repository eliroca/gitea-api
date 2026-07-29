# TopicListResponse

TopicListResponse returns a list of TopicResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | [**List[TopicResponse]**](TopicResponse.md) |  | [optional] 

## Example

```python
from gitea_api.models.topic_list_response import TopicListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicListResponse from a JSON string
topic_list_response_instance = TopicListResponse.from_json(json)
# print the JSON string representation of the object
print(TopicListResponse.to_json())

# convert the object into a dict
topic_list_response_dict = topic_list_response_instance.to_dict()
# create an instance of TopicListResponse from a dict
topic_list_response_from_dict = TopicListResponse.from_dict(topic_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


