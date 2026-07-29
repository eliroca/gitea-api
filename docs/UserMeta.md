# UserMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the user | [optional] 
**login** | **str** | The username of the user | [optional] 

## Example

```python
from gitea_api.models.user_meta import UserMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UserMeta from a JSON string
user_meta_instance = UserMeta.from_json(json)
# print the JSON string representation of the object
print(UserMeta.to_json())

# convert the object into a dict
user_meta_dict = user_meta_instance.to_dict()
# create an instance of UserMeta from a dict
user_meta_from_dict = UserMeta.from_dict(user_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


