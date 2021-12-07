from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType


class Female(GenderType):
    """The female gender.

    See https://schema.org/Female.

    """
    type_: str = Field("Female", const=True, alias='@type')
    

Female.update_forward_refs()
