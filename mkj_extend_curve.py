#python
#-------------------------------------------------------------------------------
# Name:mkj_extend_curve
# Version: 1.0
# Description: This script is designed to extend a curves start and end points, and keep those vertices selected
#
# Author:      Marcus Kjeldsen
#
# Created:     2015/03/12
#-------------------------------------------------------------------------------
import lx


#Get layer info
layer = lx.eval('query layerservice layer.index ? main')
polys = lx.evalN('query layerservice polys ? selected')# index of polys

lx.eval('select.drop polygon')

def extendCurve(curveVerts):
	# add one point to end of curve in same position as the last one
	lx.eval('tool.set prim.curve on')
	lx.eval('tool.setAttr prim.curve current %s' % str(len(curveVerts)-1)) # get last point index in curve
	lx.eval('tool.setAttr prim.curve mode add') 
	lx.eval('tool.setAttr prim.curve number %s' % str(len(curveVerts)+1)) # add 2 for number, not index
	'''
	lx.eval('tool.setAttr prim.curve ptX 2.0')
	lx.eval('tool.setAttr prim.curve ptY 1.0')
	lx.eval('tool.setAttr prim.curve ptZ 1.0')
	'''
	lx.eval('tool.doApply')
	lx.eval('tool.set prim.curve off 0')
	lx.eval('poly.flip')


for p in polys:
	#select an individual curve by its index that was stored earlier
	lx.eval('select.element %s polygon set %s' % (layer,p))
	
	#get list of vertexes and extend curve in start and end
	verts = lx.eval('query layerservice poly.vertList ? %s' % p)
	extendCurve(verts)
	verts = lx.eval('query layerservice poly.vertList ? %s' % p)
	extendCurve(verts)
	
	
	verts = lx.eval('query layerservice poly.vertList ? %s' % p)
	#select first and last vertex in curve
	lx.eval('select.element %s vertex add %s' % (layer, verts[0]))
	lx.eval('select.element %s vertex add %s' % (layer, verts[-1]))
	

lx.eval('select.type vertex')

