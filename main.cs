using System;
using System.Threading;
using System.Text;
using listener;
using sender;
using contactStruct;
using fileConfiguration;
using consoleApp;

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
        DataFile dataFile = new DataFile();
        dataFile = dataFile.ReadFile();
        //=========test struct contact====================
        /*dataFile = dataFile.ReadFile();
        dataFile.contacts.Add(new Contact() { Username = "Jean", IpAddress = "80.120.250.4" });
        dataFile.contacts.Add(new Contact() { Username = "Adrien", IpAddress = "140.225.30.15" });
        dataFile.contacts.Add(new Contact() { Username = "Roger", IpAddress = "220.14.100.55" });
        dataFile.contacts.RemoveAt(0);
        dataFile.WriteFile();*/

        /*//=========server & client=======================
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
        }*/

        //==================== Menu =======================
        Menu menu = new Menu();
        string asciiArt = @"
           ##############(         
       *#####,         ######      
     #%%/                  ####(   
       #%%/                  ####  
  ...    #%%(                  ### 
    ...    #%%(                ####
 ,    ...    #%%(              .###
  ##    ...    #%%(            ####
  ,###    ...    #%%(          ### 
    ,###    ...    #    __  ____________  __  ______________
      ,###    ...      / / / / ____/ __ \/  |/  / ____/ ___/
        ,###    .     / /_/ / __/ / /_/ / /|_/ / __/  \__ \ 
          .### ,     / __  / /___/ _, _/ /  / / /___ ___/ / 
             #######/_/ /_/_____/_/ |_/_/  /_/_____//____/  
";
        Console.WriteLine(asciiArt);
        Console.WriteLine("Welcome to hermes secure messaging");
        Console.WriteLine("Press any key to continue ...");
        Console.ReadKey();

        menu.dataFile = dataFile;
        menu.FirstMenu();
        menu.Start();
        return 0;
    }
}