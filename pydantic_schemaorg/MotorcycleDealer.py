from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """A motorcycle dealer.

    See https://schema.org/MotorcycleDealer.

    """

    locals().update({"@type": Field("MotorcycleDealer", const=True)})


MotorcycleDealer.update_forward_refs()
