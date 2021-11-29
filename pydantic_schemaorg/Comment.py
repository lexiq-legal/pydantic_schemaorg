from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed"
     "via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.

    See https://schema.org/Comment.

    """

    downvoteCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of downvotes this question, answer or comment has received from the community.",
    )
    upvoteCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of upvotes this question, answer or comment has received from the community.",
    )
    parentItem: Any = Field(
        None,
        description="The parent of a question, answer or item in general.",
    )
    locals().update({"@type": Field("Comment", const=True)})


Comment.update_forward_refs()
