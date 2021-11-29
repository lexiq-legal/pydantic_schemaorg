from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementWeight(BodyMeasurementTypeEnumeration):
    """Body weight. Used, for example, to measure pantyhose.

    See https://schema.org/BodyMeasurementWeight.

    """

    locals().update({"@type": Field("BodyMeasurementWeight", const=True)})


BodyMeasurementWeight.update_forward_refs()
