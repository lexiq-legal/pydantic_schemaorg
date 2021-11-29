from pydantic import Field
from pydantic_schema_org.UserInteraction import UserInteraction


class UserTweets(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserTweets.

    """

    locals().update({"@type": Field("UserTweets", const=True)})


UserTweets.update_forward_refs()
