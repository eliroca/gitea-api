# CreatePullReviewCommentReplyOptions

CreatePullReviewCommentReplyOptions are options to reply to a pull request review comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | [optional] 

## Example

```python
from gitea_api.models.create_pull_review_comment_reply_options import CreatePullReviewCommentReplyOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePullReviewCommentReplyOptions from a JSON string
create_pull_review_comment_reply_options_instance = CreatePullReviewCommentReplyOptions.from_json(json)
# print the JSON string representation of the object
print(CreatePullReviewCommentReplyOptions.to_json())

# convert the object into a dict
create_pull_review_comment_reply_options_dict = create_pull_review_comment_reply_options_instance.to_dict()
# create an instance of CreatePullReviewCommentReplyOptions from a dict
create_pull_review_comment_reply_options_from_dict = CreatePullReviewCommentReplyOptions.from_dict(create_pull_review_comment_reply_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


