Imports Newtonsoft.Json.JsonConvert
Public Class Host

    Public Shared Hosting As Boolean = False

    Dim hostFile As String = "host.py"

    Dim usr_name As String
    Private password As String

    Private init As Boolean = False ' See if Class object was initialized with username & pass

    Public Shared JoinedCls As List(Of String)


    Sub New(u_name As String, pass As String)
        usr_name = u_name
        password = pass
        init = True
    End Sub


    Public Shared Sub UpdateLoop()
        Try
            JoinedCls = DeserializeObject(Of List(Of String))(Utils.ReadFile(Utils.Dumps + "UsrJoined.json"))
        Catch ex As Exception
        End Try
    End Sub

    Public Shared Sub Send(data, usr)
        If Hosting = True Then
            If usr = "All" Then
                Utils.WriteJsonData("SerDataV", data)
            Else
                Dim dumData As New Dictionary(Of String, String)
                dumData.Add("User", usr)
                dumData.Add("Data", data)

                Utils.WriteJsonData("SpecUser", dumData)
            End If
        Else
            MsgBox("You Need To host First!")
        End If
    End Sub

    ''' <summary>
    ''' Start hosting, Returns  <c>1 [Success]</c>, <c>-1 [Invalid Credentials]</c>, <c>-2 [Please enter username / pass]</c>
    ''' </summary>
    Function Start(s_ip, s_Port)
        If init = True Then
            Dim p As New ProcessStartInfo
            p.FileName = hostFile
            p.WindowStyle = ProcessWindowStyle.Normal
            p.Arguments = s_ip & " " & s_Port & " " & usr_name & " " & password

            Process.Start(p)

            If Utils.ReadUntilFound("Validate") = "1" Then
                Hosting = True
                Return 1
            Else
                Return -1
            End If

        Else
            Return -2
        End If
    End Function

End Class
