Public Class Form1
    Private Sub UpdateHosts_Tick(sender As Object, e As EventArgs) Handles UpdateHosts.Tick
        Client.UpdateLoop()
        Utils.UpdateSafe_ListBox(OnlinehostsB, OnlinehostsB.SelectedItem, Client.OnlineHosts.Keys().ToList())

        If Host.Hosting Then
            Host.UpdateLoop()
            Utils.UpdateSafe_ListBox(ClJoinedB, ClJoinedB.SelectedItem, Host.JoinedCls)
        End If

        Try
            If Utils.ReadFile(Utils.Dumps & "updated.txt") Then
                Utils.DeleteFile(Utils.Dumps & "updated.txt")
                dataRecv.AppendText(Utils.ReadFile(Utils.Dumps & "SerDataP.json") & vbCrLf)
            End If
        Catch ex As Exception
        End Try
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Utils.Initialize()
    End Sub

    Private Sub Login_Click(sender As Object, e As EventArgs) Handles Login.Click
        Dim host As New Host(Uname.Text, Pass.Text)

        If host.Start(Server_ip.Text, Server_Port.Text) = 1 Then
            MsgBox("Host Login Success!")

            ClJoinedB.Items.Add("All")
            ClJoinedB.SelectedItem = "All"
        Else
            MsgBox("Host Login Failed!")
        End If
    End Sub

    Private Sub Send_Click(sender As Object, e As EventArgs) Handles Send.Click
        Host.Send(DataB.Text, ClJoinedB.SelectedItem)
    End Sub

    Private Sub JoinB_Click(sender As Object, e As EventArgs) Handles JoinB.Click
        If OnlinehostsB.SelectedItem IsNot Nothing Then
            Client.Join(OnlinehostsB.SelectedItem)
        Else
            MsgBox("Please Select Host!")
        End If
    End Sub

    Private Sub DisconnectB_Click(sender As Object, e As EventArgs) Handles DisconnectB.Click
        Client.Disconnect()
    End Sub

    Private Sub ClUname_TextChanged(sender As Object, e As EventArgs) Handles ClUname.TextChanged
        If ClUname.Text.Length > 0 Then
            startCl.Enabled = True
        End If
    End Sub

    Private Sub startCl_Click(sender As Object, e As EventArgs) Handles startCl.Click
        Dim cl As New Client(ClUname.Text)
        cl.Start(Server_ip.Text, Server_Port.Text)
        UpdateHosts.Enabled = True

        startCl.Enabled = False

        JoinB.Enabled = True
        DisconnectB.Enabled = True
    End Sub

    Private Sub Port_KeyPress(ByVal sender As Object, ByVal e As System.Windows.Forms.KeyPressEventArgs) Handles Server_Port.KeyPress

        '97 - 122 = Ascii codes for simple letters
        '65 - 90  = Ascii codes for capital letters
        '48 - 57  = Ascii codes for numbers

        If Asc(e.KeyChar) <> 8 Then
            If Asc(e.KeyChar) < 48 Or Asc(e.KeyChar) > 57 Then
                e.Handled = True
            End If
        End If

    End Sub
End Class
