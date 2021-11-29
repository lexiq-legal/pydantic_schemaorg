from pydantic import Field
from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting"
     "of clothes.

    See https://schema.org/BodyMeasurementTypeEnumeration.

    """

    locals().update({"@type": Field("BodyMeasurementTypeEnumeration", const=True)})


BodyMeasurementTypeEnumeration.update_forward_refs()
