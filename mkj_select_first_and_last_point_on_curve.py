#python
#-------------------------------------------------------------------------------
# Name:mkj_select_first_and_last_vertex_on_curve
# Version: 1.0
# Description: This script is designed to select the first and last vert in selected curves
#              Altered from William Vaughan's original script "pp_firstverts_from_curves.py"
#
# Author:      William Vaughan, pushingpoints.com
# Author:      Marcus Kjeldsen
#
# Created:     2015/03/12
#-------------------------------------------------------------------------------


import lx

#Get layer info
layer = lx.eval('query layerservice layer.index ? main')
polys = lx.evalN('query layerservice polys ? selected')# index of polys
polysN = lx.eval('query layerservice poly.N ? selected') #poly count
lx.out('polys', polys)
lx.out('polysN', polysN)

lx.eval('select.drop polygon')

for p in polys:
	#select an individual curve by its index that was stored earlier
	lx.eval('select.element %s polygon set %s' % (layer,p))
	
	#get list of vertexes in curve by order
	polyVerts = lx.eval('query layerservice poly.vertList ? %s' % p)
	
	#select first and last vertex in curve
	lx.eval('select.element %s vertex add %s' % (layer, polyVerts[0]))
	lx.eval('select.element %s vertex add %s' % (layer, polyVerts[-1]))

lx.eval('select.type vertex')