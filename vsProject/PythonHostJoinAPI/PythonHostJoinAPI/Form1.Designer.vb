<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.Uname = New System.Windows.Forms.TextBox()
        Me.Pass = New System.Windows.Forms.TextBox()
        Me.Login = New System.Windows.Forms.Button()
        Me.DataB = New System.Windows.Forms.TextBox()
        Me.Send = New System.Windows.Forms.Button()
        Me.JoinB = New System.Windows.Forms.Button()
        Me.dataRecv = New System.Windows.Forms.RichTextBox()
        Me.DisconnectB = New System.Windows.Forms.Button()
        Me.UpdateHosts = New System.Windows.Forms.Timer(Me.components)
        Me.OnlinehostsB = New System.Windows.Forms.ListBox()
        Me.ClJoinedB = New System.Windows.Forms.ListBox()
        Me.ClUname = New System.Windows.Forms.TextBox()
        Me.startCl = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Panel1 = New System.Windows.Forms.Panel()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.Label9 = New System.Windows.Forms.Label()
        Me.Server_ip = New System.Windows.Forms.TextBox()
        Me.Server_Port = New System.Windows.Forms.TextBox()
        Me.Label10 = New System.Windows.Forms.Label()
        Me.Label11 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'Uname
        '
        Me.Uname.Location = New System.Drawing.Point(12, 229)
        Me.Uname.Name = "Uname"
        Me.Uname.Size = New System.Drawing.Size(100, 20)
        Me.Uname.TabIndex = 0
        '
        'Pass
        '
        Me.Pass.Location = New System.Drawing.Point(12, 264)
        Me.Pass.Name = "Pass"
        Me.Pass.Size = New System.Drawing.Size(100, 20)
        Me.Pass.TabIndex = 1
        '
        'Login
        '
        Me.Login.Location = New System.Drawing.Point(61, 291)
        Me.Login.Name = "Login"
        Me.Login.Size = New System.Drawing.Size(50, 23)
        Me.Login.TabIndex = 2
        Me.Login.Text = "Login!"
        Me.Login.UseVisualStyleBackColor = True
        '
        'DataB
        '
        Me.DataB.Location = New System.Drawing.Point(139, 229)
        Me.DataB.Name = "DataB"
        Me.DataB.Size = New System.Drawing.Size(118, 20)
        Me.DataB.TabIndex = 3
        '
        'Send
        '
        Me.Send.Location = New System.Drawing.Point(206, 255)
        Me.Send.Name = "Send"
        Me.Send.Size = New System.Drawing.Size(50, 23)
        Me.Send.TabIndex = 4
        Me.Send.Text = "Send!"
        Me.Send.UseVisualStyleBackColor = True
        '
        'JoinB
        '
        Me.JoinB.Enabled = False
        Me.JoinB.Location = New System.Drawing.Point(479, 229)
        Me.JoinB.Name = "JoinB"
        Me.JoinB.Size = New System.Drawing.Size(54, 23)
        Me.JoinB.TabIndex = 7
        Me.JoinB.Text = "Join!"
        Me.JoinB.UseVisualStyleBackColor = True
        '
        'dataRecv
        '
        Me.dataRecv.BackColor = System.Drawing.Color.White
        Me.dataRecv.Font = New System.Drawing.Font("Segoe UI", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.dataRecv.Location = New System.Drawing.Point(12, 332)
        Me.dataRecv.Name = "dataRecv"
        Me.dataRecv.ReadOnly = True
        Me.dataRecv.Size = New System.Drawing.Size(609, 178)
        Me.dataRecv.TabIndex = 8
        Me.dataRecv.Text = ""
        '
        'DisconnectB
        '
        Me.DisconnectB.Enabled = False
        Me.DisconnectB.Location = New System.Drawing.Point(539, 229)
        Me.DisconnectB.Name = "DisconnectB"
        Me.DisconnectB.Size = New System.Drawing.Size(82, 23)
        Me.DisconnectB.TabIndex = 9
        Me.DisconnectB.Text = "Disconnect!"
        Me.DisconnectB.UseVisualStyleBackColor = True
        '
        'UpdateHosts
        '
        Me.UpdateHosts.Interval = 25
        '
        'OnlinehostsB
        '
        Me.OnlinehostsB.FormattingEnabled = True
        Me.OnlinehostsB.Location = New System.Drawing.Point(299, 91)
        Me.OnlinehostsB.Name = "OnlinehostsB"
        Me.OnlinehostsB.Size = New System.Drawing.Size(322, 121)
        Me.OnlinehostsB.TabIndex = 10
        '
        'ClJoinedB
        '
        Me.ClJoinedB.FormattingEnabled = True
        Me.ClJoinedB.Location = New System.Drawing.Point(12, 91)
        Me.ClJoinedB.Name = "ClJoinedB"
        Me.ClJoinedB.Size = New System.Drawing.Size(245, 121)
        Me.ClJoinedB.TabIndex = 11
        '
        'ClUname
        '
        Me.ClUname.Location = New System.Drawing.Point(299, 230)
        Me.ClUname.Name = "ClUname"
        Me.ClUname.Size = New System.Drawing.Size(100, 20)
        Me.ClUname.TabIndex = 12
        '
        'startCl
        '
        Me.startCl.Enabled = False
        Me.startCl.Location = New System.Drawing.Point(405, 229)
        Me.startCl.Name = "startCl"
        Me.startCl.Size = New System.Drawing.Size(53, 23)
        Me.startCl.TabIndex = 13
        Me.startCl.Text = "Start!"
        Me.startCl.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Font = New System.Drawing.Font("Segoe UI", 20.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.Location = New System.Drawing.Point(12, 51)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(143, 37)
        Me.Label1.TabIndex = 14
        Me.Label1.Text = "Host-Side"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Font = New System.Drawing.Font("Segoe UI", 20.25!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.Location = New System.Drawing.Point(292, 51)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(157, 37)
        Me.Label2.TabIndex = 15
        Me.Label2.Text = "Client-Side"
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Font = New System.Drawing.Font("Segoe UI", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.Location = New System.Drawing.Point(177, 75)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(79, 13)
        Me.Label3.TabIndex = 16
        Me.Label3.Text = "Clients Joined"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Font = New System.Drawing.Font("Segoe UI", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.Location = New System.Drawing.Point(547, 75)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(74, 13)
        Me.Label4.TabIndex = 17
        Me.Label4.Text = "Online Hosts"
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Font = New System.Drawing.Font("Segoe UI", 12.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label5.Location = New System.Drawing.Point(468, 308)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(153, 21)
        Me.Label5.TabIndex = 18
        Me.Label5.Text = "Data Sent / Recieved"
        '
        'Panel1
        '
        Me.Panel1.BackColor = System.Drawing.Color.White
        Me.Panel1.Location = New System.Drawing.Point(277, 30)
        Me.Panel1.Name = "Panel1"
        Me.Panel1.Size = New System.Drawing.Size(3, 400)
        Me.Panel1.TabIndex = 19
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Font = New System.Drawing.Font("Segoe UI", 6.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label6.Location = New System.Drawing.Point(297, 215)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(50, 12)
        Me.Label6.TabIndex = 20
        Me.Label6.Text = "Username:"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Font = New System.Drawing.Font("Segoe UI", 6.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label7.Location = New System.Drawing.Point(137, 215)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(28, 12)
        Me.Label7.TabIndex = 21
        Me.Label7.Text = "Data:"
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Font = New System.Drawing.Font("Segoe UI", 6.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label8.Location = New System.Drawing.Point(10, 215)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(51, 12)
        Me.Label8.TabIndex = 22
        Me.Label8.Text = "Hostname:"
        '
        'Label9
        '
        Me.Label9.AutoSize = True
        Me.Label9.Font = New System.Drawing.Font("Segoe UI", 6.75!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label9.Location = New System.Drawing.Point(10, 252)
        Me.Label9.Name = "Label9"
        Me.Label9.Size = New System.Drawing.Size(49, 12)
        Me.Label9.TabIndex = 23
        Me.Label9.Text = "Password:"
        '
        'Server_ip
        '
        Me.Server_ip.Location = New System.Drawing.Point(228, 14)
        Me.Server_ip.Name = "Server_ip"
        Me.Server_ip.Size = New System.Drawing.Size(100, 20)
        Me.Server_ip.TabIndex = 24
        Me.Server_ip.Text = "192.168.0.107"
        '
        'Server_Port
        '
        Me.Server_Port.Location = New System.Drawing.Point(334, 14)
        Me.Server_Port.Name = "Server_Port"
        Me.Server_Port.Size = New System.Drawing.Size(39, 20)
        Me.Server_Port.TabIndex = 25
        Me.Server_Port.Text = "1234"
        '
        'Label10
        '
        Me.Label10.AutoSize = True
        Me.Label10.Font = New System.Drawing.Font("Segoe UI", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label10.Location = New System.Drawing.Point(150, 17)
        Me.Label10.Name = "Label10"
        Me.Label10.Size = New System.Drawing.Size(74, 13)
        Me.Label10.TabIndex = 26
        Me.Label10.Text = "Server IP:Port"
        '
        'Label11
        '
        Me.Label11.AutoSize = True
        Me.Label11.Font = New System.Drawing.Font("Segoe UI", 8.25!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label11.Location = New System.Drawing.Point(327, 17)
        Me.Label11.Name = "Label11"
        Me.Label11.Size = New System.Drawing.Size(10, 13)
        Me.Label11.TabIndex = 27
        Me.Label11.Text = ":"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(633, 521)
        Me.Controls.Add(Me.Label10)
        Me.Controls.Add(Me.Server_Port)
        Me.Controls.Add(Me.Server_ip)
        Me.Controls.Add(Me.Label9)
        Me.Controls.Add(Me.Label8)
        Me.Controls.Add(Me.Label7)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.Label5)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.startCl)
        Me.Controls.Add(Me.ClUname)
        Me.Controls.Add(Me.ClJoinedB)
        Me.Controls.Add(Me.OnlinehostsB)
        Me.Controls.Add(Me.DisconnectB)
        Me.Controls.Add(Me.dataRecv)
        Me.Controls.Add(Me.JoinB)
        Me.Controls.Add(Me.Send)
        Me.Controls.Add(Me.DataB)
        Me.Controls.Add(Me.Login)
        Me.Controls.Add(Me.Pass)
        Me.Controls.Add(Me.Uname)
        Me.Controls.Add(Me.Panel1)
        Me.Controls.Add(Me.Label11)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Uname As TextBox
    Friend WithEvents Pass As TextBox
    Friend WithEvents Login As Button
    Friend WithEvents DataB As TextBox
    Friend WithEvents Send As Button
    Friend WithEvents JoinB As Button
    Friend WithEvents dataRecv As RichTextBox
    Friend WithEvents DisconnectB As Button
    Friend WithEvents UpdateHosts As Timer
    Friend WithEvents OnlinehostsB As ListBox
    Friend WithEvents ClJoinedB As ListBox
    Friend WithEvents ClUname As TextBox
    Friend WithEvents startCl As Button
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents Label3 As Label
    Friend WithEvents Label4 As Label
    Friend WithEvents Label5 As Label
    Friend WithEvents Panel1 As Panel
    Friend WithEvents Label6 As Label
    Friend WithEvents Label7 As Label
    Friend WithEvents Label8 As Label
    Friend WithEvents Label9 As Label
    Friend WithEvents Server_ip As TextBox
    Friend WithEvents Server_Port As TextBox
    Friend WithEvents Label10 As Label
    Friend WithEvents Label11 As Label
End Class
