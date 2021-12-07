from pydantic import Field
from pydantic_schemaorg.GovernmentOffice import GovernmentOffice


class PostOffice(GovernmentOffice):
    """A post office.

    See https://schema.org/PostOffice.

    """
    type_: str = Field("PostOffice", const=True, alias='@type')
    

PostOffice.update_forward_refs()
