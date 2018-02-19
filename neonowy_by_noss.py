#!/usr/bin/env python

# GIMP Python plug-in Neonowy by noss tutorial.

from gimpfu import *

def neonowy_noss(image, drawable, color1, color2, color3, color4, gauss1, gauss2, gauss3) :
	#Get active layer
	start_layer = image.active_layer

	#############################################
	#Step 1: Add Background1#####################
	#############################################

	background_layer_1 = gimp.Layer(image, "Background1", image.width, image.height, RGB_IMAGE, 100, NORMAL_MODE)
	image.add_layer(background_layer_1, 0)

	#Change active layer
	pdb.gimp_image_set_active_layer(image, background_layer_1)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)
	#Change foreground color
	gimp.set_foreground("#000000")
	#Use bucket
	pdb.gimp_bucket_fill(dra, 0, 0, 100, 15, False, 0, 0)

	#############################################
	#Step 2: Copy layer##########################
	#############################################

	work_layer_1 = start_layer.copy()
	work_layer_1.name = "Element1"
	image.add_layer(work_layer_1, 0)

	#Change active layer
	pdb.gimp_image_set_active_layer(image, work_layer_1)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)

	#Alpha to selection
	pdb.gimp_selection_layer_alpha(image.active_layer)

	#Set color
	gimp.set_foreground(color1)
	gimp.set_background(color1)

	#Change shape color
	pdb.gimp_blend(dra, 0, 0, 0, 100, 0, 0, False, False, 9, 4, False, 0, 0, 0, dra.height)

	#Set selection none
	pdb.gimp_selection_none(image)

	#############################################
	#Step 3: Add Background2#####################
	#############################################

	background_layer_2 = gimp.Layer(image, "Background2", image.width, image.height, RGB_IMAGE, 100, DODGE_MODE)
	image.add_layer(background_layer_2, 0)

	#Change active layer
	pdb.gimp_image_set_active_layer(image, background_layer_2)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)
	#Change foreground color
	gimp.set_foreground(color3)
	#Use bucket
	pdb.gimp_bucket_fill(dra, 0, 0, 100, 15, False, 0, 0)

	#############################################
	#Step 4: Add Second Element##################
	#############################################

	work_layer_2 = start_layer.copy()
	work_layer_2.name = "Element2"
	image.add_layer(work_layer_2, 0)

	#Change active layer
	pdb.gimp_image_set_active_layer(image, work_layer_2)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)

	#Alpha to selection
	pdb.gimp_selection_layer_alpha(image.active_layer)

	#Set color
	gimp.set_foreground(color2)
	gimp.set_background(color2)

	#Change shape color
	pdb.gimp_blend(dra, 0, 0, 0, 100, 0, 0, False, False, 9, 4, False, 0, 0, 0, dra.height)

	#Set selection none
	pdb.gimp_selection_none(image)

	#############################################
	#Step 5: Add Background3#####################
	#############################################

	background_layer_3 = gimp.Layer(image, "Background3", image.width, image.height, RGB_IMAGE, 100, DODGE_MODE)
	image.add_layer(background_layer_3, 0)

	#Change active layer
	pdb.gimp_image_set_active_layer(image, background_layer_3)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)
	#Change foreground color
	gimp.set_foreground(color4)
	#Use bucket
	pdb.gimp_bucket_fill(dra, 0, 0, 100, 15, False, 0, 0)

	#############################################
	#Step 6: Add Third Element###################
	#############################################

	work_layer_3 = work_layer_2.copy()
	work_layer_3.name = "Element3"
	image.add_layer(work_layer_3, 0)

	#############################################
	#Step 7: Add Fourth Element##################
	#############################################

	work_layer_4 = work_layer_1.copy()
	work_layer_4.name = "Element4"
	image.add_layer(work_layer_4, 0)

	#############################################
	#Step 8: Gauss Blur1#########################
	#############################################

	#Change active layer
	pdb.gimp_image_set_active_layer(image, work_layer_3)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)

	pdb.plug_in_gauss_rle2(image, dra, gauss1, gauss1)

	#############################################
	#Step 9: Gauss Blur2#########################
	#############################################

	#Change active layer
	pdb.gimp_image_set_active_layer(image, work_layer_2)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)

	pdb.plug_in_gauss_rle2(image, dra, gauss2, gauss2)

	#############################################
	#Step 10: Gauss Blur3########################
	#############################################

	#Change active layer
	pdb.gimp_image_set_active_layer(image, work_layer_1)
	#Set value dra -> active layer
	dra = pdb.gimp_image_active_drawable(image)

	pdb.plug_in_gauss_rle2(image, dra, gauss3, gauss3)

	#############################################
	#Step 11: Hide Start Element#################
	#############################################

	#Hide start layer
	start_layer.visible = False

register(
	"python_fu_neonowy_noss",
	"Neonowy by noss tutorial",
	"Change image to Neonowy by noss tutorial",
	"Noss (Tutorial) | EgzoT (Mod)",
    "---",
    "2006 (Tutorial) | 2018 (Mod)",
    "Neonowy (noss)...",
    "*",
    [
    	#Variables
    	(PF_IMAGE, "image", "Input image", None),
    	(PF_DRAWABLE, "drawable", "Input drawable", None),
    	#Colors
    	(PF_COLOUR, "color1", "Darker layer color", "#10315E"),
    	(PF_COLOUR, "color2", "Brighter layer color", "#1757ae"),
    	(PF_COLOUR, "color3", "Higher layer colour", "#888888"),
    	(PF_COLOUR, "color4", "Lower layer colour", "#CDCDCD"),
    	#Gauss -> layers
    	(PF_INT, "gauss1", "Gauss -> higher layer", 2),
    	(PF_INT, "gauss2", "Gauss -> medium layer", 5),
    	(PF_INT, "gauss3", "Gauss -> lower layer", 10)
    ],
    [],
    neonowy_noss, menu="<Image>/Filters/Gimpuj")

main()