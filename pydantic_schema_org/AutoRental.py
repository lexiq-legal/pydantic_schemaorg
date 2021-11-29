from pydantic import Field
from pydantic_schema_org.AutomotiveBusiness import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    See https://schema.org/AutoRental.

    """

    locals().update({"@type": Field("AutoRental", const=True)})


AutoRental.update_forward_refs()
