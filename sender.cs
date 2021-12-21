using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace sender
{
    public class Client
    {
        /**
         * @file        sender.cs
         * @class       Client "sender.cs"
         * @brief       declaration of class Client
         * @details     Used for sending data to a server
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
        public static void Start(string ip, int port, string message)
        {
            /**
             * @brief       Open a socket and send message to a server
             * @param       ip :        ip address of listening
             * @param       port :      port of listening  
             * @param       message :   message to send
             */
            try
            {
                IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
                IPAddress ipAddress = IPAddress.Parse(ip);
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, port);
                Socket sender = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
                try
                {
                    sender.Connect(remoteEP);
                    Console.WriteLine("Socket connected to {0}", sender.RemoteEndPoint.ToString());
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
                catch (ArgumentNullException ane)
                {
                    Console.WriteLine("ArgumentNullException : {0}", ane.ToString());
                }
                catch (SocketException se)
                {
                    Console.WriteLine("SocketException : {0}", se.ToString());
                }
                catch (Exception e)
                {
                    Console.WriteLine("Unexpected exception : {0}", e.ToString());
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }
    }
}