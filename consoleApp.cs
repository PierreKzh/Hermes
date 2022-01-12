using System;
using System.Collections.Generic;
using System.Threading;
using fileConfiguration;
using contactStruct;
using hostConnection;
using appTools;

namespace consoleApp
{
    class Menu
    {
        /**
         * @file        consoleApp.cs
         * @class       Menu "consoleApp.cs"
         * @brief       declaration of class Menu
         * @details     Used for create a menu and naviguate in
         * @bug         
         * @warning       
         * @remark      
         */
        public List<Option> options = new List<Option>();
        public List<Title> titleMenu = new List<Title>();
        public List<Title> subTitleMenu = new List<Title>();
        public DataFile dataFile = new DataFile();
        public Thread threadListener;
        public void Start()
        {
            /**
            * @brief    The allow to naviguate like a menu.
            * @brief    The menu is define by options.
            * @ brief   Its possible to add a Title to the menu.
            */
            int index = 0;
            Console.Clear();
            WriteMenu(index);
            ConsoleKeyInfo keyinfo;
            do
            {
                keyinfo = Console.ReadKey();
                if (keyinfo.Key == ConsoleKey.DownArrow)
                {
                    if (index + 1 < options.Count)
                    {
                        index++;
                        Console.Clear();
                        WriteMenu(index);
                    }
                    else
                    {
                        index = 0;
                        Console.Clear();
                        WriteMenu(index);
                    }
                }
                if (keyinfo.Key == ConsoleKey.UpArrow)
                {
                    if (index - 1 >= 0)
                    {
                        index--;
                        Console.Clear();
                        WriteMenu(index);
                    }
                    else
                    {
                        index = options.Count-1;
                        Console.Clear();
                        WriteMenu(index);
                    }
                }
                if (keyinfo.Key == ConsoleKey.Enter)
                {
                    options[index].Selected.Invoke();
                    index = 0;
                }
                else
                {
                    Console.Clear();
                    WriteMenu(index);
                }
            }
            while (true);
        }
        private void WriteMenu(int index)
        {
            /**
            * @brief    The function display all options of the menu.
            * @brief    And place the cursor when the option is choice.
            * @param    index :  index of tha option choice.
            */
            dataFile.WriteFile();
            Console.ResetColor();
            Tool.WriteTitle(titleMenu);
            Console.Write("\n\n");
            Tool.WriteTitle(subTitleMenu);
            Console.Write("\n");
            for (int i = 0; i < options.Count; i++)
            {
                if (options[i] == options[index])
                {
                    Console.BackgroundColor = ConsoleColor.Gray;
                    Console.ForegroundColor = ConsoleColor.Black;
                    Console.Write("> ");
                }
                else
                {
                    Console.ResetColor();
                    Console.Write("  ");
                }
                Console.WriteLine(options[i].Name);
                Console.ResetColor();
            }
        }
        private void DisplayTitle()
        {
            /**
            * @brief    The function display a menu without options but just with the title.
            */
            options.Clear();
            Console.Clear();
            WriteMenu(0);
        }
        public void FirstMenu()
        {
            /**
            * @brief    This function is the declaration of the first menu.
            * @brief    Then create a message with this after a question.
            */
            string spaces;
            subTitleMenu.Clear();
            options.Clear();
            options.Add(new Option("| Add contact", () => { DisplayTitle(); Contact.AddContact(dataFile); FirstMenu(); Console.Clear(); WriteMenu(0); }));
            for (int i = 0; i < dataFile.contacts.Count; i++)
            {
                spaces = new string(' ', (dataFile.contacts.Count.ToString().Length - (i + 1).ToString().Length) + 1);
                int id = i;
                options.Add(new Option($"[{i + 1}]{spaces}{ dataFile.contacts[i].Username} - { dataFile.contacts[i].IpAddress}", () => { SubMenu(id); Console.Clear(); WriteMenu(0); }));
            }
            options.Add(new Option("| Exit", () => { threadListener.Interrupt(); Environment.Exit(0); }));
        }
        private void SubMenu(int currentContactId)
        {
            /**
            * @brief    This function is the declaration of the sub menu.
            * @brief    each contact have one sub menu
            * @param    currentContactId :  Id of the contact sub menu's
            */
            subTitleMenu.Clear();
            options.Clear();
            options.Add(new Option("| Chat", () => { DisplayTitle(); Client.Communication(dataFile, currentContactId); SubMenu(currentContactId); Console.Clear(); WriteMenu(0); }));
            options.Add(new Option("| Delete", () => VerifMenu($"Do you want delete {dataFile.contacts[currentContactId].Username} ?\n", () => dataFile.contacts.RemoveAt(currentContactId), currentContactId)));
            options.Add(new Option("| Return", () => { FirstMenu(); Console.Clear(); WriteMenu(0); }));
        }
        private void VerifMenu(string message, Action action, int currentContactId)
        {
            /**
            * @brief    The function create a menu with 2 choices.
            * @brief    Yes or no and execute an action if Yes is selected.
            * @param    message :           message of the new menu
            * @param    action :            action to execute
            * @param    currentContactId :  Id of the contact selected before
            */
            Console.Clear();
            subTitleMenu = new List<Title>{ new Title { Text=message, TextColor = ConsoleColor.Red } };
            Console.ResetColor();
            options.Clear();
            options.Add(new Option("Yes", () => { action(); FirstMenu(); Console.Clear(); WriteMenu(0); }));
            options.Add(new Option("No", () => { SubMenu(currentContactId); Console.Clear(); WriteMenu(0); }));
            WriteMenu(0);
        }
    }

    public class Option
    {
        /**
     * @file        consoleApp.cs
     * @class       Option "consoleApp.cs"
     * @brief       declaration of class Option
     * @details     Used for create options in menus
     * @bug         
     * @warning       
     * @remark      
     */
        public string Name { get; }
        public Action Selected { get; }
        public Option(string name, Action selected)
        {
            Name = name;
            Selected = selected;
        }
    }
}