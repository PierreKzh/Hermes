using System;
using System.Collections.Generic;
using System.IO;
using contactStruct;
using Newtonsoft.Json;

namespace fileConfiguration
{
    [JsonObject(MemberSerialization.OptOut)]
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
        }
        private static string file = "HermesData.json";
        public List<Contact> contacts = new List<Contact>();
        static public void WriteFile(DataFile dataFile)
        {
            /**
             * @brief   write the content of DataFIle in a file
             */
            File.WriteAllText(DataFile.file, JsonConvert.SerializeObject(dataFile));
            /*Stream stream = File.Open(DataFile.file, FileMode.Open);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            binaryFormatter.Serialize(stream, MemberwiseClone());
            stream.Close();*/
        }
        public DataFile ReadFile()
        {
            /**
             * @brief   read the content of a file to return it in DataFile
             * @return  DataFile :  The DataFile read in a file
             */
            if (!File.Exists(DataFile.file))
            {
                File.WriteAllText(DataFile.file, JsonConvert.SerializeObject(this.MemberwiseClone()));
            }
            var json = File.ReadAllText(DataFile.file);
            var dataFile = JsonConvert.DeserializeObject<DataFile>(json);
            return dataFile;
            /*
            Stream stream = File.Open(DataFile.file, FileMode.Open);
            var binaryFormatter = new System.Runtime.Serialization.Formatters.Binary.BinaryFormatter();
            DataFile dataFile = (DataFile)binaryFormatter.Deserialize(stream);
            stream.Close();
            return dataFile;*/
        }
    }
}