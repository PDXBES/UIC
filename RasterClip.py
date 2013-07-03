# -----------------------------------------------------------------------------------------------
#    file name: RasterClip.py
#   Written by: Neil Revello
#   Org Source: none
#   Created on: Tue May 05 2009 05:58:10 PM
#  Modified on: none
#     argument: Input Raster, Output Raster, Clip Buffer
#       output: Clipped Raster
#      purpose: Raster Clipping script for fixing ESRI Bug for not reading a changed envelope in clipBuffer extents
#    revisions: none
#        notes: To be retired when ESRI Fixes issue
#        logic: read envelope extents for clip buffer then pass it to Clip process
#       errors: none
# -----------------------------------------------------------------------------------------------

import arcgisscripting

gp = arcgisscripting.create()
gp.overwriteoutput = 1

inRaster = gp.GetParameterAsText(0)
outRaster = gp.GetParameterAsText(1)
clipBuffer = gp.GetParameterAsText(2)
envelope = gp.Describe(clipBuffer).Extent

gp.Clip_management(inRaster, envelope, outRaster, clipBuffer)
