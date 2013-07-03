# ---------------------------------------------------------------------------
# 02d. Reproject Registration UICs to Oregon State Plane.py
# Created on: Fri Apr 09 2010 12:45:18 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
UIC_Registration_Spatial__2_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial_temp__1_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial_Pro"
UIC_Registration_Spatial__1_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
Delete_succeeded__1_ = "true"
UIC_Registration_Spatial__3_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial__4_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial__5_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial__6_ = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"
UIC_Registration_Spatial = "\\\\Oberon\\GRP104\\UIC_Management_Program\\Registrations\\UIC_Registration.mdb\\UIC_Registration_Spatial"

# Process: Project (1)...
gp.Project_management(UIC_Registration_Spatial__2_, UIC_Registration_Spatial_temp__1_,"PROJCS['NAD_1983_HARN_StatePlane_Oregon_North_FIPS_3601',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',8202099.737532808],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',44.33333333333334],PARAMETER['Standard_Parallel_2',46.0],PARAMETER['Latitude_Of_Origin',43.66666666666666],UNIT['Foot',0.3048]]", "","GEOGCS['GCS_Assumed_Geographic_1',DATUM['D_North_American_1927',SPHEROID['Clarke_1866',6378206.4,294.9786982]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_Spatial__1_, "FeatureClass")

# Process: Copy (1)...
gp.Copy_management(UIC_Registration_Spatial_temp__1_, UIC_Registration_Spatial__3_, "")

# Process: Add XY Coordinates...
gp.AddXY_management(UIC_Registration_Spatial__3_)

# Process: Calculate Field (1)...
gp.CalculateField_management(UIC_Registration_Spatial__4_, "longFeet", "[POINT_X]", "VB", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(UIC_Registration_Spatial__5_, "latFeet", "[POINT_Y]", "VB", "")

# Process: Delete Field (1)...
gp.DeleteField_management(UIC_Registration_Spatial__6_, "POINT_X;POINT_Y")
