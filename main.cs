using System;
using System.Threading;
using System.Text;
using listener;
using sender;
using contactStruct;
using fileConfiguration;
using application;
class Source
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
        DataFile dataFile = Program.StartUp();

        //=========test struct contact====================
        dataFile = dataFile.ReadFile();
        dataFile.contacts.Add(new Contact() { Username = "contact1", IpAddress = "ip1" });
        dataFile.contacts.Add(new Contact() { Username = "contact2", IpAddress = "ip2" });
        dataFile.contacts.Add(new Contact() { Username = "contact3", IpAddress = "ip3" });
        dataFile.contacts.RemoveAt(0);
        for (int i = 0; i < dataFile.contacts.Count; i++)
        {
            Console.WriteLine($"{i}.{dataFile.contacts[i].Username}");
        }
        dataFile.WriteFile();

        //=========server & client=======================
        Console.OutputEncoding = Encoding.Unicode;
        string message;
        string ip;
        Thread threadListener = new Thread(() => Server.Start("0.0.0.0", 11000));
        threadListener.Start();
        Console.WriteLine("Adresse IP de destination : ");
        ip = Console.ReadLine();
        while (true)
        {
            try
            {
                Console.WriteLine("Envoyer un méssage : ");
                message = Console.ReadLine();
                Client.Start(ip, 11000, message);
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