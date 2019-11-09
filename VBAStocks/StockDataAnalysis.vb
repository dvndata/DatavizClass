Sub StockData()

For Each ws In Worksheets

    ' To clear the data and formating from previous run, delete the columns.
    Columns("I:Q").EntireColumn.Delete
    
    ' Get # of rows in the raw data provided
    RowCount = ws.Range("A" & Rows.Count).End(xlUp).Row
    
  
    'Initialization of variables
    j = 1
    Ticker = ""
    TotalStockVolume = 0
    
    greatestincrease = 0
    greatestdecrease = 0
    greatestvolume = 0
    GITicker = ""
    GDTicker = ""
    GVTicker = ""
    
    ' Start from second row. First row has headings.
    For i = 2 To RowCount
       
        If Ticker <> ws.Cells(i, 1).Value Then
        
            If i > 2 Then
                ws.Cells(j, 9).Value = Ticker
                ws.Cells(j, 10).Value = YearClose - yearopen
                If yearopen <> 0 Then
                    ws.Cells(j, 11).Value = (YearClose - yearopen) / yearopen
                Else
                    ws.Cells(j, 11).Value = 0
                End If
            End If
            ws.Cells(j, 12).Value = TotalStockVolume

            Ticker = ws.Cells(i, 1).Value
            TotalStockVolume = 0
            yearopen = ws.Cells(i, 3).Value
            j = j + 1
        Else
            TotalStockVolume = TotalStockVolume + ws.Cells(i, 7).Value
            YearClose = ws.Cells(i, 6).Value
        End If
    
    Next i
    
        ' Entry for the last ticker after all rows are processed
        ws.Cells(j, 9).Value = Ticker
        ws.Cells(j, 10).Value = YearClose - yearopen
        If yearopen <> 0 Then
            ws.Cells(j, 11).Value = (YearClose - yearopen) / yearopen
        Else
            ws.Cells(j, 11).Value = 0
        End If
        ws.Cells(j, 12).Value = TotalStockVolume

    'Loop through the newly formed list
    RowCount2 = ws.Range("I" & Rows.Count).End(xlUp).Row
    For x = 2 To RowCount2
        
        'Color red or green based on positive or negative gain
        If ws.Cells(x, 10) >= 0 Then
            ws.Cells(x, 10).Interior.Color = vbGreen
        Else
            ws.Cells(x, 10).Interior.Color = vbRed
        End If
    
        'Record greatest % increase. % decrease and greatest volume
        If greatestincrease < ws.Cells(x, 11).Value Then
            greatestincrease = ws.Cells(x, 11).Value
            GITicker = ws.Cells(x, 9)
                
        End If
        If greatestdecrease > ws.Cells(x, 11).Value Then
            greatestdecrease = ws.Cells(x, 11).Value
            GDTicker = ws.Cells(x, 9)
        End If
        
        If greatestvolume < ws.Cells(x, 12).Value Then
            greatestvolume = ws.Cells(x, 12).Value
            GVTicker = ws.Cells(x, 9)
        End If
    Next x
    
    ' load final values to the spreadsheet cells
    ws.Cells(2, 17).Value = greatestincrease
    ws.Cells(3, 17).Value = greatestdecrease
    ws.Cells(4, 17).Value = greatestvolume
    
    ws.Cells(2, 16).Value = GITicker
    ws.Cells(3, 16).Value = GDTicker
    ws.Cells(4, 16).Value = GVTicker
    
    ' Formating numbers
    ws.Columns(11).NumberFormat = "0.00%"
    ws.Range("q2").NumberFormat = "0.00%"
    ws.Range("q3").NumberFormat = "0.00%"
    ws.Range("q4").NumberFormat = "000,000"
    
    ' Headings for calculated data
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"
    ws.Cells(1, 16).Value = "Ticker"
    ws.Cells(1, 17).Value = "Value"
    ws.Cells(2, 15).Value = "Greatest % Increase"
    ws.Cells(3, 15).Value = "Greatest % Decrease"
    ws.Cells(4, 15).Value = "Greatest Total Volume"
Next ws
End Sub


