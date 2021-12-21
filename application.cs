using fileConfiguration;

namespace application
{
    class Program
    {
        public static DataFile StartUp()
        {
            /**
             * @brief   initialize the beginin of the program
             * @return  DataFile :  the first initialized DataFile  
             */
            DataFile dataFile = new DataFile();
            return dataFile;
        }
    }
}
