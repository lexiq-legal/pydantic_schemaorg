from pydantic import Field
from pydantic_schemaorg.BlogPosting import BlogPosting
from typing import List, Optional, Any, Union
from pydantic_schemaorg.CreativeWork import CreativeWork


class Blog(CreativeWork):
    """A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a \"weblog\"."
     "Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloqually"
     "referred to by the same term.

    See https://schema.org/Blog.

    """
    type_: str = Field("Blog", const=True, alias='@type')
    blogPosts: Optional[Union[List[Union[BlogPosting, str]], Union[BlogPosting, str]]] = Field(
        None,
        description="Indicates a post that is part of a [[Blog]]. Note that historically, what we term a \"Blog\""
     "was once known as a \"weblog\", and that what we term a \"BlogPosting\" is now often colloquially"
     "referred to as a \"blog\".",
    )
    blogPost: Optional[Union[List[Union[BlogPosting, str]], Union[BlogPosting, str]]] = Field(
        None,
        description="A posting that is part of this blog.",
    )
    issn: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    

Blog.update_forward_refs()
