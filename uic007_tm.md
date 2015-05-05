| UIC007 | Technical Memorandums | Current - Final |
|:-------|:----------------------|:----------------|

| From  | Stephen Himes |
|:------|:--------------|
| Reviewed By | Mark Liebe, Joel Bowker |
| Date | February 20, 2007 |
| Project | 7750 – UIC System Assessment |
| Subject | UIC Subcatchment Delineations |

| Revision History |
|:-----------------|
| Date | Editor | Description |
| June 8, 2012  | Neil Revello | Conversion to WIKI for UIC and Auto-Delineation Dev. Projects |



# Introduction #
Two methods have been employed by BES Systems Analysis to delineate drainage catchments for City of Portland underground injection controls (UICs): manual and automated.  This memo describes the data and methods used for these two methods, the status of each, and potential future work.
# Background #
Though there are multiple drivers for having such delineations, the primary one is the current Water Pollution Control Facilities Permit #102830 (“the permit”) for City of Portland UICs, issued by Oregon Department of Environmental Quality (ODEQ) on June 1, 2005.  Though the permit does not explicitly require drainage catchments to be completed for each UIC, they are necessary to characterize the area draining to each UIC.
Systems Analysis has been manually delineating UIC drainages in support of the UIC Program and the Eastside CSO Tunnel design for several years.  For the UIC Program, the effort targeted UICs that drain either commercial or industrial zoned properties, and for the Eastside Tunnel the effort targeted UICs in the CSO area only.  There was some redundancy between these two efforts, and approximately 5,640 UICs were left without a manually delineated catchment.  Further, the two efforts had different standards and goals – thus different polygon boundaries, preventing seamless merging of the resultant datasets.  Systems Analysis was asked to develop a process to automatically delineate UIC catchment areas, the primary benefits of such a process being:
  1. Repeatable process: dependant on data – not subject to delineator’s opinion – and can be quickly and easily repeated should the underlying system data change.
  1. Full system solution: eliminates concern over merging of disparate datasets.
# Data Sources #
## Manual Delineation ##
The following primary data sources used in the process of manual delineation are typical BES or City GIS datasets.  These include:
  * Mapped collection system data (All\_s, All\_n)
  * Elevation contours
  * Zoning
  * Aerial photography
The following secondary data sources used in the process of manual delineation are specific to BES Systems Analysis.  These include:
  * “Smart” streets (cl\_same\_segs, cl\_back\_segs)
  * Point elevation data (Spotelev)
  * Aspect arrows
  * Curb and sidewalk lines
  * Depth to groundwater
## Automated Delineation ##
The following datasets were used in the automated delineation process:
  * 5-ft interval elevation points
  * Street surface impervious area polygons
  * Street centerlines
  * Mapped facilities data (All\_s, All\_n)
# Methods #
The manual delineations were completed using MapInfo Professional GIS.  This software package was the Bureau GIS standard when most of the manual delineations were completed.  Though BES has now changed GIS platforms from MapInfo to ESRI ArcMap 9, manual delineations continued in MapInfo because all data layers and processes were already standardized, allowing for the delineations to continue efficiently and consistently.  Automatic delineations of UIC subcatchments were completed in ArcMap so that the process could continue into the future consistent with Bureau standards.
## Manual Delineation ##
Manual delineations of UIC subcatchments were created solely using GIS layers in MapInfo.  The first delineations were created by Limno-Tech, Inc. (LTI).  Deana Foster (contract Technician) continued where LTI left off, doing the bulk of the delineations.  Stephen Himes (BES Technician), Andrey Nikolayev (contract Technician) and Meredith Rizzari (contract Technician) also contributed to the delineation layer.  The entire existing coverage of manual delineation polygons is shown in Figure 4-1.  Following is the basic process list used in the creation of these delineations:
  1. Delineate estimated catchment polygons using available GIS layers and general knowledge of hydrology/physical processes.  Delineate catchments to inlets that flow to UICs, not to the UIC locations themselves.  Where GIS layers are incomplete or show conflicting information, use best judgment in determining where stormwater would likely flow.
  1. Start delineation process in commercial and industrial zoned areas.  The primary regulatory driver behind creating delineation catchments is to characterize the landuse in the areas draining to UICs, and commercial/industrial taxlots are the current priority.  Since explicit landuse data is not available for the City of Portland, zoning should be used as a surrogate.
  1. Start delineation process in areas with high ground water (less than 30 ft depth to groundwater).
  1. Continue delineation layer created/edited by previous delineator – catchments should be seamless, with no overlaps.
  1. Each catchment polygon must have a valid Hansen ID number for the UIC it drains to in the UNITID1 field.  If catchment drains to more than one UIC (i.e. sumps in series) than the additional UIC IDs must be entered in the subsequent UNITIDx fields.
  1. Enter the initials of delineator in the Source field.
![http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure41.jpg](http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure41.jpg)<div>Figure 4-1.  Manual delineation polygons for UICs in commercial and industrial zoned areas.<br>
<h2>Automated Delineation</h2>
Automated delineations were created using the Hydrology toolset in ESRI’s Spatial Analyst extension, and are based on a 5-ft digital elevation model (DEM).  The Hydrology toolset includes the tools required to delineate drainage areas by the Deterministic-8 Node (D8) algorithm, which requires each grid cell to flow into only one of its eight neighboring cells, and must follow the path of steepest descent (O’Callaghan and Mark, 1984).  Garbrecht and Martz (2000) discuss the limitations of this method, including “difficulties identifying surface drainage in the presence of depressions, flat areas, and flow blockages.”  The authors dismiss these problematic landscape features as being “often the result of data noise, interpolation errors, and systematic production errors in DEM elevation values.”  While this method has been used extensively for watershed-scale delineations, no literature was found regarding its use delineating urban areas of the scale being discussed here.  Therefore some of the pre-processing steps in the following sections were modified from a watershed-scale context to an urban drainage context.<br>
The general steps taken to create the delineations are presented below, with a more detailed process list provided in Appendix A.<br>
<h3>Elevation Data Conversion</h3>
The first step in automating the UIC delineations was to prep the spatial data for processing.  Point data in 5-ft interval grids (see Figure 4-3b for an example) already existed for the entire City in MapInfo table format.  Figure 4-2 shows the areal extent of these sectioned elevation point layers.  The origin of this data is a triangulated irregular network (TIN) that was created from BES 2-ft topographic contours and BES photogrammetric elevation points.  A TIN creates an elevation surface by triangulating between known elevation points (Figure 4-3a).  The geometry of each triangle, then, is planar and is defined by the (x, y, z) values of each of its nodes (Bonham-Carter, 2002).  Interpolated elevation values were extracted from the TIN to 5-ft interval points (Figure 4-3b).  A DEM was then created using the interpolated elevation values (Figure 4-3c).<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure42.jpg' /><div>Figure 4-2.  Area Covered by 5-ft Elevation Grid Point Layers.<div></li></ul>

Since all delineation processing was done in ESRI, the MapInfo point grid tables were converted to ESRI shapefile format using MapInfo’s Universal Translator 4.0 tool, which uses the FME translation engine.  The shapefile point elevation data was then converted to raster (ESRI’s GRID format).  All of the three Eastside DEM segments (Columbia Slough, Eastside CSO, and sewer extension) were stitched together using ESRI’s Mosaic geoprocessing tool.<br>
<br>
<table><thead><th> <img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure43a.jpg' /><div>Figure 4-3a. Example of TIN created from irregularly distributed elevation points. </th><th> <img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure43b.jpg' /><div>Figure 4-3b. Interpolated elevation values extracted from TIN to points at 5-ft intervals. </th></thead><tbody>
<tr><td> <img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure43c.jpg' /><div>Figure 4-3c. Example raster resultant from 5-ft interval elevation points.<div>Note each point is at the center of its corresponding grid cell. </td></tr></tbody></table>

<h3>Inlet Identification</h3>
To obtain the most accurate delineations possible, the inlet-to-UIC relationship needed to be established.  Delineating to the location of the UIC would be incorrect because that is typically not the point of entry for stormwater into the UIC system.<br>
Though it is possible to establish point-line-point connectivity using attributes in the Hansen facility management database, this method could not be used in this instance because the majority – approximately 70% – of inlets contains null values in the ID fields necessary for such an analysis.  The best remaining option was to use GIS spatial facility datasets to establish the necessary connectivity.  InletGrouper is a custom MapBasic program written to “crawl” up the connecting storm pipes from each mapped UIC facility point.  All inlets that were found to be upstream were tagged with the unique ID for that UIC.  The resultant dataset contains 16,559 inlet points that drain stormwater to UICs.<br>
It should be noted that this process is not perfect, and depends completely on the correctness of the GIS collection system dataset being used.  One major issue that was discovered in this process is that many inlet leaders are drawn flowing the wrong way (i.e. from the UIC to the inlet), which InletGrouper cannot detect.  As many cases of this that the author has noted in the DME dataset while processing the auto-delineations have been passed on to the BES Mapping Group for verification/correction.  This should greatly improve the connectivity detectible by InletGrouper in the future.<br>
<h3>DEM Data Pre-Processing</h3>
The Eastside DEM required some pre-processing prior to use in creating delineation polygons.  Those steps are summarized in the following sections.<br>
<h4>Raise Water Body Elevations</h4>
All grid cells located within water bodies had 1,000ft added to their elevation.  This step created artificially elevated areas that protected the water bodies from being filled in step 4.2.3.2.<br>
<h4>Fill Sinks</h4>
All sinks were filled using ESRI’s Fill geoprocessing tool.  Sinks are areas in a DEM from which flow cannot escape due to being surrounded by grid cells with higher elevations.  It is probable that in an urban DEM of this scale many sinks are real and not just data errors; however, specific knowledge of those sinks that should be preserved would be required in order to only fill erroneous sinks.  In the absence of such a dataset, the City of Portland water body coverage is the closest thing to an available sink inventory, as most of the water bodies are surrounded by ground of higher elevation.  Though off-stream water polygons should be filled when delineating to a stream network (Saunders, 2000), water bodies within the City of Portland – particularly in the Columbia Slough Watershed – may constitute a significant barrier to overland flow, and should be preserved in the interest of accuracy (Figure 4-4).<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure44.jpg' /><div>Figure 4-4.  One example of a water body in the Columbia Slough that would be filled in step 4.2.2.2 were it not preserved in steps 4.2.2.1 and 4.2.2.3.<br>
<h4>Lower Water Body Elevations</h4>
All grid cells located within water bodies had 1,000ft subtracted from their elevation.  This step returned water body cells to their original elevation, reversing the effect of step 4.2.2.1.<br>
<h4>Burn in Street Surface</h4>
Because the D8 algorithm allows flow in only one direction from each grid cell, it performs best when used in areas that contain well-defined flow paths (Garbrecht and Martz, 2000).  A city’s absence of highly defined natural drainage paths, then, would seem to preclude the use of this algorithm.  However, gutters provide a unique urban equivalent to stream channels that can be used to much success.  In order to use gutters as the stream channel, the DEM must be conditioned to include lowered gutters and raised street crowns to represent the parabolic shape of typical city streets with curbs (Figure 4-5).<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure45.jpg' /><div>Figure 4-5.  Typical neighborhood collector street cross-section.  From City of Portland Standard Construction Specifications, 2002 Revision.<br>
Street surface objects were buffered 10-ft in order to prevent the creation of more sinks (Figure 4-6), then all DEM grid cells that were within the buffered street surface coverage were lowered by 0.5-ft.  The street centerline coverage was then used to raise the crown of the streets 0.5-ft, back to their original elevation.<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure46.jpg' /><div>Figure 4-6.  In this instance, lowering the street surface and raising the centerline creates a new sink where indicated, eliminating flow in the east gutter. Buffering the street surface 10-ft allows flow to get through this pinch point.<br>
<h4>Burn in Inlets</h4>
The final DEM pre-processing step is to burn the inlets into the elevation grid.  First, each inlet was buffered to a radius of 20-ft.  All overlapping inlet buffers where the two buffers belong to two different UIC systems were manually checked and resolved.  All grid cells that were located within the inlet buffers were then lowered 2-ft in order to focus regional flow accumulation into the areas around inlets.<br>
<h3>Delineation</h3>
The general process to delineate using the Hydrology toolset is shown in Figure 4-7, and is described in the following sections.<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure47.jpg' /><div>Figure 4-7.  Overview of typical delineation process.  From ArcGIS 9.1 Desktop Help.<br>
<h4>Flow Direction</h4>
Upon completion of the pre-processing of the Eastside DEM, a flow direction raster was created using the Spatial Analyst Tools?Hydrology?Flow Direction tool (Figure 4-8).  Essentially, each cell in the output raster is assigned a numeric value that indicates which direction that cell will flow completely to.  As stated earlier, the D8 method requires that each cell must flow completely to the neighboring cell that provides the path of steepest descent; the flow direction raster is the dataset that defines this flow pattern.<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure48.jpg' /><div>Figure 4-8.  Process to create flow direction grid.  Each grid cell in the elevation grid (a) is evaluated with the flow direction key (b) and is assigned a corresponding flow direction integer in the output (c).  The arrows in (d) represent the flow direction integers shown in (c).  Adopted from Brown et al., 2000.<br>
<h4>Flow Accumulation</h4>
This step is primarily used in watershed-scale delineations in order to help identify stream channels, but is not necessary to run for this process.  However, the result can be interesting to look at nonetheless, and is therefore included here as optional.<br>
The flow direction raster created in step 4.2.4.1 is used as the input to create the flow accumulation raster, which totals the number of upstream cells flowing to each cell (Figure 4-9).  This is done using the Spatial Analyst Tools?Hydrology?Flow Accumulation tool.  In a watershed-scale delineation, the flow accumulation raster would highlight surface collection areas, such as stream channels.  For the UIC delineation, the resultant flow accumulation raster highlights gutters and some intra-block surface drainage.<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure49.jpg' /><div>Figure 4-9.  Process to create flow accumulation grid.  Each grid cell in the flow direction grid (a) is<div>evaluated to determine the total number of upstream cells that are flowing to it.  That number<div>then gets written to the corresponding cell in the output (b) to represent the accumulated flow to that cell.<i><br>
<h4>Delineate UIC Drainage Areas</h4>
The final step in the delineation process is to run the Watershed tool in ArcGIS (Spatial Analyst Tools?Hydrology?Watershed).  The inputs to this tool are the flow direction raster created in step 4.2.4.1 and the rasterized, 20-ft buffered inlet dataset created in step 4.2.3.5.  The inlet dataset is the pour point – the dataset that the tool traces up from to determine drainage area.  The pour point dataset can consist of either points or a raster, but it was determined that using the inlet points resulted in delineations that were not capturing enough area.  This was likely the result of two things: (1) new sinks were inadvertently created when the inlet basins were burned into the DEM (step 4.2.3.5), and (2) points intersect only one raster cell, which determines where the delineation will start – if the mapped location of the inlet is different than where the gutter was created, the delineation will dwindle quickly upstream, because it is not capturing the major flow accumulation lines nearby.  The buffered inlets received all the drainage coming into the 20-ft radius area, thus eliminating the effects of the two shortcomings listed above and increasing the area captured in the delineation.<br>
<h3>DEM Post-Processing</h3>
After the delineation process was complete, the DEM went through several post-processing steps in order to be finalized.  First, the delineation dataset was converted to polygons.  The polygons were then grouped and dissolved together according to which combination of UICs they drained to.  It is important to note that more than one sump can be chained together in the same system.  In such a case, any area that flows directly to the downstream sump while bypassing the upstream sump should not be lumped together with the area that flows both to the upstream sump and then the downstream sump.  Should those two areas be combined, too much drainage area would be credited to the upstream sump.  Finally, the regions were checked for overlaps, which were then resolved.<br>
<h1>Final Products</h1>
<h2>Manual Delineation</h2>
The final product of the manual delineation effort is the polygon dataset located in the following formats and locations:<br></i><div>ESRI: \\Cassio\GIS3\mi_data_shp\FACILITY\SUMPS\Drainage_Basins\Sump_Drainages.shp<br>
<div>MapInfo: \\Cassio\GIS1\MI_DATA\FACILITY\SUMPS\Drainage_Basins\Sump_Drainages.tab<div>As indicated in Section 4.1, the manual delineations are not complete and are focused in areas of commercial or industrial zoning (Figure 4-1).  These datasets consist of 1,278 polygons with a total area of approximately 114,562,573 sq ft (2,630 acres).<br>
<h2>Automatic Delineation</h2>
The final product of the auto-delineation is the polygon dataset located in the following formats and locations:<br>
<div>ESRI: \\Cassio\gis3\mi_data_shp\facility\sumps\Drainage_Basins\UIC_SC_auto.shp<br>
<div>MapInfo: \\Cassio\gis1\mi_data\facility\sumps\Drainage_Basins\UIC_SC_auto.tab<div>These two datasets were identical at the time of posting to the network, and consist of 7,837 polygons with a total area of approximately 726,762,260 sq ft (16,684 acres).  Figure 5-1 shows the final delineation polygons.<br>
<div><img src='http://wiki.besasm-uic.googlecode.com/hg/UIC007-Figure51.jpg' /><div>Figure 5-1.  Automatically delineated UIC drainage polygons.<i><br>
<h1>Future Work</h1>
Automated delineations used standardized criteria and data sources, and every effort was made to ensure consistency in their creation.  However, the following aspects of their creation should be noted:<br>
Delineations were completed using now-archived BES collection system data, i.e. All_n (nodes) and All_s (pipes), and should be repeated with the current BES standard collection system data, i.e. the Data Maintenance Environment (DME) data that is available on the CGIS hub.  In order to do this, some of the processes will need to be adjusted.  For instance, the MapBasic program that spatially identifies inlets (see section 4.2.2 and Appendix A) is written with hard-coded field names that only apply to All_n or All_s.  In this case, references to field name NODE_ID would have to be updated to UNITID, references to ID_GLBL and BLOCK are obsolete and should be removed, etc.<br>
As new DEM data becomes available, i.e. LIDAR based, these delineations should be re-run to produce more detailed results.  With the greater resolution available with LIDAR data, it may become unnecessary to burn in the street surface and raise the crown of the streets.  This should be investigated prior to delineation.<br>
The UIC delineation polygons are desktop renderings only, and although they are currently considered suitable for the City permitting process, little to no field verification has been conducted.  Ground conditions that may have a dramatic effect on the delineation datasets include local changes in topography, on-site drainage conditions (i.e. private stormwater facilities) and local changes in storm sewer infrastructure.  As the City goes through the permit cycle, field verification will be a necessary step to assess corrective action status.  Assuming there is an adequate feedback pathway from the ground-truther(s) to the keeper(s) of the spatial datasets, the delineation layers will continue to mature.<br>
<h1>References</h1>
Bonham-Carter, Graeme F., 2002.  Geographic Information Systems for Geoscientists: Modelling with GIS.  Pergamon Publishing, Ottawa, Canada.</i><div>

Brown, J., Parcher, J. W., and Ulery, R. L., 2000.  Creating a Standardized Watersheds Database for the Lower Rio Grande/Río Bravo, Texas.  U.S. Geological Survey Open-File Report 00-065, 17 p.  <<a href='http://pubs.usgs.gov/of/2000/ofr00-065/00-065.pdf>'>http://pubs.usgs.gov/of/2000/ofr00-065/00-065.pdf&gt;</a><div>

Garbrecht, J. and Martz, L., 2000.  Digital Elevation Model Issues in Water Resources Modeling.  In Hydrologic and Hydraulic Modeling Support: With Geographic Information Systems, 2000, ESRI Press.<div>
O’Callaghan, J. F., and D. M. Mark.  1984.  The Extraction of Drainage Networks from Digital Elevation Data.  Computer Vision, Graphics and Image Processing 28:323-344.<div>

Saunders, William, 2000.  Preparation of DEMs for Use in Environmental Modeling Analysis.  In Hydrologic and Hydraulic Modeling Support: With Geographic Information Systems, 2000, ESRI Press.<div>

<h1>Appendix A</h1>
<b>Detailed Process Steps for UIC Delineation</b>
All datasets presented herein are archived to DVDs SAGIS022007_1, SAGIS022007_2, SAGIS022007_3, and SAGIS022007_4 unless preceded with a network path.<br>
<br>
Process list legend:<br>
<ol><li><i>Step</i>
<ul><li>Denotes output from the previous step, where applicable<br>
<code>[ ]</code> Bracketed output are raster format<div><code>[ ] = …</code> Specific formula used to derive raster output in the ArcGIS raster calculator (Spatial Analyst)<div><code>(x secs)</code> Number of seconds it took to run the process on machine BES4808<div></li></ul></li></ol>

<h2>Identify Inlets</h2>
<ol><li>Since most UICs have more than one connecting inlet, delineating to all inlets that drain to each sump is necessary to create the most accurate output.  Therefore all inlets that drain surface water to UICs must be identified.  Some chaining analyses can be done using Hansen data provided all facilities contain unique IDs within the database; an example is the analysis of which UIC systems contain a sedimentation manhole.  The inlet analysis cannot be done using Hansen attribute data, however, because inlet data in Hansen is incomplete.  Therefore this analysis must be done spatially.  Run the MapBasic program InletGrouper.mbx.<br>
<ul><li>\\Cassio\GIS2\PROJECTS\7750\TASKS\Task3D_Delineation\tab\SumpInlets.TAB<br>
</li></ul></li><li>The MBX in the previous step is not currently intelligent enough to remove duplicate inlets in situations where there are multiple UICs in sequence.  For example, in a situation where there is a chain of three UICs with one contributing inlet, the output from the MBX will contain three inlets at the identical location, each tagged with the ID of one of the three UICs.  In order to rectify this, a second MBX is run (Inlet_dataConsolidate.mbx).  This program determines where there are duplicate inlets, groups all corresponding UIC ID’s into a single record, and deletes the duplicates.<br>
<ul><li>\\Cassio\GIS2\PROJECTS\7750\TASKS\Task3D_Delineation\tab\SumpInlets_grpd_fnl.TAB</li></ul></li></ol>

<h2>Water Body Conditioning</h2>
<ol><li>Create raster of Portland water bodies, where cells that correspond to water body locations have value of 1.  Reclassify this raster so that all NODATA cells – those that do not represent water bodies – have a value of 2.  This is necessary in order to run the conditional raster calculator statement in the next step.<br>
<ul><li><a href='detail_wtrbdy.md'>detail_wtrbdy</a>
</li><li><a href='Reclass.md'>of detail_wtrbdy</a>
</li></ul></li><li>Create raster from base eastside DEM where all cells that correspond with water body cells in <a href='detail_wtrbdy.md'>detail_wtrbdy</a> are given an arbitrarily high number (original value + 1000).  The result of this is a DEM that is identical to the original DEM <a href='emosaic5ftgrd.md'>emosaic5ftgrd</a> except that water bodies are now peaks instead of sinks.  This is done to prevent water body areas from being treated as sinks in the following steps.  If there is a sink fully contained within a water body it will get filled in, while still maintaining the integrity of the water body depression.<br>
<ul><li><a href='emosaic_con.md'>emosaic_con</a> = con(<a href='Reclass.md'>of detail_wtrbdy</a>==1, <a href='emosaic5ftgrd.md'>emosaic5ftgrd</a>+1000, <a href='emosaic5ftgrd.md'>emosaic5ftgrd</a>)<br>
</li></ul></li><li>Create flow direction raster from conditional DEM <a href='emosaic_con.md'>emosaic_con</a>.<br>
<ul><li><a href='flowdir_emos2.md'>flowdir_emos2</a> (501  secs)<br>
</li></ul></li><li>Find sinks.<br>
<ul><li><a href='sink_flowdir2.md'>sink_flowdir2</a> (182  secs)<br>
</li></ul></li><li>Create ‘watersheds’ for sinks.<br>
<ul><li><a href='wshd_sinks2.md'>wshd_sinks2</a> (831 secs)<br>
</li></ul></li><li>In raster calculator, create raster of minimum elevation cells in watershed of each sink.<br>
<ul><li><a href='sink_min2.md'>sink_min2</a> = zonalmin (<a href='wshd_sinks2.md'>wshd_sinks2</a>, <a href='emosaic_con.md'>emosaic_con</a>, data)<br>
</li></ul></li><li>In raster calculator, create raster of minimum elevation cell along boundary of each sink’s watershed – this represents the elevation at which flow would leave the sink were it to be filled gradually with water.<br>
<ul><li><a href='sink_max2.md'>sink_max2</a> = zonalfill (<a href='wshd_sinks2.md'>wshd_sinks2</a>, <a href='emosaic_con.md'>emosaic_con</a>)<br>
</li></ul></li><li>Subtract minimum elevation from minimum boundary cell elevation.<br>
<ul><li><a href='sink_depth2.md'>sink_depth2</a> = <a href='sink_max2.md'>sink_max2</a> – <a href='sink_min2.md'>sink_min2</a>
</li></ul></li><li>Use sink_depth2 to determine appropriate depth (z-limit) to use as upper limit of fill sinks command.  This is based on visual inspection of known natural sinks and suspected data error sinks.<br>
<ul><li>Z-limit should be 25’ based on visual inspection<br>
</li></ul></li><li>Fill sinks using z-limit in previous step.  Attempts to fill sinks fail when inputting a z-limit, after approximately 2807 seconds.  Assuming this error is because ArcGIS cannot handle a z-limit on a high-resolution DEM, I will attempt it without a z-limit.  Fill command is successful using no z-limit, after 18,800 seconds.  This means that every sink was filled, regardless of whether or not it was natural.  This is probably acceptable, as the majority of sinks are very shallow, and are data errors created through the raster creation process.  Most significant sinks that actually exist on the ground are water bodies, which were preserved by artificially raising those cells in previous steps.<br>
<ul><li><a href='fill_emosaic2.md'>fill_emosaic2</a>
</li></ul></li><li>In raster calculator, calculate difference between original DEM and filled DEM.<br>
<ul><li><a href='diff_fillemo2.md'>diff_fillemo2</a> = <a href='fill_emosaic2.md'>fill_emosaic2</a> – <a href='emosaic_con.md'>emosaic_con</a>
</li></ul></li><li>Now the conditional DEM with filled sinks (<a href='fill_emosaic2.md'>fill_emosaic2</a>) must have 1,000 subtracted from all cells that are within water bodies, to reverse the effect of artificially raising the water body cell elevations.  However, because some cells that were islands surrounded by water body cells didn’t initially have their elevations raised using <a href='detail_wtrbdy.md'>detail_wtrbdy</a> – but became sinks once the surrounding water body cells were artificially raised – these ‘island’ cells wound up being 1,000 ft too high so that they could spill over into the surrounding artificially-raised water body cells.  In order to fix this, subtract <a href='emosaic_con.md'>emosaic_con</a> from <a href='fill_emosaic2.md'>fill_emosaic2</a> in order to highlight where the filled DEM is close to 1,000 ft different from the original DEM.  Those islands that were raised accidentally through the fill sinks process are thus highlighted when using <a href='detail_wtrbdy.md'>detail_wtrbdy</a> as a mask.  The original detailed water bodies’ shapefile can then be modified to include the highlighted areas.  Convert the modified shapefile into a new water body raster that includes incorrectly filled areas (<a href='detail_wtrbd2.md'>detail_wtrbd2</a>) to use for subtracting 1,000 ft from the filled DEM.  This raster must be reclassified so that all NODATA cells – those that do not represent water bodies – have a value of 2.  This is necessary in order to run the conditional raster calculator statement in the following step.<br>
<ul><li><a href='detail_wtrbd2.md'>detail_wtrbd2</a>
</li><li><a href='Reclass.md'>of detail_wtrbd2</a>
</li></ul></li><li>Finally, in order to get the water body elevations back to their natural levels, 1,000 must be conditionally subtracted from cells in <a href='fill_emosaic2.md'>fill_emosaic2</a> that overlap with cells in <a href='Reclass.md'>of detail_wtrbd2</a> where value = 1.<br>
<ul><li><a href='es5ft_filled2.md'>es5ft_filled2</a> = con(<a href='Reclass.md'>of detail_wtrbd2</a> == 1, <a href='fill_emosaic2.md'>fill_emosaic2</a> - 1000, <a href='fill_emosaic2.md'>fill_emosaic2</a>)</li></ul></li></ol>

<h2>Street Surface Conditioning</h2>
<ol><li>Scrub street impervious surface layer in MapInfo.<br>
<ul><li>ImpArea_StreetFinal_011006.TAB<br>
</li></ul></li><li>Buffer street surface by 10 ft using BufferIterate.MBX.  This is necessary for two reasons:<br>
<ul><li>Even after scrubbing the street surface data in the previous step, there are still errors, including areas where the mapped street surface is narrower than the actual street.  This would be a problem in instances where mapped inlets are located outside the street surface layer, when in reality they are located just inside the curb.<br>
</li><li>To help rectify shift between the street surface layer and the street centerline layer used in later steps.  For example, if the street centerline for a particular street is off-center from the street surface layer even slightly, when each are converted to raster and the appropriate conditional subtractions/additions have been made to the base DEM new sinks could appear, adversely affecting the delineation process.  The additional 10 ft of street width equals approximately 2 pixels in a 5-foot DEM, providing the additional space needed for flow to continue unhindered.<br>
</li><li>ImpArea_StreetFinal_011006_buff10.TAB<br>
</li></ul></li><li>Convert buffered street surface to Arc shapefile, then to raster.<br>
<ul><li>ImpArea_StreetFinal_COMBINE.shp<br>
</li><li><a href='Street_5ftgrd.md'>Street_5ftgrd</a>
</li></ul></li><li>Reclass NODATA street surface raster cells to 2.<br>
<ul><li><a href='Reclass.md'>of Street_5ftgrd</a>
</li></ul></li><li>Conditionally subtract 0.5 ft from <a href='es5ft_filled2.md'>es5ft_filled2</a> where <a href='Reclass.md'>of Street_5ftgrd</a> = 1.  This effectively lowers the street surface in the raster 6 inches, per the City of Portland Standard Construction Specifications for gutter dimension for a typical neighborhood collector street (see Figure 4-5 in UIC007).<br>
<ul><li><a href='es5ft_filled3.md'>es5ft_filled3</a> = con(<a href='Reclass.md'>of Street_5ftgrd</a> == 1, <a href='es5ft_filled2.md'>es5ft_filled2</a> - 0.5, <a href='es5ft_filled2.md'>es5ft_filled2</a>)</li></ul></li></ol>

<h2>Street Centerline Conditioning</h2>
<ol><li>Convert CGIS hub streets layer (CGISSDE.CGIS.CITY.sde\ egh_Public.ARCMAP_ADMIN.Transportation\EGH_Public.ARCMAP_ADMIN.streets_pdx) to shapefile and clip to DEM area.<br>
<ul><li>All_streets_NAD83_clip.shp<br>
</li></ul></li><li>Convert All_streets_NAD83_clip.shp to raster, and reclass NODATA values to 2.<br>
<ul><li><a href='centerli_5ft.md'>centerli_5ft</a>
</li><li><a href='Reclass.md'>of centerli_5ft</a>
</li></ul></li><li>Conditionally add 0.5 ft to <a href='es5ft_filled3.md'>es5ft_filled3</a> where <a href='Reclass.md'>of centerli_5ft</a> = 1<br>
<ul><li><a href='es5ft_filled4.md'>es5ft_filled4</a> = con(<a href='Reclass.md'>of centerli_5ft</a> == 1, <a href='es5ft_filled3.md'>es5ft_filled3</a> + 0.5, <a href='es5ft_filled3.md'>es5ft_filled3</a>)</li></ul></li></ol>

<h2>Burn in Inlets</h2>
<ol><li>In order to facilitate the connection between inlet locations and the flow direction raster – i.e. to create artificial basins around each inlet – create a table representing each inlet buffered to 20ft (InletBuffer.mbx).  Convert to ESRI shapefile, then to raster.<br>
<ul><li>SumpInlets_poly.shp<br>
</li><li><a href='Inletspoly5ft.md'>Inletspoly5ft</a>
</li></ul></li><li>Reclass <a href='Inletspoly5ft.md'>Inletspoly5ft</a> so that NODATA cells equal 2.<br>
<ul><li><a href='Reclass.md'>of Inletspoly5ft</a>
</li></ul></li><li>Conditionally subtract 2 ft from <a href='es5ft_filled4.md'>es5ft_filled4</a> where <a href='Reclass.md'>of Inletspoly5ft</a> = 1.<br>
<ul><li><a href='es5ft_filled5.md'>es5ft_filled5</a> =  con(<a href='Reclass.md'>of Inletspoly5ft</a> == 1, <a href='es5ft_filled4.md'>es5ft_filled4</a> – 2, <a href='es5ft_filled4.md'>es5ft_filled4</a>)</li></ul></li></ol>

<h2>Create Delineations</h2>
<ol><li>Create flow direction raster using Spatial Analyst Hydrology toolset.<br>
<ul><li><a href='flowdir_es5f1.md'>flowdir_es5f1</a> (661 secs)<br>
</li></ul></li><li>Create flow accumulation raster using Spatial Analyst Hydrology toolset.<br>
<ul><li><a href='FlowAcc_flow1.md'>FlowAcc_flow1</a> (1137 secs)<br>
</li></ul></li><li>Run Watershed tool using <a href='Inletspoly5ft.md'>Inletspoly5ft</a> as the pour point raster and <a href='flowdir_es5f1.md'>flowdir_es5f1</a> as the flow direction table.  Use Value as the pour point field, which contains the value from the ID field in SumpInlets_grpd_fnl so that data can be joined back to the delineations.<br>
<ul><li><a href='Watersh_5ft.md'>Watersh_5ft</a> (360 secs)</li></ul></li></ol>

<h2>Post-Processing the Delineation Data</h2>
<ol><li>Convert <a href='Watersh_5ft.md'>Watersh_5ft</a> to polygon feature class (not generalized).  Use Value as field.<br>
<ul><li>Watersh_5ft.shp (lines not generalized)<br>
</li></ul></li><li>Dissolve Watersh_5ft.shp by field GRIDCODE – the value in this field corresponds to the unique ID given to SumpInlets_grpd_fnl.<br>
<ul><li>Watersh_5ft_dissol.shp (30 secs)<br>
</li></ul></li><li>Convert watershed shapefile to MapInfo tables.<br>
<ul><li>Watersh_5ft_dissol.tab (16,647.84 acres, compared with 11,138.87 for first auto delineation layer [11,638.92 acres with voronoi holes fix, UIC_SC_auto.tab])<br>
</li></ul></li><li>Join attributes from SumpInlets_grpd_fnl to Watersh_5ft_dissol.tab where SumpInlets_grpd_fnl.ID = Watersh_5ft_dissol.GRIDCODE<br>
<ul><li>Watersh_attr.tab<br>
</li></ul></li><li>To group delineation polygons based on matching UICs IDs, first the UIC IDs need to be ordered so that when the IDs are concatenated, the delineation polygons can be accurately grouped by the concatenation field.  To order the UIC IDs in each delineation record, first query out those records that only contain one UIC ID (SUMPID2 = “ ”); since they only contain one UIC ID, they are already sorted.  Run the MapBasic program Sorter.mbx on those delineation polygons that contain more than one UIC ID (SUMPID2 <> “ “).  Append the unsorted one-UIC dataset to the sorted multi-UIC dataset.<br>
<ul><li>Watersh_attr_grpd.tab<br>
</li></ul></li><li>Add temporary field (t_concat) and update to concatenation of all “tx” fields, where x is an integer.  Combine objects in table Watersh_attr_grpd using the Table>Combine Objects Using Column command.  Group on field t_concat.  Check region objects for overlaps and resolve them.<br>
<ul><li>Watersh_attr_grpd.tab<br>
</li></ul></li><li>Save Watersh_attr_grpd as final delineation table.<br>
<ul><li>\\Cassio\GIS2\PROJECTS\7750\TASKS\Task3D_Delineation\tab\UIC_SC_auto_v2_Mar2006.tab<br>
</li></ul></li><li>Convert MapInfo file to ESRI format.<br>
<ul><li>\\Cassio\GIS2\PROJECTS\7750\TASKS\Task3D_Delineation\shp\UIC_SC_auto_v2_Mar2006.shp<br>
</li></ul></li><li>Replace MI_DATA versions<br>
<ul><li>\\Cassio\GIS1\MI_DATA\FACILITY\SUMPS\Drainage_Basins\UIC_SC_auto.TAB<br>
</li><li>\\Cassio\GIS3\mi_data_shp\FACILITY\SUMPS\Drainage_Basins\ UIC_SC_auto.shp