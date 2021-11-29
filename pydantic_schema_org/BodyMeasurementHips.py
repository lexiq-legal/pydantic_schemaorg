from pydantic import Field
from pydantic_schema_org.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHips(BodyMeasurementTypeEnumeration):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    See https://schema.org/BodyMeasurementHips.

    """

    locals().update({"@type": Field("BodyMeasurementHips", const=True)})


BodyMeasurementHips.update_forward_refs()
