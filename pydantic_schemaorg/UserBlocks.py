from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserBlocks(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserBlocks
    Model depth: 4
    """
    type_: str = Field("UserBlocks", alias='@type')
    

