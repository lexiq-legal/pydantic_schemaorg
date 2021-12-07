from pydantic import Field
from pydantic_schemaorg.DoseSchedule import DoseSchedule


class ReportedDoseSchedule(DoseSchedule):
    """A patient-reported or observed dosing schedule for a drug or supplement.

    See https://schema.org/ReportedDoseSchedule.

    """
    type_: str = Field("ReportedDoseSchedule", const=True, alias='@type')
    

ReportedDoseSchedule.update_forward_refs()
