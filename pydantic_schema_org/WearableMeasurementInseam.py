from pydantic import Field
from pydantic_schema_org.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementInseam(WearableMeasurementTypeEnumeration):
    """Measurement of the inseam, for example of pants

    See https://schema.org/WearableMeasurementInseam.

    """

    locals().update({"@type": Field("WearableMeasurementInseam", const=True)})


WearableMeasurementInseam.update_forward_refs()
