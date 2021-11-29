from pydantic import Field
from pydantic_schemaorg.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementCollar(WearableMeasurementTypeEnumeration):
    """Measurement of the collar, for example of a shirt

    See https://schema.org/WearableMeasurementCollar.

    """

    locals().update({"@type": Field("WearableMeasurementCollar", const=True)})


WearableMeasurementCollar.update_forward_refs()
