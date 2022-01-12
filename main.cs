using System;
using System.Collections.Generic;
using System.Threading;
using fileConfiguration;
using consoleApp;
using hostConnection;
using appTools;

class Source
{
    /**
     * @file main.cs
     *
     * @brief principal program
     * @details 
     * @author Pierre Kerzerho <kerzerho.pierre13@gmail.com>
     * @author 
     *
     */
    public static int Main(String[] args)
    {
        /**
        * @brief   First display the logo of the game.
        * @brief   Then after press an input the function initialized a menu and display it.
        * @return  DataFile :  The DataFile read in a file
        */
        List<Title> asciiArt = new List<Title>
            {
                new Title { Text="           ##############(         \n       *#####,         ######      \n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="     #%%/", TextColor = ConsoleColor.Red },
                new Title { Text="                  ####(   \n", TextColor = ConsoleColor.DarkBlue},
                new Title { Text="       #%%/", TextColor = ConsoleColor.Red },
                new Title { Text="                  ####  \n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="  ...", TextColor = ConsoleColor.White },
                new Title { Text="    #%%(", TextColor = ConsoleColor.Red },
                new Title { Text="                  ### \n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="    #%%(", TextColor = ConsoleColor.Red },
                new Title { Text="                ####\n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text=" ,", TextColor = ConsoleColor.Blue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="    #%%(", TextColor = ConsoleColor.Red },
                new Title { Text="              .###\n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="  ##", TextColor = ConsoleColor.Blue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="    #%%(", TextColor = ConsoleColor.Red },
                new Title { Text="            ####\n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="  ,###", TextColor = ConsoleColor.Blue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="    #%%(", TextColor = ConsoleColor.Red },
                new Title { Text="          ### \n", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="    ,###", TextColor = ConsoleColor.Blue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="    #", TextColor = ConsoleColor.Red },
                new Title { Text="    __  ____________  __  ______________\n", TextColor = ConsoleColor.Gray },
                new Title { Text="      ,###", TextColor = ConsoleColor.Blue },
                new Title { Text="    ...", TextColor = ConsoleColor.White },
                new Title { Text="      / / / / ____/ __ \\/  |/  / ____/ ___/\n", TextColor = ConsoleColor.Gray },
                new Title { Text="        ,###", TextColor = ConsoleColor.Blue },
                new Title { Text="    .", TextColor = ConsoleColor.White },
                new Title { Text="     / /_/ / __/ / /_/ / /|_/ / __/  \\__ \\ \n", TextColor = ConsoleColor.Gray },
                new Title { Text="          .###", TextColor = ConsoleColor.Blue },
                new Title { Text=" ,", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="     / __  / /___/ _, _/ /  / / /___ ___/ / \n", TextColor = ConsoleColor.Gray },
                new Title { Text="             #######", TextColor = ConsoleColor.DarkBlue },
                new Title { Text="/_/ /_/_____/_/ |_/_/  /_/_____//____/  \n\n", TextColor = ConsoleColor.Gray },
            };
        Tool.WriteTitle(asciiArt);
        Console.ForegroundColor = ConsoleColor.White;
        Console.WriteLine("Welcome to hermes secure messaging");
        Console.ForegroundColor = ConsoleColor.Gray;
        Console.WriteLine("\nContact : MailAddress            WebSite : SiteAddress\n");
        Console.ForegroundColor = ConsoleColor.DarkGray;
        Console.WriteLine("Press any key to continue ...");
        Console.ReadKey();

        Menu menu = new Menu();
        menu.threadListener = new Thread(() => Server.Start("0.0.0.0", 11000));
        menu.threadListener.Start();
        menu.dataFile = new DataFile();
        menu.dataFile = menu.dataFile.ReadFile();
        menu.titleMenu = new List<Title>
            {
                new Title { Text="Hermes ", TextColor = ConsoleColor.Blue },
                new Title { Text="Secure ", TextColor = ConsoleColor.White },
                new Title { Text="Messaging", TextColor = ConsoleColor.Red }
            };
        menu.FirstMenu();
        menu.Start();
        return 0;
    }
}