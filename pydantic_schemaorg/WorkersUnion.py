from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class WorkersUnion(Organization):
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization"
     "that promotes the interests of its worker members by collectively bargaining with management,"
     "organizing, and political lobbying.

    See https://schema.org/WorkersUnion.

    """
    type_: str = Field("WorkersUnion", const=True, alias='@type')
    

WorkersUnion.update_forward_refs()
