from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserLikes(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserLikes.

    """
    type_: str = Field("UserLikes", const=True, alias='@type')
    

UserLikes.update_forward_refs()
