""" -----------------------------------------------------------------------------------------------
    file name: DataRefreshDomains.py
   Written by: Neil Revello
   Org Source: ArcGIS ModelBuilder - Port
   Created on: 4/16/2013 5:00PM
  Modified on: 4/16/2013 6:00PM
     argument:
       output: <Results Directory>
      purpose: Relinks Domains after data update
    revisions:
        notes:
        logic:
       errors:
  ----------------------------------------------------------------------------------------------"""
# Import system modules
import sys, string, os, arcgisscripting
# import for ArcGIS 10.1
# import arcpy

# Create the Geoprocessor object and Set Environment
gp = arcgisscripting.create(9.3)
gp.overwriteoutput = 1

# Load required toolboxes
# Modules
# Local variables
regSpt = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"

# Main Function
arcpy.AssignDomainToField_management(regSpt, "userID", "userID", "")
arcpy.AssignDomainToField_management(regSpt, "uicType", "uicType", "")
arcpy.AssignDomainToField_management(regSpt, "uicPretreatmentType1", "preTreatment", "")
arcpy.AssignDomainToField_management(regSpt, "uicPretreatmentType2", "preTreatment", "")
arcpy.AssignDomainToField_management(regSpt, "approvedByID", "aUserId", "")

# End
