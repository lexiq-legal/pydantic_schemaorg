from pydantic import Field
from pydantic_schemaorg.Event import Event


class UserInteraction(Event):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserInteraction.

    """
    type_: str = Field("UserInteraction", const=True, alias='@type')
    

UserInteraction.update_forward_refs()
