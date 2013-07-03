# -----------------------------------------------------------------------------------------------
#    file name: 01. Refresh BESUICs.py
#   Written by: Neil Revello
#   Org Source: ArcGIS/ModelBuilder
#   Created on: Wed April 07 2010 04:36:50 PM
#  Modified on: Wed April 08 2010 07:00:30 PM
#     argument: none
#       output: none
#      purpose: Retresh local data set for UIC from DME by selecting UnitType SUM & Infinl and
#               Ownrship is no value or AGRE, BES, UNKN, PARK, WTR, FIRE, PDOT.  Add the Fields
#               need for Quarterly Reporting
#    revisions: none
#        notes: none
#        logic: none
#       errors: none
# -----------------------------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object and Set Environment
gp = arcgisscripting.create()
gp.overwriteoutput = 1
gp.workspace = "c:/temp/"

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")

# Local variables...
uic_mdb = "uicTest.mdb"
UIC = gp.workspace + "/" + uic_mdb + "/uic"

# Create UIC Personal GDB
gp.CreatePersonalGDB_management(gp.workspace, uic_mdb)

# Connection to CGIS published DME
EGHPublicCollectionPoints = "Database Connections\\Connection to EGH_Public on GISSQLProd1.rose.portland.local.sde\
    \\EGH_PUBLIC.ARCMAP_ADMIN.collection_points_bes_pdx"

# Select City Managed UICs from DME
gp.Select_analysis(EGHPublicCollectionPoints, UIC, "[UNITTYPE] in ( 'SUM', 'INFINL') AND ([OWNRSHIP] IS NULL OR\
    [OWNRSHIP] IN ( ' ', 'AGRE', 'BES', 'BGS', 'UNKN', 'PARK', 'WTR', 'FIRE', 'PDOT' ))")

# Add Fields
gp.AddField_management(UIC, "DepthText", "TEXT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "Elevation", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "LongFeet", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "LatFeet", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "LongDecimalDegrees", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "LatDecimalDegrees", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "DepthToGW2008", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "GWVariation2008", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "SepDistance2008", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "DepthToGWCSM", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "SepDistanceCSM", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearDWWell", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearIrrWell", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearWellTaxlot", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearPotentialWell", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearWellMin", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearWetland", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearSurfaceWater", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearECSI", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "InTOT", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "GenZone", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "StreetType", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "NearWellTOTScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "SepDistScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "ZoningScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "TrafficCountScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "PretreatmentScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "DistanceToSurfaceWaterScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "StormwaterQualityScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "MobilityScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "SoilPermeabilityScore", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "PriorityScore", "SHORT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")
gp.AddField_management(UIC, "ComplianceCategory", "SHORT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

# Cast DEPTH to int and Calculate DepthTextField
gp.CalculateField_management(UIC, "DEPTH", "int(!DEPTH!)", "PYTHON", "")
gp.CalculateField_management(UIC, "DepthText", "!DEPTH!", "PYTHON", "")
