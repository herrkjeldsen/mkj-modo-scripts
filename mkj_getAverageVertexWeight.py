#python
import lx

vmaps_count = lx.eval('query layerservice vmap.N ?')

value_count = 0
avg_value = 0.0

# TODO :: check that only one vertexmap is selected?

lx.eval('select.convert vertex')

for map in range(vmaps_count):

	vertices = lx.evalN('query layerservice verts ? all')
	total_vert_count = len(vertices)
	
	vmap_name = lx.eval('query layerservice vmap.name ? %i' % map)
	vmap_selected = lx.eval('query layerservice vmap.selected ? %i' % map)
	vmap_type = lx.eval('query layerservice vmap.type ? %i' % map)
	lx.out(vmap_name)
	
	if vmap_type == "weight" or vmap_type == "subvweight": # TODO :: improve this check to include other relevant maps
		if vmap_selected == 1:
			for vert in range(total_vert_count):
				vert_selected = lx.eval('query layerservice vert.selected ? {%s}' % vert)
				if vert_selected:
					vertVal = lx.eval('query layerservice vert.vmapValue ? {%s}' % vert)
					lx.out(vertVal)
					value_count += 1
					avg_value += vertVal

if value_count > 0:
	avg_value = avg_value / value_count
	lx.out("Average value of selected verts is:")
	lx.out(avg_value)

# copy average value to weight tool	
lx.eval('tool.set vertMap.setWeight on')
lx.eval('tool.attr vertMap.setWeight weight {%s}' % avg_value)
lx.eval('tool.set vertMap.setWeight off')

lx.eval('select.type edge')

# TODO :: make proper python version