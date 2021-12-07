from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country.

    See https://schema.org/State.

    """
    type_: str = Field("State", const=True, alias='@type')
    

State.update_forward_refs()
