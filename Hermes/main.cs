using System;
using listener;
using sender;
class main
{
    /**
     * @file main.cs
     *
     * @brief principal program
     * @details 
     * @author Pierre Kerzerho <kerzerho.pierre13@gmail.com>
     * @author 
     * @version 0.1
     *
     * @return int
     *
     */
    public static int Main(String[] args)
    {
        client client1 = new client();
        server server1 = new server();
        server.StartServer("127.0.0.1", 11000);
        client.StartClient("127.0.0.1", 11000, "test message");
        return 0;
    }
}