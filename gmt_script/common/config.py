#!/usr/bin/env python3

######################################### common PATH settings
gmt6_binary_path    = '/usr/bin/gmt'
my_gmt_data_path    = '/home/rau/Projects/mygmtdata/'
lun_gmt_data_path   = '/home/rau/Projects/mygmtdata/lun/'
#########################################
gridpath            = lun_gmt_data_path + '20mDEM.grd'
gridpath_sea        = lun_gmt_data_path + 'SeaTopo.grd'
gridshadpath        = lun_gmt_data_path + '20mDEM_shad_n80.grd'         #TODO: Add a function to import custom shad
gridshadpath_sea    = lun_gmt_data_path + 'SeaTopo_shad_n20.grd'        #TODO: Add a function to import custom shad
#topo_cptpath        = lun_gmt_data_path + 'topo_w.cpt'
topo_cptpath        = my_gmt_data_path + 'geo_tainan.cpt'
time_cptpath        = my_gmt_data_path  + 'color_time.cpt'
depth_cptpath       = my_gmt_data_path  + 'color_depth.cpt'