from pydantic import Field
from pydantic_schema_org.AutomotiveBusiness import AutomotiveBusiness


class AutoDealer(AutomotiveBusiness):
    """An car dealership.

    See https://schema.org/AutoDealer.

    """

    locals().update({"@type": Field("AutoDealer", const=True)})


AutoDealer.update_forward_refs()
