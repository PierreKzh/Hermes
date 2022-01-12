using System;
using System.Collections.Generic;
using System.IO;
using contactStruct;

namespace fileConfiguration
{
    [Serializable]
    public class DataFile
    {
        /**
     * @file        fileConfiguration.cs
     * @class       DataFile "fileConfiguration.cs"
     * @brief       declaration of a Datafile
     * @details     Used for create a file to back up each datas
     * @bug         
     * @warning     
     * @remark      
     */
        public DataFile()
        {
            if (!File.Exists(file)) 
            {
                Stream stream = File.Open(DataFile.file, FileMode.Create);
                var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
                binaryFormatter.Serialize(stream, MemberwiseClone());
                stream.Close();
            }
        }
        private static string file = "HermesData.data";
        public List<Contact> contacts = new List<Contact>();
        public void WriteFile()
        {
            /**
             * @brief   write the content of DataFIle in a file
             */
            Stream stream = File.Open(DataFile.file, FileMode.Open);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            binaryFormatter.Serialize(stream, MemberwiseClone());
            stream.Close();
        }
        public DataFile ReadFile()
        {
            /**
             * @brief   read the content of a file to return it in DataFile
             * @return  DataFile :  The DataFile read in a file
             */
            Stream stream = File.Open(DataFile.file, FileMode.Open);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            DataFile dataFile = (DataFile)binaryFormatter.Deserialize(stream);
            stream.Close();
            return dataFile;
        }
    }
}