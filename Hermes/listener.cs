using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

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
                Byte[] buffer = new Byte[1024];
                String data = null;
                while (true)
                {
                    server.Start();
                    //Console.Write("Waiting for a connection... ");
                    TcpClient client = server.AcceptTcpClient();
                    Console.WriteLine("\nConnected!");
                    data = null;
                    NetworkStream stream = client.GetStream();
                    int i;
                    while ((i = stream.Read(buffer, 0, buffer.Length)) != 0)
                    {
                        data = Encoding.UTF8.GetString(buffer, 0, i);
                        Console.WriteLine("Received: {0}\n", data);
                        /*data = data.ToUpper();
                        byte[] msg = System.Text.Encoding.ASCII.GetBytes(data);
                        // Send back a response.
                        stream.Write(msg, 0, msg.Length);
                        Console.WriteLine("Sent: {0}", data);*/
                    }
                    client.Close();
                    Thread.Sleep(500);
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
            Thread.Sleep(500);
        }
    }
}