cmake_minimum_required(VERSION 2.8)

project(GLib_samples)


include_directories (
    ${Glib_INCLUDE_DIRS} 
)


aux_source_directory(. DIR_TOOT_SRCS)

set (CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g")
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")

add_subdirectory (tcp_client)

add_executable(main ${DIR_TOOT_SRCS})

