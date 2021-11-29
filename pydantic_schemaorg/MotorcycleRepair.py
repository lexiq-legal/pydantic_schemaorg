from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    See https://schema.org/MotorcycleRepair.

    """

    locals().update({"@type": Field("MotorcycleRepair", const=True)})


MotorcycleRepair.update_forward_refs()
