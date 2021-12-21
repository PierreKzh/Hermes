using System;
using System.Collections.Generic;
using contactStruct;

namespace fileConfiguration
{
    [Serializable]
    public class DataFile
    {
        public DataFile()
        {
            WriteFile();
        }
        private static string file = "HermesData.data";
        public List<Contact> contacts = new List<Contact>();
        public void WriteFile()
        {
            /**
             * @brief   write the content of DataFIle in a file
             */
            System.IO.Stream stream = System.IO.File.Open(DataFile.file, System.IO.FileMode.Create);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            binaryFormatter.Serialize(stream, this.MemberwiseClone());
            stream.Close();
        }
        public DataFile ReadFile()
        {
            /**
             * @brief   read the content of a file to return it in DataFile
             * @return  DataFile :  The DataFile read in a file
             */
            System.IO.Stream stream = System.IO.File.Open(DataFile.file, System.IO.FileMode.Open);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            DataFile dataFile = (DataFile)binaryFormatter.Deserialize(stream);
            stream.Close();
            return dataFile;
        }
    }
}