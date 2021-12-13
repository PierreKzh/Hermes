using System;
using listener;
using sender;
using System.Threading;
using System.Text;
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
        Console.OutputEncoding = Encoding.Unicode;
        string message;
        string ip;
        client client1 = new client();
        Thread threadListener = new Thread(() => server.StartServer("0.0.0.0", 11000));
        threadListener.Start();
        Console.WriteLine("Adresse IP de destination : ");
        ip = Console.ReadLine();
        while (true)
        {
            try
            {
                Console.WriteLine("Envoyer un méssage : ");
                message = Console.ReadLine();
                client.StartClient(ip, 11000, message);
            }
            catch (OverflowException e)
            {
                Console.WriteLine("{0} Value read = {1}.", e.Message);
            }
            Thread.Sleep(200);
        }
        return 0;
    }
}