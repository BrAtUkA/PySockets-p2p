Imports Newtonsoft.Json.JsonConvert
Public Class Client

    Public Shared Joined = False
    Dim joinFile As String = "join.py"

    Public Shared init As Boolean = False ' See if Class object was initialized with username & pass

    Dim usr_name As String

    Public Shared OnlineHosts As Dictionary(Of String, List(Of String))
    Sub New(u_name As String)
        usr_name = u_name
        init = True
    End Sub

    Public Shared Sub UpdateLoop()
        If Joined Then
            Try
                If Utils.ReadFile(Utils.Dumps & "Dis.txt") = "4O4" Then
                    Joined = False
                End If
            Catch ex As Exception
            End Try
        End If

        Try
            OnlineHosts = DeserializeObject(Of Dictionary(Of String, List(Of String)))(Utils.ReadFile(Utils.Dumps + "CurrentHosts.json"))
        Catch ex As Exception
        End Try
    End Sub

    Sub Start(s_ip, s_Port)
        If init = True Then
            Dim p As New ProcessStartInfo
            p.FileName = joinFile
            p.WindowStyle = ProcessWindowStyle.Normal
            p.Arguments = s_ip & " " & s_Port & " " & usr_name

            Process.Start(p)
        End If
    End Sub

    Public Shared Sub Disconnect()
        If Joined Then
            Utils.WriteData("DisV.txt", "Now")
        Else
            MsgBox("No host Joined!")
        End If
    End Sub
    Public Shared Sub Join(HostName)
        If Host.Hosting Then
            MsgBox("Can't Join While Hosting!")
        Else
            Utils.WriteData("SelectedHost.txt", HostName)
            Joined = True
        End If
    End Sub
End Class
