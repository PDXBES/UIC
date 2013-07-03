""" -----------------------------------------------------------------------------------------------
    file name: createDomain_wasteType.py
   Written by: Neil Revello
   Org Source: ArcGIS Modeler
   Created on: 8/4/2010 10:03AM
  Modified on: 8/4/2010 10:03AM
     argument: None
       output:
      purpose: Create an attribute domain to constrain waste type values
    revisions:
        notes:
        logic:
       errors:
  ----------------------------------------------------------------------------------------------"""
# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object and Set Environment
gp = arcgisscripting.create(9.3)
gp.overwriteoutput = 1
# Load required toolboxes
# Modules
# Local variables
# Set the workspace (to avoid having to type in the full path to the data every time)
gp.Workspace = "E:/arcgis/ArcTutor/BuildingaGeodatabase"
# Set variable for database & domain names
dbName =
domainName = ("wasteType", "Deq Waste Type Description")
# set domain  to (Waste_Key, Waste_Desc) list
domain = ((1, "Stormwater"),(2, "Agriculture"),(3, "Grey water"),(4, "Geothermal/heat Pump"),(5, "Drinking Water"), (6, "Condensate"),(7, "Vehicle Wash Water"),(8, "Auto Waste"),(9, "Domestic Sewage"),(10, "Reuse Water/Recycled"),(11, "Treated Water"),(12, "Petroleum Products"),(13, "Process Water"),(14, "Remediation"),(15, "Other/Waste Fluids"),(16, "Medical Waste"),(17, "ASR"),(18, "Mixed Fluids"),(19, "Industrial"))

# Main Function

try:
    # Create the coded value domain
    gp.CreateDomain(dbName, domainName[0], domainName[1], "TEXT", "CODED")

    # Add valid material types to the domain
    for codeValue in domain :
        gp.AddCodedValueToDomain(dbContainer, domainName, codeValue[0], codeValue[0])

    # Constrain the material value of distribution mains
    #gp.AssignDomainToField("Montgomery.mdb/Water/Distribmains", "Material", domname)

except:
    # If an error occurred while running a tool print the messages
    print gp.GetMessages()
# End

preTreatmentDescriptions
Treatment_Key, Treatment_Description
1, Curb inlets
2, Sediment manhole
3, Catch basin
4, Gravel filter or trench
5, Lynch catch basin
6, Manhole w/settling sump
7, None
8, Activated sludge drainfield
9, Bioswale
10, Settling basin
11, Oil Water separator
12, O/Grit separator
13, Large OS w/drainfield
14, Leachfield
15, Inverted syphon catch basin
16, Extraction w/carbon filter
17, Kristar hi capacity Flo-guard+
18, Filter tanks
19, Disinfection
20, Stormceptor
21, Carbon filter
22, Anaerobic digestion
23, Sediment trap
24, Orenco filter (leaching)
25, Perforated sediment manhole
26, Re-circulating gravel filter onsite
27, Bioremediation
28, Chemical remediation
30, Sand filter
33, Seepage bed
34, Settling tank
35, Sump basket w/filter
36, Vortechics WQ vault
37, Infiltration basin/pond
38, Sump
39, Drywell
40, Peat/compost filter
41, Peat/sand filter
42, Vegetated rock/rock reed filter
43, Wet pond/constructed wetland
44, Presettling/settling basin
45, Extended detention dry pond
46, Wet/dry vault
47, Catch basin insert (see if type is listed)
48, Multi-chambered treatment train
49, Vegetated buffer strips
50, Stormdrain inlet protection
51, Absorbant pads
52, Stabilized lagoon
54, Trash Screen
55, Sedimentation Manhole w/baffle
56, Sediment Catch Basin
57, Drainfield
58, S.I.F.T. Filter
59, Settling Sump
60, Siphon
61, Water Recycler
62, Water Conditioner
63, Remediation
64, Air Stripper
65, Aeration
66, Stormfilter vault
67, Stormgate separator
68, Recirulating textile filter
69, Grease trap
70, Trench drain
71, Vortex
72, CDS (swirl)
73, StormFilter catch basin insert
74, Abtech Ultra Urban Filter
75, perforated piping
76, planter box
77, CDS media filter
78, stormtech (roof UIC)


wellTypeID, EPA WELL TYPES
5A5, Electric Power Generator
5A6, Geothermal Heat
5A7, Closed Loop Heat Pump Return
5A19, Cooling Water Return
5D2, Stormwater
5D3, Drill Hole
5D4, Industrial Storm Runoff
5G30, Special Drainage Water
5R21, Aquifer Recharge
5W10, Cesspool
5W11, Septic System (gen)
5W12, Water Treatment Plant Effluent
5W20, Industrial Process Water
5W31, Septic System (well disposal)
5W32, Septic System (drainfield)
5W9 , Untreated Sewage
5X26, Aquifer Remediation
5X27, Other Wells
5X28, Motor Vehicle Waste
5X29, Abandoned Drinking Well

PROJECT_STATUS
status_id, status
1, Open
2, Completed
3, Cancelled
4, Future
5, On Hold
6, Prior Fy
7, Prim Bud

BUREAU
bureauID, bureauName
PDT, Office of Transportation
WTR, Water Bureau
PKS, Parks Bureau
PDC, Portland Development Commission
OMF, Office of Management and Finance
BGS, Bureau of General Services
GIS, Coprorate GIS
BOP, Bureau of Planning
ONI, Office of Neighborhood Involvement


cipOBJECTIVE
copObjectiveCode, Description
C01, Mandated
C02, Maintenance/Repair
C03, Expansion
C04, Replacement
C05, Efficiency

dbo_PHASE_DEFINITION:Table
phase_id  phase_code     phase_name     phase_display_order
   3           P          Predesign             2
   4           D          Design                3
   5           A          Advertise-NTP         4
   6           C          Construction          5
   7           S          Startup/Closeout      6
   8           L          Land Acquisition      1

  dbo_V_BES_ELEMENT:Table
item_key  customer_field_desc
 BEK001, E01 CORNERSTONE
 BEK002, E02 COLUMBIA SLOUGH
 BEK003, E03 WILLAMETTE
 BEK004, E04 EAST WILLAMETTE
 BEK005, E05 WEST WILLAMETTE

   dbo_V_BES_GROUP:Table
item_key, customer_field_desc
 BGRT02, T02 SEWAGE TREATMENT
 BGRT03, T03 MAINT & RELIABILITY
 BGRT04, T04 SURFACE WATER MGMT
 BGRT05, T05 COMBINED SEWER
 BGRT06, T06 SYSTEMS DEVELOPMENT
 BGRT13, T13 OPERATING PROJECT
 BGRT99, T99 MISCELLANEOUS

dbo_V_BES_KIND:Table
item_key,  customer_field_desc
 BKI001, K01 SANITARY PIPELINE
 BKI002, K02 STORMWATER PIPELINE
 BKI003, K03 COMBINED SEWER
 BKI004, K04 WASTEWATER FACILITY
 BKI005, K05 STORMWATER FACILITY
 BKI006, K06 PUMP STATION
 BKI007, K07 STREAM RESTORATION
 BKI008, K08 PLANT/PS MACHINERY
 BKI099, K99 NON-INFRASTRUCTURE

dbo_V_BES_TYPE:Table
item_key,  customer_field_desc
 BTY001, STAND-ALONE
 BTY002, PRIMARY
 BTY003, SECONDARY

dbo_V_BES_WATERSHED:Table
item_key,  customer_field_desc
 BWS001, EAST WILLAMETTE
 BWS002, JOHNSON CREEK
 BWS003, ALL WATERSHEDS
 BWS004, COLUMBIA SLOUGH
 BWS005, NW WILLAMETTE
 BWS006, SW WILLAMETTE
 BWS007, FANNO BASIN


Well Classifications Domain
typeCODE, PURPOSE
 1L,  Industrial Disposal
 1M,  Municipal Disposal
 1N,  Nuclear Waste Disposal Or Storage
 1X,  Other Class 1
 2A,  Annular Injection
 2D,  Produced Fluid Disposal
 2H,  Hydrocarbon Storage
 2R,  Enhanced Recovery Injection
 2X,  Other Class 2
 3G,  In Situ Gassification
 3M,  Solution Mining
 3S,  Sulfer Mining By Frasch Process
 3T,  Geothermal
 3U,  Uranium Mining
 3X,  Other Class 3
 4H,  Hazardous Facility Injection
 5F1, Agricultural Drainage
 5D2, Storm Water Drainage
 5D3, Storm Water Drill Holes/seepage Pits
 5D4, Industrial Storm Water Drainage
 5A5, Electric Power Reinjection
 5A6, Direct Heat Reinjection
 5A7, Heat Pump/air Conditioning Return Flow
 5A8, Groundwater Aquaculture Return Flow
 5W9, Sewage Drill Holes/seepage Pits
 5W10, Cesspools
 5W11, Septic Systems (undifferentiated Disposal Method)
 5W12, Domestic Wastewater Treatment Plant Effluent Disposal
 5X13, Mining, Sand, Or Other Backfill
 5X14, Solution Mining
 5X15, In-situ Fossil Fuel Recovery
 5X16, Spent-brine Return Flow
 5X17, Air Scrubber Waste Disposal
 5X18, Water Softener Regeneration Brine Disposal
 5A19, Cooling Water Return Flow
 5W20, Industrial Process Water And Waste Disposal
 5R21, Aquifer Recharge
 5B22, Saline Water Intrusion Barrier
 5S23, Subsidence Control
 5N24, Radioactive Waste Disposal
 5X25, Experimental Technology
 5X26, Aquifer Remediation Related
 5X27, Other Wells - including greywater
 5X28, Motor Vehicle Waste Disposal Wells
 5X29, Abandoned Drinking Water Wells Used For Disposal Of Waste
 5G30, Other Drainage-Potable or Dewatering
 5W31, Septic Systems (well Disposal Method)
 5W32, Septic Systems (drainfield Disposal Method)
 5ZZZ, Unknown-not Registered

Codes used for Risk_Priorty UIC Regional Action List Report.  1=5X28, 2=5X50, 3=5W9 & 5W10, 4=5D2,5D3,5D4

Well Status Domain
wellStatus, Status Description
AC, Active
UC, Under Construction
TA, Temporarily Abandoned
PA, Plugged and Abandoned
AN, Abandoned w/o Authority
CL, Formal Closure
RU, Proposed Under Review
RA, Active Under Review
RT, Temporarily Abandoned Under Review
RP, Abandoned Under Review
RC, Closure Under Review
AP, Active Permit
CO, Conversion


Facility Discharge Domain
uicIDNumber, Discharge Process
10102, Dry Well or sump
11191, Aquifer recharge
10016, Dry Well or sump
10017, Cesspool
11465, Greywater
11868, Dry Well or sump
10651, Dry Well or sump
11074, ASR
11074, Greywater
11191, Greywater
11195, Aquifer recharge
11195, Greywater
11196, Others
11197, Dry Well or sump
12033, Dry Well or sump
12117, Dry Well or sump
