set(SOURCE_FILES_VTK vtk_polydata.cpp vtk_polydata.h
                          point.cpp point.h
                          line.cpp line.h)

ADD_LIBRARY(vtk_polydata STATIC ${SOURCE_FILES_VTK})

set_property(TARGET vtk_polydata PROPERTY POSITION_INDEPENDENT_CODE ON)