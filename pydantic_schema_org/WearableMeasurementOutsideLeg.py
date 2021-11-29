from pydantic import Field
from pydantic_schema_org.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementOutsideLeg(WearableMeasurementTypeEnumeration):
    """Measurement of the outside leg, for example of pants

    See https://schema.org/WearableMeasurementOutsideLeg.

    """

    locals().update({"@type": Field("WearableMeasurementOutsideLeg", const=True)})


WearableMeasurementOutsideLeg.update_forward_refs()
