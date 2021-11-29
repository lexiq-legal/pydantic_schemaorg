from pydantic import Field
from pydantic_schema_org.WearableMeasurementTypeEnumeration import WearableMeasurementTypeEnumeration


class WearableMeasurementCup(WearableMeasurementTypeEnumeration):
    """Measurement of the cup, for example of a bra

    See https://schema.org/WearableMeasurementCup.

    """

    locals().update({"@type": Field("WearableMeasurementCup", const=True)})


WearableMeasurementCup.update_forward_refs()
