
aux_source_directory(. DIR_TCP_CLIENT_SRCS)
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")
SET (CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g")

add_executable(tcp_server ${DIR_TCP_CLIENT_SRCS})
target_link_libraries (tcp_server -lgobject-2.0 -lgio-2.0 -lglib-2.0)