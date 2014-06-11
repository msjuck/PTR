using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace Client
{       
    class Program{
        static void Main(string[] args)
        {
            string ipAddr = "127.0.0.1";
            int port = 5000;

            Interface i = new Interface(ipAddr, port);
            i.Run();
        }      
    }
}
