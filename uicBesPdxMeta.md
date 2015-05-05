<h1>UIC_BES_PDX</h1>

# Identification Information #
## Citation: ##
  * Originator: Underground Injection Control (UIC) Program & Asset System Management (ASM)
  * Title: uic\_bes\_pdx
  * Geospatial Data Presentation Form: point - vector digital data
  * Online Linkage: EGH\_Public.sde CGIS2.rose.portland.local

## Description: ##
  * Abstract: UIC data set
  * Purpose: ODEQ UIC regulatory reporting dataset (authoritative).  Attribute information is as reported to ODEQ in Quarterly Report
  * Time Period of Content: 2005 to Current (permit cycle)

## Status: ##
  * Progress: Currently maintained
  * Maintenance and Update Frequency: updated as new UIC's are registered and on Quarterly Basis - Reporting Cycle

## Spatial Domain: ##
  * Bounding Coordinates:
    * West Bounding Coordinate: -122.781469
    * East Bounding Coordinate: -122.436764
    * North Bounding Coordinate: 45.613793
    * South Bounding Coordinate: 45.448342

## Access Constraints & Use Constraints: ##
Contact Underground Injection Control (UIC) Program

## Native Data Set Environment: ##
ESRI Geodatabase 9X

## Data Quality Information: ##
Process Step:
  * Process Description: Dataset copied.
  * Source Used Citation Abbreviation: 7750\UIC\_DB\UIC\_DATABASE\_91.mdb

## Spatial Data Organization Information: ##
  * Direct Spatial Reference Method: Vector
  * SDTS Point and Vector Object Type: Entity point
  * Point and Vector Object Count: 9500 +

## Spatial Reference Information: ##
  * Horizontal Coordinate System Definition:
    * Map Projection:
      * Map Projection Name: Lambert Conformal Conic
      * Lambert Conformal Conic:
        * Standard Parallel: 44.333333
        * Standard Parallel: 46.000000
        * Longitude of Central Meridian: -120.500000
        * Latitude of Projection Origin: 43.666667
        * False Easting: 8202099.737533
        * False Northing: 0.000000
    * Planar Coordinate Information:
      * Planar Coordinate Encoding Method: coordinate pair
      * Coordinate Representation:
        * Abscissa Resolution: 0.000000
        * Ordinate Resolution: 0.000000
      * Planar Distance Units: international feet
      * Geodetic Model:
        * Horizontal Datum Name: `D_North_American_1983_HARN`
        * Ellipsoid Name: Geodetic Reference System 80
        * Semi-major Axis: 6378137.000000
        * Denominator of Flattening Ratio: 298.257222
  * Vertical Coordinate System Definition:
    * Altitude Resolution: 1.000000

## Distribution Information: ##
Contact Information: Underground Injection Control (UIC) Program<div>
Contact Organization: City of Portland, Bureau of Enviromental Services, Stormwater Management, Underground Injection Control (UIC) Program<div>
Contact Address: 1120 SW 5th Avenue, Suite 1000, Portland, OR 97204<div>
Contact Voice Telephone: 503-823-7740<div>

<h2>Metadata Reference Information:</h2>
Metadata Date: 20131022<br>
<br>
<h2>Entity and Information:</h2>
<ul><li>Entity Type: point<br>
</li><li>Entity Type Label: uic_bes_pdx</li></ul>

<hr />
<hr />

<h1>Attribute Information</h1>

<h2><b>Field:</b> OBJECTID</h2>
<table><thead><th> <b>Alias:</b> ObjectID </th><th> <b>Data Type:</b> Long </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> yes </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> AutoNumber  </td><td> <b>Domain:</b> {1 - 999999} </td><td> <b>Source:</b> ESRI </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> A unique number assigned by ESRI ArcGIS program. </th><th> Authoritative: n/a </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Well #</h2>
<table><thead><th> <b>Alias:</b> wellId </th><th> <b>Data Type:</b> Long </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> yes </th><th> <b>Index:</b> yes </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {1 - 9999} </td><td> <b>Source:</b> UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Unique ID (birth to death - never re-used) for each individual facility.  The relationship between Well # and the Hansen CompKey and Unit ID is maintained within the UIC database. </th></thead><tbody></tbody></table>


<h2><b>Field:</b> UIC #</h2>
<table><thead><th> <b>Alias:</b> uicId </th><th> <b>Data Type:</b> Long </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> 10102 </td><td> <b>Domain:</b> {10102} </td><td> <b>Source:</b> DEQ </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Identifies City of Portland permitted UICs.  Assigned by ODEQ </th></thead><tbody></tbody></table>


<h2><b>Field:</b> DEQID #</h2>
<table><thead><th> <b>Alias:</b> DEQID </th><th> <b>Data Type:</b> Text (6) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> yes </th><th> <b>Index:</b> yes </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {1 - 9999} </td><td> <b>Source:</b> UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Full UIC DEQID, also refered to ALTID in Hansen System.  The ID is concatenation of <a href='UIC.md'>#</a> & " - " & <a href='Well.md'>#</a>.  Rules for Well# apply. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> UnitID #</h2>
<table><thead><th> <b>Alias:</b> Hansen UnitID </th><th> <b>Data Type:</b> Long (4) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> yes </th><th> <b>Index:</b> yes </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {XXX###} </td><td> <b>Source:</b> Hansen, UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Unique ID (birth to death - never re-used) for each individual facility.  The relationship between Well # and the Hansen CompKey and Unit ID is maintained within the UIC database. </th></thead><tbody></tbody></table>


<h2><b>Field:</b> Compkey #</h2>
<table><thead><th> <b>Alias:</b> Hansen Compkey </th><th> <b>Data Type:</b> Long </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> yes </th><th> <b>Index:</b> yes </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {1 - 999999} </td><td> <b>Source:</b> Hansen </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Unique ID (birth to death - never re-used) for each individual facility.  The relationship between Well # and the Hansen CompKey and Unit ID is maintained within the UIC database. </th></thead><tbody></tbody></table>

<hr />


<h2><b>Field:</b> Date Updated</h2>
<table><thead><th> <b>Alias:</b> dateUpdate </th><th> <b>Data Type:</b> Date/Time (8) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b>{MM/DD/YYYY} </td><td> <b>Source:</b> UICP - Derived </td><td> Authoritative: n/a </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Date the information (change detection or record update) transmitted to ODEQ. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Type Code</h2>
<table><thead><th> <b>Alias:</b> typeCode </th><th> <b>Data Type:</b> Character (4) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {5D2, 5G30, 5R21, 5X27} </td><td> <b>Source:</b> UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Facility type code taken from DEQ Well Classifications. </th></thead><tbody></tbody></table>

Well Classification Type Code & Type Description<br>
<br>
<b>LUT Name:</b> Lookup_Type_Code  {only used domain codes listed}<br>
<table><thead><th> DEQ Code </th><th> Description </th></thead><tbody>
<tr><td> 5D2 </td><td> Storm water </td></tr>
<tr><td> 5D3 </td><td> Storm Water Drill Holes/seepage Pits </td></tr>
<tr><td> 5D4 </td><td> Industrial Storm Water Drainage </td></tr>
<tr><td> 5G30 </td><td> Special Drainage Water </td></tr>
<tr><td> 5R21 </td><td> Aquifer Recharge </td></tr>
<tr><td> 5X27 </td><td> Other Wells </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_WellClassification<br>
<table><thead><th> Code </th><th> Type Description </th></thead><tbody>
<tr><td> 5A19 </td><td> Cooling Water Return </td></tr>
<tr><td> 5A5  </td><td> Electric Power Generator </td></tr>
<tr><td> 5A6  </td><td> Geothermal Heat </td></tr>
<tr><td> 5A7  </td><td> Closed Loop Heat Pump Return </td></tr>
<tr><td> 5D2  </td><td> Storm water </td></tr>
<tr><td> 5D3  </td><td> Drill Hole </td></tr>
<tr><td> 5D4  </td><td> Industrial Storm Runoff </td></tr>
<tr><td> 5G30 </td><td> Special Drainage Water </td></tr>
<tr><td> 5R21 </td><td> Aquifer Recharge </td></tr>
<tr><td> 5W10 </td><td> Cesspool </td></tr>
<tr><td> 5W11 </td><td> Septic System (gen) </td></tr>
<tr><td> 5W12 </td><td> Water Treatment Plant Effluent </td></tr>
<tr><td> 5W20 </td><td> Industrial Process Water </td></tr>
<tr><td> 5W31 </td><td> Septic System (well disposal) </td></tr>
<tr><td> 5W32 </td><td> Septic System (drainfield) </td></tr>
<tr><td> 5W9  </td><td> Untreated Sewage </td></tr>
<tr><td> 5X26 </td><td> Aquifer Remediation </td></tr>
<tr><td> 5X27 </td><td> Other Wells </td></tr>
<tr><td> 5X28 </td><td> Motor Vehicle Waste </td></tr>
<tr><td> 5X29 </td><td> Abandoned Drinking Well </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Unit Type</h2>
<table><thead><th> <b>Alias:</b> typeCode </th><th> <b>Data Type:</b> Character (4) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {CB, CBM, CO, INFINL, INLET, MH, MHCB,<div>OVRINF, OVRPIP, SUM, WWE, WWJ, WYE} </td><td> <b>Source:</b> Hansen </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Facility type code taken from DEQ Well Classifications. </th></thead><tbody></tbody></table>

<br>
<br>
<H4><br>
<br>
<b>LUT Name:</b> Lookup_UnitType<br>
<br>
</H4><br>
<br>
<br>
<table><thead><th> Code   </th><th> Description </th><th> UIC Use </th><th> Extract </th><th> Notes </th></thead><tbody>
<tr><td> CB     </td><td> CATCH BASIN </td><td> No </td><td> No </td><td>  </td></tr>
<tr><td> CBM    </td><td> CATCH BASIN MANHOLE </td><td> No </td><td> No </td><td>  </td></tr>
<tr><td> CO     </td><td> CLEAN OUT OR FLUSHER </td><td> Yes </td><td> Manual </td><td> Associated with Perf Pipe or Hybrid UIC </td></tr>
<tr><td> INFINL </td><td> INFILTRATION INLET IN MH INV </td><td> Yes </td><td> Automatic </td><td> infiltrating inlet </td></tr>
<tr><td> INLET  </td><td> INLET IN MH INVENTORY </td><td> No </td><td> No </td><td>  </td></tr>
<tr><td> MH     </td><td> STANDARD MANHOLE </td><td> Yes </td><td> Manual </td><td> Associated with Perf Pipe UIC </td></tr>
<tr><td> MHCB   </td><td> CATCH BASIN IN MH INVENTORY </td><td> No </td><td> No </td><td> Data Error </td></tr>
<tr><td> OVRINF </td><td> UIC INFILTRATION OVERFLOW PIPE </td><td> Yes </td><td> Automatic </td><td> infiltrating overflow - Hybrid UIC</td></tr>
<tr><td> OVRPIP </td><td> OVERFLOW STAND PIPE </td><td>  No </td><td> No </td><td> If found Data Error - Never Valid </td></tr>
<tr><td> SUM    </td><td> SUMP </td><td> Yes </td><td> Automatic </td><td> default UIC</td></tr>
<tr><td> WWE    </td><td> WATER WAY END </td><td> Yes </td><td> Manual </td><td> Associated Hybrid UIC </td></tr>
<tr><td> WWJ    </td><td> WATERWAY JUNCTION </td><td> Yes </td><td> Manual </td><td> Associated Hybrid UIC </td></tr>
<tr><td> WYE    </td><td> JUNCTION OR WYE (NO MH) </td><td> Yes </td><td> Manual </td><td> Associated Hybrid UIC </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Ownership</h2>
<table><thead><th> <b>Alias:</b> typeCode </th><th> <b>Data Type:</b> Character (4) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {AGRE, BES, BGS, FIRE, PARK, WTR, UNKN, } </td><td> <b>Source:</b> UICP, Hansen </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Facility Ownership or Reporting Responsibility. Rules to determine Ownership when <b><i>blank or Unknown</i></b>, See Rules to Determine Facility Ownership for Regulatory Reporting </th></thead><tbody></tbody></table>

<b>LUT Name:</b> Lookup_Reporting_Ownership<br>
<table><thead><th> Code   </th><th> Description </th></thead><tbody>
<tr><td> AGRE   </td><td> UNINCORP MULTCO AGREEMENT AREA </td></tr>
<tr><td> BES    </td><td> ENVIRONMENTAL SERVICES </td></tr>
<tr><td> BGS    </td><td> GENERAL SERVICES </td></tr>
<tr><td> FIRE   </td><td> PORTLAND FIRE BUREAU </td></tr>
<tr><td> PARK   </td><td> PARK BUREAU </td></tr>
<tr><td> PDOT   </td><td> PORTLAND DPT OF TRANSPORTATION </td></tr>
<tr><td> UNKN   </td><td> UNDETERMINED AT THIS TIME - ASSUMED BES </td></tr>
<tr><td>        </td><td> UNDETERMINED - ASSUMED BES </td></tr>
<tr><td> WTR    </td><td> WATER BUREAU </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Well Depth and Diameter</h2>
<table><thead><th> <b>Alias:</b> depthDiameter </th><th> <b>Data Type:</b> Character (50) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {} </td><td> <b>Source:</b> Hansen - UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> The standard UIC sump design specifies 4-ft diameter by 30-ft depth. For UICs with Unit Type is SUMP and Ownership is BES, where actual diameter values are unavailable in Hansen the standard design value is assumed. For other Unit Types where actual diameter or depth values are unavailable, records are assigned "Unknown" for diameter or depth. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Discharge Rate</h2>
<table><thead><th> <b>Alias:</b> dschgRt </th><th> <b>Data Type:</b> Character (50) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> 2.23 gpm (est) </td><td> <b>Domain:</b> {} </td><td> <b>Source:</b> UICP, Asbuilts </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> For UICs where Unit Type is SUMP, and the individual discharge rates have not been tested, records are assigned estimated value. For other UICs Unit Types where actual discharge rate values are unavailable, records are assigned "Unknown". </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Waste Type</h2>
<table><thead><th> <b>Alias:</b> wasteTyp </th><th> <b>Data Type:</b> Long (4) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> 1 </td><td> <b>Domain:</b> {1, 5, 17} </td><td> <b>Source:</b> UICP </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Type of waste going to each facility. Value taken from 'Lookup_Waste_Type_Tbl' lookup table. </th></thead><tbody></tbody></table>

<b>LUT Name:</b> Lookup_Waste_Type {only used codes listed}<br>
<table><thead><th> Waste_Key </th><th> Waste_Desc </th></thead><tbody>
<tr><td> 1 </td><td> Storm water </td></tr>
<tr><td> 5 </td><td> Drinking Water </td></tr>
<tr><td> 17 </td><td> ASR (Aquifer storage and recovery) </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Ops Status</h2>
<table><thead><th> <b>Alias:</b> status </th><th> <b>Data Type:</b> Character (2) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {AC, PA, UC, NB} </td><td> <b>Source:</b> Hansen (normalized) </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Operational status of facility. Values taken from 'WELL STATUS' lookup table.  Operational Status data is granulated in recStatus Field (see below).  All City owned UICs fall under one of the following four classifications:<div>AC = In service, PA = Abandoned, UC = Under Construction, NB = Not Built / Does not Exist.</th></thead><tbody></tbody></table>

<h3><b>LUT Name:</b> Lookup Well Status</h3>
<table><thead><th>Code </th><th> Hansen Description </th><th> Status </th></thead><tbody>
<tr><td> AC </td><td> IN </td><td> In Service </td><td> Active </td></tr>
<tr><td> AC </td><td> CNS </td><td> Constructed No Service </td><td> Active </td></tr>
<tr><td> AC </td><td> TBAB </td><td> To be Abandoned </td><td> Active </td></tr>
<tr><td> AC </td><td> PEND </td><td> In Service Action Pending </td><td> Active </td></tr>
<tr><td> PA </td><td> ABAN </td><td> Abandoned </td><td> Inactive </td></tr>
<tr><td> UC </td><td> NEW </td><td> Under Construction </td><td> Active </td></tr>
<tr><td> NB </td><td> DNE </td><td> Not Built / Does not Exist </td><td> Inactive </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> recordStatus</h2>
<table><thead><th> <b>Alias:</b> rstatus </th><th> <b>Data Type:</b> Character (2) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {0,1,11,12,13,21,22,31,<div>32,33,34,35,36,37,41,42,43,44} </td><td> <b>Source:</b> UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Operational and Record Status Data granulation.  Tracks exact UIC historical status </th></thead><tbody></tbody></table>

<h3>UIC Record Status Description Lookup Up Tables</h3>

<b>LUT Name:</b> Lookup_UIC_Status<br>
<table><thead><th> rCode </th><th> Status </th><th> rStatus </th><th>Description </th><th> Use Status </th></thead><tbody>
<tr><td> 0 </td><td> No Record </td><td> No Record </td><td> No Record Currently Exists, deqID was assigned to unitID but unitID has changed old records - usually from other Bureaus (Others Table) registration records that have been assigned unitID when entered into Hansen </td><td> In Use </td></tr>
<tr><td> 1 </td><td> No Record </td><td> No Record </td><td> not Found - wellId numbering gaps.  No evidence that wellId was ever assigned. </td><td> Deprocated 2012 </td></tr>
<tr><td> 11 </td><td> IN </td><td> AC </td><td> Active Reporting Facility - all tables & FDS </td><td> In Use </td></tr>
<tr><td> 12 </td><td> TBA </td><td> AC </td><td> Active Reporting Facility - To Be Abandoned, formal closure started - all tables & FDS </td><td> In Use </td></tr>
<tr><td> 13 </td><td> CNS </td><td> AC </td><td> Constructed Not in Service (CNS) Constructed Not In Service. Built but does not recieve drainage.  May be plugged. </td><td> In Use </td></tr>
<tr><td> 21 </td><td> UC </td><td> UC </td><td> Active Registration - no Hansen ID assigned   <a href='https://code.google.com/p/besasm-uic/source/detail?r=00'>R00</a>###  No spatial feature in DME & no record in Hansen.  Usually associated with planned / pre-construction. </td><td> In Use </td></tr>
<tr><td> 22 </td><td> UCH </td><td> UC </td><td> Hansen ID assigned from construction documents.  Construction may be complete, but waiting on asbuilts </td><td> In Use </td></tr>
<tr><td> 31 </td><td> SED </td><td> DEQ Removal </td><td> Active - UIC that was converted to non-infiltrating facility (SED) has a wellID assigned to Hansen ID, does not allow pentration to ground water.  Removed from DEQ database thru Quarterly Reporting  </td><td> In Use </td></tr>
<tr><td> 32 </td><td> SAN </td><td> DEQ Removal </td><td> Active - compkey - unitID - not found in Hansen stormWater db but the unitID exist in sanitary db with new compKey Facility mis-catagorized and corrected.  Reported if compKey exists.  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 33 </td><td> OWN </td><td> DEQ Removal </td><td> Active - Ownership change - DEQID assigned, non reporting.  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 34 </td><td> TST </td><td> DEQ Removal </td><td> Registered as UIC but is test Sump - No service Provided - not reported .  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 35 </td><td> DE </td><td> DEQ Removal </td><td> Data Error - wellId assigned record existed in Registration now removed - special case Duplicate registeration record and assignment Unit ID - CompKey - deqId may have not been used or changed on asbuilt facility exists in DME conflicting deqId assignment made (old records).  Hansen data entry error. </td><td> In Use </td></tr>
<tr><td> 36 </td><td> NB </td><td> DEQ Removal </td><td> Does Not Exist - DNE {physically} - deqId was assigned but DNE field verified.  Hansen Status DNE </td><td> In Use </td></tr>
<tr><td> 37 </td><td> NBU </td><td> DEQ Removal </td><td> Registered as UIC but confirmed not Built or Built but not UIC </td><td> In Use </td></tr>
<tr><td> 41 </td><td> PAC </td><td> PA </td><td> Active (PA) Facwell & DME & Hansen records exist with status of PA - Plugged or filled - Decommissioned / Closure </td><td> In Use </td></tr>
<tr><td> 42 </td><td> PAN </td><td> PA </td><td> Active (PA) Facwell & DME & Hansen records exist with status of PA - Plugged or filled - Not Decommissioned </td><td> In Use </td></tr>
<tr><td> 43 </td><td> PAR </td><td> PA<div>DEQ Removal </td><td> Active (PA) Facwell & Hansen records exist with status of PA - Removed - DNE - Decommissioned </td><td> In Use </td></tr>
<tr><td> 44 </td><td> PAG </td><td> PA </td><td> Active (PA) Facwell table record status of PA - Hansen record but no record found in DME, exist in UIC archive table - removed FDS obsolute Pre July 2011 (Hansen 8 Migration).  Spatial location deleted from DME & Hansen;<div>to correct address was geocoded - location is aproximate - No Decommissioning Data </td><td> Deprocated 2012 </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_UIC_rCode<br>
<table><thead><th> <b>rCode</b> </th><th> <b>Status</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> 0 </td><td> No Record </td><td> No Record Currently Exists </td></tr>
<tr><td> 1 </td><td> No Record </td><td> No Record Currently Exists </td></tr>
<tr><td> 11 </td><td> IN </td><td> Active </td></tr>
<tr><td> 12 </td><td> TBA </td><td> To Be Abandoned </td></tr>
<tr><td> 13 </td><td> CNS </td><td> Constructed not in Service </td></tr>
<tr><td> 21 </td><td> UC  </td><td> Under Construction or Planned </td></tr>
<tr><td> 22 </td><td> UCH </td><td> Constructed - Awaiting Asbuilts </td></tr>
<tr><td> 31 </td><td> SED </td><td> Sedimentation Manhole </td></tr>
<tr><td> 32 </td><td> SAN </td><td> Sanitary System </td></tr>
<tr><td> 33 </td><td> OWN </td><td> Ownership Change </td></tr>
<tr><td> 34 </td><td> TST </td><td> Test Sump </td></tr>
<tr><td> 35 </td><td> DE  </td><td> Data Error </td></tr>
<tr><td> 36 </td><td> NB  </td><td> Never Built </td></tr>
<tr><td> 37 </td><td> NBU </td><td> Built but not as UIC </td></tr>
<tr><td> 41 </td><td> PAC </td><td> PA with Closure RPT </td></tr>
<tr><td> 42 </td><td> PAN </td><td> PA no Closure, w/o Authority </td></tr>
<tr><td> 43 </td><td> PAR </td><td> PA Removed with Closure RPT </td></tr>
<tr><td> 44 </td><td> PAG </td><td> PA Removed no Closure & Geocoded, w/o Authority </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_UIC_rCodeRollup - DEQ Quarterly Reporting Code, role up look up table for major rCode classifications<br>
<table><thead><th> <b>Reporting</b><div>Status</th><th> <b>rCode</b><div>Class</th><th> <b>Description</b> </th></thead><tbody>
<tr><td> NR </td><td>  0 </td><td> No Record Found </td></tr>
<tr><td> AC </td><td> 10 </td><td> Active Report Record </td></tr>
<tr><td> UC </td><td> 20 </td><td> Under Construction </td></tr>
<tr><td> RM </td><td> 30 </td><td> Removed from DEQ Database </td></tr>
<tr><td> PA </td><td> 40 </td><td> Plugged - Abandoned </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Installation Date</h2>
<table><thead><th> <b>Alias:</b> instDt </th><th> <b>Data Type:</b> Long (4) </th><th> <b>Nulls:</b> yes </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> Null </td><td> <b>Domain:</b> {YYYY} </td><td> <b>Source:</b> Hansen </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Installation Date by year, in 'YYYY' format. Where data is unavailable, records remain null. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Maintenance Period</h2>
<table><thead><th> <b>Alias:</b> maintPrd </th><th> <b>Data Type:</b> Character (50) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {4 years, 10 years, NA, unknown} </td><td> <b>Source:</b> DME / Hansen - derived, UICP</td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate average maintenance cycle for all BES UICs and based on standard practice. </th></thead><tbody>
<tr><td> <b>Catagory Descriptions:</b><div><b>4 Years</b> - UIC's categorized unit types of Sumps, with pretreatment by Sedimentation Manhole (SED).  Included are destination end points with upstream SED pretreatment.  Example: SED -> perf-pipe -> clean-out. Where the clean-out is designated as the UIC and down stream from SED. Upstream Sumps that are in series with SED are included.<div>  <b>10 Years</b> - UIC's categorized unit types of Sumps without pretreatment by Sedimentation Manhole (SED). Upstream 10 years for UICs without sedimentation manhole.  For non-BES UICs, where Sumps that are in series without SED are included.  In-Series Sump exception  is a direct connection to a inlet actual maintenance period is unavailable, records remain null. (no SED) that is also In-Series, are considered not to have pre-treatment. This applies to Sumps downstream of this point.  Sumps with green facility designations (swales, planters, bio-swales, channels,...) also fall into this designation.<div>  <b>Unknown</b> -  UIC's categorized unit types of Non-Sumps.  These unit type include Rock Trenches, Hybrid (Infiltrating Overflow Pipe), Water Way End Points, .. Also included is non-BES ownership where maintenance period is unknown or maintained by another Bureau.<div><b>NA</b> - UIC's with operation status of Abandoned (PA) </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Location</h2>
<table><thead><th> <b>Alias:</b> location </th><th> <b>Data Type:</b> Character (100) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {UnitID & Address} </td><td> <b>Source:</b> Hansen - Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> For BES UICs, the first 6 characters are unique BES license plate ID (i.e. 'ABC123'). Following the ID is the approximate<div>address location of the UIC. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Lat</h2>
<table><thead><th> <b>Alias:</b> latitude </th><th> <b>Data Type:</b> Single (4) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {} </td><td> <b>Source:</b> Derived </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Latitude in decimal degrees (geographic coordinate system North American 1983 HARN datum). </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Long</h2>
<table><thead><th> <b>Alias:</b> longitude </th><th> <b>Data Type:</b> Single (4) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {} </td><td> <b>Source:</b> Derived </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Longitude in decimal degrees (geographic coordinate system North American 1983 HARN datum). </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Distance to nearest water well</h2>
<table><thead><th> <b>Alias:</b> </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {nearest foot} </td><td> <b>Source:</b> Derived </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate distance in feet to nearest confirmed domestic use drinking water or irrigation well (based on confirmed OWRD/DHS well location data). For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA". </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Distance to nearest wetland</h2>
<table><thead><th> <b>Alias:</b> </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {nearest foot} </td><td> <b>Source:</b> Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate distance in feet to nearest wetland (based on Metro regional wetland GIS data). For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA". </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Distance to nearest surface water</h2>
<table><thead><th> <b>Alias:</b> </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {nearest foot} </td><td> <b>Source:</b> Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate distance in feet to nearest surface water (based on City of Portland surface water GIS data). For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA". </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Depth to groundwater</h2>
<table><thead><th> <b>Alias:</b> Separation Distance </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> None </td><td> <b>Domain:</b> {nearest foot} </td><td> <b>Source:</b> Derived </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate distance in feet from bottom-most perforation to estimated seasonal high groundwater. For BES UICs, where depth of UIC is unknown a depth of 30-ft is assumed, consistent with BES standard UIC design. For BES UICs, 2-ft are subtracted from UIC depth to account for sediment trap ring, consistent with BES standard UIC design. For all non-BES UICs, where UIC depth is unknown, depth to groundwater is calculated from ground elevation. For all UICs, if Ops Status = "PA" (abandoned), records are assigned "NA". </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Size of impervious area</h2>

<table><thead><th> <b>Alias:</b> ImpArea </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> No </th><th> <b>Unique:</b> N/A </th><th> <b>Index:</b> N/A </th></thead><tbody>
<tr><td> <b>Default Value:</b> Averaged </td><td> <b>Domain:</b> {nearest foot} </td><td> <b>Source:</b> Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> Approximate quantity of impervious area draining to UIC in square feet. Where explicit UIC drainage delineations are available, these are intersected with a mapped impervious GIS data set to determine impervious per UIC. For BES UICs, where UIC drainage delineations are unavailable, average impervious is calculated from UICs with available catchment delineations. For non-BES UICs, where impervious area is not available records<div>are assigned "Unknown" impervious. </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Treatment Key</h2>
<table><thead><th> <b>Alias:</b> preTreatment  </th><th> <b>Data Type:</b> Long (4) </th><th> <b>Nulls:</b> </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b> {2,4,7,9,38,43,56,57,69,76} </td><td> <b>Source:</b> </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th> <b>Description:</b> This field contains only primary pretreatment. Actual pretreatment information is housed in the 'Treatment_Tbl' table, because this is a one-to-many relationship. </th></thead><tbody></tbody></table>

<h3>Treatment Key - Treatment Description</h3>
(subset of ODEQ Treatment Key)<br>
<table><thead><th> Code </th><th> Treatment Description</th></thead><tbody>
<tr><td> 2 </td><td> Sediment Manhole </td></tr>
<tr><td> 4 </td><td> Gravel filter or trench </td></tr>
<tr><td> 7 </td><td> None </td></tr>
<tr><td> 9 </td><td> Bioswale - Hybrid </td></tr>
<tr><td> 38 </td><td> Sump in-series with SED </td></tr>
<tr><td> 43 </td><td> Wet pond/constructed wetland </td></tr>
<tr><td> 56 </td><td> Sediment Catch Basin - infiltration inlet </td></tr>
<tr><td> 57 </td><td> Drainfield </td></tr>
<tr><td> 69 </td><td> Grease trap </td></tr>
<tr><td> 76 </td><td> Planter Box </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> Zoning</h2>
<table><thead><th> <b>Alias:</b> genZone  </th><th> <b>Data Type:</b> Character (3) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b> {COM, IND, MFR, MUE,<div>MUR, PF, POS, RUR, SFR} </td><td> <b>Source:</b> UICP, CGIS - Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th><b>Description:</b> Generalized Zone Classifications. Zoning from City of Portland and Metro Planning process is normalized into nine generalized classifications. </th></thead><tbody></tbody></table>

<h3>Zoning Lookup Tables</h3>
<b>LUT Name:</b> Lookup_GenZone<br>
<table><thead><th> Code </th><th> Classifications </th></thead><tbody>
<tr><td> IND </td><td> Industrial </td></tr>
<tr><td> COM </td><td> Commercial </td></tr>
<tr><td> MFR </td><td> Multi-family residential </td></tr>
<tr><td> POS </td><td> Parks and open space </td></tr>
<tr><td> MUR </td><td> Mixed-use residential </td></tr>
<tr><td> SFR </td><td> Single family residential </td></tr>
<tr><td> MUE </td><td> Mixed-use employment </td></tr>
<tr><td> PF  </td><td> Public facilities </td></tr>
<tr><td> RUR </td><td> Rural </td></tr></tbody></table>

<b><i>Metro Land Use</i></b><div><b>LUT Name:</b> Lookup_MetroZoneClass<div><b>Description:</b> 44 regional zoning generalized classifications, is then normalized into 9 genZone classifications.<div>
<table><thead><th> genZone </th><th> Code </th><th> Classification </th><th> Description </th></thead><tbody>
<tr><td> COM </td><td> CC    </td><td> Central Commercial </td><td> Central Commercial allows a full range of commercial typically associated with CBD's and downtowns. More restrictive than general commercial in the case of large lot and highway-oriented uses. Encourages higher FAR uses including multi-story development. </td></tr>
<tr><td> COM </td><td> CG    </td><td> General Commercial </td><td> General Commercial larger scale commercial districts, often with a more regional orientation for providing goods and services. Businesses offering a wider variety of goods and services (including large format retailers) are permitted in this district and include mid-rise office buildings, and highway and strip commercial zones. </td></tr>
<tr><td> COM </td><td> CN    </td><td> Neighborhood Commercial </td><td> Neighborhood Commercial small-scale commercial districts permitting retail and serice activities such as grocery stores and neighborhood service establishments that support the local residential community. Floor space and/or lot sizes are usually limited to between 5,000 to 10,000 square feet. </td></tr>
<tr><td> COM </td><td> CO    </td><td> Office Commercial </td><td> Office Commercial districts accommodating a range of low-rise offices; supports various community business establishments, professional and medical offices; typically as a buffer between residential areas and more intensive commercial districts. </td></tr>
<tr><td> FF  </td><td> FF    </td><td> Agriculture or Forestry </td><td> Agriculture or Forestry activities suited to commercial scale agricultural production or forestry, typically with lot sizes of 10, 20 or 30 acres or more. </td></tr>
<tr><td> IND </td><td> IH    </td><td> Heavy Industrial </td><td> Heavy Industrial districts permit light industrial and intensive industrial activity such as bottling, chemical processing, heavy manufacturing and similar uses with noxious externalities. </td></tr>
<tr><td> IND </td><td> IL    </td><td> Light Industrial </td><td> Light Industrial districts permit warehousing and distribution facilities, light manufacturing, processing, fabrication or assembly. May allow limited commercial activities such as retail and service functions that support the businesses and workers in the district. </td></tr>
<tr><td> MFR </td><td> MFR1  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 15 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR2  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 20 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR3  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 25 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR4  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 30 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR5  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 35 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR6  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 40 units / net acre. </td></tr>
<tr><td> MFR </td><td> MFR7  </td><td> Multi-family </td><td> Multi-family single family, townhouses, row houses permitted outright. Max density permitted is 60 units / net acre. </td></tr>
<tr><td> MUE </td><td> MUE   </td><td> Multiple Use Employment </td><td> an employment district that accommodates a broad range of users including offices, retail stores, warehouse distribution, and light industrial including manufacturing, fabrication, and assembly. </td></tr>
<tr><td> MUR </td><td> MUR1  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.35 </td></tr>
<tr><td> MUR </td><td> MUR10 </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 12.5 </td></tr>
<tr><td> MUR </td><td> MUR2  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.5 </td></tr>
<tr><td> MUR </td><td> MUR3  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 0.75 </td></tr>
<tr><td> MUR </td><td> MUR4  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.25 </td></tr>
<tr><td> MUR </td><td> MUR5  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.5 </td></tr>
<tr><td> MUR </td><td> MUR6  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 1.75 </td></tr>
<tr><td> MUR </td><td> MUR7  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 2 </td></tr>
<tr><td> MUR </td><td> MUR8  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 3 </td></tr>
<tr><td> MUR </td><td> MUR9  </td><td> Mixed Use </td><td> Mixed Use Commercial & Residential with FAR maximum of about 4 </td></tr>
<tr><td> PF  </td><td> PF    </td><td> Public Facilities </td><td> Public Facilities allows government building, institutional and cultural uses such as museums. </td></tr>
<tr><td> POS </td><td> POS   </td><td> Parks and Open Space </td><td> Parks and Open Space </td></tr>
<tr><td> RUR </td><td> RRFU  </td><td> Rural </td><td> Rural Residential or Future Urban - residential uses permitted on rural lands (1 dwelling unit per lot) or areas designated for future urban development, typically lots are 10 or more acres </td></tr>
<tr><td> SFR </td><td> SFR1  </td><td> Single family </td><td> Single family detached housing with minimum lot size from 35,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR2  </td><td> Single family </td><td> Single family detached housing with minimum lot size from 15,000 sq. ft. to a net acre </td></tr>
<tr><td> SFR </td><td> SFR3  </td><td> Single family </td><td> Single family detached housing with lot sizes from about 10,000 sq. ft. to 15,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR4  </td><td> Single family </td><td> Single family detached housing with lot sizes around 9,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR5  </td><td> Single family </td><td> Single family detached housing with lot sizes around 7,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR6  </td><td> Single family </td><td> Single family detached housing with lot sizes around 6,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR7  </td><td> Single family </td><td> Single family detached housing with lot sizes around 5,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR8  </td><td> Single family </td><td> Single family detached housing with lot sizes around 4,500 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR9  </td><td> Single family </td><td> Single family detached housing with lot sizes around 4,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR10 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 3,500 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR11 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 3,000 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR12 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,900 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR13 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,700 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR14 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,500 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR15 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,300 sq. ft. </td></tr>
<tr><td> SFR </td><td> SFR16 </td><td> Single family </td><td> Single family detached or attached housing with lot sizes around 2,000 sq. ft. </td></tr>
<tr><td> UNK </td><td> Null  </td><td> Unknown </td><td> Unknown Zoning or GenZone Classification (Null or Blank) </td></tr></tbody></table>

<b>LUT Name:</b> Lookup_Zoning-genZone<br>
<table><thead><th>Zone </th><th> GenZone </th></thead><tbody>
<tr><td> blank or Null </td><td> UNK </td></tr>
<tr><td>CG </td><td> COM </td></tr>
<tr><td>CM </td><td> COM </td></tr>
<tr><td>CN1 </td><td> COM </td></tr>
<tr><td>CN2 </td><td> COM </td></tr>
<tr><td>CO1 </td><td> COM </td></tr>
<tr><td>CO2 </td><td> COM </td></tr>
<tr><td>CS </td><td> COM </td></tr>
<tr><td>CX </td><td> COM </td></tr>
<tr><td>EG1 </td><td> IND </td></tr>
<tr><td>EG2 </td><td> IND </td></tr>
<tr><td>EX </td><td> IND </td></tr>
<tr><td>IG1 </td><td> IND </td></tr>
<tr><td>IG2 </td><td> IND </td></tr>
<tr><td>IH </td><td> IND </td></tr>
<tr><td>IR </td><td> MFR </td></tr>
<tr><td>IS </td><td> IND </td></tr>
<tr><td>MC </td><td> IND </td></tr>
<tr><td>ME </td><td> IND </td></tr>
<tr><td>Maywo </td><td> SFR </td></tr>
<tr><td>Maywoo </td><td> SFR </td></tr>
<tr><td>Maywood </td><td> SFR </td></tr>
<tr><td>NC </td><td> COM </td></tr>
<tr><td>OC </td><td> COM </td></tr>
<tr><td>OS </td><td> POS </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=1'>R1</a> </td><td> MFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=10'>R10</a> </td><td> SFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=2'>R2</a> </td><td> MFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=2'>R2</a>.5 </td><td> SFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=20'>R20</a> </td><td> SFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=3'>R3</a> </td><td> MFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=5'>R5</a> </td><td> SFR </td></tr>
<tr><td><a href='https://code.google.com/p/besasm-uic/source/detail?r=7'>R7</a> </td><td> SFR </td></tr>
<tr><td>RF </td><td> SFR </td></tr>
<tr><td>RH </td><td> MFR </td></tr>
<tr><td>RX </td><td> MFR </td></tr>
<tr><td>TRA </td><td> TRA </td></tr>
<tr><td>UC </td><td> COM </td></tr>
<tr><td>WC </td><td> UNK </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> constPkg</h2>
<table><thead><th> <b>Alias:</b> constructionPackage  </th><th> <b>Data Type:</b> Character (50) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b> {2, 3, 4, 5, Shallow Sump, Wellfield Retrofit}  </td><td> <b>Source:</b> UICP </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th><b>Description:</b> Sump Rehabilitation Project Design / Construction Package Designator </th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> monPanelID</h2>
<table><thead><th> <b>Alias:</b> monitoringPanel  </th><th> <b>Data Type:</b> Character (10) </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b> P1 1-15, P2 1-15, P3 1-15,<div>P4 1-15, P5 1-15, P6 1-15<div>PBP 1-5, SP1 1-10, SP2 1-10, SP3 1-10,<div>SP4 1-10, SP5 1-10, SP6 1-10 </td><td> <b>Source:</b> UICP </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th><b>Description:</b> UICP Water Pollution Control Facilities (WPCF) Permit Monitoring Sites - Rotating, Stationary, Supplemental Panels. </th></thead><tbody></tbody></table>

<h3><b>LUT Name:</b> Lookup Year-Panel</h3>
<table><thead><th> Year </th><th> Year Dates </th><th> Type </th><th> Panel </th></thead><tbody>
<tr><td> Year 1 </td><td> 2005-2006 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 1 </td><td> 2005-2006 </td><td> Rotating </td><td> P1 </td></tr>
<tr><td> Year 2 </td><td> 2006-2007 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 2 </td><td> 2006-2007 </td><td> Rotating </td><td> P2 </td></tr>
<tr><td> Year 2 </td><td> 2006-2007 </td><td> Penta Baseline </td><td> PBP1 </td></tr>
<tr><td> Year 2 </td><td> 2006-2007 </td><td> Supplemental </td><td> SP1 </td></tr>
<tr><td> Year 3 </td><td> 2007-2008 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 3 </td><td> 2007-2008 </td><td> Rotating </td><td> P3 </td></tr>
<tr><td> Year 3 </td><td> 2007-2008 </td><td> Supplemental </td><td> SP2 </td></tr>
<tr><td> Year 4 </td><td> 2008-2009 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 4 </td><td> 2008-2009 </td><td> Rotating </td><td> P4 </td></tr>
<tr><td> Year 4 </td><td> 2008-2009 </td><td> Supplemental </td><td> SP3 </td></tr>
<tr><td> Year 5 </td><td> 2009-2010 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 5 </td><td> 2009-2010 </td><td> Rotating </td><td> P5 </td></tr>
<tr><td> Year 5 </td><td> 2009-2010 </td><td> Supplemental </td><td> SP4 </td></tr>
<tr><td> Year 6 </td><td> 2010-2011 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 6 </td><td> 2010-2011 </td><td> Rotating </td><td> P1 </td></tr>
<tr><td> Year 6 </td><td> 2010-2011 </td><td> Supplemental </td><td> SP5 </td></tr>
<tr><td> Year 7 </td><td> 2011-2012 </td><td> Stationary </td><td> P6 </td></tr>
<tr><td> Year 7 </td><td> 2011-2012 </td><td> Rotating </td><td> P2 </td></tr>
<tr><td> Year 7 </td><td> 2011-2012 </td><td> Supplemental </td><td> SP6 </td></tr>
<tr><td> Year 8 </td><td> 2012-2013 </td><td> Rotating </td><td> P3 </td></tr></tbody></table>

<hr />

<h2><b>Field:</b> compliance</h2>
<table><thead><th> <b>Alias:</b> uicCat  </th><th> <b>Data Type:</b> Double </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b> {1, 2, 3, 4} </td><td> <b>Source:</b> UICP - Derived </td><td> Authoritative: yes </td></tr></tbody></table>

<table><thead><th><b>Description:</b>  ODEQ Classifications for non-compliant UIC, relating to date of discovery of non-compliance.<div><b>Category 1:</b> UICs known to be non-compliant upon the date of permit issuance (June 1, 2005).<div><b>Category 2:</b> UICs discovered as non-compliant during the Systemwide Assessment (by July 15, 2006).<div><b>Category 3:</b> UICs discovered as non-compliant after completion of the Systemwide Assessment (after July 15, 2006).<div><b>Category 4:</b> UICs that become non-compliant by failing to meet the annual mean maximum allowable discharge<div>limits (MADLs) within one wet season after the exceedance or failing to satisfy any groundwater protection conditions<div>of Schedule A of the permit.</th></thead><tbody></tbody></table>

<hr />

<h2><b>Field:</b> Traffic Counts</h2>
<table><thead><th> <b>Alias:</b> adtCnts  </th><th> <b>Data Type:</b> Double </th><th> <b>Nulls:</b> no </th><th> <b>Unique:</b> no </th><th> <b>Index:</b> no </th></thead><tbody>
<tr><td> <b>Default Value:</b> None  </td><td> <b>Domain:</b>  </td><td> <b>Source:</b> UICP, CGIS (PBOT) - Derived </td><td> Authoritative: no </td></tr></tbody></table>

<table><thead><th><b>Description:</b>  Maxium Average Daily Traffic (ADT) count from PBOT data </th></thead><tbody>