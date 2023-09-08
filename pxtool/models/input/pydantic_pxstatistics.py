# generated by datamodel-codegen:
#   filename:  pxstatistics.yaml
#   timestamp: 2023-09-08T10:23:01+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Contact(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = Field(
        None, description='Personal or functional', example='epost@epost.no'
    )
    name: Optional[Dict[str, str]] = None
    raw: Optional[Dict[str, str]] = None


class PxStatistics(BaseModel):
    id: str = Field(
        ...,
        description='Id of a group of tables in the registry of statistics.',
        example=8765,
    )
    updateFrequency: Optional[Dict[str, str]] = None
    metaId: Optional[str] = Field(
        None,
        description='Will be added to metaid on table level. lead to https://www.ssb.no/en/priser-og-prisindekser/konsumpriser/statistikk/konsumprisindeksen#om-statistikken',
        example='KORTNAVN:kpi',
    )
    subjectCode: Optional[str] = Field(None, example='be')
    subjectText: Optional[Dict[str, str]] = None
    upcomingReleases: Optional[List[str]] = None
    contacts: Optional[List[Contact]] = None