# ---------------------------------------------------------------------------
# 12. CalcElevation.py
# Created on: Tue Apr 16 2013 05:33:31 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Check out any necessary licenses
gp.CheckOutExtension("spatial")

# Load required toolboxes...
gp.AddToolbox("C:/Documents and Settings/nrevello/Application Data/ESRI/ArcToolbox/My Toolboxes/ASM-UIC Tools.tbx")
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Spatial Analyst Tools.tbx")
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files (x86)/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
EGH_RASTER_ARCMAP_ADMIN_LIDAR_DEM_2012 = "Database Connections\\egh_raster.sde\\EGH_RASTER.ARCMAP_ADMIN.LIDAR_DEM_2012"
UIC_Registration_LiDARElevation = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_LiDARElevation"
UICBfr12ft = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UICBfr12ft"
UICCrnt = "UICCrnt"
UIC_Registration_Spatial = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_Spatial"
Delete_succeeded__1_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_LiDARElevation"
UIC_Registration_LiDARElevation__2_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_LiDARElevation"
UIC_Registration_LiDARElevation__3_ = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\UIC_Registration_LiDARElevation"
CGISLidarDEM_UICLocate12ftBfr = "\\\\cassio\\gis2\\PROJECTS\\7750\\Registrations\\UIC_Locator.mdb\\CGISLidarDEM_UICLocate12ftBfr"

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(UIC_Registration_Spatial, UICCrnt, " [regIDFull] IS NULL", "", "regID regID VISIBLE NONE;regIDFull regIDFull VISIBLE NONE;userID userID VISIBLE NONE;createdDate createdDate VISIBLE NONE;siteAddress siteAddress VISIBLE NONE;uicType uicType VISIBLE NONE;latDD latDD VISIBLE NONE;longDD longDD VISIBLE NONE;latDMS latDMS VISIBLE NONE;longDMS longDMS VISIBLE NONE;latFeet latFeet VISIBLE NONE;longFeet longFeet VISIBLE NONE;uicDepth uicDepth VISIBLE NONE;uicDiameter uicDiameter VISIBLE NONE;elevation elevation VISIBLE NONE;designDrainageRateCFS designDrainageRateCFS VISIBLE NONE;designDrainageRateGPM designDrainageRateGPM VISIBLE NONE;testDrainageRateCFS testDrainageRateCFS VISIBLE NONE;testDrainageRateGPM testDrainageRateGPM VISIBLE NONE;impAreaAcres impAreaAcres VISIBLE NONE;uicPretreatmentType1 uicPretreatmentType1 VISIBLE NONE;uicPretreatmentType2 uicPretreatmentType2 VISIBLE NONE;nearDWWellID nearDWWellID VISIBLE NONE;nearDWWell nearDWWell VISIBLE NONE;dwWellOwnerType dwWellOwnerType VISIBLE NONE;nearIrrWellID nearIrrWellID VISIBLE NONE;nearIrrWell nearIrrWell VISIBLE NONE;irrWellOwnerType irrWellOwnerType VISIBLE NONE;nearPotentialWellID nearPotentialWellID VISIBLE NONE;nearPotentialWell nearPotentialWell VISIBLE NONE;potentialWellOwnerType potentialWellOwnerType VISIBLE NONE;nearWellTaxlotID nearWellTaxlotID VISIBLE NONE;nearWellTaxlot nearWellTaxlot VISIBLE NONE;wellTaxlotOwnerType wellTaxlotOwnerType VISIBLE NONE;nearECSIID nearECSIID VISIBLE NONE;nearECSI nearECSI VISIBLE NONE;inTOT inTOT VISIBLE NONE;genZone genZone VISIBLE NONE;streetType streetType VISIBLE NONE;approvedByID approvedByID VISIBLE NONE;approvalDate approvalDate VISIBLE NONE;wellNumber wellNumber VISIBLE NONE;deqID deqID VISIBLE NONE;unitID unitID VISIBLE NONE;projectNumber projectNumber VISIBLE NONE;comments comments VISIBLE NONE;nearWetland nearWetland VISIBLE NONE;nearSurfaceWater nearSurfaceWater VISIBLE NONE;gwDepth2008 gwDepth2008 VISIBLE NONE;gwVar2008 gwVar2008 VISIBLE NONE;sepDist2008 sepDist2008 VISIBLE NONE;gwDepth2007 gwDepth2007 VISIBLE NONE;gwVar2007 gwVar2007 VISIBLE NONE;sepDist2007 sepDist2007 VISIBLE NONE;gwDepthCSM gwDepthCSM VISIBLE NONE;sepDistCSM sepDistCSM VISIBLE NONE;altRegID altRegID VISIBLE NONE;POINT_X POINT_X VISIBLE NONE;POINT_Y POINT_Y VISIBLE NONE")

# Process: Buffer...
gp.Buffer_analysis(UICCrnt, UICBfr12ft, "12 Feet", "FULL", "ROUND", "NONE", "")

# Process: RasterClip...
gp.toolbox = "C:/Documents and Settings/nrevello/Application Data/ESRI/ArcToolbox/My Toolboxes/ASM-UIC Tools.tbx";
gp.RasterClip(EGH_RASTER_ARCMAP_ADMIN_LIDAR_DEM_2012, CGISLidarDEM_UICLocate12ftBfr, UICBfr12ft)

# Process: Delete (1)...
gp.Delete_management(UIC_Registration_LiDARElevation__2_, "FeatureClass")

# Process: Extract Values to Points (1)...
gp.ExtractValuesToPoints_sa(UICCrnt, CGISLidarDEM_UICLocate12ftBfr, UIC_Registration_LiDARElevation, "INTERPOLATE", "ALL")

# Process: Calculate Field...
gp.CalculateField_management(UIC_Registration_LiDARElevation, "ELEVATION", "[RASTERVALU]", "VB", "")
