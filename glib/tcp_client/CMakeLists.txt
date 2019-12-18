
aux_source_directory(. DIR_TCP_CLIENT_SRCS)
SET (EXECUTABLE_OUTPUT_PATH "${CMAKE_SOURCE_DIR}/build")


add_executable(tcp_client ${DIR_TCP_CLIENT_SRCS})
target_link_libraries (tcp_client -lgobject-2.0 -lgio-2.0 -lglib-2.0)