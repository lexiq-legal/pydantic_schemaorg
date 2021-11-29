from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementUnderbust(BodyMeasurementTypeEnumeration):
    """Girth of body just below the bust. Used, for example, to fit women's swimwear.

    See https://schema.org/BodyMeasurementUnderbust.

    """

    locals().update({"@type": Field("BodyMeasurementUnderbust", const=True)})


BodyMeasurementUnderbust.update_forward_refs()
