from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementBust(BodyMeasurementTypeEnumeration):
    """Maximum girth of bust. Used, for example, to fit women's suits.

    See https://schema.org/BodyMeasurementBust.

    """

    locals().update({"@type": Field("BodyMeasurementBust", const=True)})


BodyMeasurementBust.update_forward_refs()
