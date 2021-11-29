from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class CaseSeries(MedicalObservationalStudyDesign):
    """A case series (also known as a clinical series) is a medical research study that tracks"
     "patients with a known exposure given similar treatment or examines their medical records"
     "for exposure and outcome. A case series can be retrospective or prospective and usually"
     "involves a smaller number of patients than the more powerful case-control studies or"
     "randomized controlled trials. Case series may be consecutive or non-consecutive,"
     "depending on whether all cases presenting to the reporting authors over a period of time"
     "were included, or only a selection.

    See https://schema.org/CaseSeries.

    """

    locals().update({"@type": Field("CaseSeries", const=True)})


CaseSeries.update_forward_refs()
