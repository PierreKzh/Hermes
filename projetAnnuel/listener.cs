using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace listener
{
    class server
    {
        /**
         * @file        listener.cs
         * @class       server "server.cs"
         * @brief       declaration of class server
         * @details     Used for listening any clients who would like to connect
         * @version     0.1
         * @date        2021
         * @note        
         * @pre         
         * @post        
         * @bug         
         * @warning     
         * @attention   
         * @remark      
         * @copyright   
         */
        public static void StartServer(string ip, int port)
        {
            /**
             * @brief           Listening for client connection
             * @param[in]       ip  ip address of listening
             * @param[in]       port  port of listening
             * @param[out]      
             * @param[in,out]   
             */
            TcpListener server = null;
            try
            {
                IPAddress ipAddress = IPAddress.Parse(ip);
                server = new TcpListener(ipAddress, port);
                Byte[] bytes = new Byte[256];
                String data = null;
                server.Start();
                while (true)
                {
                    Console.Write("Waiting for a connection... ");
                    TcpClient client = server.AcceptTcpClient();
                    Console.WriteLine("Connected!");
                    data = null;
                    NetworkStream stream = client.GetStream();
                    int i;
                    while ((i = stream.Read(bytes, 0, bytes.Length)) != 0)
                    {
                        data = System.Text.Encoding.ASCII.GetString(bytes, 0, i);
                        Console.WriteLine("Received: {0}", data);
                        /*data = data.ToUpper();
                        byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);
                        // Send back a response.
                        stream.Write(msg, 0, msg.Length);
                        Console.WriteLine("Sent: {0}", data);*/
                    }
                    client.Close();
                }
            }
            catch (SocketException e)
            {
                Console.WriteLine("SocketException: {0}", e);
            }
            finally
            {
                server.Stop();
            }
            Console.WriteLine("\nHit enter to continue...");
            Console.Read();
        }
    }
}