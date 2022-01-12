using System;
using System.Collections.Generic;

namespace appTools
{
    class Tool
    {
        /**
         * @file        tools.cs
         * @class       Tool "tools.cs"
         * @brief       declaration of class Tool
         * @details     Used for create tools usefull in the program
         * @bug         
         * @warning       
         * @remark      
         */
        public static void ClearLastLine(int lineNumber)
        {
            /**
            * @brief   The function clear the line of the number passed.
            * @param    lineNumber :    Number of the line to clear
            */
            Console.SetCursorPosition(0, Console.CursorTop + lineNumber);
            Console.Write(new string(' ', Console.BufferWidth));
            Console.SetCursorPosition(0, Console.CursorTop - 1);
        }
        public static void WriteTitle(List<Title> currentTitle)
        {
            /**
            * @brief   Write an object Title
            * @param    currentTitle :  Title to write
            */
            foreach (var textInfo in currentTitle)
            {
                Console.ForegroundColor = textInfo.TextColor;
                Console.Write(textInfo.Text);
            }
            Console.ResetColor();
        }
        public static void WriteAtLine(int lineNumber, string message, ConsoleColor color)
        {
            /**
            * @brief   The function Write at the line selected then return to the current line
            * @param    lineNumber :    Number of the line to clear
            * @param    message :       message to print
            * @param    color :         color of the message
            */
            Tool.ClearLastLine(lineNumber);
            Console.ForegroundColor = color;
            Console.Write(message);
            Console.ResetColor();
            Tool.ClearLastLine((lineNumber*(-1)));
        }
        public static (string, ConsoleKeyInfo) InputEscape(string question)
        {
            /**
            * @brief    The function listen key pressed.
            * @brief    Then create a message with this after a question.
            * @param    question :  Question to Write before write the message
            * @return   message :   message printed
            * @return   cki :       value of the key pressed
            */
            string message = "";
            ConsoleKeyInfo cki;
            Console.Write(question);
            cki = Console.ReadKey();
            while (cki.Key != ConsoleKey.Enter && cki.Key != ConsoleKey.Escape)
            {
                if (cki.Key == ConsoleKey.Backspace && message.Length > 0)
                {
                    message = message.Remove(message.Length - 1);
                }
                else if (cki.Key != ConsoleKey.Escape)
                {
                    message += cki.KeyChar;
                }
                Tool.ClearLastLine(0);
                Console.Write(question+message);
                cki = Console.ReadKey();
            }
            return (message, cki);
        }
    }
    public class Title
    {
        /**
         * @file        tools.cs
         * @class       Title "tools.cs"
         * @brief       declaration of class Title
         * @details     Used for link a text with a color
         * @bug         
         * @warning       
         * @remark      
         */
        public string Text { get; set; }
        public ConsoleColor TextColor { get; set; }
    }
}
