using System.Collections.Generic;
using System;
using fileConfiguration;
using contactStruct;

namespace consoleApp
{
    class Menu
    {
        public List<Option> options = new List<Option>();
        public DataFile dataFile = new DataFile();
        public void Start()
        {
            int index = 0;
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
                        WriteMenu(index);
                    }
                    else
                    {
                        index = 0;
                        WriteMenu(index);
                    }
                }
                if (keyinfo.Key == ConsoleKey.UpArrow)
                {
                    if (index - 1 >= 0)
                    {
                        index--;
                        WriteMenu(index);
                    }
                    else
                    {
                        index = options.Count-1;
                        WriteMenu(index);
                    }
                }
                if (keyinfo.Key == ConsoleKey.Enter)
                {
                    options[index].Selected.Invoke();
                    index = 0;
                }
            }
            while (keyinfo.Key != ConsoleKey.X);
            Console.ReadKey();
        }
        void WriteMenu(int index)
        {
            dataFile.WriteFile();
            Console.ResetColor();
            Console.Clear();
            Console.WriteLine("Menu\n");
            for(int i = 0; i < options.Count; i++)
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
        private void SubMenu(int contactNumber)
        {
            options.Clear();
            options.Add(new Option("| Chat", () => Console.WriteLine("ok")));
            options.Add(new Option("| Delete", () => DeleteContact(dataFile, contactNumber)));
            options.Add(new Option("| Return", () => { FirstMenu(); WriteMenu(0); }));
        }
        public void FirstMenu()
        {
            string spaces;
            options.Clear();
            options.Add(new Option("| Add contact", () => AddContact(dataFile)));
            for (int i = 0; i < dataFile.contacts.Count; i++)
            {
                spaces = new string(' ', (dataFile.contacts.Count.ToString().Length - (i + 1).ToString().Length) + 1);
                int id = i;
                options.Add(new Option($"[{i + 1}]{spaces}{ dataFile.contacts[i].Username} - { dataFile.contacts[i].IpAddress}", () => { SubMenu(id); WriteMenu(0); }));
            }
            options.Add(new Option("| Exit", () => Environment.Exit(0)));
        }
        private void AddContact(DataFile dataFile)
        {
            string name;
            string ipAddress;
            Console.Clear();
            Console.Write("Enter contact name : ");
            name = Console.ReadLine();
            Console.Write("Enter contact IP address : ");
            ipAddress = Console.ReadLine();
            dataFile.contacts.Add(new Contact() { Username = name, IpAddress = ipAddress });
            FirstMenu();
            WriteMenu(0);
        }
        private void DeleteContact(DataFile dataFile, int contactNumber)
        {
            dataFile.contacts.RemoveAt(contactNumber);
            FirstMenu();
            WriteMenu(0);
        }
    }

    public class Option
    {
        public string Name { get; }
        public Action Selected { get; }
        public Option(string name, Action selected)
        {
            Name = name;
            Selected = selected;
        }
    }
}