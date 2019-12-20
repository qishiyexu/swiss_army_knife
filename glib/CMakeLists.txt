cmake_minimum_required(VERSION 2.8)

project(GLib_samples)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")


find_package(Glib REQUIRED)
include_directories(${GLIB_INCLUDE_DIR})
include_directories(${GLIBCONFIG_INCLUDE_DIR})

aux_source_directory(. DIR_TOOT_SRCS)

SET (CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g")
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")

add_subdirectory (tcp_client)
add_subdirectory (ucontext)

add_executable(main ${DIR_TOOT_SRCS})

