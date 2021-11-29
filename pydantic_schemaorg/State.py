from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class State(AdministrativeArea):
    """A state or province of a country.

    See https://schema.org/State.

    """

    locals().update({"@type": Field("State", const=True)})


State.update_forward_refs()
