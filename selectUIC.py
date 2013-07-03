""" -----------------------------------------------------------------------------------------------
    file name: selectUIC.py
   Written by: Neil Revello
   Org Source: ArcGIS/ModelBuilder
   Created on: 2013-04-25 14:56/
  Modified on: 4/26/2013 4:09PM
     argument:
       output:
      purpose:
    revisions:
        notes:
        logic:
       errors:
  ----------------------------------------------------------------------------------------------"""
# Import system modules
import sys, string, os, arcpy, arcgisscripting

# Create the Geoprocessor object and Set Environment
gp = arcgisscripting.create()
gp.overwriteoutput = 1
gp.CheckOutExtension("spatial")  # Check out any necessary licenses
#    Load required toolboxes

#    Print script ident
print "Running Script: " + sys.argv[0]

# Local variables:
  # Data Sources
EGH_Public_collection_points_bes_pdx = "Database Connections\\egh_public.sde\\EGH_PUBLIC.ARCMAP_ADMIN.collection_points_bes_pdx"
EGH_Public_collection_points_alt_bes_pdx = "Database Connections\\egh_public.sde\\EGH_PUBLIC.ARCMAP_ADMIN.collection_points_alt_bes_pdx"
UIC_Registration_Spatial = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
UIC_GIS_status7 = "Database Connections\\besdbdev1.UIC.sde\\UIC.GIS.status7"
  # Feature Data Sets (fds)
besuic = "C:/temp/temp.mdb/besuic"    # Merged set of permit covered UICs
besuica = "C:/temp/temp.mdb/besuica"  # COP Owned UICs with type of Sump, Infinitration Inlet, Overflow Stand Pipe Infilitration
besuicb = "C:/temp/temp.mdb/besuicb"  # COP Owned UICs with type of CleanOut, DE, ManHole, Overflow Stand Pipe, Water Way End, Null and ALTIDTYP of UICDEQID
besuicc = "C:/temp/temp.mdb/besuicc"  # New COP Permit UICs
besuic7 = "C:/temp/temp.mdb/besuic7"  # Status Group 4 - oCode 7, pCode 44

fds = besuic7 + ";" + besuica + ";" + besuicb + ";" + besuicc
"""
Field_Map = "UNITID \"UNITID\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,UNITID,-1,-1,besuica,UNITID,-1,-1,besuicb,UnitID,-1,-1,besuicc,regIDFull,-1,-1;\
             deqID \"deqID\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,deqID,-1,-1,besuicc,deqID,-1,-1,besuicb,ALTID,-1,-1;\
             compKey \"compKey\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,compKey,-1,-1,besuica,COMPKEY,-1,-1,besuicb,COMPKEY,-1,-1;\
             OWNRSHIP \"OWNRSHIP\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,OWNRSHIP,-1,-1,besuicb,OWNRSHIP,-1,-1;\
             SERVSTAT \"SERVSTAT\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,SERVSTAT,-1,-1,besuicb,SERVSTAT,-1,-1,besuic7,recStatus,-1,-1;\
             UNITTYPE \"UNITTYPE\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,UNITTYPE,-1,-1,besuicb,UNITTYPE,-1,-1,besuicc,uicType,-1,-1"
"""
# Field_Map = "UNITID \"UNITID\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,UNITID,-1,-1,besuica,UNITID,-1,-1,besuicb,UnitID,-1,-1,besuicc,regIDFull,-1,-1;\deqID \"deqID\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,deqID,-1,-1,besuicc,deqID,-1,-1,besuicb,ALTID,-1,-1;compKey \"compKey\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,compKey,-1,-1,besuica,COMPKEY,-1,-1,besuicb,COMPKEY,-1,-1;OWNRSHIP \"Ownership\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,OWNRSHIP,-1,-1,besuicb,OWNRSHIP,-1,-1;SERVSTAT \"Service Status\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,SERVSTAT,-1,-1,besuicb,SERVSTAT,-1,-1,besuic7,recStatus,-1,-1;UNITTYPE \"UNITYPE\" true true false 50 Text 0 0 ,First,\" \\ \",besuica,UNITTYPE,-1,-1,besuicb,UNITTYPE,-1,-1,besuicc,uicType,-1,-1"
Field_Map = "UNITID \"UNITID\" true true false 50 Text 0 0 ,First,\" \\ \",besuic7,UNITID,-1,-1,besuica,UNITID,-1,-1,besuicb,UnitID,-1,-1,besuicc,regIDFull,-1,-1;"
# Main
  # Select UIC from different data sources
arcpy.Select_analysis(EGH_Public_collection_points_bes_pdx, besuica, "[UNITTYPE] in ( 'SUM', 'INFINL', 'OVRINF' ) AND ([OWNRSHIP] IS NULL OR\
                                                                      [OWNRSHIP] IN ( ' ', 'AGRE', 'BES', 'BGS', 'UNKN', 'PARK', 'WTR', 'FIRE', 'PDOT' ))")
arcpy.Select_analysis(EGH_Public_collection_points_alt_bes_pdx, besuicb, "[UNITTYPE] in ( 'CO', 'DE', 'MH', 'OVRPIP', 'WWE', NULL  ) AND\
                                                                          ([OWNRSHIP] IS NULL OR [OWNRSHIP] IN ( ' ', 'AGRE', 'BES', 'BGS', 'UNKN', 'PARK', 'WTR', 'FIRE', 'PDOT' )) AND\
                                                                          [ALTIDTYP] = 'UICDEQID' AND [SYSTEM] ='STORM'")
arcpy.Select_analysis(UIC_Registration_Spatial, besuicc, "[unitID] IS NULL OR [unitID] = ''")
arcpy.Select_analysis(UIC_GIS_status7, besuic7, "")

  # Merge Feature Data Sets into one
arcpy.Merge_management(fds, besuic, Field_Map)

print "Script Complete: " + sys.argv[0]


