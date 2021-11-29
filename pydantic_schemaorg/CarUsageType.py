from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class CarUsageType(Enumeration):
    """A value indicating a special usage of a car, e.g. commercial rental, driving school,"
     "or as a taxi.

    See https://schema.org/CarUsageType.

    """

    locals().update({"@type": Field("CarUsageType", const=True)})


CarUsageType.update_forward_refs()
