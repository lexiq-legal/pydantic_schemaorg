from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed"
     "via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.

    See: https://schema.org/Comment
    Model depth: 3
    """

    type_: str = Field("Comment", const=True, alias="@type")
    downvoteCount: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="The number of downvotes this question, answer or comment has received from the community.",
    )
    upvoteCount: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="The number of upvotes this question, answer or comment has received from the community.",
    )
    parentItem: "Optional[Union[List[Union['Comment', str]], Union['Comment', str]]]" = Field(
        None,
        description="The parent of a question, answer or item in general.",
    )


if TYPE_CHECKING:

    Comment.update_forward_refs()
