Imports VB = Microsoft.VisualBasic
Imports System.IO
Imports Newtonsoft.Json

Public Class Utils
    Public Shared Dumps As String = Environment.GetEnvironmentVariable("appdata")

    ''' <summary>
    ''' Updates data in listbox while preseving the selected item.
    ''' </summary>
    Public Shared Sub UpdateSafe_ListBox(Lb As ListBox, selItem As Object, Iterator As List(Of String))
        If Iterator IsNot Nothing Then
            Lb.Items.Clear()

            For Each itm As String In Iterator
                Lb.Items.Add(itm)
            Next

            Try
                If Lb.Items.Contains(selItem) Then
                    Lb.SelectedItem = selItem
                End If
            Catch ex As Exception
            End Try
        End If
    End Sub
    Shared Sub Initialize()
        Dumps += "\HostJoinSys"

        If Not Directory.Exists(Dumps) Then
            Directory.CreateDirectory(Dumps)
        End If

        For Each OldFile In Directory.GetFiles(Dumps, "*.*", SearchOption.TopDirectoryOnly)
            File.Delete(OldFile)
        Next

        Dumps += "\"

        WriteData("CurrentHosts.json", "{}")
        WriteData("SerDataV.json", "{}")
        WriteData("UsrJoined.json", "{}")
        WriteData("DisV.txt", "")
    End Sub

    Shared Sub wait(ByVal seconds As Single)
        Static start As Single
        start = VB.Timer()
        Do While VB.Timer() < start + seconds
            System.Windows.Forms.Application.DoEvents()
        Loop
    End Sub
    Public Shared Sub DeleteFile(FilePath)
        My.Computer.FileSystem.DeleteFile(FilePath)
    End Sub

    Shared Function ReadFile(FilePath) As String
        Try
            Return My.Computer.FileSystem.ReadAllText(FilePath)
        Catch ex As Exception
        End Try
        Return -1
    End Function

    Public Shared Sub WriteJsonData(filename As String, data As Object)
        Using sw As StreamWriter = New StreamWriter(Dumps + filename + ".json")
            sw.Write(JsonConvert.SerializeObject(data, Formatting.Indented))
        End Using
    End Sub

    Public Shared Sub WriteData(filename As String, data As String)
        Using sw As StreamWriter = New StreamWriter(Dumps + filename)
            sw.Write(data)
        End Using
    End Sub

    Shared Function ReadUntilFound(varname)
        Dim tmp As String
        Console.WriteLine(Dumps & varname & ".txt")
        While True
            Try
                tmp = ReadFile(Dumps & varname & ".txt")
                DeleteFile(Dumps & varname & ".txt")
                Return tmp
            Catch ex As Exception
            End Try

            wait(0.1)
        End While

        Return -1
    End Function

End Class
