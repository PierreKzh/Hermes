using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using fileConfiguration;
using appTools;

namespace hostConnection
{
    class Server
    {
        /**
         * @file        listener.cs
         * @class       Server "server.cs"
         * @brief       declaration of class Server
         * @details     Used for listening any clients who would like to connect
         * @bug         
         * @warning     
         * @remark      
         */
        public static void Start(string ip, int port)
        {
            /**
             * @brief       Listening for client connection
             * @param       ip :    ip address of listening
             * @param       port :  port of listening     
             */
            TcpListener server = null;
            IPAddress ipAddress = IPAddress.Parse(ip);
            server = new TcpListener(ipAddress, port);
            Byte[] buffer = new Byte[1024];
            String data = null;
            while (true)
            {
                server.Start();
                //Console.Write("Waiting for a connection... ");
                TcpClient client = server.AcceptTcpClient();
                //Console.WriteLine("\nConnected!");
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
    }
    public class Client
    {
        /**
         * @file        sender.cs
         * @class       Client "sender.cs"
         * @brief       declaration of class Client
         * @details     Used for sending data to a server  
         * @bug         
         * @warning     
         * @remark       
         */
        public static void Start(string ip, int port, string message)
        {
            /**
             * @brief       Open a socket and send message to a server
             * @param       ip :        ip address of listening
             * @param       port :      port of listening  
             * @param       message :   message to send
             */
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
            IPAddress ipAddress = IPAddress.Parse(ip);
            IPEndPoint remoteEP = new IPEndPoint(ipAddress, port);
            Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            Thread waiting = new Thread(() => WaitingDisplay());
            try
            {
                waiting.Start();
                sender.Connect(remoteEP);
                Tool.ClearLastLine(0);
                waiting.Interrupt();
                //Console.WriteLine("Socket connected to {0}", sender.RemoteEndPoint.ToString());
                byte[] msg = Encoding.UTF8.GetBytes(message);
                int bytesSent = sender.Send(msg);
                /*
                // Receive the response from the remote device.  
                int bytesRec = sender.Receive(bytes);
                Console.WriteLine("Echoed test = {0}", Encoding.ASCII.GetString(bytes, 0, bytesRec));
                */
                sender.Shutdown(SocketShutdown.Both);
                sender.Close();
            }
            catch (SocketException)
            {
                waiting.Interrupt();
                Tool.ClearLastLine(0);
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("The host does not respond");
                Console.ResetColor();
            }
        }
        public static void Communication(DataFile dataFile, int contactNumber)
        {
            /**
             * @brief    Get a message to send and go back to the menu if [Escape] is pressed
             * @param    dataFile :  The struct file to back up datas.
             * @param    contactNumber :  Id of the contact selected
             */
            Console.OutputEncoding = Encoding.Unicode;
            ConsoleKeyInfo cki;
            Tool.WriteAtLine(-1, "Press [Escape] to quit\n", ConsoleColor.Red);
            string question = "Send message : ";
            do
            {
                string message;
                (message, cki) = Tool.InputEscape(question);
                if (cki.Key != ConsoleKey.Escape)
                {
                    Console.WriteLine(question+message);
                    Client.Start(dataFile.contacts[contactNumber].IpAddress, 11000, message);
                    Thread.Sleep(200);
                }
            } while (cki.Key != ConsoleKey.Escape);
        }
        private static void WaitingDisplay()
        {
            /**
             * @brief    Display 3 points with 1 seconde between.
             */
            int timer = 1000;
            while (true)
            {
                try
                {
                    for (int i = 0; i < 3; i++)
                    {
                        Console.Write(".");
                        Thread.Sleep(timer);
                    }
                    Tool.ClearLastLine(0);
                    Thread.Sleep(timer);
                }
                catch (ThreadInterruptedException)
                {
                    break;
                }
            }
        }
    }
}