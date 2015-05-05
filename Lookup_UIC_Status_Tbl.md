
<h1>UIC Record Status Description Lookup Table</h1>

The field "Status" is a non-ODEQ Reporting field.  This field is used as a bridge between DME - Hansen systems and UIC's status.  The field grandularizes data reported in the Operational Status Field (Ops Status), Ownership Field (OWN), Unit Type (typeCode), and the regularatory required decommissioning.  With the use of monitoring and these indicators, status for Active Reporting, database Removal and historical record tracting is preformed.

<div><b>LUT Name:</b> Lookup_UIC_Status_Tbl<div>
<table><thead><th> Code </th><th> Status </th><th> recStatus </th><th>Description </th><th> Use Status </th></thead><tbody>
<tr><td> 0 </td><td> No Record </td><td> No Record </td><td> No Record Currently Exists, deqID was assigned to unitID but unitID has changed old records - usually from<div>other Bureaus (Others Table) registration records that have been assigned unitID when entered into Hansen </td><td> In Use </td></tr>
<tr><td> 1 </td><td> No Record </td><td> No Record </td><td> not Found - wellId numbering gaps.  No evidence that wellId was ever assigned. </td><td> Deprecated 2012 </td></tr>
<tr><td> 11 </td><td> IN </td><td> AC </td><td> Active Reporting Facility - all tables & FDS </td><td> In Use </td></tr>
<tr><td> 12 </td><td> TBA </td><td> AC </td><td> Active Reporting Facility - To Be Abandoned, formal closure started - all tables & FDS </td><td> In Use </td></tr>
<tr><td> 13 </td><td> CNS </td><td> AC </td><td> Constructed Not in Service (CNS) Constructed Not In Service. Built but does not receive drainage.  May be plugged. </td><td> In Use </td></tr>
<tr><td> 21 </td><td> UC </td><td> UC </td><td> Active Registration - no Hansen ID assigned   <a href='https://code.google.com/p/besasm-uic/source/detail?r=00'>R00</a>###  No spatial feature in DME & no record in Hansen.<div>Usually associated with planned / pre-construction. </td><td> In Use </td></tr>
<tr><td> 22 </td><td> UCH </td><td> UC </td><td> Hansen ID assigned from construction documents.  Construction may be complete, but waiting on as-builts </td><td> In Use </td></tr>
<tr><td> 23 </td><td> UCO </td><td> UC </td><td> Hansen ID assigned from construction documents.  Construction may be complete, but waiting on as-builts<div> Ownership is other than BES</td><td> In Use </td></tr>
<tr><td> 31 </td><td> SED </td><td> RM </td><td> Active but DEQ Removal - UIC that was converted to non-infiltrating facility (SED) has a wellID assigned to Hansen ID, does not allow<div>penetration to ground water.  Removed from DEQ database thru Quarterly Reporting  </td><td> In Use </td></tr>
<tr><td> 32 </td><td> SAN </td><td> RM </td><td> Active but DEQ Removal - compkey - unitID - not found in Hansen stormWater db but the unitID exist in sanitary db with new compKey Facility<div>mis-catagorized and corrected.  Reported if compKey exists.  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 33 </td><td> OWN </td><td> RM </td><td> Active but DEQ Removal - Ownership change - DEQID assigned, non reporting.  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 34 </td><td> TST </td><td> RM </td><td> DEQ Removal - Registered as UIC but is test Sump - No service Provided - not reported .  Removed from DEQ database thru Quarterly Reporting </td><td> In Use </td></tr>
<tr><td> 35 </td><td> DE </td><td> RM </td><td> DEQ Removal - Data Error - wellId assigned record existed in Registration now removed - special case Duplicate registration record<div>and assignment Unit ID - CompKey - deqId may have not been used or changed on as-built facility exists in DME<div>conflicting deqId assignment made (old records).  Hansen data entry error. </td><td> In Use </td></tr>
<tr><td> 36 </td><td> NB </td><td> RM </td><td> DEQ Removal - Does Not Exist - DNE {physically} - deqId was assigned but DNE field verified.  Hansen Status DNE </td><td> In Use </td></tr>
<tr><td> 37 </td><td> NBU </td><td> RM </td><td> DEQ Removal - Registered as UIC but confirmed not Built or Built but not UIC </td><td> In Use </td></tr>
<tr><td> 38 </td><td> MH </td><td> RM </td><td>Active but DEQ Removal - UIC that was converted to non-infiltrating facility (MH) has a wellID assigned to Hansen ID, does not allow<div>penetration to ground water.  Removed from DEQ database thru Quarterly Reporting  </td><td> In Use </td></tr>
<tr><td> 41 </td><td> PAC </td><td> PA </td><td> Active (PA) Facwell & DME & Hansen records exist with status of PA - Plugged or filled - Decommissioned / Closure </td><td> In Use </td></tr>
<tr><td> 42 </td><td> PAN </td><td> PA </td><td> Active (PA) Facwell & DME & Hansen records exist with status of PA - Plugged or filled - Not Decommissioned </td><td> In Use </td></tr>
<tr><td> 43 </td><td> PAR </td><td> PA </td><td> Active (PA) Facwell & Hansen records exist with status of PA - Removed (DEQ Removal??) - DNE - Decommissioned </td><td> In Use </td></tr>
<tr><td> 44 </td><td> PAG </td><td> PA </td><td> Active (PA) Facwell table record status of PA - Hansen record but no record found in DME, exist in UIC archive<div>table - removed FDS obsolete Pre July 2011 (Hansen 8 Migration).  Spatial location deleted from DME & Hansen;<div>to correct address was geocoded - location is approximate - No Decommissioning Data </td><td> Deprecated 2012 </td></tr></tbody></table>

<div><div>
<b>LUT Name:</b> Lookup_UIC_Status_abbrTbl<br>
<div><b>Description:</b> Status - Code and Status abbreviated<br>
<p><p />
<table><thead><th> <b>Code</b> </th><th> <b>Status</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> 0 </td><td> No Record </td><td> No Record Currently Exists </td></tr>
<tr><td> 1 </td><td> No Record </td><td> No Record Currently Exists </td></tr>
<tr><td> 11 </td><td> IN </td><td> Active </td></tr>
<tr><td> 12 </td><td> TBA </td><td> To Be Abandoned </td></tr>
<tr><td> 13 </td><td> CNS </td><td> Constructed not in Service </td></tr>
<tr><td> 21 </td><td> UC </td><td>  Under Construction </td></tr>
<tr><td> 22 </td><td> UCH </td><td> Constructed - Awaiting Asbuilts </td></tr>
<tr><td> 23 </td><td> UCO </td><td> Constructed - Awaiting Asbuilts Ownership is not BES </td></tr>
<tr><td> 31 </td><td> SED </td><td> Sedimentation Manhole </td></tr>
<tr><td> 32 </td><td> SAN </td><td> Sanitary System </td></tr>
<tr><td> 33 </td><td> OWN </td><td> Ownership Change </td></tr>
<tr><td> 34 </td><td> TST </td><td> Test Sump </td></tr>
<tr><td> 35 </td><td> DE  </td><td> Data Error </td></tr>
<tr><td> 36 </td><td> NB </td><td>  Never Built </td></tr>
<tr><td> 37 </td><td> NBU </td><td> Built but not as UIC </td></tr>
<tr><td> 38 </td><td> MH </td><td> Manhole </td></tr>
<tr><td> 41 </td><td> PAC </td><td> PA with Closure RPT </td></tr>
<tr><td> 42 </td><td> PAN </td><td> PA no Closure, w/o Authority </td></tr>
<tr><td> 43 </td><td> PAR </td><td> PA Removed with Closure RPT </td></tr>
<tr><td> 44 </td><td> PAG </td><td> PA Removed no Closure & Geocoded, w/o Authority </td></tr>
<p><p />
<p><p /></tbody></table>

<div><div>
<b>LUT Name:</b> Lookup_UIC_recStatus_abbrTbl<br>
<div><b>Description:</b> recStatus - DEQ Quarterly Reporting Code, role up look up table for major Code classifications<br>
<p><p />
<table><thead><th> <b>recStatus</b> </th><th> <b>Code</b><div>Class</th><th> <b>Description</b> </th></thead><tbody>
<tr><td> NR </td><td>  0 </td><td> No Record Found </td></tr>
<tr><td> AC </td><td> 10 </td><td> Active Report Record </td></tr>
<tr><td> UC </td><td> 20 </td><td> Under Construction </td></tr>
<tr><td> RM </td><td> 30 </td><td> Removed from DEQ Database </td></tr>
<tr><td> PA </td><td> 40 </td><td> Plugged - Abandoned </td></tr></tbody></table>

<b>Description</b> - Metadata full description<br>
<br>
<b>Use Status</b> - Current abbreviation status<br>
<p><p />
<table><thead><th> <b>Name</b> </th><th> <b>Description</b> </th></thead><tbody>
<tr><td> In Use </td><td> Active </td></tr>
<tr><td> Deprocated {date} </td><td> No longer used as of Date </td></tr>