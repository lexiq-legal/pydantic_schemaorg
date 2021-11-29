from pydantic import Field
from pydantic_schema_org.QualitativeValue import QualitativeValue


class SteeringPositionValue(QualitativeValue):
    """A value indicating a steering position.

    See https://schema.org/SteeringPositionValue.

    """

    locals().update({"@type": Field("SteeringPositionValue", const=True)})


SteeringPositionValue.update_forward_refs()
