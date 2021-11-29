from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementChest(BodyMeasurementTypeEnumeration):
    """Maximum girth of chest. Used, for example, to fit men's suits.

    See https://schema.org/BodyMeasurementChest.

    """

    locals().update({"@type": Field("BodyMeasurementChest", const=True)})


BodyMeasurementChest.update_forward_refs()
