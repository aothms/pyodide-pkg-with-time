project(mytime)
cmake_minimum_required(VERSION 3.22)
find_package(SWIG)
include(${SWIG_USE_FILE})

find_package(PythonLibs)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

add_library(util SHARED mytime.cpp)

set_source_files_properties(mytime.i PROPERTIES CPLUSPLUS ON)
swig_add_library(mytime LANGUAGE python SOURCES mytime.i)
swig_link_libraries(mytime util)
