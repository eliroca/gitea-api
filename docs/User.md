# User

User represents a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is user active | [optional] 
**avatar_url** | **str** | URL to the user&#39;s avatar | [optional] 
**created** | **datetime** |  | [optional] 
**description** | **str** | the user&#39;s description | [optional] 
**email** | **str** |  | [optional] 
**followers_count** | **int** | user counts | [optional] 
**following_count** | **int** |  | [optional] 
**full_name** | **str** | the user&#39;s full name | [optional] 
**html_url** | **str** | URL to the user&#39;s gitea page | [optional] 
**id** | **int** | the user&#39;s id | [optional] 
**is_admin** | **bool** | Is the user an administrator | [optional] 
**language** | **str** | User locale | [optional] 
**last_login** | **datetime** |  | [optional] 
**location** | **str** | the user&#39;s location | [optional] 
**login** | **str** | the user&#39;s username | [optional] 
**login_name** | **str** | the user&#39;s authentication sign-in name. | [optional] [default to 'empty']
**prohibit_login** | **bool** | Is user login prohibited | [optional] 
**restricted** | **bool** | Is user restricted | [optional] 
**source_id** | **int** | The ID of the user&#39;s Authentication Source | [optional] 
**starred_repos_count** | **int** |  | [optional] 
**visibility** | **str** | User visibility level option: public, limited, private | [optional] 
**website** | **str** | the user&#39;s website | [optional] 

## Example

```python
from gitea_api.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


