from pydantic import Field
from pydantic_schemaorg.DoseSchedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    See https://schema.org/ReportedDoseSchedule.

    """

    locals().update({"@type": Field("ReportedDoseSchedule", const=True)})


ReportedDoseSchedule.update_forward_refs()
