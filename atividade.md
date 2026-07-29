Windows PowerShell
Copyright (C) Microsoft Corporation. Todos os direitos reservados.

PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Batatas ambulantes","autor":"Enzo Oliveira","ano": 1999}'


ano          : 1999
autor        : Enzo Oliveira
data_criacao : 2026-07-29 09:15:45.827137
id           : 4
titulo       : Batatas ambulantes



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
>>    -Method PUT `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Cotemig","autor":"3B1","ano":2026}'


ano          : 2026
autor        : 3B1
data_criacao : 2026-07-29 09:12:07.265622
id           : 1
titulo       : Cotemig



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Eco do Amanhã","autor":"Mariana Silva","ano":2024}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe3 in position 25: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Noites de Outono","autor":"Sofia Meireles","ano":1975}'


ano          : 1975
autor        : Sofia Meireles
data_criacao : 2026-07-29 09:28:44.898761
id           : 5
titulo       : Noites de Outono



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"A Última Engrenagem","autor":"Lucas Vasconcelos","ano":2019}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xda in position 13: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Labirintos do Tempo","autor":"Ricardo Antunes","ano":2002}'


ano          : 2002
autor        : Ricardo Antunes
data_criacao : 2026-07-29 09:29:04.171843
id           : 6
titulo       : Labirintos do Tempo



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"O Segredo do Vale","autor":"Beatriz Fontes","ano":1988}'


ano          : 1988
autor        : Beatriz Fontes
data_criacao : 2026-07-29 09:29:09.705186
id           : 7
titulo       : O Segredo do Vale



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Pétalas de Ferro","autor":"Carlos Drummond Neto","ano":2015}'
Invoke-RestMethod :
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 12: invalid continuation
byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebExc
   eption
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand
PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Mar","autor":"J. Amado","ano":1936}'


ano          : 1936
autor        : J. Amado
data_criacao : 2026-07-29 09:31:13.740065
id           : 8
titulo       : Mar



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Rio","autor":"M. Assis","ano":1881}'


ano          : 1881
autor        : M. Assis
data_criacao : 2026-07-29 09:31:18.932739
id           : 9
titulo       : Rio



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
>>    -Method POST `
>>    -ContentType "application/json" `
>>    -Body '{"titulo":"Sol","autor":"J. Alencar","ano":1870}'


ano          : 1870
autor        : J. Alencar
data_criacao : 2026-07-29 09:31:23.714720
id           : 10
titulo       : Sol



PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE

PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE

PS C:\Users\12400025> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE