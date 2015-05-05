
## ODEQ Tables ##
### Facility Well Table ###
ODEQ specified data structure
  * Field: Counter
    * Alias:
    * Data Type: Counter (4)
    * Nulls: no
    * Unique: yes
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: Access
    * Description: A unique number assigned by the database program.

  * Field: UIC #
    * Alias: uicId
    * Data Type: Long (4)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: 10102
    * Domain:{10102}
    * Source: DEQ
    * Description: Identifies City of Portland permitted UICs.

  * Field: Well #
    * Alias: wellId
    * Data Type: Long (4)
    * Nulls: no
    * Unique: yes
    * Index: yes
    * Default Value: None
    * Domain:{}
    * Source: UIC Program
    * Old Description: Unique ID for each individual facility.  The relationship between Well # and the BES ID is maintained within the BES UIC database.
    * New Description: Unique ID (birth to death - never re-used) for each individual facility.  The relationship between Well # and the Hansen CompKey and Unit ID is maintained within the UIC database.

  * Field: Date Updated
    * Alias: dateUpdate
    * Data Type: Date/Time (8)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Date the information (change detection or record update) transmitted to ODEQ.

  * Field: Type Code
    * Alias: typeCode
    * Data Type: Character (4)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{5D2, 5G30, 5R21, 5X27}
    * Source: UICP
    * Old Description: Facility type code taken from 'WELL CLASSIFICATION' lookup table.
    * New Description: Facility type code taken from DEQ Well Classifications.
LUT Name: Lookup\_Type\_Code
| DEQ Code | Description |
|:---------|:------------|
| 5D2 | Stormwater |
| 5D3 | Storm Water Drill Holes/seepage Pits |
| 5D4 | Industrial Storm Water Drainage |
| 5G30 | Special Drainage Water |
| 5R21 | Aquifer Recharge |
| 5X27 | Other Wells |

  * Field: Well Depth and Diameter
    * Alias: depthDiameter
    * Data Type: Character (50)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: Hansen - UICP
    * Old Description: The BES standard UIC design specifies 4-ft diameter by 30-ft depth.  For BES UICs, where actual diameter values are unavailable in Hansen the standard design value is assumed.  For all non-BES UICs where actual diameter values are unavailable, records are assigned "Unknown" diameter.  For all UICs, where actual depth values are unavailable, records are assigned "Unknown" depth.
    * New Description: The standard UIC sump design specifies 4-ft diameter by 30-ft depth.  For UICs with Unit Type is SUMP and Ownership is BES, where actual diameter values are unavailable in Hansen the standard design value is assumed.  For other Unit Types where actual diameter or depth values are unavailable, records are assigned "Unknown" for diameter or depth.

  * Field: Discharge Rate
    * Alias: dschgRt
    * Data Type: Character (50)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: 2.23 gpm (est)
    * Domain:{}
    * Source: UICP
    * Old Description: For BES UICs, where individual discharge rates have not been tested, records are assigned estimated value.  For all non-BES UICs, where actual discharge rate values are unavailable, records are assigned "Unknown".
    * New Description: For UICs where Unit Type is SUMP, and the individual discharge rates have not been tested, records are assigned estimated value.  For other UICs Unit Types where actual discharge rate values are unavailable, records are assigned "Unknown". <div><a href='query.md'>update required</a></li></ul></li></ul>

<ul><li>Field: Waste Type<br>
<ul><li>Alias: wasteTyp<br>
</li><li>Data Type: Long (4)<br>
</li><li>Nulls: no<br>
</li><li>Unique: no<br>
</li><li>Index: no<br>
</li><li>Default Value: 1<br>
</li><li>Domain: {1, 5, 17}<br>
</li><li>Source: UICP<br>
</li><li>Description: Type of waste going to each facility.  Value taken from 'Lookup_Waste_Type_Tbl' lookup table.<br>
LUT Name: Lookup_Waste_Type_Tbl<br>
<table><thead><th> Waste_Key </th><th> Waste_Desc </th></thead><tbody>
<tr><td> 1 </td><td> Storm water </td></tr>
<tr><td> 5 </td><td> Drinking Water </td></tr>
<tr><td> 17 </td><td> ASR (Aquifer storage and recovery) </td></tr></li></ul></li></ul></tbody></table>

<ul><li>Field: Ops Status<br>
<ul><li>Alias: status<br>
</li><li>Data Type: Character (2)<br>
</li><li>Nulls: no<br>
</li><li>Unique: no<br>
</li><li>Index: no<br>
</li><li>Default Value: None<br>
</li><li>Domain:{AC, PA, UC, NB}<br>
</li><li>Source: Hansen (normalized)<br>
</li><li>Description: Operational status of facility. Values taken from 'WELL STATUS' lookup table. All City owned UICs fall under one of the following four designations: AC = In service, PA = Abandoned, UC = Under Construction, NB = Not Built / Does not Exist.<div><a href='query.md'>update required</a>
LUT Name: Lookup_Well_Status_Tbl<br>
<table><thead><th>Code </th><th> Hansen </th><th> Description </th></thead><tbody>
<tr><td> AC </td><td> IN </td><td> In Service </td><td> Active </td></tr>
<tr><td> AC </td><td> CNS </td><td> Constructed No Service </td><td> Active </td></tr>
<tr><td> AC </td><td> TBAB </td><td> To be Abandoned </td><td> Active </td></tr>
<tr><td> AC </td><td> PEND </td><td> In Service Action Pending </td><td> Active </td></tr>
<tr><td> PA </td><td> ABAN </td><td> Abandoned </td><td> Inactive </td></tr>
<tr><td> UC </td><td> NEW </td><td> Under Construction </td><td> Active </td></tr>
<tr><td> NB </td><td> DNE </td><td> Not Built / Does not Exist </td><td> Inactive </td></tr></li></ul></li></ul>

  * Field: Installation Date\_old
    * Alias:
    * Data Type: Date/Time (8)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: Blank - null
    * Domain:{}
    * Source:
    * Description: Leave blank - unused field. Deprecated field

  * Field: Installation Date
    * Alias: install
    * Data Type: Long (4)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: Hansen
    * Description: Installation year in 'YYYY' format.  Where data is unavailable, records remain null.

  * Field: Maintenance Period
    * Alias:
    * Data Type: Character (50)
    * Nulls:
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain: {4 years, 10 years, NA, As Required, Annually, None, Once a year, Once every 2-3 yrs, When needed}
    * Source: DME - Hansen derived, UICP
    * Old Description: Approximate average maintenance cycle for all BES UICs, based on standard practice, is every 4 years for UICs with sedimentation manhole, and every 10 years for UICs without sedimentation manhole.  For non-BES UICs, where actual maintenance period is unavailable, records remain null.
    * New Description: Approximate average maintenance cycle for UICs where Ownership is BES and the Unit Type of SUMP, based on standard practice, is every 4 years for UICs with sedimentation manhole, and every 10 years for UICs without sedimentation manhole.  For all other UICs, where actual maintenance period is unavailable, records remain null.

  * Field: Location
    * Alias: location
    * Data Type: Character (100)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: Hansen
    * Old Description: For BES UICs, the first 6 characters are unique BES license plate ID (i.e. 'ABC123'). For non-BES UICs, unique ID is either 5 or 6 characters (i.e. 'ST17A' or 'PRK008'). Following the ID is the approximate address location of the UIC.
    * New Description: For BES UICs, the first 6 characters are unique BES license plate ID (i.e. 'ABC123'). Following the ID is the approximate address location of the UIC.

  * Field: Lat
    * Alias: latitude
    * Data Type: Single (4)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Latitude in decimal degrees (geographic coordinate system North American 1983 HARN datum).

  * Field: Long
    * Alias: longitude
    * Data Type: Single (4)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Longitude in decimal degrees (geographic coordinate system North American 1983 HARN datum).

  * Field: Distance to nearest water well
    * Alias:
    * Data Type: Character (50)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Approximate distance in feet to nearest confirmed domestic use drinking water or irrigation well (based on confirmed OWRD/DHS well location data).  For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA".

  * Field: Distance to nearest wetland
    * Alias:
    * Data Type: Character (50)
    * Nulls: no
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Approximate distance in feet to nearest wetland (based on Metro regional wetland GIS data). For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA".

  * Field: Distance to nearest surface water
    * Alias:
    * Data Type: Character (50)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Approximate distance in feet to nearest surface water (based on City of Portland surface water GIS data).  For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA".

  * Field: Depth to groundwater
    * Alias:
    * Data Type: Character (50)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: None
    * Domain:{}
    * Source: Derived
    * Description: Approximate distance in feet from bottom-most perforation to estimated seasonal high groundwater.  For BES UICs, where depth of UIC is unknown a depth of 30-ft is assumed, consistent with BES standard UIC design.  For BES UICs, 2-ft are subtracted from UIC depth to account for sediment trap ring, consistent with BES standard UIC design.  For all non-BES UICs, where UIC depth is unknown, depth to groundwater is calculated from ground elevation.  For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA".

  * Field: Size of impervious area
    * Alias:
    * Data Type: Character (50)
    * Nulls: No
    * Unique: N/A
    * Index: N/A
    * Default Value: Averaged
    * Domain:{}
    * Source: Derived
    * Description: Approximate quantity of impervious area draining to UIC in square feet.  Where explicit UIC drainage delineations are available, these are intersected with a mapped impervious GIS dataset to determine impervious area per UIC.  For BES UICs, where UIC drainage delineations are unavailable, average impervious area is calculated from UICs with available catchment delineations.  For non-BES UICs, where impervious area is not available records are assigned "Unknown".

  * Field: Treatment type
    * Alias:
    * Data Type: Character (255)
    * Nulls:
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source:
    * Description: This field is not used.  Actual pretreatment information is housed in the table 'Treatment\_Tbl' because this is a one-to-many relationship.

  * Field: Treatment\_Key
    * Alias:
    * Data Type: Long (4)
    * Nulls:
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source:
    * Description: This field is not used.  Actual pretreatment information is housed in the table 'Treatment\_Tbl' because this is a one-to-many relationship.

  * Field: Sub-basin
    * Alias:
    * Data Type: Character (50)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: LOWER WILLAMETTE
    * Domain:{}
    * Source: HUC
    * Description: Sub-basin the UICs are in, from 'HUCSubBasins' lookup table and front page of permit.

  * Field: Map Attached
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: None
    * Domain:{}
    * Source: DME - Hansen
    * Description: Per ODEQ, leave blank - individual UIC maps are not required.

  * Field: RA
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: No
    * Domain:{}
    * Source: DEQ
    * Description: Per ODEQ, default to "no".

  * Field: Discharge\_document
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: None
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply.

  * Field: Confinement
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: None
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply.


  * Field: Well\_Log
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls:  see description
    * Unique:  see description
    * Index:  see description
    * Default Value: None
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply.

  * Field: Soils\_Info
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: None
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply.

  * Field: Monitoring\_Plan
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: Yes
    * Domain:{}
    * Source: UICP
    * Description: BES input - if monitoring plan exists.

  * Field: Stormwater\_Plan
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: Yes
    * Domain:{}
    * Source: UICP
    * Description: BES input - if storm water plan exists.

  * Field: Sewer\_available
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: {blank}
    * Domain:{}
    * Source: DME - Hansen
    * Description: BES input - if storm sewer is available.

  * Field: Cleanup\_Supplies
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: Yes
    * Domain:{}
    * Source: UICP
    * Description: BES input - if cleanup supplies are available.

  * Field: Delineation\_complete
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: {blank}
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply.  Refers to wellhead protection delineation, not individual UIC catchment delineation.

  * Field: Remediation\_Plan
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: None
    * Domain:{}
    * Source: UICP - CIP
    * Description: BES input - if remediation plan exists.
  * Field: Mixed\_Waste
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: no
    * Unique: no
    * Index: no
    * Default Value: No
    * Domain:{}
    * Source: UICP
    * Description: BES input - 'Yes' if UIC is receiving fluids other than stormwater.

  * Field: Not registered
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: No
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply to City of Portland as all UICs are being registered.

  * Field: Information
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: see description
    * Unique: see description
    * Index: see description
    * Default Value: No
    * Domain:{}
    * Source: none
    * Description: Per ODEQ, leave blank - does not apply to City of Portland as it refers to "asking for information phase".

  * Field: Plugging
    * Alias:
    * Data Type: Yes/No (1)
    * Nulls: yes
    * Unique: no
    * Index: no
    * Default Value: Yes
    * Domain:{}
    * Source: UICP
    * Description: BES input - 'Yes' if UIC has plug available.
### Environmental Cleanup Site Information (ESCI) ###
## UIC Program ##
### Flow Map Interp Volume ###
### Impervious Area ###
### Master Tables ###
Master Table Database Names
| Table Name | Database Name | Descriptions |
|:-----------|:--------------|:-------------|
| Master ID  | uicMasterIDs | Master UIC Status |
| Registration | uicRegMaster | Registrations |
| Not Registered | noRegistration | Rejected & Not Need Registrations |
| Abandoned UIC | abandUIC<div> csaUIC<div> csaMain<div> <tr><td> Abandoned / Decommissioned UICS<div> CSA UIC Lookup Table<div> CSA Main Lookup Table </td></tr></li></ul></li></ul></tbody></table>

<h2>Hansen ##
### Tables Extracted from Hansen by ODBC Link ###
| **Linked Table Name** | **Hansen V8 Table** |
|:----------------------|:--------------------|
| IMP7\_ACTDEFN | WORKMANAGEMENT.ACTDEFN |
| IMP7\_ADDRESS | PROPERTY.ADDRESS |
| IMP7\_COMP | ASSETMANAGEMENT.COMP |
| IMP7\_COMPSMH | ASSETMANAGEMENT\_STORM.COMPSMH |
| IMP7\_COMPSTCH | ASSETMANAGEMENT\_STORM.COMPSTCH |
| IMP7\_COMPSTIN | ASSETMANAGEMENT\_STORM.COMPSTIN |
| IMP7\_COMPSTLS | (was not pulled foward to V8) |
| IMP7\_COMPSTMH | ASSETMANAGEMENT\_STORM.COMPSTMH |
| IMP7\_COMPSTMN | ASSETMANAGEMENT\_STORM.COMPSTMN |
| IMP7\_COMPSTMS | ASSETMANAGEMENT\_STORM.COMPSTMS |
| IMP7\_COMPSTSL | (was not pulled foward to V8) |
| IMP7\_COMPTYPE | ASSETMANAGEMENT.COMPTYPE |
| IMP7\_HISTORY | WORKMANAGEMENT.HISTORY |
| IMP7\_VARGALT | COPASSETMANAGEMENTSTORM.COPSTMHALTGRD |
| IMP7\_VARHSTMN | (was not pulled foward to V8) |
| IMSV8\_COPSMHALTGRD | COPASSETMANAGEMENTSEWER.COPSMHALTGRD |
| IMSV8\_COPSMNALTGRD | COPASSETMANAGEMENTSEWER.COPSMNALTGRD |
| IMSV8\_COPSMNDETLGRD | COPASSETMANAGEMENTSEWER.COPSMNDETLGRD |
| IMSV8\_COPSMSALTGRD | COPASSETMANAGEMENTSEWER.COPSMSALTGRD |
| IMSV8\_COPSTCHALTGRD | COPASSETMANAGEMENTSTORM.COPSTCHALTGRD |
| IMSV8\_COPSTCHDETLGRD | COPASSETMANAGEMENTSTORM.COPSTCHDETLGRD |
| IMSV8\_COPSTINALTGRD | COPASSETMANAGEMENTSTORM.COPSTINALTGRD |
| IMSV8\_COPSTINDETLGRD | COPASSETMANAGEMENTSTORM.COPSTINDETLGRD |
| IMSV8\_COPSTMHALTGRD | COPASSETMANAGEMENTSTORM.COPSTMHALTGRD |
| IMSV8\_COPSTMNALTGRD | COPASSETMANAGEMENTSTORM.COPSTMNALTGRD |
| IMSV8\_COPSTMNDETLGRD | COPASSETMANAGEMENTSTORM.COPSTMNDETLGRD |
| IMSV8\_COPSTMSALTGRD | COPASSETMANAGEMENTSTORM.COPSTMSALTGRD |
| IMSV8\_COPSTORMINLET | COPASSETMANAGEMENTSTORM.COPSTORMINLET |
| IMSV8\_COPSTORMMANHOLE | COPASSETMANAGEMENTSTORM.COPSTORMMANHOLE |
| IMSV8\_COPSTORMMISCELLANEOUS | COPASSETMANAGEMENTSTORM.COPSTORMMISCELLANEOUS |

### Hansen Activity Defination Table ###
### Hansen Work Order Table ###
## Corporate GIS (CGIS) ##
### PDX Zoning ###
### Water Bodies Table ###
### Wetlands Table ###
## Un-catagorized datasets ##
### CONFIRMED\_WELLS ###
  * CONFIRMED\_WELLS\_drinking\_features
  * CONFIRMED\_WELLS\_irrigation\_features
  * ConfirmedWellTaxlots
  * POTENTIAL\_WELLS
### Raster Data ###
  * d5\_masked\_UTM1083\_2008
  * d5\_seasvar\_UTM1083\_2008
  * pdx\_seasonal\_flux\_UTM1083
  * pdx\_seasonal\_flux\_2 (state plane)
  * elevationDEM
### Traffic ###
  * trafficCountsClass
  * TSP
### zoning ###
### `BuriedSumps` ###
needs to be decommissioned
### panelsConstMonCompliance ###
  * ComplianceCategory
need to be decommissioned - replaced by `panelsConstMonCompliance`
  * CorrectiveAction
need to be decommissioned - replaced by panelsConstMonCompliance
### Surface Features ###
  * Waterbodies
  * Wetlands
  * ECSI
  * TOT2yr\_All - / - Two\_year\_TOT
  * SC\_auto
    * Programmically Generated Sub-Catchments
  * Impervious Area
  * SOILS (New)
  * percentSandWeightedAvg
  * SSURGO\_cHorizon\_sand
  * uic\_infiltration\_bes\_pdx
  * UIC Drainage Systems (New)
### Location ###
  * Address
needs to be decommissioned - replaced by location table
  * UTM1083
needs to be decommissioned - replaced by location table
  * LATLONG
needs to be decommissioned - replaced by location table
### Ground Water Depth Tables ###
  * DTWG2007
needs to be decommissioned
  * DTWG2008
  * DTWGCSM
needs to be decommissioned
### Decommissioning (CSA) Tables ###
LUT Name: Lookup\_CSA\_Status\_Tbl
| Code | Status | Desciption |
|:-----|:-------|:-----------|
| 0 | Info | report not in file |
| 1 | Info | information only |
| 11 | Active | in-progress |
| 12 | Active | ongoing - different CAS# |
| 13 | Active | on-going - monitoring |
| 14 | Active | investigating |
| 21 | In-Active | Finished or Completed |
| 22 | In-Active | Cancelled |
| 23 | In-Active | Closed - Not completed |
| 24 | In-Active | On-Hold |
| 25 | In-Active | Finished or Completed - No letter from DEQ |
| 26 | In-Active | Finished or Completed - Hansen not matching |

## Production Wells ##
Production Well Data Structure - Feature Data Set
> updDate : Date ()     : Date of Update
> > ufacID : Char (255)  : UICP GUID

> GlobalID : Numb (20)   : ArcGIS Global ID
> > dataSrc : Numb (2)    : Attribute Data Source
> > > SDSID : Numb (2)    : Spatial Data Source

> > m\_SDSID : text (255)  : Multiple Spatial Data Source for same Well

> altSDSID : text (255)  : Updated
> > uLogID : Char (15)   : LogID

> uLogIDSec : text (17)   : Secondary LogID
> > logTag : Char (15)   : Well Tag
> > Location : Char (255)  : Street ADDRESS
> > > UseID : Numb (2)    : Well Use
> > > > OPS : Numb (2)    : Operational Status by Agency

> > > CoordID : Numb (2)    : not used - replaced by SDSID
> > > > TRS : Char (15)   : Township Range Section Qtr40 Qtr160

> > wbTypeID : Numb (2)    : not used - Water Bureau Well TypeID - replaced by UseID
> > taxLotID : Char (50)   : Township Range Section TaxLotID



SDS - Spatial Data Source
Build complete list of Wells with spatial references

> Confirmed Well                Table Updated & Coded
> Confirmed Well TaxLots        Table Updated & Coded
> Potential Wells               Table Updated & Coded
> OWRD Well Cards               Coded
> OWRD\_pdx (SDS)
> > Imported from shape file
> > Clipped to study area WRD\_Shape -> OWRD\_pdx

> PWB Wells



Production Well Data Structure - Feature Data Set
> updDate : Date of record creation or refreshed
> > ufacID : UICP internal ID (GUID)

> GlobalID : BES internal globalID
> > dataSrc : Data source (Domain below)
> > > dataSrcID   Description
        1. BES Internal Information (survey)
> > > > 20   Water Bureau
> > > > 30   State of Oregon Health Department (DHS) or OWRD
> > > > 90   USGS

> > > SDSID : Spatial Data Source ID - Used to determine spatial location (Domain below)
> > > > SDSID   Agency - Description, Notes
> > > > > 00          - No Data
          1. Field Verified UICP / Survey - authoritative
          1. UICP  - Confirmed Well Table - Field Verified UICP / Survey - authoritative
          1. UICP  - PWB SDS (Original Location) - Field Verified UICP / Survey - authoritative
> > > > > 20   As-Built Information - Not Field Verified / Survey
> > > > > 21    PWB   - Maintained (WB\_SDE) - AS-Built Information - Not Field Verified / Survey
> > > > > 30   OWRD Maintained Spatial Location
> > > > > 31    OWRD  - GWATER - OWRD Maintained Spatial Location
> > > > > 32    OWRD  - WATER RIGHT - OWRD Maintained Spatial Location
> > > > > 33    OWRD  - USGS WILLGW - OWRD Maintained Spatial Location
> > > > > 34    OWRD  - WATERMASTER - OWRD Maintained Spatial Location
> > > > > 35    OWRD  - USGS - NWIS GPS-Way Point - OWRD Maintained Spatial Location
> > > > > 40   Alternate Spatial Sources - non-authoritative
> > > > > 41    UICP  - Potential Wells Table
> > > > > 42    OWRD  - OWRD Well Log Coordinates
> > > > > 43    UICP  - Parcel Situs Address Resolved - Accuracy Parcel Centroid
> > > > > > (UICP - Confirmed Well Taxlots)

> > > > > 44    UICP  - Geocode unable to resolve by Situs Address, Accuracy parcel to fit
> > > > > > Geocoded Location

> > > > > 50   SDS Unknown - Not Field Verified / Survey
> > > > > 51    OWRD  - TRS Not Field Verified / Survey
> > > > > 52    UNKN  - SDS is Unknown


> Group SDSID - Accuracy Description - Notes
> SDSID Group   Description
    1. Field Verified UICP / Survey - authoritative
> > 20   As-built Information - Not Field Verified / Survey
> > 30   OWRD Maintained Spatial Location
> > 40   Alternate Spatial Sources - non-authoritative
> > 50   SDS Unknown - Not Field Verified / Survey


> UlogID : This field is a unique key for a given well log. The combination of County Code and Well
> > Log ID# is created when a well log is entered. You may see some records where the Well Log ID
> > is list multiple times with version numbers. There are some well logs where through field
> > inspection, State Staff, or other sources, State Staff have discovered that the data on the
> > original well log is not accurate.  On those logs, the state add another record with a higher
> > version.  Once a well log has been submitted, the State assigns a Well Log ID# for the
> > database. This identification is the combination of a county code (which may be different than
> > the county where the well is located) and a numeric id. These combination of these fields
> > allows you to locate an individual well log via this reference number.

> logTag : After June 1996, wells constructed, altered, or on property that has changed ownership,
> > have a metal tag placed on them with this number. This field allows you to locate an
> > individual well log via this reference number.

> Location : The address of the property where the well was constructed. This information may or may not
> > be the current address of the property due to address changes.
> > UseID : Wells are used for numerous purposes. These fields denote the different types of uses a well
> > > might have.  The use indicated on the log is the original use the owner indicated. This may
> > > have changed over time.
> > > UseID   Description : Well use from State Well Log Cards
> > > > 00   No Data
        1. Drinking Water Classification
        1. DW
        1. DW - IR
        1. DW - CM
        1. DW - IR - CM
> > > > 20   Irrigation Classification
> > > > 21   IR
> > > > 22   IR - CM
> > > > 30   Commercial / Industrial                                 do not report
> > > > 31   CM
> > > > 40   Well use is unknown                                     do not report
> > > > 41   Unknown - None - No Use Marked (all Categories)
> > > > 50   Community - Municipal (Public)
> > > > 51   Public Water System (PWS)
> > > > 52   Community Water System - Not Public Agency (NPA)
> > > > 53   Unknown Use but PWS or NPA                              do not report
> > > > 60   Non Used for reporting
> > > > 61   piezometer (only)
> > > > 62   Thermal (only)
> > > > 63   Livestock (only)
> > > > 64   Dewatering (only)
> > > > 65   Injection
> > > > 66   Use\_Other
> > > > > Test - Observation - Monitoring
> > > > > Extraction - Heat Pump - LTGT
> > > > > Ground Bed - Dust control - Dry Well

> > > Abbreviations used by UseID
> > > > DW   Drinking Water
> > > > IR   Irrigation
> > > > CM   Commercial - Industrial
> > > > PW   Public Water Well (Municipal)


> OPS : Operational Status & Agency
> > OPS   Description
> > > 00   No Data
      1. ACT - UICP
      1. ACT - OWRD
      1. ACT - PWB
> > > 20   ABN - Abandoned
> > > 21   ABN - OWRD
> > > 22   ABN - PWD
> > > 30   NIS - Not in Service (Reporting)                         catagories
> > > 31   NIS - OWRD
> > > 32   NIS - PWB
> > > 40   NOR - Non reporting Use type (Status does not matter)
> > > 41   NOR - OWRD
> > > 42   NOR - PWB


> OPSID Group   Description
    1. Active (Act)
> > 20   Abandoned or Inactive (ABN)
> > 30   Not in Service (NIS)
> > 40   Non Report Use Type (Nor) {Status does not matter}


> CoordID : Coordinate Origin
> > CoordID, Description
> > > 00   No Data
> > > 01   Latitude & Longitude
> > > 02   Spatial Location
> > > 03   TRS
> > > 04   Parcel - Polygon Centroid




> WTypeID : Water Bureau Well Type
> > WTypeID  Description
> > > 00   No Data - Unknown
> > > 01   Bull Run Groundwater Well
> > > 02   Exploratory Boring
> > > 03   Monitoring Well
> > > 04   Piezometer
> > > 05   Pilot Well
> > > 06   PVRWD Well - Powell Valley Road Water District Well
> > > 07   Production Well
> > > 08   SSPW (Not in Service) - Small System Production Wells (Not in Service)
> > > 09   Test Well