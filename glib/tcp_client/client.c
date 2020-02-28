#include <stdlib.h>
#include <stdio.h>
#include <gio/gio.h>

#define HOST "127.0.0.1"
#define PORT 2345


typedef struct ClientConnection {
    int conn_id;
    GSocket *socket;
	GSocketAddress *address;
    GSocketConnectable *connectable;
	GInputStream *istream;
	GOutputStream *ostream;
    GSocketClient *client;
    GSocketConnection *connection;
    GCancellable* cancellable;
    guint wait_id;
    GSource* src;
    gchar* host;
    int port;
} ClientConnection;

static void socket_client_connect_ready_cb(GObject *source_object, GAsyncResult *result, gpointer data);
static void write_all_cb(GObject *source, GAsyncResult *result, gpointer user_data);
static void write_data(ClientConnection* conn, void* data, int len);


static void socket_client_connect_ready_cb(GObject *source_object, GAsyncResult *result,
                                        gpointer data)
{
    ClientConnection* conn = (ClientConnection*)data;
    GError* error = NULL;
    conn->connection = g_socket_client_connect_finish(conn->client, result, &error);
    if (conn->connection == NULL) {
        printf ("conn error %s\n", error->message);
        g_clear_error(&error);
    } else {
        conn->istream = g_io_stream_get_input_stream(G_IO_STREAM(conn->connection));
		conn->ostream = g_io_stream_get_output_stream(G_IO_STREAM(conn->connection));

        write_data (conn, "hello", 5);
    }
}

static void write_all_cb(GObject *source, GAsyncResult *result, gpointer user_data)
{
    ClientConnection* conn = (ClientConnection*)user_data;
    gboolean ret;
    GError* error = NULL;
    gsize nbytes = 0;

    ret = g_output_stream_write_all_finish(G_OUTPUT_STREAM(source), result, &nbytes, &error);
    if (!ret) {
        printf ("write data error %s\n", error->message);
        g_clear_error(&error);
    }
    sleep(1);
    write_data(conn, "hello", 5);


}

static void write_data(ClientConnection* conn, void* data, int len)
{
        printf("write data\n");
        // GError* error = NULL;
        // gssize s = g_pollable_output_stream_write_nonblocking(conn->ostream, data, 
        //                             len, conn->cancellable, &error);
        // if (error)
        //     printf ("write %lu, error: %s", s, error->message);

       g_output_stream_write_all_async(conn->ostream, data, 
                                    len,
                                    G_PRIORITY_DEFAULT, NULL, write_all_cb, conn);
}

int main(int argc, char* argv[])
{
    ClientConnection* conn = g_new0(ClientConnection, 1);
    GError* error = NULL;

    conn->socket = g_socket_new(G_SOCKET_FAMILY_IPV4, G_SOCKET_TYPE_STREAM, 0, &error);
    g_socket_set_blocking(conn->socket, FALSE);
    g_socket_set_keepalive(conn->socket, TRUE);
    conn->connectable = g_network_address_parse(HOST, PORT, &error);
    if (!conn->connectable) {
        //
    }

    conn->client = g_socket_client_new();
    g_socket_client_set_timeout(conn->client, 5);

    g_socket_client_connect_async(conn->client, conn->connectable,
                                  conn->cancellable,
                                  socket_client_connect_ready_cb, conn);

    GMainLoop *loop = g_main_loop_new(NULL, FALSE);
    g_main_loop_run(loop);

    return 0;
}