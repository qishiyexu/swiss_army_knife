cmake_minimum_required(VERSION 2.8)

project(libevent_samples)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")


aux_source_directory(. DIR_TOOT_SRCS)

SET (CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g")
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")


add_executable(server1 ${DIR_TOOT_SRCS})
target_link_libraries (server1 -levent)
