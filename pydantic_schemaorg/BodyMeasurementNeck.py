from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementNeck(BodyMeasurementTypeEnumeration):
    """Girth of neck. Used, for example, to fit shirts.

    See https://schema.org/BodyMeasurementNeck.

    """

    locals().update({"@type": Field("BodyMeasurementNeck", const=True)})


BodyMeasurementNeck.update_forward_refs()
