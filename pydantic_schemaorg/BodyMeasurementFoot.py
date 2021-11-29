from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementFoot(BodyMeasurementTypeEnumeration):
    """Foot length (measured between end of the most prominent toe and the most prominent part"
     "of the heel). Used, for example, to measure socks.

    See https://schema.org/BodyMeasurementFoot.

    """

    locals().update({"@type": Field("BodyMeasurementFoot", const=True)})


BodyMeasurementFoot.update_forward_refs()
