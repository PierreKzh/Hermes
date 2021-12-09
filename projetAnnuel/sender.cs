using System;  
using System.Net;  
using System.Net.Sockets;  
using System.Text;  
  
namespace sender
{
    public class client
    {
        /**
         * @file        sender.cs
         * @class       sender "sender.cs"
         * @brief       declaration of class sender
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
        public static void StartClient(string ip, int port, string message)
        {  
            /*
            This function, create an end point to connect to this.
            Then try to connect to the server and send data.
            */
            byte[] bytes = new byte[1024];
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
                    byte[] msg = Encoding.ASCII.GetBytes(message); 
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