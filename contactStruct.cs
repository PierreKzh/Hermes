using System;
using System.Text.RegularExpressions;
using fileConfiguration;
using appTools;
using Newtonsoft.Json;

namespace contactStruct
{
    [JsonObject(MemberSerialization.OptOut)]
    public class Contact
    {
        /**
         * @file        contact.cs
         * @class       Contact "contact.cs"
         * @brief       declaration of a contact
         * @details     Used create a contact
         * @bug         
         * @warning     
         * @remark      
         */
        public Contact()
        {
        }
        public string Username;
        public string IpAddress;
        public static void AddContact(DataFile dataFile)
        {
            /**
            * @brief    The function get the name of the contact.
            * @brief    Then get the contact IP's and verif if its a right IP.
            * @brief    The user can press [Escap] to come back in the menu
            * @param    dataFile :  The struct file to back up datas.
            */
            string name = "";
            string ipAddress = "";
            string ipRegex = @"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$";
            string question1 = "Enter contact name: ";
            string question2 = "Enter contact IP address : ";
            ConsoleKeyInfo cki;
            Tool.WriteAtLine(-1, "Press [Escape] to quit\n", ConsoleColor.Red);
            do
            {
                (name, cki) = Tool.InputEscape(question1);
                if (cki.Key == ConsoleKey.Enter)
                {
                    Console.WriteLine(question1+name);
                    Console.WriteLine();
                    do
                    {
                        (ipAddress, cki) = Tool.InputEscape(question2);
                        if (cki.Key == ConsoleKey.Enter)
                        {
                            if (!Regex.IsMatch(ipAddress, ipRegex))
                            {
                                Tool.WriteAtLine(1, "Ivalide IP address", ConsoleColor.Red);
                            }
                            else
                            {
                                dataFile.contacts.Add(new Contact() { Username = name, IpAddress = ipAddress });
                                DataFile.WriteFile(dataFile);
                            }
                        }
                    } while (!Regex.IsMatch(ipAddress, ipRegex) && cki.Key != ConsoleKey.Escape);
                }
            } while (!Regex.IsMatch(ipAddress, ipRegex) && cki.Key != ConsoleKey.Escape);
        }
    }
}