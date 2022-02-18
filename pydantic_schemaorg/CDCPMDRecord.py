from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class CDCPMDRecord(StructuredValue):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format"
     "used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for"
     "details, and the linked CDC materials for authoritative definitions used as the source"
     "here.

    See: https://schema.org/CDCPMDRecord
    Model depth: 4
    """
    type_: str = Field(default="CDCPMDRecord", alias='@type', constant=True)
    cvdNumVentUse: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.",
    )
    cvdNumTotBeds: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numtotbeds - ALL HOSPITAL BEDS: Total number of all Inpatient and outpatient beds, including"
     "all staffed,ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.",
    )
    cvdNumC19Died: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital,"
     "ED, or any overflow location.",
    )
    cvdNumC19HOPats: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location"
     "with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.",
    )
    cvdFacilityCounty: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]]"
     "to identify the facility. To provide other details, [[healthcareReportingData]]"
     "can be used on a [[Hospital]] entry.",
    )
    cvdNumC19OverflowPats: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19"
     "who are in the ED or any overflow location awaiting an inpatient bed.",
    )
    cvdNumBeds: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed,"
     "and overflow (surge) beds used for inpatients.",
    )
    datePosted: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Publication date of an online listing.",
    )
    cvdNumICUBedsOcc: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are"
     "occupied.",
    )
    cvdNumVent: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numvent - MECHANICAL VENTILATORS: Total number of ventilators available.",
    )
    cvdNumC19HospPats: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care"
     "location who have suspected or confirmed COVID-19.",
    )
    cvdNumICUBeds: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.",
    )
    cvdNumC19OFMechVentPats: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed"
     "COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical"
     "ventilator.",
    )
    cvdNumC19MechVentPats: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN"
     "inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical"
     "ventilator.",
    )
    cvdFacilityId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]]"
     "to indicate the county. To provide other details, [[healthcareReportingData]] can"
     "be used on a [[Hospital]] entry.",
    )
    cvdCollectionDate: Optional[Union[List[Union[datetime, 'DateTime', str, 'Text']], datetime, 'DateTime', str, 'Text']] = Field(
        default=None,
        description="collectiondate - Date for which patient counts are reported.",
    )
    cvdNumBedsOcc: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds"
     "that are occupied.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
