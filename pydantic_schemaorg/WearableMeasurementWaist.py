from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementWaist(WearableMeasurementTypeEnumeration):
    """Measurement of the waist section, for example of pants

    See https://schema.org/WearableMeasurementWaist.

    """

    locals().update({"@type": Field("WearableMeasurementWaist", const=True)})


WearableMeasurementWaist.update_forward_refs()
