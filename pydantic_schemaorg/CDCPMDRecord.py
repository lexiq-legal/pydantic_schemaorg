from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from datetime import date, datetime
from pydantic_schemaorg.StructuredValue import StructuredValue


class CDCPMDRecord(StructuredValue):
    """A CDCPMDRecord is a data structure representing a record in a CDC tabular data format"
     "used for hospital data reporting. See [documentation](/docs/cdc-covid.html) for"
     "details, and the linked CDC materials for authoritative definitions used as the source"
     "here.

    See https://schema.org/CDCPMDRecord.

    """

    cvdNumVentUse: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numventuse - MECHANICAL VENTILATORS IN USE: Total number of ventilators in use.",
    )
    cvdNumTotBeds: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numtotbeds - ALL HOSPITAL BEDS: Total number of all Inpatient and outpatient beds, including"
     "all staffed,ICU, licensed, and overflow (surge) beds used for inpatients or outpatients.",
    )
    cvdNumC19Died: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19died - DEATHS: Patients with suspected or confirmed COVID-19 who died in the hospital,"
     "ED, or any overflow location.",
    )
    cvdNumC19HOPats: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19hopats - HOSPITAL ONSET: Patients hospitalized in an NHSN inpatient care location"
     "with onset of suspected or confirmed COVID-19 14 or more days after hospitalization.",
    )
    cvdFacilityCounty: Optional[Union[List[str], str]] = Field(
        None,
        description="Name of the County of the NHSN facility that this data record applies to. Use [[cvdFacilityId]]"
     "to identify the facility. To provide other details, [[healthcareReportingData]]"
     "can be used on a [[Hospital]] entry.",
    )
    cvdNumC19OverflowPats: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19overflowpats - ED/OVERFLOW: Patients with suspected or confirmed COVID-19"
     "who are in the ED or any overflow location awaiting an inpatient bed.",
    )
    cvdNumBeds: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numbeds - HOSPITAL INPATIENT BEDS: Inpatient beds, including all staffed, licensed,"
     "and overflow (surge) beds used for inpatients.",
    )
    datePosted: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="Publication date of an online listing.",
    )
    cvdNumICUBedsOcc: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numicubedsocc - ICU BED OCCUPANCY: Total number of staffed inpatient ICU beds that are"
     "occupied.",
    )
    cvdNumVent: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numvent - MECHANICAL VENTILATORS: Total number of ventilators available.",
    )
    cvdNumC19HospPats: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19hosppats - HOSPITALIZED: Patients currently hospitalized in an inpatient care"
     "location who have suspected or confirmed COVID-19.",
    )
    cvdNumICUBeds: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numicubeds - ICU BEDS: Total number of staffed inpatient intensive care unit (ICU) beds.",
    )
    cvdNumC19OFMechVentPats: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19ofmechventpats - ED/OVERFLOW and VENTILATED: Patients with suspected or confirmed"
     "COVID-19 who are in the ED or any overflow location awaiting an inpatient bed and on a mechanical"
     "ventilator.",
    )
    cvdNumC19MechVentPats: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numc19mechventpats - HOSPITALIZED and VENTILATED: Patients hospitalized in an NHSN"
     "inpatient care location who have suspected or confirmed COVID-19 and are on a mechanical"
     "ventilator.",
    )
    cvdFacilityId: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifier of the NHSN facility that this data record applies to. Use [[cvdFacilityCounty]]"
     "to indicate the county. To provide other details, [[healthcareReportingData]] can"
     "be used on a [[Hospital]] entry.",
    )
    cvdCollectionDate: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="collectiondate - Date for which patient counts are reported.",
    )
    cvdNumBedsOcc: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="numbedsocc - HOSPITAL INPATIENT BED OCCUPANCY: Total number of staffed inpatient beds"
     "that are occupied.",
    )
    locals().update({"@type": Field("CDCPMDRecord", const=True)})


CDCPMDRecord.update_forward_refs()
