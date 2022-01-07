# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

for i in range(4):
    # create a new 'XML Image Data Reader'
    current_bijel = XMLImageDataReader(registrationName=f'phi_bijel_1194121309-000{i}0000.vti', FileName=[f'C:\\Users\\Admin\\Pictures\\ParaviewPics\\PythonScript\\phi_bijel_1194121309-000{i}0000.vti'])
    current_bijel.PointArrayStatus = ['order parameter']

    # Properties modified on current_bijel
    current_bijel.TimeArray = 'None'

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    current_bijelDisplay = Show(current_bijel, renderView1, 'UniformGridRepresentation')

    # trace defaults for the display properties.
    current_bijelDisplay.Representation = 'Outline'
    current_bijelDisplay.ColorArrayName = [None, '']
    current_bijelDisplay.SelectTCoordArray = 'None'
    current_bijelDisplay.SelectNormalArray = 'None'
    current_bijelDisplay.SelectTangentArray = 'None'
    current_bijelDisplay.OSPRayScaleArray = 'order parameter'
    current_bijelDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    current_bijelDisplay.SelectOrientationVectors = 'None'
    current_bijelDisplay.ScaleFactor = 25.5
    current_bijelDisplay.SelectScaleArray = 'None'
    current_bijelDisplay.GlyphType = 'Arrow'
    current_bijelDisplay.GlyphTableIndexArray = 'None'
    current_bijelDisplay.GaussianRadius = 1.2750000000000001
    current_bijelDisplay.SetScaleArray = ['POINTS', 'order parameter']
    current_bijelDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    current_bijelDisplay.OpacityArray = ['POINTS', 'order parameter']
    current_bijelDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    current_bijelDisplay.DataAxesGrid = 'GridAxesRepresentation'
    current_bijelDisplay.PolarAxes = 'PolarAxesRepresentation'
    current_bijelDisplay.ScalarOpacityUnitDistance = 1.7320508075688774
    current_bijelDisplay.OpacityArrayName = ['POINTS', 'order parameter']
    current_bijelDisplay.SliceFunction = 'Plane'
    current_bijelDisplay.Slice = 127

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    current_bijelDisplay.ScaleTransferFunction.Points = [-0.24494406067985666, 0.0, 0.5, 0.0, 0.24488316932476215, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    current_bijelDisplay.OpacityTransferFunction.Points = [-0.24494406067985666, 0.0, 0.5, 0.0, 0.24488316932476215, 1.0, 0.5, 0.0]

    # init the 'Plane' selected for 'SliceFunction'
    current_bijelDisplay.SliceFunction.Origin = [127.5, 127.5, 127.5]

    # reset view to fit data
    renderView1.ResetCamera()

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # update the view to ensure updated data information
    renderView1.Update()

    # set scalar coloring
    ColorBy(current_bijelDisplay, ('POINTS', 'order parameter'))

    # rescale color and/or opacity maps used to include current data range
    current_bijelDisplay.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    current_bijelDisplay.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'orderparameter'
    orderparameterLUT = GetColorTransferFunction('orderparameter')

    # get opacity transfer function/opacity map for 'orderparameter'
    orderparameterPWF = GetOpacityTransferFunction('orderparameter')

    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=current_bijel)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = ['POINTS', 'order parameter']
    clip1.Value = -3.0445677547258354e-05

    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [127.5, 127.5, 127.5]

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [127.5, 127.5, 127.5]

    # Properties modified on clip1.ClipType
    clip1.ClipType.Origin = [150.0, 127.5, 150.0]
    clip1.ClipType.Normal = [0.707, 0.0, 0.707]

    # show data in view
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = ['POINTS', 'order parameter']
    clip1Display.LookupTable = orderparameterLUT
    clip1Display.SelectTCoordArray = 'None'
    clip1Display.SelectNormalArray = 'None'
    clip1Display.SelectTangentArray = 'None'
    clip1Display.OSPRayScaleArray = 'order parameter'
    clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip1Display.SelectOrientationVectors = 'None'
    clip1Display.ScaleFactor = 25.5
    clip1Display.SelectScaleArray = 'None'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.GlyphTableIndexArray = 'None'
    clip1Display.GaussianRadius = 1.2750000000000001
    clip1Display.SetScaleArray = ['POINTS', 'order parameter']
    clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip1Display.OpacityArray = ['POINTS', 'order parameter']
    clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip1Display.DataAxesGrid = 'GridAxesRepresentation'
    clip1Display.PolarAxes = 'PolarAxesRepresentation'
    clip1Display.ScalarOpacityFunction = orderparameterPWF
    clip1Display.ScalarOpacityUnitDistance = 1.9836035415412256
    clip1Display.OpacityArrayName = ['POINTS', 'order parameter']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [-0.24494406067985666, 0.0, 0.5, 0.0, 0.2448485794048679, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [-0.24494406067985666, 0.0, 0.5, 0.0, 0.2448485794048679, 1.0, 0.5, 0.0]

    # show color bar/color legend
    clip1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=clip1)
    threshold1.Scalars = ['POINTS', 'order parameter']
    threshold1.ThresholdRange = [-0.24494406067985666, 0.2448485794048679]

    # Properties modified on threshold1
    threshold1.ThresholdRange = [-0.05, 0.2448485794048679]

    # show data in view
    threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    threshold1Display.Representation = 'Surface'
    threshold1Display.ColorArrayName = ['POINTS', 'order parameter']
    threshold1Display.LookupTable = orderparameterLUT
    threshold1Display.SelectTCoordArray = 'None'
    threshold1Display.SelectNormalArray = 'None'
    threshold1Display.SelectTangentArray = 'None'
    threshold1Display.OSPRayScaleArray = 'order parameter'
    threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold1Display.SelectOrientationVectors = 'None'
    threshold1Display.ScaleFactor = 25.5
    threshold1Display.SelectScaleArray = 'None'
    threshold1Display.GlyphType = 'Arrow'
    threshold1Display.GlyphTableIndexArray = 'None'
    threshold1Display.GaussianRadius = 1.2750000000000001
    threshold1Display.SetScaleArray = ['POINTS', 'order parameter']
    threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold1Display.OpacityArray = ['POINTS', 'order parameter']
    threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold1Display.PolarAxes = 'PolarAxesRepresentation'
    threshold1Display.ScalarOpacityFunction = orderparameterPWF
    threshold1Display.ScalarOpacityUnitDistance = 3.4184400137335773
    threshold1Display.OpacityArrayName = ['POINTS', 'order parameter']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold1Display.ScaleTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold1Display.OpacityTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(clip1, renderView1)

    # show color bar/color legend
    threshold1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Extract Surface'
    extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=threshold1)

    # show data in view
    extractSurface1Display = Show(extractSurface1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    extractSurface1Display.Representation = 'Surface'
    extractSurface1Display.ColorArrayName = ['POINTS', 'order parameter']
    extractSurface1Display.LookupTable = orderparameterLUT
    extractSurface1Display.SelectTCoordArray = 'None'
    extractSurface1Display.SelectNormalArray = 'None'
    extractSurface1Display.SelectTangentArray = 'None'
    extractSurface1Display.OSPRayScaleArray = 'order parameter'
    extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractSurface1Display.SelectOrientationVectors = 'None'
    extractSurface1Display.ScaleFactor = 25.5
    extractSurface1Display.SelectScaleArray = 'None'
    extractSurface1Display.GlyphType = 'Arrow'
    extractSurface1Display.GlyphTableIndexArray = 'None'
    extractSurface1Display.GaussianRadius = 1.2750000000000001
    extractSurface1Display.SetScaleArray = ['POINTS', 'order parameter']
    extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractSurface1Display.OpacityArray = ['POINTS', 'order parameter']
    extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
    extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
    extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    extractSurface1Display.ScaleTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    extractSurface1Display.OpacityTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(threshold1, renderView1)

    # show color bar/color legend
    extractSurface1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Smooth'
    smooth1 = Smooth(registrationName='Smooth1', Input=extractSurface1)

    # Properties modified on smooth1
    smooth1.NumberofIterations = 500

    # show data in view
    smooth1Display = Show(smooth1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    smooth1Display.Representation = 'Surface'
    smooth1Display.ColorArrayName = ['POINTS', 'order parameter']
    smooth1Display.LookupTable = orderparameterLUT
    smooth1Display.SelectTCoordArray = 'None'
    smooth1Display.SelectNormalArray = 'None'
    smooth1Display.SelectTangentArray = 'None'
    smooth1Display.OSPRayScaleArray = 'order parameter'
    smooth1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    smooth1Display.SelectOrientationVectors = 'None'
    smooth1Display.ScaleFactor = 25.5
    smooth1Display.SelectScaleArray = 'None'
    smooth1Display.GlyphType = 'Arrow'
    smooth1Display.GlyphTableIndexArray = 'None'
    smooth1Display.GaussianRadius = 1.2750000000000001
    smooth1Display.SetScaleArray = ['POINTS', 'order parameter']
    smooth1Display.ScaleTransferFunction = 'PiecewiseFunction'
    smooth1Display.OpacityArray = ['POINTS', 'order parameter']
    smooth1Display.OpacityTransferFunction = 'PiecewiseFunction'
    smooth1Display.DataAxesGrid = 'GridAxesRepresentation'
    smooth1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    smooth1Display.ScaleTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    smooth1Display.OpacityTransferFunction.Points = [-0.04999989734777101, 0.0, 0.5, 0.0, 0.24484857940486793, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(extractSurface1, renderView1)

    # show color bar/color legend
    smooth1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # set active source
    SetActiveSource(current_bijel)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=current_bijelDisplay.SliceFunction)

    # toggle 3D widget visibility (only when running from the GUI)
    Show3DWidgets(proxy=current_bijelDisplay)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=current_bijelDisplay.SliceFunction)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=current_bijelDisplay)

    # create a new 'Clip'
    clip2 = Clip(registrationName='Clip2', Input=current_bijel)
    clip2.ClipType = 'Plane'
    clip2.HyperTreeGridClipper = 'Plane'
    clip2.Scalars = ['POINTS', 'order parameter']
    clip2.Value = -3.0445677547258354e-05

    # init the 'Plane' selected for 'ClipType'
    clip2.ClipType.Origin = [127.5, 127.5, 127.5]

    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip2.HyperTreeGridClipper.Origin = [127.5, 127.5, 127.5]

    # Properties modified on clip2.ClipType
    clip2.ClipType.Origin = [105.0, 127.5, 105.0]
    clip2.ClipType.Normal = [-0.707, 0.0, -0.707]

    # show data in view
    clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'
    clip2Display.ColorArrayName = ['POINTS', 'order parameter']
    clip2Display.LookupTable = orderparameterLUT
    clip2Display.SelectTCoordArray = 'None'
    clip2Display.SelectNormalArray = 'None'
    clip2Display.SelectTangentArray = 'None'
    clip2Display.OSPRayScaleArray = 'order parameter'
    clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip2Display.SelectOrientationVectors = 'None'
    clip2Display.ScaleFactor = 25.5
    clip2Display.SelectScaleArray = 'None'
    clip2Display.GlyphType = 'Arrow'
    clip2Display.GlyphTableIndexArray = 'None'
    clip2Display.GaussianRadius = 1.2750000000000001
    clip2Display.SetScaleArray = ['POINTS', 'order parameter']
    clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip2Display.OpacityArray = ['POINTS', 'order parameter']
    clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip2Display.DataAxesGrid = 'GridAxesRepresentation'
    clip2Display.PolarAxes = 'PolarAxesRepresentation'
    clip2Display.ScalarOpacityFunction = orderparameterPWF
    clip2Display.ScalarOpacityUnitDistance = 1.9836035415412256
    clip2Display.OpacityArrayName = ['POINTS', 'order parameter']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    clip2Display.ScaleTransferFunction.Points = [-0.24487605495175233, 0.0, 0.5, 0.0, 0.24488316932476215, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    clip2Display.OpacityTransferFunction.Points = [-0.24487605495175233, 0.0, 0.5, 0.0, 0.24488316932476215, 1.0, 0.5, 0.0]

    # show color bar/color legend
    clip2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Threshold'
    threshold2 = Threshold(registrationName='Threshold2', Input=clip2)
    threshold2.Scalars = ['POINTS', 'order parameter']
    threshold2.ThresholdRange = [-0.24487605495175233, 0.24488316932476215]

    # Properties modified on threshold2
    threshold2.ThresholdRange = [-0.24487605495175233, 0.05]

    # show data in view
    threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

    # trace defaults for the display properties.
    threshold2Display.Representation = 'Surface'
    threshold2Display.ColorArrayName = ['POINTS', 'order parameter']
    threshold2Display.LookupTable = orderparameterLUT
    threshold2Display.SelectTCoordArray = 'None'
    threshold2Display.SelectNormalArray = 'None'
    threshold2Display.SelectTangentArray = 'None'
    threshold2Display.OSPRayScaleArray = 'order parameter'
    threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    threshold2Display.SelectOrientationVectors = 'None'
    threshold2Display.ScaleFactor = 25.5
    threshold2Display.SelectScaleArray = 'None'
    threshold2Display.GlyphType = 'Arrow'
    threshold2Display.GlyphTableIndexArray = 'None'
    threshold2Display.GaussianRadius = 1.2750000000000001
    threshold2Display.SetScaleArray = ['POINTS', 'order parameter']
    threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
    threshold2Display.OpacityArray = ['POINTS', 'order parameter']
    threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
    threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
    threshold2Display.PolarAxes = 'PolarAxesRepresentation'
    threshold2Display.ScalarOpacityFunction = orderparameterPWF
    threshold2Display.ScalarOpacityUnitDistance = 3.413945906988877
    threshold2Display.OpacityArrayName = ['POINTS', 'order parameter']

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    threshold2Display.ScaleTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    threshold2Display.OpacityTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(clip2, renderView1)

    # show color bar/color legend
    threshold2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Extract Surface'
    extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=threshold2)

    # show data in view
    extractSurface2Display = Show(extractSurface2, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    extractSurface2Display.Representation = 'Surface'
    extractSurface2Display.ColorArrayName = ['POINTS', 'order parameter']
    extractSurface2Display.LookupTable = orderparameterLUT
    extractSurface2Display.SelectTCoordArray = 'None'
    extractSurface2Display.SelectNormalArray = 'None'
    extractSurface2Display.SelectTangentArray = 'None'
    extractSurface2Display.OSPRayScaleArray = 'order parameter'
    extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    extractSurface2Display.SelectOrientationVectors = 'None'
    extractSurface2Display.ScaleFactor = 25.5
    extractSurface2Display.SelectScaleArray = 'None'
    extractSurface2Display.GlyphType = 'Arrow'
    extractSurface2Display.GlyphTableIndexArray = 'None'
    extractSurface2Display.GaussianRadius = 1.2750000000000001
    extractSurface2Display.SetScaleArray = ['POINTS', 'order parameter']
    extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
    extractSurface2Display.OpacityArray = ['POINTS', 'order parameter']
    extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
    extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
    extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    extractSurface2Display.ScaleTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    extractSurface2Display.OpacityTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(threshold2, renderView1)

    # show color bar/color legend
    extractSurface2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # create a new 'Smooth'
    smooth2 = Smooth(registrationName='Smooth2', Input=extractSurface2)

    # Properties modified on smooth2
    smooth2.NumberofIterations = 500

    # show data in view
    smooth2Display = Show(smooth2, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    smooth2Display.Representation = 'Surface'
    smooth2Display.ColorArrayName = ['POINTS', 'order parameter']
    smooth2Display.LookupTable = orderparameterLUT
    smooth2Display.SelectTCoordArray = 'None'
    smooth2Display.SelectNormalArray = 'None'
    smooth2Display.SelectTangentArray = 'None'
    smooth2Display.OSPRayScaleArray = 'order parameter'
    smooth2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    smooth2Display.SelectOrientationVectors = 'None'
    smooth2Display.ScaleFactor = 25.5
    smooth2Display.SelectScaleArray = 'None'
    smooth2Display.GlyphType = 'Arrow'
    smooth2Display.GlyphTableIndexArray = 'None'
    smooth2Display.GaussianRadius = 1.2750000000000001
    smooth2Display.SetScaleArray = ['POINTS', 'order parameter']
    smooth2Display.ScaleTransferFunction = 'PiecewiseFunction'
    smooth2Display.OpacityArray = ['POINTS', 'order parameter']
    smooth2Display.OpacityTransferFunction = 'PiecewiseFunction'
    smooth2Display.DataAxesGrid = 'GridAxesRepresentation'
    smooth2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    smooth2Display.ScaleTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    smooth2Display.OpacityTransferFunction.Points = [-0.24475670814584044, 0.0, 0.5, 0.0, 0.04999990336483595, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(extractSurface2, renderView1)

    # show color bar/color legend
    smooth2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # reset view to fit data
    renderView1.ResetCamera()

    # get layout
    layout1 = GetLayout()

    # layout/tab size in pixels
    layout1.SetSize(1052, 553)

    # current camera placement for renderView1
    renderView1.CameraPosition = [127.5, -725.7466298125642, 127.5]
    renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 220.83647796503186

    # save screenshot
    SaveScreenshot(f'C:/Users/Admin/Pictures/ParaviewPics/PythonScript/Bijel{i}.png', renderView1, ImageResolution=[1052, 553])
    SaveState(f'C:/Users/Admin/Pictures/ParaviewPics/PythonScript/Bijel{i}.pvsm')
    #================================================================
    # addendum: following script captures some of the application
    # state to faithfully reproduce the visualization during playback
    #================================================================

    #--------------------------------
    # saving layout sizes for layouts

    # layout/tab size in pixels
    layout1.SetSize(1052, 553)

    #-----------------------------------
    # saving camera placements for views

    # current camera placement for renderView1
    renderView1.CameraPosition = [127.5, -725.7466298125642, 127.5]
    renderView1.CameraFocalPoint = [127.5, 127.5, 127.5]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraParallelScale = 220.83647796503186

    #--------------------------------------------
    # uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
