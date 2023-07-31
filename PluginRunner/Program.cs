using System;
using System.Diagnostics;

namespace PluginRunner
{
    class Program
    {
        static Process _cmd;
        static void Main(string[] args)
        {
            AppDomain.CurrentDomain.ProcessExit += new EventHandler (OnProcessExit);

            Console.CancelKeyPress += delegate {
                _cmd.Kill(true);
            };

            _cmd = new Process();
            _cmd.StartInfo.FileName = "PluginDeltaSharing-PY.exe";
            _cmd.StartInfo.RedirectStandardInput = true;
            _cmd.StartInfo.RedirectStandardOutput = true;
            _cmd.StartInfo.RedirectStandardError = true;
            _cmd.StartInfo.CreateNoWindow = true;
            _cmd.StartInfo.UseShellExecute = false;
            _cmd.OutputDataReceived += (sender, args) => Console.WriteLine(args.Data);
            _cmd.Start();
            _cmd.BeginOutputReadLine();
            _cmd.WaitForExit();
        }

        static void OnProcessExit (object sender, EventArgs e)
        {
            _cmd.Kill(true);
        }
    }
}
