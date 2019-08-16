cmake_minimum_required(VERSION 3.0.1)
project(VTK_Parser)

if (CMAKE_VERSION VERSION_LESS "3.1")
    if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
      set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")
    endif ()
else ()
    set (CMAKE_CXX_STANDARD 11)
endif ()

SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/bin)

SET (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -fno-strict-aliasing -Wall -Wno-unused-function")

ADD_SUBDIRECTORY(src/vtk_polydata)
ADD_SUBDIRECTORY(src/utils)

ADD_EXECUTABLE(VTK_Parser src/main.cpp)

ADD_DEPENDENCIES(VTK_Parser vtk_polydata utils)

TARGET_LINK_LIBRARIES(VTK_Parser vtk_polydata utils m)