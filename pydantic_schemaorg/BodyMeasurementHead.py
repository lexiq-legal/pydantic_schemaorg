from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementHead(BodyMeasurementTypeEnumeration):
    """Maximum girth of head above the ears. Used, for example, to fit hats.

    See https://schema.org/BodyMeasurementHead.

    """

    locals().update({"@type": Field("BodyMeasurementHead", const=True)})


BodyMeasurementHead.update_forward_refs()
