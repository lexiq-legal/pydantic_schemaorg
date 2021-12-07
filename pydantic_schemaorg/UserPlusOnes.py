from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserPlusOnes(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserPlusOnes.

    """
    type_: str = Field("UserPlusOnes", const=True, alias='@type')
    

UserPlusOnes.update_forward_refs()
